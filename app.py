from flask import Flask, send_from_directory,request
import os

import aikido_zen
aikido_zen.protect()

app = Flask(__name__)

@app.route('/download')
def download_file():
    # 获取路径参数
    path = request.args.get('path')
    
    # 拼接完整文件路径
    file_path = os.path.join('data', path)
    
    # 提取目录和文件名
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    
    # 发送文件
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
