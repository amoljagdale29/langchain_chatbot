"""
To run

chainlit run rag_chatbot.py

creates chatbot with chainlit UI
"""
import chainlit as cl
import os
from langchain import HuggingFaceHub, PromptTemplate
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings
os.environ["OTEL_SDK_DISABLED"] = "true"
model_id = "mistralai/Mistral-7B-Instruct-v0.3"
conv_model = HuggingFaceHub(task="conversational",
                            repo_id=model_id,
                            model_kwargs={"temperature": 0.1,
                                          "return_full_text": False,
                                          "stop_token": ["\n\n    Human:"]},
                            )
embeddings_func = HuggingFaceEndpointEmbeddings()
store = Chroma(persist_directory=r"db",
               embedding_function=embeddings_func,
               collection_name="ipl-embeddings")


@cl.on_chat_start
def main():
    template = """You are a cricket expert that answers questions about IPL(Indian Premier League)
    context:
    # {context}
    End of context
    Do not answer questions outside of context.
    If you can't find answers in context, simply state that you don't know.
    Human: {question}
    Chatbot: """

    prompt = PromptTemplate(
        input_variables=["context", "question"], template=template
    )
    llm_chain = RetrievalQA.from_chain_type(
        llm=conv_model,
        chain_type="stuff",
        retriever=store.as_retriever(),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True,
    )
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message):
    llm_chain = cl.user_session.get("llm_chain")
    input_list = [{
        "query": message.content,
        "stop": ["\n\n    Human:"]  # List of stopping signals
    }]
    res = llm_chain.apply(input_list)[0]["result"]
    await cl.Message(content=res).send()
