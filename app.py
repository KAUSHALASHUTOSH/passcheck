from flask import Flask, render_template, request, jsonify
from analyzer import analyze_password, generate_suggestions

app = Flask(__name__)
history = []  # 🔁 store last 5 passwords

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", endpoint="analyze_page")
def analyze():
    return render_template("analyze.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    password = data.get("password", "")

    verdict, score = analyze_password(password)
    suggestions = generate_suggestions(password)

    history.append(password)
    if len(history) > 5:
        history.pop(0)

    return jsonify({
        "verdict": verdict,
        "suggestions": suggestions,
        "history": list(reversed(history))
    })

if __name__ == "__main__":
    app.run(debug=True)
