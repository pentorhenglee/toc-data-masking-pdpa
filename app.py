"""
ToC Assignment - Data Masking for PDPA
------------------------------------------------
This is the MOST BASIC Flask app (same starting point as the tutorial).
It only proves your setup works. Everything else is up to us to build.

Run:
    python app.py
Then open http://127.0.0.1:5000  ->  you should see "Setup works!"

WHERE TO GO FROM HERE (do NOT just copy a tutorial line-by-line):
  1. Make this route render an HTML page with an input box + submit button.
  2. Accept the submitted text (look up: request.form, methods=["GET","POST"]).
  3. Run that text through OUR masking logic (regex with Python `re`).
  4. Show the censored result back on the page.
  5. Make it look good (CSS) - design is graded.

Think through the regex yourselves - that's the whole point of the assignment.
"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Setup works! Now go build the data-masking app. See README.md."

@app.route("/knock", methods=["GET", "POST"])
def knock():
    if request.method == "POST":
        return "มีคนเคาะ"
    return '<form method="post"><input name="who"><button>ส่ง</button></form>'

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        return "สวัสดี" + render_template("greet.html", message="who")
    return render_template("greet.html", message="who")

@app.route("/about")
def about():
    return "กลุ่มของโดม"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
