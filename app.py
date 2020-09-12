from flask import *
from util import *

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    td = action.readtable("")
    if not td:
        td = [('EMPTY', 'EMPTY', 'EMPTY', 'EMPTY')]
    return render_template("home.html", data=td, dataL=len(td))


# @app.route("/test")
# def test():
#     return render_template("test.html")


@app.route("/post", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        uname = request.form["username"]
        pwd = request.form["password"]
        action.write("", uname, pwd)

        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
