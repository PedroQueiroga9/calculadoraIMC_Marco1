"""
Suite de Testes Unitários - Calculadora de IMC

"""

import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from imc import calcular_imc, classificar_imc, calcular_e_classificar


# ───────────────────────────────────────────────
# FIXTURES
# ───────────────────────────────────────────────

@pytest.fixture
def peso_altura_normais():
    """Fixture: dados válidos padrão para reutilização nos testes."""
    return {"peso": 70.0, "altura": 1.75}


# ───────────────────────────────────────────────
# TESTES: calcular_imc()
# ───────────────────────────────────────────────

class TestCalcularImc:

    def test_calcularImc_pesoAlturaValidos_retornaImcCorreto(self, peso_altura_normais):
        """RN01 - Fórmula correta: 70 / 1.75² = 22.86"""
        assert calcular_imc(70.0, 1.75) == 22.86

    def test_calcularImc_pesoAlturaValidos_retornaFloat(self, peso_altura_normais):
        """RN01 - Retorno deve ser float."""
        assert isinstance(calcular_imc(70.0, 1.75), float)

    def test_calcularImc_valoresValidos_retornaArredondadoDuasCasas(self):
        """RN05 - Resultado arredondado a 2 casas decimais."""
        assert calcular_imc(60, 1.70) == round(60 / (1.70 ** 2), 2)

    def test_calcularImc_pesoInteiro_retornaImcCorreto(self):
        """RN01 - Deve aceitar peso como inteiro."""
        assert calcular_imc(80, 1.80) == round(80 / (1.80 ** 2), 2)

    def test_calcularImc_valoresDecimais_retornaImcCorreto(self):
        """RN01 - Deve aceitar peso e altura decimais."""
        assert calcular_imc(55.5, 1.62) == round(55.5 / (1.62 ** 2), 2)

    def test_calcularImc_pesoZero_lancaValueError(self):
        """RN02 - Peso = 0 deve lançar ValueError."""
        with pytest.raises(ValueError, match="peso deve ser maior que zero"):
            calcular_imc(0, 1.75)

    def test_calcularImc_pesoNegativo_lancaValueError(self):
        """RN02 - Peso negativo deve lançar ValueError."""
        with pytest.raises(ValueError, match="peso deve ser maior que zero"):
            calcular_imc(-10, 1.75)

    def test_calcularImc_pesoString_lancaTypeError(self):
        """RN04 - Peso como string deve lançar TypeError."""
        with pytest.raises(TypeError):
            calcular_imc("setenta", 1.75)

    def test_calcularImc_pesoBool_lancaTypeError(self):
        """RN04 - Bool não deve ser aceito como peso."""
        with pytest.raises(TypeError):
            calcular_imc(True, 1.75)

    def test_calcularImc_alturaZero_lancaValueError(self):
        """RN03 - Altura = 0 deve lançar ValueError."""
        with pytest.raises(ValueError, match="altura deve ser maior que zero"):
            calcular_imc(70, 0)

    def test_calcularImc_alturaNegativa_lancaValueError(self):
        """RN03 - Altura negativa deve lançar ValueError."""
        with pytest.raises(ValueError, match="altura deve ser maior que zero"):
            calcular_imc(70, -1.75)

    def test_calcularImc_alturaString_lancaTypeError(self):
        """RN04 - Altura como string deve lançar TypeError."""
        with pytest.raises(TypeError):
            calcular_imc(70, "um metro")

    def test_calcularImc_alturaBool_lancaTypeError(self):
        """RN04 - Bool não deve ser aceito como altura."""
        with pytest.raises(TypeError):
            calcular_imc(70, False)


# ───────────────────────────────────────────────
# TESTES: classificar_imc()
# ───────────────────────────────────────────────

class TestClassificarImc:

    def test_classificarImc_imcAbaixo185_retornaAbaixoDoPeso(self):
        """RN06 - IMC 17.0 → Abaixo do peso"""
        assert classificar_imc(17.0) == "Abaixo do peso"

    def test_classificarImc_imc184_retornaAbaixoDoPeso(self):
        """RN06 - IMC 18.4 ainda é abaixo do peso (valor-limite)."""
        assert classificar_imc(18.4) == "Abaixo do peso"

    def test_classificarImc_imcEntre185e25_retornaPesoNormal(self):
        """RN07 - IMC 22.0 → Peso normal"""
        assert classificar_imc(22.0) == "Peso normal"

    def test_classificarImc_imc185_retornaPesoNormal(self):
        """RN07 - IMC 18.5 é exatamente peso normal (valor-limite)."""
        assert classificar_imc(18.5) == "Peso normal"

    def test_classificarImc_imcEntre25e30_retornaSobrepeso(self):
        """RN08 - IMC 27.5 → Sobrepeso"""
        assert classificar_imc(27.5) == "Sobrepeso"

    def test_classificarImc_imc25_retornaSobrepeso(self):
        """RN08 - IMC 25.0 é exatamente sobrepeso (valor-limite)."""
        assert classificar_imc(25.0) == "Sobrepeso"

    def test_classificarImc_imcEntre30e35_retornaObesidadeGrau1(self):
        """RN09 - IMC 32.0 → Obesidade Grau I"""
        assert classificar_imc(32.0) == "Obesidade Grau I"

    def test_classificarImc_imc30_retornaObesidadeGrau1(self):
        """RN09 - IMC 30.0 é exatamente Obesidade Grau I (valor-limite)."""
        assert classificar_imc(30.0) == "Obesidade Grau I"

    def test_classificarImc_imcEntre35e40_retornaObesidadeGrau2(self):
        """RN10 - IMC 37.0 → Obesidade Grau II"""
        assert classificar_imc(37.0) == "Obesidade Grau II"

    def test_classificarImc_imc35_retornaObesidadeGrau2(self):
        """RN10 - IMC 35.0 é exatamente Obesidade Grau II (valor-limite)."""
        assert classificar_imc(35.0) == "Obesidade Grau II"

    def test_classificarImc_imcAcima40_retornaObesidadeGrau3(self):
        """RN11 - IMC 45.0 → Obesidade Grau III (Mórbida)"""
        assert classificar_imc(45.0) == "Obesidade Grau III (Mórbida)"

    def test_classificarImc_imc40_retornaObesidadeGrau3(self):
        """RN11 - IMC 40.0 é exatamente Obesidade Grau III (valor-limite)."""
        assert classificar_imc(40.0) == "Obesidade Grau III (Mórbida)"

    def test_classificarImc_imcZero_lancaValueError(self):
        """RN12 - IMC = 0 deve lançar ValueError."""
        with pytest.raises(ValueError):
            classificar_imc(0)

    def test_classificarImc_imcNegativo_lancaValueError(self):
        """RN12 - IMC negativo deve lançar ValueError."""
        with pytest.raises(ValueError):
            classificar_imc(-5.0)

    def test_classificarImc_imcString_lancaTypeError(self):
        """RN04 - IMC como string deve lançar TypeError."""
        with pytest.raises(TypeError):
            classificar_imc("alto")


# ───────────────────────────────────────────────
# TESTES: calcular_e_classificar()
# ───────────────────────────────────────────────

class TestCalcularEClassificar:

    def test_calcularEClassificar_pesoAlturaValidos_retornaDicionario(self):
        """Retorno deve ser um dicionário."""
        assert isinstance(calcular_e_classificar(70, 1.75), dict)

    def test_calcularEClassificar_pesoAlturaValidos_dicionarioContemChaveImc(self):
        """Dicionário deve ter chave 'imc'."""
        assert "imc" in calcular_e_classificar(70, 1.75)

    def test_calcularEClassificar_pesoAlturaValidos_dicionarioContemChaveClassificacao(self):
        """Dicionário deve ter chave 'classificacao'."""
        assert "classificacao" in calcular_e_classificar(70, 1.75)

    def test_calcularEClassificar_peso70Altura175_retornaPesoNormal(self):
        """Fluxo completo: peso=70, altura=1.75 → imc=22.86, Peso normal."""
        r = calcular_e_classificar(70, 1.75)
        assert r["imc"] == 22.86
        assert r["classificacao"] == "Peso normal"

    def test_calcularEClassificar_peso90Altura175_retornaSobrepeso(self):
        """Fluxo completo: peso=90, altura=1.75 → Sobrepeso."""
        assert calcular_e_classificar(90, 1.75)["classificacao"] == "Sobrepeso"

    def test_calcularEClassificar_peso45Altura170_retornaAbaixoDoPeso(self):
        """Fluxo completo: peso=45, altura=1.70 → Abaixo do peso."""
        assert calcular_e_classificar(45, 1.70)["classificacao"] == "Abaixo do peso"

    def test_calcularEClassificar_pesoZero_lancaValueError(self):
        """Entradas inválidas devem propagar ValueError."""
        with pytest.raises(ValueError):
            calcular_e_classificar(0, 1.75)

    @pytest.mark.parametrize("peso,altura,esperado", [
        (40,  1.70, "Abaixo do peso"),
        (65,  1.70, "Peso normal"),
        (85,  1.70, "Sobrepeso"),
        (100, 1.70, "Obesidade Grau I"),
        (115, 1.70, "Obesidade Grau II"),
        (130, 1.70, "Obesidade Grau III (Mórbida)"),
    ])
    def test_calcularEClassificar_todasFaixasOMS_retornaClassificacaoCorreta(self, peso, altura, esperado):
        """Teste parametrizado cobrindo todas as 6 faixas da OMS."""
        assert calcular_e_classificar(peso, altura)["classificacao"] == esperado
