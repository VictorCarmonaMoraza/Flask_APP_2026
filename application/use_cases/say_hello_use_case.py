from domain.services.hello_service import HelloService


class SayHelloUseCase:
    def __init__(self):
        self.hello_service = HelloService()

    def execute(self):
        return self.hello_service.say_hello()
