# Clase base Persona
class Soplin_Persona:
    def __init__(self, nombre):
        self.soplin_nombre = nombre
        self.soplin_distancia_recorrida = 0

    def soplin_caminar(self):
        self.soplin_distancia_recorrida += 2  # Caminar incrementa la distancia en 2 kms
        return f'{self.soplin_nombre} ha caminado 2 kms, distancia total: {self.soplin_distancia_recorrida} kms.'

# Clase derivada Atleta que hereda de Persona
class Soplin_Atleta(Soplin_Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.soplin_calorias_consumidas = 0

    def soplin_entrenar(self, distancia=10):
        self.soplin_distancia_recorrida += distancia
        self.soplin_calorias_consumidas += distancia * 500  # 500 calorías por km entrenado
        return f'{self.soplin_nombre} entrenó {distancia} kms, consumió {distancia * 500} cal.'

    def soplin_competir(self, distancia=20):
        self.soplin_distancia_recorrida += distancia
        self.soplin_calorias_consumidas += distancia * 750  # 750 calorías por km competido
        return f'{self.soplin_nombre} compitió {distancia} kms, consumió {distancia * 750} cal.'
