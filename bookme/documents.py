from django_elasticsearch_dsl import Document
from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections, Search, Index
from django_elasticsearch_dsl.registries import registry
from .models import Book

client = Elasticsearch()
my_search = Search(using=client)
connections.create_connection()

# book = Index('book')
#
# book.settings(
#         number_of_shrads=1,
#         number_of_replicas=0
# )

@registry.register_document
class BookDocument(Document):
    class Index:
        name = 'book'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}


    class Django:
        model = Book
        fields = ['title','isbn','category']

def search(title):
    query = my_search.query("match", title=title)
    response = query.execute()
    return response
