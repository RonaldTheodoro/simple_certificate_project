from workers.register import register
from workers.base import BaseWorker
from commons.load_resource import load_resource
from commons.convert_pdf_to_text import convert_pdf_to_text
from commons.parse_regex_or_raise_error import parse_regex_or_raise_error
from entity import ParsedData
from consts import CertificateStatus


@register(1)
class WorkerSefazPE(BaseWorker):
    def download_certificate_document(self):
        self.certificate.pdf = load_resource(
            "certificates/sefazpe/sefazpe_cnpj.pdf", mode="rb"
        )

    def parse_certificate_data(self):
        pdf_text = convert_pdf_to_text(self.certificate.pdf)

        publication_date = parse_regex_or_raise_error(
            r'DADOS DO REQUERENTE(?P<publication_date>\d{2}/\d{2}/\d{4})',
            pdf_text
        )
        expiration_date = parse_regex_or_raise_error(
            r'sefaz\.pe\.gov\.br\.(?P<expiration_date>\d{2}/\d{2}/\d{4})',
            pdf_text
        )
        protocol = parse_regex_or_raise_error(
            r'(?P<protocol>\d{4}\.\d{12}-\d{2}) Número:',
            pdf_text
        )

        parsed_data = ParsedData()
        parsed_data.publication_date = publication_date.group('publication_date')
        parsed_data.expiration_date = expiration_date.group('expiration_date')
        parsed_data.protocol = protocol.group('protocol')
        parsed_data.certificate_status = CertificateStatus.CONSTA
        self.certificate.parsed_data = parsed_data
