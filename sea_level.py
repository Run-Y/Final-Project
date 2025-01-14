import random

import pandas as pd
import numpy as np
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
import language_library as ll


def create_plot(start_year, end_year):
    # 读取数据
    file_path = './data/gmsl_data.csv'
    data = pd.read_csv(file_path)

    # 根据年份范围筛选数据
    filtered_data = data[(data['year_fraction'] >= start_year) & (data['year_fraction'] <= end_year)]


    # 创建 Plotly 图表
    trace = go.Scatter(
        x=filtered_data['year_fraction'],
        y=filtered_data['GMSL_GIA_applied'],  # 使用加上 37.9 后的值
        mode='lines+markers',
        name='Global Mean Sea Level',
        hovertemplate='Year: %{x}<br>GMSL: %{y} mm<br>',
    )

    layout = go.Layout(
        title=f'Global Mean Sea Level Change ({start_year} - {end_year})',
        xaxis=dict(title='Year (Fraction)'),
        yaxis=dict(title='Global Mean Sea Level (mm)'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        template='plotly_white'
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure


def predict_future_sea_level(data, end_year, predict_years):
    """
    根据现有数据预测未来的海平面变化。

    参数:
        data: DataFrame 包含所有历史数据
        end_year: int 当前数据的最后一年
        predict_years: int 需要预测的年份范围

    返回:
        future_years: ndarray 包含预测的年份
        future_predictions: ndarray 包含预测的 GMSL 值
    """
    # 硬编码使用 1993 年到 2024 年作为训练数据
    training_data = data[(data['year_fraction'] >= 1993) & (data['year_fraction'] <= 2024)]

    # 准备用于训练的特征和目标值
    X_train = training_data[['year_fraction']]
    y_train = training_data['GMSL_GIA_applied']

    # 训练线性回归模型
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 生成未来年份数据
    future_years = np.arange(end_year, end_year + predict_years, 1)
    future_X = pd.DataFrame({'year_fraction': future_years})

    # 预测未来的 GMSL 值
    future_predictions = model.predict(future_X)

    return future_years, future_predictions


def create_prediction_plot(start_year, end_year, predict_years):
    """
    基于历史数据绘制包含预测的图表。

    参数:
        start_year: int 起始年份（仅用于显示历史数据）
        end_year: int 结束年份（用于预测的起点）
        predict_years: int 预测未来的年份范围

    返回:
        Plotly 图表对象
    """
    # 读取数据
    file_path = './data/gmsl_data.csv'
    data = pd.read_csv(file_path)

    # 根据年份范围筛选数据，仅用于显示历史数据
    filtered_data = data[(data['year_fraction'] >= start_year) & (data['year_fraction'] <= end_year)]

    # 使用默认训练数据范围（1993-2024）进行预测
    future_years, future_predictions = predict_future_sea_level(data, end_year, predict_years)

    # 创建历史数据的图表
    trace_actual = go.Scatter(
        x=filtered_data['year_fraction'],
        y=filtered_data['GMSL_GIA_applied'],
        mode='lines+markers',
        name='Observed GMSL',
        hovertemplate='Year: %{x}<br>GMSL: %{y} mm<br>',
    )

    # 创建预测数据的图表
    trace_predicted = go.Scatter(
        x=future_years,
        y=future_predictions,
        mode='lines',
        name='Predicted GMSL',
        line=dict(dash='dot', color='red'),
        hovertemplate='Year: %{x}<br>Predicted GMSL: %{y} mm<br>',
    )

    # 定义布局
    layout = go.Layout(
        title=f'Global Mean Sea Level Change ({start_year} - {end_year + predict_years})',
        xaxis=dict(title='Year (Fraction)', gridcolor='lightgray'),
        yaxis=dict(title='Global Mean Sea Level (mm)', gridcolor='lightgray'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        template='plotly_white'
    )

    # 创建图表对象
    figure = go.Figure(data=[trace_actual, trace_predicted], layout=layout)
    return figure

def generate_analysis(start_year, end_year):
    """
    根据起始年份和结束年份生成海平面变化的分析。

    参数:
        start_year: int 起始年份
        end_year: int 结束年份

    返回:
        str 包含分析结果的字符串
    """
    # 读取数据
    file_path = './data/gmsl_data.csv'
    data = pd.read_csv(file_path)

    # 筛选指定年份范围内的数据
    filtered_data = data[(data['year_fraction'] >= start_year) & (data['year_fraction'] <= end_year)]

    # 如果没有数据，返回提示
    if filtered_data.empty:
        return f"No data available for the years {start_year} to {end_year}."

    # 计算分析数据
    start_gmsl = filtered_data['GMSL_GIA_applied'].iloc[0]
    end_gmsl = filtered_data['GMSL_GIA_applied'].iloc[-1]
    gmsl_change = end_gmsl - start_gmsl
    mean_gmsl = filtered_data['GMSL_GIA_applied'].mean()
    max_gmsl = filtered_data['GMSL_GIA_applied'].max()
    min_gmsl = filtered_data['GMSL_GIA_applied'].min()

    # 从模板中随机选择一个句式
    template = random.choice(ll.ANALYSIS_SEA_Sentence_Templates)
    analysis = template.format(
        start_year=start_year,
        end_year=end_year,
        start_gmsl=start_gmsl,
        end_gmsl=end_gmsl,
        gmsl_change=gmsl_change,
        mean_gmsl=mean_gmsl,
        max_gmsl=max_gmsl,
        min_gmsl=min_gmsl
    )

    return analysis


def generate_advice(start_year, end_year):
    """
    根据指定的年份范围，从气象灾难语料库中随机选择三个气象灾难，并给出相关建议。

    参数:
        start_year: int 起始年份
        end_year: int 结束年份

    返回:
        str 包含气象灾难事件和建议的字符串
    """
    # 筛选指定年份范围内的气象灾难
    disasters_in_range = {year: event for year, event in ll.climate_disasters.items() if start_year <= year <= end_year}

    # 如果指定范围内没有灾难事件
    if not disasters_in_range:
        return f"No significant meteorological disasters occurred between {start_year} and {end_year}."

    # 随机选择三个气象灾难
    selected_years = random.sample(list(disasters_in_range.keys()), 2)
    selected_disasters = [disasters_in_range[year] for year in selected_years]

    # 为每个灾难生成相关建议
    advice = []
    for year in selected_years:
        advice.append(ll.environmental_recommendations.get(year, "No specific advice available."))

    # 返回完整的分析和建议
    result = f"From {start_year} to {end_year}, the following meteorological disasters have been observed:\n"
    for disaster in selected_disasters:
        result += f"{disaster}\n"
        result += '\n'

    # 添加建议部分
    result += "\nAdvice:\n"
    result += '\n'
    for advice_text in advice:
        result += f"{advice_text}\n"
        result += '\n'

    return result



if __name__ == '__main__':
    figure = create_prediction_plot(2000, 2024, 10)
    figure.show()

