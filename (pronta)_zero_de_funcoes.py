# Autor - Gilson Carvalho Filho - Engenharia Civil UFAL - 25/09/2021
# Código para resolução de problemas de zero de funções
# Métodos adotados:
# - Método da Bissetriz
# - Método das cordas
# - Método de Newton-Rhapson

import math
import numpy as np
from sympy import*
x,y,z=symbols('x,y,z')


# Temporário para testes
#met=3
#p=1
#ite=4
#a=0
#b=1
#funcao="10-40*((((math.e)**(-0.25*x))-((math.e)**(-0.75*x))))"
#erro=0.00001


print("Qual método deseja usar? ")
print("[1] Método da Bissetriz ")
print("[2] Método das cordas ")
print("[3] Método de Newton-Rhapson ")
met=int(input())
while(met!=1 and met!=2 and met!=3):
	print("Escolha apenas um número entre 1 e 3 ")
	print("Qual método deseja usar? ")
	print("[1] Método da Bissetriz ")
	print("[2] Método das cordas ")
	print("[3] Método de Newton-Rhapson ")
	met=int(input())
print("Insira o intervalo inicial: ")
a=float(input("Insira a: "))
b=float(input("Insira b: "))
print("Escolha o critério de parada: ")
print("[1] Até atingir a precisão definida ")
print("[2] Até atingir a iteração máxima definida ")
p=int(input())
while(p!=1 and p!=2):
	print("Escolha apenas 1 ou 2: ")
	print("Escolha o critério de parada: ")
	print("[1] Até atingir o erro definido ")
	print("[2] Até atingir a iteração máxima definida ")
	p=int(input())
if(p==2):
	print("Insira o número de iterações desejado: ")
	ite=int(input())
if(p==1):
	print("Insira o erro: ")
	erro=float(input())

print("Insira a função no padrão python, usadno x como variável: ")
print("ex: 10-40*((((math.e)**(-0.25*x))-((math.e)**(-0.75*x)))) ")
funcao=str(input())


# Método da Bisseção
if(met==1):	
	if(p==2):
		mbi=np.ones((ite,2))
		for i in range(0,ite):
			z=(a+b)/2
			mbi[i][0]=z
			funcaoz=funcao.replace("x","z")
			funcaoz=eval(funcaoz)
			mbi[i][1]=funcaoz
			funcaoa=funcao.replace("x","a")
			funcaoa=eval(funcaoa)
			funcaob=funcao.replace("x","b")
			funcaob=eval(funcaob)
			print("------------------------------------------------------------------------")
			print("Interação {} ".format(i+1))
			print("Na {}ª iteração, a={}, b={}, z{}={} ".format(i+1,a,b,i+1,z))
			print("F(z{})={}, F({})={}, F({})={} ".format(i+1,funcaoz,a,funcaoa,b,funcaob))
			if(funcaoz>0 and funcaoa<0):
				b=z
			if(funcaoz<0 and funcaoa>0):
				b=z
			if(funcaoz<0 and funcaob>0):
				a=z
			if(funcaoz>0 and funcaob<0):
				a=z

	if(p==1):
		z=(a+b)/2
		funcaoz=funcao.replace("x","z")
		funcaoz=eval(funcaoz)
		if(((funcaoz**2)**(1/2))<=erro):
			print("O problema acaba aqui!!!")
			print("O zero da funcão é {} ".format(z))
		if(((funcaoz**2)**(1/2))>erro):
			ciclo=0
			result=[]
			while(((funcaoz**2)**(1/2))>erro):
				ciclo+=1
				z=(a+b)/2
				result.append(z)
				funcaoz=funcao.replace("x","z")
				funcaoz=eval(funcaoz)
				funcaoa=funcao.replace("x","a")
				funcaoa=eval(funcaoa)
				funcaob=funcao.replace("x","b")
				funcaob=eval(funcaob)
				print("------------------------------------------------------------------------")
				print("Interação {} ".format(ciclo))
				print("Na {}ª iteração, a={}, b={}, z{}={} ".format(ciclo,a,b,ciclo,z))
				print("F(z{})={}, F({})={}, F({})={} ".format(ciclo,funcaoz,a,funcaoa,b,funcaob))
				if(funcaoz>0 and funcaoa<0):
					b=z
				if(funcaoz<0 and funcaoa>0):
					b=z
				if(funcaoz<0 and funcaob>0):
					a=z
				if(funcaoz>0 and funcaob<0):
					a=z
			print("O resultado é z={} ".format(result[len(result)-1]))

# Método das cordas

if(met==2):
	if(p==2):
		mci=np.ones((ite,2))
		for i in range(0,ite):
			funcaoa=funcao.replace("x","a")
			funcaoa=eval(funcaoa)
			funcaob=funcao.replace("x","b")
			funcaob=eval(funcaob)
			z=((a*(funcaob))-(b*(funcaoa)))/(funcaob-funcaoa)
			mci[i][0]=z
			funcaoz=funcao.replace("x","z")
			funcaoz=eval(funcaoz)
			mci[i][1]=funcaoz			
			print("------------------------------------------------------------------------")
			print("Interação {} ".format(i+1))
			print("Na {}ª iteração, a={}, b={}, z{}={} ".format(i+1,a,b,i+1,z))
			print("F(z{})={}, F({})={}, F({})={} ".format(i+1,funcaoz,a,funcaoa,b,funcaob))
			if(funcaoz>0 and funcaoa<0):
				b=z
			if(funcaoz<0 and funcaoa>0):
				b=z
			if(funcaoz<0 and funcaob>0):
				a=z
			if(funcaoz>0 and funcaob<0):
				a=z

	if(p==1):
		funcaoa=funcao.replace("x","a")
		funcaoa=eval(funcaoa)
		funcaob=funcao.replace("x","b")
		funcaob=eval(funcaob)
		z=((a*(funcaob))-(b*(funcaoa)))/(funcaob-funcaoa)
		funcaoz=funcao.replace("x","z")
		funcaoz=eval(funcaoz)
		if(((funcaoz**2)**(1/2))<=erro):
			print("O problema acaba aqui!!!")
			print("O zero da funcão é {} ".format(z))
		if(((funcaoz**2)**(1/2))>erro):
			ciclo=0
			result=[]
			while(((funcaoz**2)**(1/2))>erro):
				ciclo+=1
				funcaoa=funcao.replace("x","a")
				funcaoa=eval(funcaoa)
				funcaob=funcao.replace("x","b")
				funcaob=eval(funcaob)
				z=((a*(funcaob))-(b*(funcaoa)))/(funcaob-funcaoa)
				result.append(z)
				funcaoz=funcao.replace("x","z")
				funcaoz=eval(funcaoz)				
				print("------------------------------------------------------------------------")
				print("Interação {} ".format(ciclo))
				print("Na {}ª iteração, a={}, b={}, z{}={} ".format(ciclo,a,b,ciclo,z))
				print("F(z{})={}, F({})={}, F({})={} ".format(ciclo,funcaoz,a,funcaoa,b,funcaob))
				if(funcaoz>0 and funcaoa<0):
					b=z
				if(funcaoz<0 and funcaoa>0):
					b=z
				if(funcaoz<0 and funcaob>0):
					a=z
				if(funcaoz>0 and funcaob<0):
					a=z
			print("O resultado é z={} ".format(result[len(result)-1]))

# Método de Newton-Rhapson

if(met==3):	
	if(p==2):
		mni=np.ones((ite,2))
		funcaointer=eval(funcao)
		funcaoderivada=str(diff(funcaointer,x))		
		print("A função derivada é {} ".format(funcaoderivada))
		for i in range(0,ite):
			funcaoa=funcao.replace("x","a")
			funcaoa=eval(funcaoa)
			funcaoderia=funcaoderivada.replace("x","a")
			funcaoderia=eval(funcaoderia)
			z=a-(funcaoa/funcaoderia)
			mni[i][0]=z
			funcaoz=funcao.replace("x","z")
			funcaoz=eval(funcaoz)
			mni[i][1]=funcaoz
			print("------------------------------------------------------------------------")
			print("Interação {} ".format(i+1))
			print("Na {}ª iteração, a={}, z{}={} ".format(i+1,a,i+1,z))
			print("F(z{})={}, F({})={}, F'({})={} ".format(i+1,funcaoz,a,funcaoa,a,funcaoderia))
			a=z

	if(p==1):
		funcaointer=eval(funcao)
		funcaoderivada=str(diff(funcaointer,x))		
		print("A função derivada é {} ".format(funcaoderivada))
		funcaoa=funcao.replace("x","a")
		funcaoa=eval(funcaoa)
		funcaoderia=funcaoderivada.replace("x","a")
		funcaoderia=eval(funcaoderia)
		z=a-(funcaoa/funcaoderia)
		funcaoz=funcao.replace("x","z")
		funcaoz=eval(funcaoz)
		mnili=[]
		ciclo=0
		while(((funcaoz**2)**(1/2))>erro):
			ciclo+=1
			funcaoa=funcao.replace("x","a")
			funcaoa=eval(funcaoa)
			funcaoderia=funcaoderivada.replace("x","a")
			funcaoderia=eval(funcaoderia)
			z=a-(funcaoa/funcaoderia)
			funcaoz=funcao.replace("x","z")
			funcaoz=eval(funcaoz)
			mnili.append(funcaoz)
			print("------------------------------------------------------------------------")
			print("bosta")
			print("Interação {} ".format(ciclo))
			print("Na {}ª iteração, a={}, z{}={} ".format(ciclo,a,ciclo,z))
			print("F(z{})={}, F({})={}, F'({})={} ".format(ciclo,funcaoz,a,funcaoa,a,funcaoderia))
			a=z



