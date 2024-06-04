from flask import (Flask, jsonify, redirect, render_template, request, session,
                   url_for)

from auto_web import download_pdf_and_extract_text
from main import generate_summary

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 세션 암호화를 위한 시크릿 키 설정

# Mock database
users = {}

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

@app.route("/company")
def company():
    return "Daily Report in Company 페이지입니다."

@app.route("/chat")
def chat():
    return "Chating with PDF 페이지입니다."

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    pdf_text = download_pdf_and_extract_text(query)  # 검색어로 PDF 다운로드 및 텍스트 추출
    result = generate_summary(pdf_text)  # 텍스트를 요약하여 결과 생성
    
    # 세션에 검색 기록 저장
    if 'search_history' not in session:
        session['search_history'] = []
    session['search_history'].append(query)
    
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
