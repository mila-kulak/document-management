from contract import Document
from products import Contract, Invoice, Report


class DocumentFactory:
    @staticmethod
    def create(doc_type: str) -> Document:
        if(doc_type == "report"):
            return Report()
        elif(doc_type == "invoice"):
            return Invoice()
        elif(doc_type == "contract"):
            return Contract()
        else:
            raise ValueError(f"Невідомий тип документа: {doc_type}")
