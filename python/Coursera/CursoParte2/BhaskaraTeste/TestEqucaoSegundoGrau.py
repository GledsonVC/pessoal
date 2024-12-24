import EquacaoSegundoGrau
import pytest

class TestEquacao:

    @pytest.fixture
    def bhask(self):
        return EquacaoSegundoGrau.Bhaskara()

    @pytest.mark.parametrize('entrada, valorEsperado', [
        ([1, 0, 0], [1, 0]),
        ([1, -5, 6], [2, 3, 2]),
        ([10, 10, 10], [0]),
        ([10, 20, 10], [1, -1])
        ])

    def testEquacaoSegundoGrau(self, bhask, entrada, valorEsperado):
        assert bhask.calculaRaiz(entrada[0], entrada[1], entrada[2]) == (valorEsperado)
