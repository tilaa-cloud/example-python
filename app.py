from flask import Flask
import time
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Running for %d seconds" % (time.time() - now)

if __name__ == "__main__":
    now = time.time()
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True,host='0.0.0.0',port=port)