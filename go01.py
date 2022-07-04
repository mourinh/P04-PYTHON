p = float( input('Entre com o Valor do Produto: R$ ') )

unidade = int(input('Entre com a quantidade do produto?'))

if 0 <= quantidade < 10:

    desconto = 0

elif 10 <= quantidade < 99:

    desconto = 0.5

elif 100 <= quantidade < 999:

     desconto = 0.10

else:

   desconto = 0.15

Semdesconto =  p * unidade

Comdesconto = Semdesconto - Semdesconto * desconto

print('O produto sem desconto fica de R${:.2f}'. format(Semdesconto))
print('O produto com desconto fica de R${:.2f}' . format(Comdesconto, desconto))