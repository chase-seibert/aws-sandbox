from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! 3'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
