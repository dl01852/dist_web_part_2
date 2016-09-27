from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dom')
def dom():
    return render_template('domplay.html')
if __name__ == '__main__':
    app.run()
