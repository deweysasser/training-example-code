from flask import Flask
import html

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    page = html.HTML('html')
    page.body().h1("Hello World")
    return str(page)

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
