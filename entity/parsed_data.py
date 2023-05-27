import re
from datetime import date

from consts import CertificateStatus


class ParsedData:
    def __init__(self):
        self.__publication_date = None
        self.__expiration_date = None
        self.__protocol = None
        self.__certificate_status = CertificateStatus.SEM_STATUS

    @property
    def publication_date(self):
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, value):
        if not isinstance(value, date):
            value = self.__convert_str_to_date(value)
        self.__publication_date = value

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        if not isinstance(value, date):
            value = self.__convert_str_to_date(value)
        self.__expiration_date = value

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, value):
        self.__protocol = value

    @property
    def certificate_status(self):
        return self.__certificate_status

    @certificate_status.setter
    def certificate_status(self, value):
        self.__certificate_status = value

    def __convert_str_to_date(self, value):
        match = re.match(
            r"(?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{4})", value
        )
        value = date(
            int(match.group("year")),
            int(match.group("month")),
            int(match.group("day")),
        )
        return value
