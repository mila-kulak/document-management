from contract import Document


class Report(Document):
    def render(self) -> str:
        return "Звіт"
class Invoice(Document):
    def render(self) -> str:
        return "Рахунок-фактура"
class Contract(Document):
    def render(self) -> str:
        return "Контракт"
