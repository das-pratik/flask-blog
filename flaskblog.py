from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/About')
def hello():
    return "<H1>Hello World!</H1>"

if __name__ == "__main__":
    app.run(debug=True)