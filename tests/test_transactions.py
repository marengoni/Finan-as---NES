from finances import Transaction

def get_transaction():
    return Transaction(100.0, 1, "Transação de Teste")

def test_transaction_instance():
    tr= get_transaction
    assert isinstence(tr, Transaction), "Falha ao instanciar um objeto Transaction."

def test_transaction_atributes():
    tr= Transaction(100.0, 1, "Transação de Teste")