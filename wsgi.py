from flask import Flask
import sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! with Python %s" % sys.version

if __name__ == "__main__":
    app.run()
