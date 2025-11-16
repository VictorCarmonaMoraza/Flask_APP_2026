from domain.services.index_service import IndexService


class IndexUseCase:
    def __init__(self):
        ##Creamos una instancia del servicio IndexService
        self.index_service = IndexService()

    def execute(self):
        ##Llamamos al metodo color_index del servicio
        return self.index_service.color_index()

    def execute2(self, name, age):
        ##Llamamos al metodo persona del servicio
        return self.index_service.persona(name, age)

    def obtener_lista(self):
        #LLamamos al metodo obtener_lista del servicio
        return self.index_service.obtener_lista_servicio()

