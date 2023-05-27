from workers.register import register
from workers.base import BaseWorker
from commons.load_resource import load_resource
from commons.convert_pdf_to_text import convert_pdf_to_text
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
        parsed_data = ParsedData()
        parsed_data.publication_date = "27/05/2023"
        parsed_data.expiration_date = "24/08/2023"
        parsed_data.protocol = "2023.000003446271-04"
        parsed_data.certificate_status = CertificateStatus.CONSTA
        self.certificate.parsed_data = parsed_data
