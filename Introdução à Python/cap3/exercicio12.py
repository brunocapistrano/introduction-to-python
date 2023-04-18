# Exercício 3.12 

distancia = float(input("Qual a distância a percorrer? "))
velocidadeM = float(input("Qual a velocidade que pretende manter? "))

tempoDeViagem = int(distancia / velocidadeM)

print("A viagem irá durar %s horas." % tempoDeViagem)