from app import app



if __name__ == '__main__':
    app.run('0.0.0.0', 5123, debug=True, threaded=True)
