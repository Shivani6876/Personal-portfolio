from flask import Flask, render_template, request
import random

app = Flask(__name__)

quotes = {
    "motivation": [
        "Dream big. Do it bigger.",
        "Success is a journey, not a destination.",
        "Push yourself, because no one else will."
    ]
}

@app.route("/", methods=["GET", "POST"])
def home():
    quote = ""
    if request.method == "POST":
        topic = request.form.get("topic")
        quote = random.choice(quotes.get(topic, ["No quote found"]))
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
