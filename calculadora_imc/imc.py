"""
Fórmula: IMC = peso (kg) / altura (m)²
"""


def calcular_imc(peso: float, altura: float) -> float:
    if not isinstance(peso, (int, float)) or isinstance(peso, bool):
        raise TypeError("Peso deve ser um valor numérico.")
    if not isinstance(altura, (int, float)) or isinstance(altura, bool):
        raise TypeError("Altura deve ser um valor numérico.")
    if peso <= 0:
        raise ValueError("O peso deve ser maior que zero.")
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return round(peso / (altura ** 2), 2)


def classificar_imc(imc: float) -> str:
    if not isinstance(imc, (int, float)) or isinstance(imc, bool):
        raise TypeError("O IMC deve ser um valor numérico.")
    if imc <= 0:
        raise ValueError("O IMC deve ser maior que zero.")
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    elif imc < 35.0:
        return "Obesidade Grau I"
    elif imc < 40.0:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III (Mórbida)"


def calcular_e_classificar(peso: float, altura: float) -> dict:
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    return {"imc": imc, "classificacao": classificacao}
