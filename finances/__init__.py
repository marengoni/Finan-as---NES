from datetime import datetime

class Transaction:
    def __init__(self, amount, category, description):
        self.amount = float(amount)  # Converte o valor para float
        self.date = datetime.now()  # Data da transação como o momento atual
        self.category = int(category)  # Converte a categoria para int
        self.description = str(description)  # Converte a descrição para string
