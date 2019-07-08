from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run()

    '''
    if you want to open application on localAreaNetwork
    '''
    # app.run(host='0.0.0.0')

    '''
    if you want to switch to debug mode
    '''
    # app.debug = True
    # app.run()
    ''' or '''
    # app.run(debug=True)
