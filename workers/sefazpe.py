from workers.register import register
from workers.base import BaseWorker
from commons.load_resource import load_resource
from commons.convert_pdf_to_text import convert_pdf_to_text
from commons.parse_regex_or_raise_error import parse_regex_or_raise_error
from entity import ParsedData
from consts import CertificateStatus


@register(1)
class WorkerSefazPE(BaseWorker):
    FIELDS_REGEX = {
        "publication_date": r"DADOS DO REQUERENTE(?P<publication_date>\d{2}/\d{2}/\d{4})",
        "expiration_date": r"sefaz\.pe\.gov\.br\.(?P<expiration_date>\d{2}/\d{2}/\d{4})",
        "protocol": r"(?P<protocol>\d{4}\.\d{12}-\d{2}) Número:",
    }

    def download_certificate_document(self):
        self.certificate.pdf = load_resource(
            "certificates/sefazpe/sefazpe_cnpj.pdf", mode="rb"
        )

    def parse_certificate_data(self):
        pdf_text = convert_pdf_to_text(self.certificate.pdf)

        fields = self.__parse_mandatory_fields(pdf_text)

        parsed_data = ParsedData()
        parsed_data.publication_date = fields["publication_date"]
        parsed_data.expiration_date = fields["expiration_date"]
        parsed_data.protocol = fields["protocol"]
        parsed_data.certificate_status = CertificateStatus.CONSTA
        self.certificate.parsed_data = parsed_data

    def __parse_mandatory_fields(self, pdf_text):
        fields = {}
        for key, regex in self.FIELDS_REGEX.items():
            m = parse_regex_or_raise_error(regex, pdf_text)
            fields[key] = m.group(key)
        return fields
