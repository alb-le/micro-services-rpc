from typing import Any


class FunctionsImplementation:
    def __init__(self):
        self.functions = {
            'sum': self.__my_sum,
            'min': self.__my_min,
        }

    @staticmethod
    def __my_sum(left: int, right: int) -> int:
        return left + right

    @staticmethod
    def __my_min(left: Any, right: Any) -> bool:
        return min(left, right)

    def run_fn(self, request):
        function_name, args, kwargs = self.__get_request_obj(request)
        args = [int(i) for i in args]
        return self.functions[function_name.lower()](*args, **kwargs)

    @staticmethod
    def __get_request_obj(request):
        fn_name = request.split('(')[0]
        args = request[len(fn_name)+1:-1].strip(' ').split(',')
        kwargs = {}
        if fn_name == 'exit':
            raise KeyboardInterrupt
        return fn_name, args, kwargs
