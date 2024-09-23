import unittest

class TestSoplinAtleta(unittest.TestCase):
    
    def test_caminar(self):
        persona = Soplin_Persona("Juan")
        self.assertEqual(persona.soplin_caminar(), "Juan ha caminado 2 kms, distancia total: 2 kms.")
    
    def test_entrenar(self):
        atleta = Soplin_Atleta("Ana")
        self.assertEqual(atleta.soplin_entrenar(), "Ana entrenó 10 kms, consumió 5000 cal.")
        self.assertEqual(atleta.soplin_entrenar(5), "Ana entrenó 5 kms, consumió 2500 cal.")
    
    def test_competir(self):
        atleta = Soplin_Atleta("Carlos")
        self.assertEqual(atleta.soplin_competir(), "Carlos compitió 20 kms, consumió 15000 cal.")
        self.assertEqual(atleta.soplin_competir(15), "Carlos compitió 15 kms, consumió 11250 cal.")
        
if __name__ == '__main__':
    unittest.main()
