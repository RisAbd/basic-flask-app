from flask import Flask, render_template



app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def index():

    return render_template('index.html'), 200



if __name__ == '__main__':
    app.run('0.0.0.0', 5123, debug=True, threaded=True)

