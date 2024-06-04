from flask import Flask, render_template, request, jsonify
from auto_web import download_pdf_and_extract_text
from main import generate_summary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    pdf_text = download_pdf_and_extract_text(query)  # 검색어로 PDF 다운로드 및 텍스트 추출
    result = generate_summary(pdf_text)  # 텍스트를 요약하여 결과 생성
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
