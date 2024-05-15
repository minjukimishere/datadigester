from flask import Flask, render_template, request, jsonify
from main import generate_summary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    result = generate_summary(query)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)