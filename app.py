from flask import *
from use import *

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    td = read.readtable("")
    return render_template("home.html",data=td,dataL=len(td))


@app.route("/test")
def test():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)