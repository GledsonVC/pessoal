import Bhaskara     
import pytest

class Testbaskara:

## Opcional caso queira não atribuir o valor ao b no test_Bhaskara e assim não ficando repetitivo em proximos testes em outros módulos
##    @pytest.fixture
##    def b(self):
##        return Bhaskara.Bhaskara()
    
    @pytest.mark.parametrize('entrada, esperado', [
        [(1, 0, 0,), (1, 0,)]
        ])

    def test_Bhaskara(self, entrada, esperado): ## no seu caso aqui faltou o self
                                                ##se for colcoar Opcional, não esqueça de inclir o b ficando assim a função def
                                                ## test_Bhaskara(self, b, entrada, esperado)
        b = Bhaskara.Bhaskara()  ## se for colcoar Opcional, não esqueça de apagar essa linha ou comentar ela
        assert b.calcula_raizes(entrada[0], entrada[1], entrada[2]) == (esperado) ## aqui faltou atribuir a tupla os valores esperados de entrada[0], [1] e [2]
