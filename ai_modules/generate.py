from langchain import hub
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

def generate_answer(retriever, llm, question):
    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    output = rag_chain.invoke(question)
    
    return output.split("Answer:")[1].strip()