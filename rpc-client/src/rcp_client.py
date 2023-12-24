from src.clients.client import Client


class RcpClientController:
    def __init__(self, client: Client):
        self.client = client

    def run(self, i: str) -> str:
        self.client.handshake()
        print(f'Started RCP as Client. Server address: {self.client}')

        if i in 'exit':
            self.client.close()
            print(f'[INFO] Bye.')
            return

        try:
            return self.__run(i)

        except KeyboardInterrupt:
            self.client.close()
            print(f'[INFO] Server {self.client} interrupted.')

        except Exception as ex:
            print(f'[ERROR] Closing client because of an error:')
            self.client.close()
            raise ex

    def __run(self, i: str) -> str:
        user_input = self.__get_input(i)
        fn_name, args, kwargs = user_input

        res = self.client.call_fn(fn_name, args, kwargs)
        return res

    @staticmethod
    def __get_input(s: str):
        fn_name = s.split('(')[0]
        args = s[len(fn_name)+1:-1].strip(' ').split(',')
        kwargs = {}
        if fn_name == 'exit':
            raise KeyboardInterrupt
        return fn_name, args, kwargs
