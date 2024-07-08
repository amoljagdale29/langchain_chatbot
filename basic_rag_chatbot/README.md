# langchain_chatbot with  RAG / RetrievalQA
Create Chatbot using langchain,huggingface llm model, chainlit

# Specility

Bot is acting as Cricket Expert, you can ask question regarding IPL 2024 and general as well

# How to run?

I have used python 3.11, it should be fine with other version as well.
```
pip install -r requirement.txt
```
run fetch_data_and_store_vectorized and pass search terms as input default value is "Indian Premier League 2024"
```
python fetch_data_and_store_vectorized.py
```
```
chainlit run rag_chatbot.py -w
```


* Used chainlit to get User Interface of chatbot and on_send/on_receive message actions
* Used HuggingFace model 'mistralai/Mistral-7B-Instruct-v0.3' with api interface
* Can be run on any basic Machine, as inference via huggingface api
* Langchain used to predict and give prompt and memory to model
* Model can hold context as it retain conversation in memory

#### for using repo need to create free huggingface api and save it '.env' file as 

```
HUGGINGFACEHUB_API_TOKEN=hf_iXUYKJASkvPGrUfSVjoEaCHXXXXxxxxx
```