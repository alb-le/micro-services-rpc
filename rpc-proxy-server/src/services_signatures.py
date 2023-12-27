from typing import Any, Tuple, List, Dict, Optional

import config
from src.clients.server_client import ServerClient
from src.cache_controller import CacheController


class ServicesSignatures:
    def __init__(self, cache: CacheController):
        self.__num_functions = {
            "sum": self.__my_sum,
            "min": self.__my_min,
        }
        self.__str_functions = {
            "split": self.__my_split,
        }
        self.__cache = cache

    def __help(self, *arg, **kwargs):
        return (
            f"List of functions using strings as arguments:\n{list(self.__str_functions.keys())}\n"
            f"List of functions using numbers as arguments:\n{list(self.__num_functions.keys())}"
        )

    def __invalid_function_call(self):
        return "There is no available function with that signature. " + self.__help()

    def __my_sum(self, left: int, right: int) -> int:
        res = self.__call_num_service("sum", left, right)
        return res

    def __my_min(self, left: Any, right: Any) -> bool:
        res = self.__call_num_service("min", left, right)
        return res

    def __my_split(self, s: str) -> List[str]:
        res = self.__call_str_service("split", s)
        return res

    def run_fn(self, request: List):
        if cached_res := self.__cache.get(request):
            return cached_res

        function_type, function_name, args, kwargs = self.__get_call_signature(request)

        match function_type:
            case "help":
                return self.__help()

            case "error":
                return self.__invalid_function_call()

            case "string":
                res = self.__str_functions[function_name](*args, **kwargs)
                self.__cache.set(request, res)
                return res

            case "numeral":
                res = self.__num_functions[function_name](*args, **kwargs)
                self.__cache.set(request, res)
                return res

    def __get_call_signature(
        self, request: list
    ) -> Tuple[str, str, Optional[List], Optional[Dict]]:
        function_name = request[0].lower()

        if function_name in "help":
            function_type = "help"

        elif function_name in self.__num_functions.keys():
            function_type = "numeral"

        elif function_name in self.__str_functions.keys():
            function_type = "string"

        else:
            function_type = "error"

        args = request[1]
        kwargs = request[2]
        return function_type, function_name, args, kwargs

    @staticmethod
    def __call_num_service(fn_name, *args, **kwargs):
        host = config.NUM_SERVICE_HOST
        port = config.NUM_SERVICE_PORT
        print(f"[INFO] Creating connection for worker. Address: {host}:{port}")
        service_client = ServerClient(host=host, port=port)

        try:
            service_client.handshake(port=port, host=host)
            res = service_client.call_fn(fn_name, args, kwargs)
            service_client.close()

        except Exception as ex:
            res = str(ex)
            print(f"[ERROR] Error calling fn {fn_name}: {res}")
            service_client.close()
            raise ex

        return res

    @staticmethod
    def __call_str_service(self, fn_name, *args, **kwargs):
        host = config.STR_SERVICE_HOST
        port = config.STR_SERVICE_HOST
        print(f"[INFO] Creating connection for worker. Address: {host}:{port}")
        service_client = ServerClient(host=host, port=port)

        try:
            service_client.handshake(port=port, host=host)
            res = service_client.call_fn(fn_name, args, kwargs)
            service_client.close()

        except Exception as ex:
            res = str(ex)
            print(f"[ERROR] Error calling fn {fn_name}: {res}")
            service_client.close()
            raise ex

        return res
