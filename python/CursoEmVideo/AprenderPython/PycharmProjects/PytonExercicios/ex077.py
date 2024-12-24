# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('Aprender', 'programar', 'programar', 'linguagem', 'python',
         'Curso', 'Gratis', 'estudar', 'praticar' , 'trabalhar',
         'mercado', 'programador', 'futuro')
for c in tupla:
    print(f'\nNa palavra {c.upper()} ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
