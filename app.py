from flask import Flask, render_template, request

app = Flask(__name__)
feedbacks = []

@app.route("/", methods=["GET", "POST"])
def feedback_form():
    if request.method == "POST":
        feedback = request.form.get("feedback")
        feedbacks.append(feedback)
    return render_template("index.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)