import os

from flask import (Flask, jsonify, redirect, render_template, request, session,
                   url_for)
from werkzeug.utils import secure_filename

from auto_news import collect_news_titles
from auto_web import download_pdf_and_extract_text
from main import generate_summary
from pdf import process_pdf

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock database
users = {}

# Create the directory if it doesn't exist
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        if username in users and users[username] == password:
            session['username'] = username
            return jsonify(success=True)
        else:
            return jsonify(success=False)
    return render_template('login.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        if username not in users:
            users[username] = password
            return jsonify(success=True, message="회원가입 성공! 2초 후 로그인 페이지로 이동합니다.")
        else:
            return jsonify(success=False, message="이미 존재하는 아이디입니다.")
    return render_template('signup.html')

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/university")
def university():
    search_history = session.get('search_history', [])
    return render_template('index.html', search_history=search_history)

@app.route("/dailyreport")
def daily_report():
    return render_template('daily_report.html')

@app.route('/generate_summary', methods=['POST'])
def generate_summary():
    user_input = request.form['user_input']
    chat_query = f"{user_input}에 대한 자료조사 결과를 500자 이상의 한글로 요약해줘."
    result = chain.invoke({"input": chat_query})
    return jsonify({"summary": result})

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        temp_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(temp_path)
        session['temp_path'] = temp_path
        return render_template('chat_pdf.html', pdf_text="File uploaded successfully.")
    return 'No file provided'

@app.route('/ask-question', methods=['POST'])
def ask_question():
    question = request.form['question']
    if 'temp_path' in session:
        temp_path = session['temp_path']
        result = process_pdf(temp_path, question)
        return render_template('chat_pdf.html', pdf_text="File uploaded successfully.", answer=result['result'])
    return render_template('chat_pdf.html', answer="문서를 먼저 업로드해주세요.")

# 채팅 페이지
@app.route("/chat")
def chat():
    return render_template('chat_pdf.html')

@app.route('/get-news-titles', methods=['POST'])
def get_titles():
    data = request.json
    titles = collect_news_titles(data['query'])
    return jsonify(titles)

@app.route('/generate-summary', methods=['POST'])
def summarize():
    titles = request.json['titles']
    summary = generate_summary(' '.join(titles))
    return jsonify({"result": summary})

@app.route('/search_news', methods=['POST'])
def search_news():
    data = request.get_json()
    query = data['query']
    result = generate_summary(query)
    return jsonify(result)

@app.route('/some-endpoint', methods=['POST'])
def process_query():
    data = request.json
    query = data['query']
    titles = collect_news_titles(query)
    title_string = ' '.join(titles)
    result = generate_summary(title_string)
    return jsonify({"result": result})

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    pdf_text = download_pdf_and_extract_text(query)
    result = generate_summary(pdf_text)
    if 'search_history' not in session:
        session['search_history'] = []
    session['search_history'].append(query)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
