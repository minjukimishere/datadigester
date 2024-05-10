from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import requests
from flask import Flask

# ChatOpenAI 인스턴스 생성
llm = ChatOpenAI(api_key="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")

# ChatPromptTemplate, StrOutputParser 초기화
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])
output_parser = StrOutputParser()

# Flask 앱 초기화
app = Flask(__name__)

# Streamlit 앱
def streamlit_app():
    # 타이틀
    st.title('자료 조사 프로그램')
    # 텍스트 인풋
    content = st.text_input("무엇이 궁금하신가요?", "")
    # 버튼
    if st.button("검색"):
        with st.spinner('요약 중입니다...'):
            # LLM을 통해 요약된 결과 가져오기
            result = chain.invoke({"input": content + "에 대한 자료조사 결과를 500자 이상의 한글로 요약해줘"})
            st.write(result)
    else:
        st.write("")

# Flask 앱 라우트 설정
@app.route("/")
def flask_route():
    return streamlit_app()

if __name__ == "__main__":
    # LLM과의 연결 설정
    chain = prompt | llm | output_parser
    # Streamlit 앱 실행
    st.set_page_config(page_title="자료 조사 프로그램")
    streamlit_app()
    # Flask 앱 실행
    app.run(host='0.0.0.0')


