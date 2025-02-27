#de tres numeros indicar cual es el valor del medio 

def valor_medio (a,b,c):
     minimo= min (a,b,c)
     maximo= max (a,b,c)
     medio= (a+b+c -minimo-maximo)
     return medio
num1= int(input("ingrese el primer  numero :  "))
num2= int(input("ingrese el segundo numero :  "))
num3= int(input("ingrese el tercer  numero :  "))

print("valor del medio es :   ", valor_medio(num1,num2,num3))
