import base64
from datetime import datetime
from src.inspetor.exception.model_exception.inspetor_general_exception import InspetorGeneralException


class InspetorAbstractModel(object):

    def encode_array(self, array, isObject):
        encodedArray = []
        if array is None:
            return None
        for item in array:
            if isObject is True:
                encode_array.append(self.encodeObject(item))
            else:
                encode_array.append(self.encode_data(item))
        return

    def encode_data(self, data):
        if data is not None:
            data = str(base64.b64encode(data.encode("utf-8")), "utf-8")

        return data

    def encodeObject(self, object):
        if object is not None:
            return object.jsonSerialize()

        return object

    def inspetor_date_formatter(self, timestamp):
        if timestamp is None:
            return None

        if not isinstance(int(timestamp), int):
            raise InspetorGeneralException(
                InspetorGeneralException.WRONG_TIMESTAMP_TYPE
            )

        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S+0000')