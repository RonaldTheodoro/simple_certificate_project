from workers.register import register

class Runner:
    def __call__(self, payload):
        certificate = Certificate(payload)
        worker_cls = register.get_worker(certificate.worker)
        return worker_cls(certificate)


class Certificate:
    def __init__(self, payload):
        self.__payload = payload

    @property
    def document(self):
        if self.is_pf:
            return self.cpf
        elif self.is_pj:
            return self.cnpj
        raise Exception("Invalid person")

    @property
    def is_pf(self):
        return self.__payload["person"] == 1

    @property
    def is_pj(self):
        return self.__payload["person"] == 2

    @property
    def cpf(self):
        return self.__payload["cpf"]

    @property
    def cnpj(self):
        return self.__payload["cnpj"]

    @property
    def worker(self):
        return self.__payload['worker']