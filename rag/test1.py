
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.chains import RetrievalQA
# from langchain.llms import OpenAI
# from langchain_community.document_loaders import PyPDFLoader

# def load_documents():
#     loader = PyPDFLoader("BZATic.pdf")
#     documents = loader.load()

#     text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,chunk_overlap = 200)
#     texts = text_splitter.split_documents(documents)
#     return texts

# def create_vector_store(texts):
#     embeddings = OpenAIEmbeddings()
#     vectorstore = FAISS.from_documents(texts,embeddings)
#     return vectorstore

# def setup_rag_chain(vectorstore):
#     llm = OpenAI(temperature = 0)
#     qa_chain = RetrievalQA.from_chain_type(llm = llm,chain_type = "stuff",retriever = vectorstore.as_retriever())
#     return qa_chain

# def ask_rag_question(question):
#     texts = load_documents()
#     vectorstore = create_vector_store(texts)
#     qa_chain = setup_rag_chain(vectorstore)
#     result = qa_chain({"query":question})
#     return result["result"]

# if __name__ == "__main__":
#     question = "How are travelling in that pdf?"
#     answer = ask_rag_question(question)
#     print(answer)






import os

from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_classic.chains import RetrievalQA
from langchain_community.vectorstores import FAISS


# --------------------------------------------------
# 1. Load PDF
# --------------------------------------------------
def load_documents():
    pdf_path = "BZATic.pdf"

    reader = PdfReader(pdf_path)

    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text() or ""

        if text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": pdf_path,
                        "page": page_number + 1
                    }
                )
            )

    return documents


# --------------------------------------------------
# 2. Split PDF text into chunks
# --------------------------------------------------
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    texts = text_splitter.split_documents(documents)

    return texts


# --------------------------------------------------
# 3. Create FAISS vector store
# --------------------------------------------------
def create_vector_store(texts):
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_documents(
        texts,
        embeddings
    )

    return vectorstore


# --------------------------------------------------
# 4. Create RAG chain
# --------------------------------------------------
def setup_rag_chain(vectorstore):
    llm = OpenAI(
        temperature=0
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    return qa_chain


# --------------------------------------------------
# 5. Main program
# --------------------------------------------------
def main():
    # Check API key
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY is not set.")
        print("Set your API key before running the program.")
        return

    print("Loading PDF...")

    documents = load_documents()

    if not documents:
        print("ERROR: No text could be extracted from the PDF.")
        return

    print(f"Loaded {len(documents)} pages.")

    print("Splitting document...")

    texts = split_documents(documents)

    print(f"Created {len(texts)} text chunks.")

    print("Creating FAISS vector store...")

    vectorstore = create_vector_store(texts)

    print("Creating RAG chain...")

    qa_chain = setup_rag_chain(vectorstore)

    print("\nRAG system is ready!")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Ask a question: ")

        if question.lower().strip() == "exit":
            print("Goodbye!")
            break

        if not question.strip():
            continue

        try:
            result = qa_chain.invoke(
                {"query": question}
            )

            print("\nAnswer:")
            print(result["result"])
            print()

        except Exception as e:
            print(f"\nError: {e}\n")


# --------------------------------------------------
# Run program
# --------------------------------------------------
if __name__ == "__main__":
    main()

