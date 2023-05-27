from datetime import date

from entity import ParsedData
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
    assert worker.certificate.parsed_data is None
    worker.parse_certificate_data()
    assert worker.certificate.parsed_data is not None
    assert isinstance(worker.certificate.parsed_data, ParsedData)
    assert worker.certificate.parsed_data.publication_date == date(2023, 5, 27)
    assert worker.certificate.parsed_data.expiration_date == date(2023, 8, 24)
    assert worker.certificate.parsed_data.protocol == '2023.000003446271-04'


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
    assert worker.certificate.parsed_data.publication_date == date(2023, 5, 27)
    assert worker.certificate.parsed_data.expiration_date == date(2023, 8, 24)
    assert worker.certificate.parsed_data.protocol == '2023.000003446271-04'
