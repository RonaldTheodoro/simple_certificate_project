from abc import ABC, abstractmethod


class BaseWorker(ABC):
    def __init__(self, certificate):
        self.certificate = certificate

    @abstractmethod
    def download_certificate_document(self):
        pass

    @abstractmethod
    def parse_certificate_data(self):
        pass
