from langchain_openai import ChatOpenAI

llm = ChatOpenAI(api_key="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")

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."),
    ("user", "{input}")
])

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

content="LLM"



#타이틀
import streamlit as st

st.title('자료 조사 프로그램')

#텍스트 인풋
import streamlit as st

content = st.text_input("무엇이 궁금하신가요?", "")

#버튼
import streamlit as st

if st.button("검색"):
    with st.spinner('요약 중입니다...'):
        result=chain.invoke({"input": content+"에 대한 자료조사 결과를 500자 이상의 한글로 요약해줘"})
        st.write(result)
else:
    st.write("")
