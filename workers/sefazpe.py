from workers.register import register
from workers.base import BaseWorker
from commons.load_resource import load_resource
from entity import ParsedData


@register(1)
class WorkerSefazPE(BaseWorker):
    def download_certificate_document(self):
        self.certificate.pdf = load_resource(
            "certificates/sefazpe/sefazpe_cnpj.pdf", mode="rb"
        )

    def parse_certificate_data(self):
        parsed_data = ParsedData()
        parsed_data.publication_date = '27/05/2023'
        parsed_data.expiration_date = '24/08/2023'
        parsed_data.protocol = '2023.000003446271-04'
        self.certificate.parsed_data = parsed_data
        