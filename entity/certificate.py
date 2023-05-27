from entity.parsed_data import ParsedData


class Certificate:
    def __init__(self, payload):
        self.__payload = payload
        self.__pdf = None
        self.__parsed_data = ParsedData(self)

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
        return self.__payload["worker"]

    @property
    def pdf(self):
        return self.__pdf

    @pdf.setter
    def pdf(self, value):
        self.__pdf = value

    @property
    def parsed_data(self):
        return self.__parsed_data

    @parsed_data.setter
    def parsed_data(self, value):
        self.__parsed_data = value
