from flask import Flask, render_template_string, request, redirect, url_for
import datetime

app = Flask(__name__)

login_page_html = """
<!DOCTYPE html>
<html>
<head>
    <title>登录</title>
</head>
<body>
    <p>{{ error_message | safe }}</p>
    <p>请输入账号密码：</p>
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="账号"><br>
        <input type="password" name="password" placeholder="密码"><br>
        <button type="submit">登录</button>
    </form>
    <p>当前时间：{{ current_time }}</p>
</body>
</html>
"""

game_center_html = """
<!DOCTYPE html>
<html>
<head>
    <title>游戏大厅</title>
</head>
<body>
    <p>欢迎：{{ username }}</p>
    <p>账户余额：{{ balance }}</p>
    <p>江湖群侠传：<a href="/game1">进入游戏</a></p>
    <p>枭雄online：<a href="/game2">进入游戏</a></p>
    <p>快速报时：{{ current_time }}</p>
</body>
</html>
"""

@app.route('/')
def login():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_message = request.args.get('error', '')
    return render_template_string(login_page_html, error_message=error_message, current_time=current_time)

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    # 这里添加验证逻辑
    if username == 'admin' and password == 'password':  # 示例验证逻辑
        return redirect(url_for('game_center'))  # 登录成功，跳转到游戏大厅
    else:
        return redirect(url_for('login', error='账号或密码错误！'))

@app.route('/game_center')
def game_center():
    # 假设通过session或其他方式获取用户名和余额
    username = "示例用户"
    balance = "1000"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(game_center_html, username=username, balance=balance, current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
