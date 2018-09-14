# -*- coding:utf-8 -*-
# flask 有两个默认的文件夹 templates默认的模板文件夹 ,static默认的静态文件夹
from flask import  Flask
from flask import render_template  # 基于jinja2
from flask import request
app = Flask(__name__)
@app.route('/')     # /=定义的页面
def index():
    # 处理当前定义的这个页面的请求的响应
    return  render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files.get('file')
    filename = file.filename
    file.save('static/%s'%filename)
    return ('static/%s'%filename)
if __name__ == '__main__':
    app.run(debug=True)