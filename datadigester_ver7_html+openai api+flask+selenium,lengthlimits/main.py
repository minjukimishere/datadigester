from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# open ai의 LLM 모델 이용
llm = ChatOpenAI(api_key="sk-proj-yhsg5NrooNlcqRhn9sjkT3BlbkFJPVlyezvH9aCm3c4LlHeH")

# openai chat 설정. prompt 기능 사용
prompt = ChatPromptTemplate.from_messages([
    #AI 컨셉설정
    ("system", "You are a korean researcher conducting data collection to write a thesis at the university. Procced in the follwing order."), #AI 컨셉설정
    ("user", "{input}")
])

# open ai의 출력 기능 사용
output_parser = StrOutputParser()

# chain 으로 openAI의 3가지 기능 연결
chain = prompt | llm | output_parser

def generate_summary(query):
    # 요청할 텍스트의 양을 줄입니다.
    shortened_query = query[:4095]
    result = chain.invoke({"input":"{input}"+"논문 주제를 바탕으로 자료 조사를 했더니"+shortened_query +"이런 결과가 나왔어. 한글로 요약해줘"})
    return result