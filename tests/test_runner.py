from runner import Runner


def test_runner_pf():
    document = "11111111111"
    runner = Runner()
    worker = runner({"cpf": document, "person": 1, "worker": 1})
    assert worker.certificate.document == document
    assert worker.certificate.worker == 1
    assert worker.certificate.pdf is None
    worker.download_certificate_document()
    assert worker.certificate.pdf is not None
    assert isinstance(worker.certificate.pdf, bytes)


def test_runner_pj():
    document = "00000000000000"
    runner = Runner()
    worker = runner({"cnpj": document, "person": 2, "worker": 1})
    assert worker.certificate.document == document
    assert worker.certificate.worker == 1
    assert worker.certificate.pdf is None
    worker.download_certificate_document()
    assert worker.certificate.pdf is not None
    assert isinstance(worker.certificate.pdf, bytes)
