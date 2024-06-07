from langchain.chains import RetrievalQA
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def process_pdf(file_path, question):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )

    texts = text_splitter.split_documents(pages)

    embeddings_model = OpenAIEmbeddings(api_key="sk-proj-ej3Oeiw2RQISNgFiwq7AT3BlbkFJ3b03ApL2SsGdivEsh0tB")

    db = Chroma.from_documents(texts, embeddings_model)

    llm = ChatOpenAI(temperature=0, api_key="sk-proj-ej3Oeiw2RQISNgFiwq7AT3BlbkFJ3b03ApL2SsGdivEsh0tB")

    qa_chain = RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())
    result = qa_chain({"query": question})
    return result
