from src.inspetor.model.inspetor_abstract_model import InspetorAbstractModel
from src.inspetor.exception.model_exception.inspetor_session_exception import InspetorSessionException

class InspetorSession(InspetorAbstractModel):
    def __init__(self):
        self.id = None
        self.datetime = None

    def is_valid(self):
        if self.id is None:
            raise InspetorSessionException(
                InspetorSessionException.REQUIRED_SESSION_ID
            )

        if self.datetime is None:
            raise InspetorSessionException(
                InspetorSessionException.REQUIRED_SESSION_DATETIME
            )

    #To understand this part, please read https://bit.ly/2ywz8PN
    @property
    def datetime(self):
        return self.datetime

    @datetime.setter
    def datetime(self, datetime):
        self._datetime = self.inspetorDateFormatter(datetime)

    def jsonSerialize(self):
        return {
            "session_id"        : self.encodeData(self.id),
            "session_timestamp" : self.encodeData(self.datetime)
        }