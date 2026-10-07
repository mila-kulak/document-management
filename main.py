from factory import DocumentFactory

doc_type = input("Введіть тип документа (report, invoice, contract): ")

document = DocumentFactory.create(doc_type)
print (document.render())
