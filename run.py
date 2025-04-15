from text import Chunker
from transformer import model, SearchVectorStore,Embedder,ProcessDocument
from store import QdrantStore


def main():
    doc1 = "database-design-and-implementation.pdf"
    embed  = Embedder(model)
    chunk = Chunker(None, 20, 5)
    vstore = QdrantStore("http://localhost:6333", "my_docs")
    vstore.create_collection("my_docs")

    process_doc = ProcessDocument(embed, chunk, vstore)
    process_doc.load_documents(doc1, "database_design")
    
    search = SearchVectorStore(vstore, embed, "my_docs", limit)

    while True:
        print("Enter Query : >> ")
        input_string = input()
        if input_string == "exit":
            break
        elif input_string == "\n":
            continue
        println("results : **")
        results = eearch.search_query(input_string)
        print(results)
        print("\n**")


if __name__ == '__main__':
    main()


