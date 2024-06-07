from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# open ai의 LLM 모델 사용
llm = ChatOpenAI(api_key="sk-proj-ej3Oeiw2RQISNgFiwq7AT3BlbkFJ3b03ApL2SsGdivEsh0tB")

# openai chat 설정. prompt 템플릿을 사용하고 긴 보고서 작성 요청
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI trained to generate in-depth and detailed reports. Your responses should be as comprehensive and extensive as possible."),
    ("user", "{input}")
])

# open ai의 결과를 문자열로 파싱
output_parser = StrOutputParser()

# Prompt, LLM, OutputParser를 연결하여 처리 체인 구성
chain = prompt | llm | output_parser

def generate_summary(input_text):
    query = "{input} 주제에 대한 심층적이고 자세한 분석을 바탕으로 매우 긴 보고서를 작성해달라. 여러 관점을 조합하여 분석하고, 가능한 많은 정보를 제공해야 한다. 요약은 다음과 같습니다: " + input_text + "에 대한 자세한 설명을 포함하여 최대한 길고 자세하게 보고서를 작성해주세요."
    result = chain.invoke({"input": query})
    return result