from domain.services.hello_service import HelloService


class SayHelloUseCase:
    def __init__(self):
        ##Creamos una instancia del servicio HelloService
        self.hello_service = HelloService()

    def execute(self):
        ##Llamamos al metodo say_hello del servicio
        return self.hello_service.say_hello()
