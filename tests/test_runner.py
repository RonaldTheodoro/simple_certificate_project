from runner import Runner


def test_runner_pf():
    document = "11111111111"
    runner = Runner()
    certificate = runner({"cpf": document, "person": 1, "worker": 1})
    assert certificate.document == document
    assert certificate.worker == 1


def test_runner_pj():
    document = "00000000000000"
    runner = Runner()
    certificate = runner({"cnpj": document, "person": 2, "worker": 1})
    assert certificate.document == document
    assert certificate.worker == 1
