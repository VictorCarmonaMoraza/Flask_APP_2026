from domain.services.index_service import IndexService


class IndexUseCase:
    def __init__(self):
        ##Creamos una instancia del servicio HelloService
        self.index_service = IndexService()

    def execute(self):
        ##Llamamos al metodo say_hello del servicio
        return self.index_service.color_index()
