from pymongo import MongoClient


class Banco:
    def __init__(self, string_connection:str, string_bank:str) -> None:
        self._string_connection = string_connection
        self._client = MongoClient(string_connection)
        self._db_connection = self._client[string_bank]
    
    def get_collection(self, string_collection:str):
        return self._db_connection.get_collection(string_collection)
    
    def add_document(self, string_collection:str, document:dict):
        collection = self._db_connection.get_collection(string_collection)
        collection.insert_one(document)
    
    def find_document(self, string_collection:str, data_type:dict):
        collection = self.get_collection(string_collection)
        response = collection.find(data_type)
        
        documents = []
        for document in response:
            del document['_id']
            documents.append(document)
        return documents

    def get_last_document(self, string_collection):
        collection = self._db_connection.get_collection(string_collection)
        last_document = collection.find().sort('_id', -1).limit(1)
    
        for document in last_document:
            del document['_id']
            return document

if __name__ == '__main__':
    string_connection = 'mongodb://localhost:27017'
    string_bank = 'Biblioteca-MEPB'
    
    bancon_mg = Banco(string_connection=string_connection, string_bank=string_bank)
    
    ff = bancon_mg.find_document(string_collection='livros', data_type={'disponivel': False})
    
    collection = bancon_mg.get_collection(string_collection='livros')
    
    ultimo_documento = collection.find().sort('_id', -1).limit(1)
    
    for documento in ultimo_documento:
        del documento['_id']