from flask import Flask, render_template, request
from markupsafe import Markup
import plotly.io as pio
import ice_mass as im
import sea_level as sl

app = Flask(__name__)

# 根路径，显示首页
@app.route('/')
def index():
    return render_template('index.html')

# sea_level 路由，直接引用 sea_level.html
@app.route('/sea_level', methods=['GET', 'POST'])
def sea_level():
    if request.method == 'POST':
        # 从表单中获取用户输入的年份
        start_year = int(request.form['start_year'])
        end_year = int(request.form['end_year'])
        predict_years = int(request.form['predict_years'])

        if predict_years != 0:
            # 调用 sea_level.py 中的函数生成图表
            figure = sl.create_prediction_plot(start_year, end_year, predict_years)
        else:
            figure = sl.create_plot(start_year, end_year)

        # 将图表转换为 HTML 字符串
        graph_html = pio.to_html(figure, full_html=False)

        # 渲染 sea_level.html，同时传入生成的图表
        return render_template('sea_level.html', graph_html=graph_html)

    # 如果是 GET 请求，直接显示页面
    return render_template('sea_level.html', graph_html="")

# ice_mass 路由，直接引用 ice_mass.html
@app.route('/ice_mass', methods=['GET', 'POST'])
def ice_mass():
    if request.method == 'POST':
        # 获取表单数据
        data_file = request.form.get('data_file')
        start_year = int(request.form.get('start_year'))
        end_year = int(request.form.get('end_year'))
        predict_years = int(request.form['predict_years'])


        # 确定冰层类型
        if data_file == "antarctica_mass_data.csv":
            ice_mass_type = "Antarctic"
        elif data_file == "greenland_mass_data.csv":
            ice_mass_type = "Greenland"
        else:
            return "Invalid data file selected!", 400

        if predict_years != 0:
            # 调用 sea_level.py 中的函数生成图表
            figure = im.create_prediction_plot(start_year, end_year, predict_years, ice_mass_type)
        else:
            figure = im.create_plot(start_year, end_year, ice_mass_type)


        if figure is None:
            return "Error: Data file not found or invalid!", 500

        # 将图表转换为 HTML
        graph_html = Markup(figure.to_html(full_html=False, include_plotlyjs='cdn'))

        # 渲染模板，嵌入图表
        return render_template('ice_mass.html', graph_html=graph_html)

    # 默认 GET 请求直接返回表单页面
    return render_template('ice_mass.html', graph_html="")

if __name__ == '__main__':
    app.run(debug=True)
