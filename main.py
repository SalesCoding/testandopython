
>>> print(7+4)
11
>>> print('7'+'4')
74
>>> 7+4
11
>>> print('Olá' + 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print('Olá', 5)
Olá 5
>>> nome = 'Sales'
>>> idade = 21
>>> peso = 104
>>> print (nome+ idade, peso)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> nome = input('Qual é o seu nome? ')
Qual é o seu nome? Sales
>>> idade input('Quantos anos vc tem ? ')
  File "<stdin>", line 1
    idade input('Quantos anos vc tem ? ')
          ^^^^^
SyntaxError: invalid syntax
>>> idade input('Quantos anos vc tem ? ')
  File "<stdin>", line 1
    idade input('Quantos anos vc tem ? ')
          ^^^^^
SyntaxError: invalid syntax
>>> idade input ('Quantos anos vc tem ? ')
  File "<stdin>", line 1
    idade input ('Quantos anos vc tem ? ')
          ^^^^^
SyntaxError: invalid syntax
>>> idade = input ('Quantos anos vc tem ? ')
Quantos anos vc tem ? 120
>>> peso = input (' Qual é o seu peso? ' )
 Qual é o seu peso? 20.70
>>> print (nome, idade, peso)
Sales 120 20.70
>>>