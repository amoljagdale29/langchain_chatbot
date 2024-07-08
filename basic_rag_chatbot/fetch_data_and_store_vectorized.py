from langchain_community.document_loaders import WikipediaLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings


def search_and_load_data(search_term: str = "Indian Premier League 2024", save_folder: str = "db", collection_name: str = "ipl-embeddings"):
    """
    searches given terms in wikipedia and save embedding in db folder
    :param collection_name: str, name of collection to save data in.
    :param save_folder: location and name of folder to save data
    :param search_term: str
    :return:
    """
    data = WikipediaLoader(query=search_term).load()
    embeddings = HuggingFaceEndpointEmbeddings()

    store = Chroma.from_documents(
        data,
        embeddings,
        ids=[f"{item.metadata['source']}-{index}" for index, item in enumerate(data)],
        collection_name=collection_name,
        persist_directory=save_folder,
    )
    store.persist()
    return


if __name__ == '__main__':
    input_search_keyword = input()
    search_and_load_data(search_term=input_search_keyword)
