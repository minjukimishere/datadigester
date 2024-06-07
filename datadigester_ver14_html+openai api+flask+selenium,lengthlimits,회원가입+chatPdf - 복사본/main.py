from chromadb import ChromaDB
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter


def process_pdf(file_path, question):
    # Load and split PDF
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.split_documents(pages)

    # Create embeddings
    embeddings_model = OpenAIEmbeddings(api_key="sk-proj-ej3Oeiw2RQISNgFiwq7AT3BlbkFJ3b03ApL2SsGdivEsh0tB")

    # Initialize ChromaDB and store documents
    db = ChromaDB()
    db.add_documents(texts, embeddings_model)

    # Initialize LLM
    llm = ChatOpenAI(temperature=0, api_key="sk-proj-ej3Oeiw2RQISNgFiwq7AT3BlbkFJ3b03ApL2SsGdivEsh0tB")

    # Create RetrievalQA chain
    retriever = db.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=retriever)
    
    # Run query and return result
    result = qa_chain({"query": question})
    return result