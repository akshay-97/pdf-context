from abc import ABC
from qdrant_client import QdrantClient
from qdrant_client.http import models

class VectorStore(ABC):
    def upsert(self, points):
        pass

    def search(self, query_embeddings):
        pass


class QdrantStore(VectorStore):
    def __init__(self,url, collection_name = None, limit = 3):
        self.client = QdruantClient(url)
        self.collection_name=collection_name
        self.limit = limit

    def set_collection_name(self, collection_name):
        self.collection_name = self.collection_name

    def create_collection(self, collection_name):
        self.client.recreate_collection(
                collection_name=collection_name,
                vector_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
        )

    def upsert(self, points):
        if self.collection_name == None:
            raise ValueError("Initialize collection name")
        points' = list(map(lambda {id, vec, text} : models.PointStruct(id=id, vector=vec,payload=text),points))
        self.client.upsert(collection_name=self.collection_name,
                           points')

    def search(self, query_vector):
        if self.collection_name == None:
            raise ValueError("Init collection name")
       return  self.client.search(
                collection_name=self.collection_name,
                query_vector=query_vector,
                limit=self.limit
            )



