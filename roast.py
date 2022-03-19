from flask import Flask
from roastarray import roasterjson
app = Flask(__name__)


@app.route('/')
def hello_world():
    output = roasterjson()
    return output

if __name__ == '__main__':
   app.run()