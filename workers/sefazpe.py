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
        self.certificate.parsed_data = ParsedData()
