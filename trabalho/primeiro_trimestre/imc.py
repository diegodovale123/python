def calcular_imc(peso, altura):
   
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
  
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Função principal
def main():
    print("Calculadora de Índice de Massa Corporal (IMC)")
    print("--------------------------------------------")
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print("\nSeu IMC é:", imc)
    print("Classificação:", classificacao)

if __name__ == "__main__":
    main()
