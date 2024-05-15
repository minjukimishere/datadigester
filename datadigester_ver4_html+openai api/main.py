from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# open ai의 LLM 모델 이용
llm = ChatOpenAI(api_key="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")

# openai chat 설정. prompt 기능 사용
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a world class technical documentation writer."), #AI 컨셉설정
    ("user", "{input}")
])

# open ai의 출력 기능 사용
output_parser = StrOutputParser()

# chain 으로 openAI의 3가지 기능 연결
chain = prompt | llm | output_parser

def generate_summary(query):
    result = chain.invoke({"input": query + "에 대한 자료조사 결과를 500자 이상의 한글로 요약해줘"})
    return result
