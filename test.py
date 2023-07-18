import unittest
from app import SimuladorFutebol

# Teste unitário para a divisão
class TestCalculoDesempenho(unittest.TestCase):
    def test_calculodesempenho (self):
        resultado = SimuladorFutebol.calculodesempenho(24,20)
        self.assertEqual(resultado,40)