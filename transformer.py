from sentence_transformers import SentenceTransformers
from text import pdf_to_text_page

model = SentenceTransformer("all-MiniLM-L6-v2") # change to env configs

class Embedder():
    def __init__(self, model):
        self.model = model


    def embed_document(self, chunks):
        embeddings = self.model.encode(chunks)
        print(embeddings)
        embeddings



class ProcessDocument:
    def __init__(self, embedder, chunker, vector_store, iter_size = 1000):
        self.embedder = embedder
        self.chunker = chunker
        self.vector_store = vector_store
        self.iter_size = iter_size

    def load_documents(self, file, file_name):
        doc = pdf_text_to_page(file)
        chunker.set_doc(doc)
        chunks = self.chunker.chunk_documents()
        
        while True:
            points = []
            stop = False
            for _i in range(self.iter_size):
                i = chunks.next()
                if i is None:
                    stop = True
                text = i.join(' ')
                vector = self.embedder.embed_documents(text)
                points.append([{id: str(uuidv4()), vec  : vector, text : {"text": text}}])
            
            if stop:
                break
            self.vector_store.upsert(points)
    

class SearchVectorStore:
    def __init__(self, store,embed, collection_name, limit=3):
        self.store= store
        self.limit = limit
        self.embed = embed
        self.collection_name = collection_name

    def search_query(self, query):
        query_vector = self.embed.embed_document(query).tolist()
        self.store.search(query_vector)
