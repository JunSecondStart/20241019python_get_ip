from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def get_ip():
#     # リクエスト送信元のIPアドレスを取得
#     user_ip = request.remote_addr
#     return f"Your IP address is: {user_ip}"

@app.route('/')
def get_ip():
    if request.headers.getlist("X-Forwarded-For"):
        user_ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        user_ip = request.remote_addr
    return f"Your IP address is: {user_ip}"

if __name__ == '__main__':
    app.run()
