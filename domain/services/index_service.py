class IndexService:
    def color_index(self) -> str:
        ##Aplicamos estilo de respuesta del servicio
        return '<h1>este es el index service</h1>'

    def persona(self, name, age):
        if name ==None and age ==None:
            return '<h1>No se han proporcionado ni el nombre ni la edad</h1>'
        elif age ==None:
            return f'<h1>No se han proporcionado la edad para el usuario {name}</h1>'
        return f'<h1>El nombre de la persona es {name} y tiene {age}</h1>'
