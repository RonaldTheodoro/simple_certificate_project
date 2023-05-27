from entity import Certificate
from workers.register import register


class Runner:
    def __call__(self, payload):
        certificate = Certificate(payload)
        worker_cls = register.get_worker(certificate.worker)
        return worker_cls(certificate)
