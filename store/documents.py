# documents.py

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl.fields import (
    TextField,
    IntegerField,
    BooleanField,
    DateField,
    CompletionField,
)

from .models import Product


autocomplete_analyzer = analyzer(
    "autocomplete_analyzer",
    tokenizer="standard",
    filter=[
        "lowercase",
        "stop",
        "snowball",
    ]
)


@registry.register_document
class ProductDocument(Document):

    title = TextField(
        analyzer=autocomplete_analyzer,
        fields={
            "raw": {
                "type": "keyword"
            }
        }
    )

    description = TextField(
        analyzer=autocomplete_analyzer
    )

    price = IntegerField()
    is_active = BooleanField()
    created_at = DateField()

    suggest = CompletionField()

    class Index:
        name = "products"

        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Django:
        model = Product

        fields = [
            "id",
        ]

    def prepare_suggest(self, instance):
        return [
            instance.title,
        ]