from flask import Flask

app = Flask(__name__)

@app.route('/raouf/pa', methods=['GET'])
def hello_world():
    return 'Joyeux Anniversaire Leny!'


