from pymongo import MongoClient

from .enum_collections import TypeCollections


class Banco:
    def __init__(self, string_connection: str, string_bank: str) -> None:
        self._string_connection = string_connection
        self._client = MongoClient(string_connection)
        self._db_connection = self._client[string_bank]

    @staticmethod
    def _get_string_collection(type_collection: TypeCollections):
        match type_collection:
            case TypeCollections.LIVROS:
                return 'livros'
            case TypeCollections.ALUGUEIS:
                return 'alugueis'

    def _get_collection(self, type_collection: TypeCollections):
        return self._db_connection.get_collection(self._get_string_collection(type_collection))

    def add_document(self, type_collection: TypeCollections, document: dict) -> None:
        collection = self._get_collection(type_collection)
        collection.insert_one(document)

    def delete_document(self, type_collection: TypeCollections, code_document_delete: int) -> None:
        collection = self._get_collection(type_collection)
        collection.delete_one({'codigo': code_document_delete})

    def update_document(self, type_collection: TypeCollections, filter_document: dict, update_document: dict) -> None:
        collection = self._get_collection(type_collection)
        collection.update_one(filter=filter_document, update=update_document)

    def find_document(self, type_collection: TypeCollections, data_type: dict) -> list:
        collection = self._get_collection(type_collection)
        response = collection.find(data_type)
        documents = []

        for document in response:
            del document['_id']
            documents.append(document)
        return documents

    def exists_document(self, type_collection: TypeCollections, data_type: dict) -> bool:
        collection = self._get_collection(type_collection)
        response = collection.find(data_type)

        for _ in response:
            return True
        return False

    def get_last_document(self, type_collection) -> dict:
        collection = self._get_collection(type_collection)
        last_document = collection.find().sort('_id', -1).limit(1)

        for document in last_document:
            del document['_id']
            return document
        return {}
