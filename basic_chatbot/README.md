# langchain_chatbot
Create Chatbot using langchain,huggingface llm model, chainlit

# Specility

Bot is acting as Financial advisor, you can ask question regarding Finance and general as well
although its acting as Financial advisor it does not have latest data, its knowledge is just data its trained on
In future will add knowledge part through RAG system.

# How to run?

I have used python 3.11, it should be fine with other version as well.
```
pip install -r requirement.txt
```
```
chainlit run chatbot.py -w
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