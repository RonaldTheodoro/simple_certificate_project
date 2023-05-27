from workers.register import register
from workers.base import BaseWorker
from commons.load_resource import load_resource


@register(1)
class WorkerSefazPE(BaseWorker):
    def download_certificate_document(self):
        self.certificate.pdf = load_resource(
            "certificates/sefazpe/sefazpe_cnpj.pdf", mode="rb"
        )
