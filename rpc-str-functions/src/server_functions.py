class FunctionsImplementation:
    def __init__(self):
        self.functions = {
            'split': self.__my_split,
        }

    @staticmethod
    def __my_split(s: str) -> str:
        return str(s.split())

    def run_fn(self, request):
        function_name, args, kwargs = self.__get_request_obj(request)
        return self.functions[function_name.lower()](*args, **kwargs)

    @staticmethod
    def __get_request_obj(request):
        fn_name = request.split('(')[0]
        args = request[len(fn_name)+1:-1].strip(' ').split(',')
        kwargs = {}
        if fn_name == 'exit':
            raise KeyboardInterrupt
        return fn_name, args, kwargs
