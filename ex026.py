frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes.')
print(f'O primeiro "A" está na posição {frase.find("A")+1} e o último "A" está na posição {frase.rfind("A")+1}')
