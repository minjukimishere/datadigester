### Daterdigester
html,css,jscript UI입니다.

1_datadigester in university,
2_daily report in company,
3_chating with PDF 


selenium을 이용하여 1_ 논문 pdf, 2_뉴스 크롤러 등의 형태로 
정보를 수집하여, langchain을 이용하여 데이터를 처리합니다.
chromaDB를 이용하여 벡터임베딩 작업을 거쳤습니다.
3_pdf데이터를 vector임베딩하여 chromaDB에서 langchain이 찾아
generate된 ai로 대화를 시도합니다.

## templates
    session 버전, sql 버전 중 session 버전입니다.    

# home.html
    첫화면, 로그인,회원가입 버튼 선택합니다.

# signup.html
    회원가입 화면입니다. 성공시 자동으로 로그인 페이지로 이동합니다.

# login.html
    로그인 화면입니다. main.html로 이동합니다.

# main.html
    datadigester in university (pdf수집처리기능) : index.html
    daily report in company (뉴스 크롤러) : daily_report.html
    chating with pdf : chat_pdf.html

    세 가지 기능 중 선택합니다.

# index.html
    검색어를 입력받아 google scholars 에서 검색합니다.
    검색한 결과의 자료조사 결과를 출력합니다.

# daily_report.html 
    검색어를 입력받아 네이버 뉴스 에서 검색합니다.
    검색한 결과를 daily report 형태로 출력합니다.

# chat_pdf.html 
    pdf를 업로드합니다. 업로드한 pdf의 내용과 chat을 지원합니다.

# app.py
    flask를 통해 html과 python 코드를 연결합니다.
    flask의 session(memory) 기능을 이용하여 회원가입을 구현하였습니다.

# auto_new.py
    네이버 뉴스 크롤러부분입니다. selenium을 이용하였습니다.
    제목만 크롤링 합니다.

# auto_web.py
    구글 schorlars PDF 크롤러 부분입니다. selenium을 이용하여 논문을 로컬 C드라이브에 다운로드하여 저장합니다.
    여러 개의 논문 내용을 combine하여 app.py를 통해 main.py (chromaDB)에 전달합니다.

# main_news.py
    auto_news에서 크롤링 된 데이터를 langchian % llm을 통해
    daily report를 작성하여 출력합니다.

# main.py
    auto_web.py 에서 combine 된 pdf data를 vector embedding하여 chroma DB에서 찾아 결과를 출력하는 llm 모델을 이용합니다. 

# pdf.py
    chat_pdf.html 에서 업로드 된 pdf 파일을 vector embedding하여 chromaDB에서 찾아 결과를 출력하는 llm 모델을 이용합니다. 

# chromedriver.exe
    크롬 125버전 이상을 지원합니다.

pip install langchain
pip install langchain-openai

# requirements.txt
(make package file)

pip freeze 
pip freeze > requirements.txt
pip freeze > config.toml

(package file downloader)
pip install -r requirements.txt

https://pypi.org/project/merge-requirements/

pip install merge-requirements


# main_chat.py (chromaDB 용례)

pdf로드->split->embedding->(vector)->chromadb->find data->generate open ai % llm

https://python.langchain.com/v0.1/docs/use_cases/question_answering/

https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf/

pip install PyPDF

pip install langchain-community

https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/

https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/

https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/

https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/recursive_text_splitter/

pip install langchain-core
pip install -qU langchain-text-splitters

https://python.langchain.com/v0.1/docs/modules/data_connection/text_embedding/

https://docs.trychroma.com/

pip install chromadb

https://python.langchain.com/v0.1/docs/integrations/vectorstores/chroma/

pip install langchain-chroma

Chroma runs in various modes. See below for examples of each integrated with LangChain.
    
    in-memory - in a python script or jupyter notebook (현재 버전, LAM)
    
    in-memory with persistance - in a script or notebook and save/load to disk 
    (# save to disk
        db2 = Chroma.from_documents(docs, embedding_function, persist_directory="./chroma_db")
        docs = db2.similarity_search(query))
    
    in a docker container - as a server running your local machine or in the cloud (다음목표)

https://python.langchain.com/v0.1/docs/modules/data_connection/document_transformers/split_by_token/#tiktoken

pip install tiktoken

https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/MultiQueryRetriever/

https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/

https://api.python.langchain.com/en/latest/chains/langchain.chains.retrieval_qa.base.RetrievalQA.html#langchain.chains.retrieval_qa.base.RetrievalQA


