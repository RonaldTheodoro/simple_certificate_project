from datetime import date

from consts import CertificateStatus
from entity.parsed_data import ParsedData
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
    worker.parse_certificate_data()
    assert worker.certificate.parsed_data is not None
    assert isinstance(worker.certificate.parsed_data, ParsedData)
    assert worker.certificate.parsed_data.publication_date == date(2023, 5, 27)
    assert worker.certificate.parsed_data.expiration_date == date(2023, 8, 24)
    assert worker.certificate.parsed_data.protocol == "2023.000003446271-04"
    assert (
        worker.certificate.parsed_data.certificate_status
        is CertificateStatus.CONSTA
    )
    worker.save_certificate()
    assert worker.certificate.report == {
        "worker": 1,
        "cpf": "11111111111",
        "certificate_status": 1,
        "expiration_date": '24/08/2023',
        "publication_date": '27/05/2023',
        "protocol": "2023.000003446271-04",
    }


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
    worker.parse_certificate_data()
    assert worker.certificate.parsed_data is not None
    assert isinstance(worker.certificate.parsed_data, ParsedData)
    assert worker.certificate.parsed_data.publication_date == date(2023, 5, 27)
    assert worker.certificate.parsed_data.expiration_date == date(2023, 8, 24)
    assert worker.certificate.parsed_data.protocol == "2023.000003446272-95"
    assert (
        worker.certificate.parsed_data.certificate_status
        is CertificateStatus.NAO_CONSTA
    )
    assert worker.certificate.report == {
        "worker": 1,
        "cnpj": "00000000000000",
        "certificate_status": 2,
        "expiration_date": '24/08/2023',
        "publication_date": '27/05/2023',
        "protocol": "2023.000003446272-95",
    }
