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

app = Flask(__name__)


@app.route("/")
def index():
    return "Setup works! Now go build the data-masking app. See README.md."


if __name__ == "__main__":
    app.run(debug=True)
