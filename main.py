# Import
from flask import Flask,redirect,url_for,render_template,request




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html',button_python=button_python)

@app.route('/', methods=['POST'])
def index2procces_form():
    button_python = request.form.get('button_python')
    return render_template('index2.html',button_python=button_python)

if __name__ == "__main__":
    app.run(port=4000, debug=True)

