from runner import Runner
from entity import ParsedData

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
    assert worker.certificate.parsed_data is None
    worker.parse_certificate_data()
    assert worker.certificate.parsed_data is not None
    assert isinstance(worker.certificate.parsed_data, ParsedData)


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
    assert worker.certificate.parsed_data is None
    worker.parse_certificate_data()
    assert worker.certificate.parsed_data is not None
    assert isinstance(worker.certificate.parsed_data, ParsedData)
