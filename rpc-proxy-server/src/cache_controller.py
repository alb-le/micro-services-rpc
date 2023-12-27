import redis
from typing import Dict, List


class CacheController:
    def __init__(self, host: str, port: int, decode_responses: bool = True):
        _r = redis.Redis(host=host, port=port, decode_responses=decode_responses)

    @staticmethod
    def __get_call_signature_as_str(request) -> str:
        function_name: str = request[0]
        args: List[str] = request[1]
        kwargs: Dict[str] = request[2]
        return f"{function_name}{args}{kwargs}"

    def get(self, request: List) -> str:
        signature = self.__get_call_signature_as_str(request)
        res = self._r.get(signature + ":1")
        return res

    def set(self, request: List, res: str):
        signature = self.__get_call_signature_as_str(request)
        res = self._r.set(signature + ":1", res)
