from flask import Flask, render_template, request
from optimizer import optimize_study_time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    plan = None   # IMPORTANT: must be None

    if request.method == "POST":

        subjects = request.form.getlist("subject")
        difficulties = request.form.getlist("difficulty")
        hours = float(request.form["hours"])

        plan = optimize_study_time(subjects, difficulties, hours)

    return render_template("index.html", plan=plan)

if __name__ == "__main__":
    app.run(debug=True)