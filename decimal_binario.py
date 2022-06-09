#Conversao do numero decimal para o binario.

valor_entrada = int(input("Digite um numero decimal:"))
numero_dig = valor_entrada
resultado_da_div =1 
lista = []

while resultado_da_div >= 1:
  resto = valor_entrada%2
  lista.insert(0, resto )
  resultado_da_div = valor_entrada //2
  valor_entrada = resultado_da_div 

binario = "".join([str(item)for item in lista])
print("Numero decimal : ", numero_dig,"\n", " Convertido para binario:", binario)