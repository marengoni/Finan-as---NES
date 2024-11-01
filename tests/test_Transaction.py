from finances import Transaction

def test_transaction():
    tr = Transaction()
    assert isinstence(tr, Transaction), "Falha ao instanciar um objeto Transaction."