from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ---------------- LOGIN PAGE ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # demo validation
        if username == "sowmya" and password == "1234":
            return redirect(url_for("upload"))
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")


# ---------------- UPLOAD PAGE ----------------
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        resume_text = request.form.get("resume")
        return redirect(url_for("analysis", resume=resume_text))

    return render_template("upload.html")


# ---------------- ANALYSIS PAGE ----------------
@app.route("/analysis", methods=["GET", "POST"])
def analysis():
    resume = request.args.get("resume")

    # dummy AI analysis (later real NLP add pannalaam)
    score = 78
    skills = ["Python", "SQL", "Machine Learning"]
    experience = "2 Years"

    return render_template(
        "analysis.html",
        score=score,
        skills=skills,
        experience=experience
    )


# ---------------- DASHBOARD PAGE ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)
