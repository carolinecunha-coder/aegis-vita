import matplotlib.pyplot as plt
import pandas as pd
import math

# -------------------------------
# FORMATAÇÃO MOEDA
# -------------------------------
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# -------------------------------
# CÁLCULO DO PRÊMIO
# -------------------------------
def calcular_premio(idade, capital, tipo):
    fatores = {
        "acidental": 0.0002,
        "natural": 0.0006
    }

    if tipo not in fatores:
        return None

    f = fatores[tipo]
    k = 0.035
    margem = 0.30

    risco_idade = math.exp(k * (idade - 18))
    premio = capital * f * risco_idade * (1 + margem)

    return round(premio, 2)


# -------------------------------
# GRÁFICO
# -------------------------------
def plotar_grafico_multiplos(capitais, tipo="natural", idade_destaque=None):
    plt.figure()
    idades = list(range(18, 61))

    for capital in capitais:

        # NATURAL
        if tipo in ["natural", "ambos"]:
            premios_natural = [
                calcular_premio(idade, capital, "natural") for idade in idades
            ]

            plt.plot(
                idades,
                premios_natural,
                label=f"Natural - {formatar_moeda(capital)}"
            )

            if idade_destaque:
                premio = calcular_premio(idade_destaque, capital, "natural")
                plt.scatter(idade_destaque, premio)
                plt.text(idade_destaque, premio, formatar_moeda(premio), fontsize=8)

        # ACIDENTAL
        if tipo in ["acidental", "ambos"]:
            premios_acidental = [
                calcular_premio(idade, capital, "acidental") for idade in idades
            ]

            plt.plot(
                idades,
                premios_acidental,
                linestyle="--",
                label=f"Acidental - {formatar_moeda(capital)}"
            )

            if idade_destaque:
                premio = calcular_premio(idade_destaque, capital, "acidental")
                plt.scatter(idade_destaque, premio)
                plt.text(idade_destaque, premio, formatar_moeda(premio), fontsize=8)

    plt.xlabel("Idade")
    plt.ylabel("Prêmio (R$)")
    plt.title("Aegis Vita - Evolução do Prêmio")

    plt.legend()
    plt.grid()
    plt.show()


# -------------------------------
# GERAR BASE PARA EXCEL
# -------------------------------
def gerar_base(capital):
    idades = list(range(18, 61))
    dados = []

    for idade in idades:
        dados.append({
            "Idade": idade,
            "Premio_Acidental": calcular_premio(idade, capital, "acidental"),
            "Premio_Natural": calcular_premio(idade, capital, "natural"),
            "Capital_Segurado": capital
        })

    return pd.DataFrame(dados)


def exportar_excel(df):
    df.to_excel("aegis_vita_dados.xlsx", index=False, engine="openpyxl")
    print("Arquivo Excel gerado com sucesso!")


# -------------------------------
# SIMULAÇÃO
# -------------------------------
def simular():
    try:
        idade = int(input("Digite a idade (18 a 60): "))
    except:
        print("Idade inválida.")
        return

    tipo = input("Tipo (acidental/natural): ").lower().strip()

    if tipo in ["a", "acidental"]:
        tipo = "acidental"
    elif tipo in ["n", "natural"]:
        tipo = "natural"
    else:
        print("Tipo inválido.")
        return

    print("\nEscolha o capital segurado:")
    print("1 - R$ 50.000")
    print("2 - R$ 100.000")
    print("3 - R$ 200.000")
    print("4 - Digitar outro valor")

    opcao = input("Opção: ").strip()

    if opcao == "1":
        capital = 50000
    elif opcao == "2":
        capital = 100000
    elif opcao == "3":
        capital = 200000
    elif opcao == "4":
        try:
            capital = float(input("Digite o capital desejado: "))
        except:
            print("Valor inválido.")
            return
    else:
        print("Opção inválida.")
        return

    premio = calcular_premio(idade, capital, tipo)

    print("\n--- Aegis Vita ---")
    print(f"Idade: {idade}")
    print(f"Tipo: {tipo.capitalize()}")
    print(f"Capital segurado: {formatar_moeda(capital)}")
    print(f"Prêmio mensal: {formatar_moeda(premio)}")


# -------------------------------
# MENU
# -------------------------------
def menu():
    while True:
        print("\n=== AEGIS VITA ===")
        print("1 - Simular seguro")
        print("2 - Gerar gráfico")
        print("3 - Exportar dados para Excel")
        print("4 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "":
            continue

        if opcao == "1":
            simular()

        elif opcao == "2":
            try:
                idade = int(input("Digite a idade para destaque: "))
            except:
                print("Idade inválida.")
                continue

            print("\nTipo de cobertura:")
            print("1 - Natural")
            print("2 - Acidental")
            print("3 - Ambos")

            tipo_opcao = input("Escolha: ").strip()

            if tipo_opcao == "1":
                tipo = "natural"
            elif tipo_opcao == "2":
                tipo = "acidental"
            elif tipo_opcao == "3":
                tipo = "ambos"
            else:
                print("Opção inválida.")
                continue

            print("\nDigite os capitais separados por vírgula")
            print("Ex: 50000,100000,200000")

            entrada = input("Capitais: ")

            try:
                capitais = [float(c.strip()) for c in entrada.split(",")]
            except:
                print("Valores inválidos.")
                continue

            plotar_grafico_multiplos(capitais, tipo, idade)

        elif opcao == "3":
            try:
                capital = float(input("Digite o capital para exportação: "))
            except:
                print("Valor inválido.")
                continue

            df = gerar_base(capital)
            exportar_excel(df)

        elif opcao == "4":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


# -------------------------------
# EXECUÇÃO
# -------------------------------
if __name__ == "__main__":
    menu()
