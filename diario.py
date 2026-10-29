from datetime import datetime

hoje = datetime.now().strftime("%d/%m/%Y")
entrada = input("O que saiu da tela hoje? ")

with open("diario.txt", "a", encoding="utf-8") as f:
    f.write(f"{hoje} - {entrada}\n")

print("Salvo.")
