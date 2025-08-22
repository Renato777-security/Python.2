'''
escreva um programa que leia o raio de ua esfera, e calcule o seu volume e área

V= (4/3) . π  . r³
A= 4 . π . r²

saida esperada

volume da esfera:
area da esfera:
'''

raio=float(input('digite o valor de raio: ')) 

v=(4/3) * 3,14 * raio**3
a=4*3,14 * raio**2

print('o volume da esfera é: ', v)

print('a area da esfera é: ', a)
