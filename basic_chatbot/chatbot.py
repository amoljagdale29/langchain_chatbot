import chainlit as cl
from langchain import HuggingFaceHub, PromptTemplate, LLMChain
from langchain.memory import ConversationBufferMemory

model_id = "mistralai/Mistral-7B-Instruct-v0.3"
conv_model = HuggingFaceHub(task="conversational",
                            repo_id=model_id,
                            model_kwargs={"temperature": 0.1, "return_full_text": False},
                            )


@cl.on_chat_start
def main():
    template = """You are Financial Advisor, you help get people with suggestion for there portfolio.
    # {chat_history}
    Human: {human_input}
    Chatbot:"""

    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], template=template
    )
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm_chain = LLMChain(
        llm=conv_model,
        prompt=prompt,
        verbose=0,
        memory=memory,
    )
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message):
    llm_chain = cl.user_session.get("llm_chain")
    res = llm_chain.predict(human_input=message.content, stop=["\n\n    Human:"])
    await cl.Message(content=res).send()
