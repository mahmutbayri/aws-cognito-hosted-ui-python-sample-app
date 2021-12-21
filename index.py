from flask import Flask, render_template, request
from dotenv import load_dotenv
from bootstrap import getAccessTokenFromCookie, getUser, getenv
from os import getenv

app = Flask(
    __name__,
    static_url_path='',
    static_folder='public',
    template_folder='views'
)

load_dotenv()  # take environment variables from .env.

@app.route('/index.html')
def index():
    user = None
    error = None
    try:
        user = getUser(getAccessTokenFromCookie(request.cookies))
    except Exception as e:
        error = str(e)

    return render_template("index.html", error=error, user=user, getenv=getenv)

@app.route('/login.html')
def login():
    return render_template("login.html", getenv=getenv)

@app.route('/logout.html')
def logout():
    return render_template("logout.html", getenv=getenv)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=getenv('PORT', 9800), debug='on')
