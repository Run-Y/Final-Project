import numpy as np
import pandas as pd
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression

def create_plot(start_year, end_year, ice_mass_type):

    # 根据选择的文件加载不同的数据
    if ice_mass_type == "Antarctic":
        file_path = './data/antarctica_mass_data.csv'
    elif ice_mass_type == "Greenland":
        file_path = './data/greenland_mass_data.csv'
    else:
        raise ValueError("Invalid ice_mass_type. Choose 'Antarctic' or 'Greenland'.")

    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        return None

    # 根据年份范围筛选数据
    filtered_data = data[(data['TIME (year.decimal)'] >= start_year) & (data['TIME (year.decimal)'] <= end_year)]

    # 根据选择的数据集设置纵坐标
    if ice_mass_type == "Antarctic":
        mass_column = 'Antarctic mass (Gigatonnes)'
        uncertainty_column = 'Antarctic mass 1 - sigma uncertainty (Gigatonnes)'
        title = "Antarctic Mass"
    else:
        mass_column = 'Greenland mass (Gigatonnes)'  # 假设你有 Greenland 数据列
        uncertainty_column = 'Greenland mass 1-sigma uncertainty (Gigatonnes)'  # 假设你有 Greenland 的 uncertainty 列
        title = "Greenland Mass"

    # 创建 Plotly 图表
    trace = go.Scatter(
        x=filtered_data['TIME (year.decimal)'],  # 横坐标为 Time
        y=filtered_data[mass_column],  # 纵坐标为对应的 Mass
        mode='lines+markers',
        name=title,
        hovertemplate='Time: %{x}<br>' +
                      f'{title}' + '%{y}(Gigatonnes)' + f' (±{filtered_data[uncertainty_column].iloc[0]})'  # 显示不确定性
    )

    layout = go.Layout(
        title=f'{title} Mass Loss ({start_year} - {end_year})',
        xaxis=dict(title='Time'),
        yaxis=dict(title=f'{title} Mass (Gigatonnes)'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        template='plotly_white'
    )

    figure = go.Figure(data=[trace], layout=layout)
    return figure

def predict_future_ice_mass(data, end_year, predict_years):
    """
    根据现有数据预测未来的冰层质量变化。

    参数:
        data: DataFrame 包含所有历史数据
        end_year: int 当前数据的最后一年
        predict_years: int 需要预测的年份范围

    返回:
        future_years: ndarray 包含预测的年份
        future_predictions: ndarray 包含预测的冰层质量 (Gigatonnes)
    """
    # 确保 predict_years 是整数
    if not isinstance(predict_years, int):
        raise TypeError(f"`predict_years` must be an integer, got {type(predict_years)} instead.")

    # 硬编码使用 2002 年到 2024 年作为训练数据
    training_data = data[(data['TIME (year.decimal)'] >= 2002) & (data['TIME (year.decimal)'] <= 2024)]

    # 准备用于训练的特征和目标值
    X_train = training_data[['TIME (year.decimal)']]  # 时间列
    y_train = training_data.iloc[:, 1]  # 第二列是冰山质量（Antarctic 或 Greenland）

    # 训练线性回归模型
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 生成未来年份数据
    future_years = np.arange(end_year, end_year + predict_years, 1)
    future_X = pd.DataFrame({'TIME (year.decimal)': future_years})

    # 预测未来的冰层质量
    future_predictions = model.predict(future_X)

    return future_years, future_predictions

def create_prediction_plot(start_year, end_year, predict_years, ice_mass_type):
    """
    基于历史数据绘制包含预测的冰层质量变化图表。

    参数:
        start_year: int 起始年份（仅用于显示历史数据）
        end_year: int 结束年份（用于预测的起点）
        predict_years: int 预测未来的年份范围
        ice_mass_type: str 'Antarctic' 或 'Greenland'，决定读取哪个数据文件

    返回:
        Plotly 图表对象
    """
    # 根据选择的冰山类型设置文件路径
    if ice_mass_type == "Antarctic":
        file_path = './data/antarctica_mass_data.csv'
    elif ice_mass_type == "Greenland":
        file_path = './data/greenland_mass_data.csv'
    else:
        raise ValueError("Invalid ice_mass_type. Choose 'Antarctic' or 'Greenland'.")

    # 读取数据
    data = pd.read_csv(file_path)

    # 根据年份范围筛选数据，仅用于可视化历史数据
    filtered_data = data[(data['TIME (year.decimal)'] >= start_year) & (data['TIME (year.decimal)'] <= end_year)]

    # 使用默认训练数据范围（2002-2024）进行预测
    future_years, future_predictions = predict_future_ice_mass(data, end_year, predict_years)

    # 创建历史数据的图表
    trace_actual = go.Scatter(
        x=filtered_data['TIME (year.decimal)'],
        y=filtered_data.iloc[:, 1],  # 第二列是冰山质量（Antarctic 或 Greenland）
        mode='lines+markers',
        name=f'Observed {ice_mass_type} Ice Mass',
        hovertemplate=f'Year: %{{x}}<br>Mass: %{{y}} Gigatonnes<br>',
    )

    # 创建预测数据的图表
    trace_predicted = go.Scatter(
        x=future_years,
        y=future_predictions,
        mode='lines',
        name=f'Predicted {ice_mass_type} Ice Mass',
        line=dict(dash='dot', color='red'),
        hovertemplate=f'Year: %{{x}}<br>Predicted Mass: %{{y}} Gigatonnes<br>',
    )

    # 定义布局
    layout = go.Layout(
        title=f'{ice_mass_type} Ice Mass Change ({start_year} - {end_year + predict_years})',
        xaxis=dict(title='Year (Decimal)', gridcolor='lightgray'),
        yaxis=dict(title=f'{ice_mass_type} Ice Mass (Gigatonnes)', gridcolor='lightgray'),
        plot_bgcolor='white',
        paper_bgcolor='white',
        template='plotly_white'
    )

    # 创建图表对象
    figure = go.Figure(data=[trace_actual, trace_predicted], layout=layout)
    return figure

# 调用示例
if __name__ == "__main__":
    start_year = 2002
    end_year = 2022
    predict_years = 10
    ice_mass_type = "Greenland"  # 或者 "Greenland"

    figure = create_plot(start_year, end_year, ice_mass_type)
    figure.show()  # 显示图表
