produtos = [500, 240, 360, 150, 400]
print(produtos)

total = sum(produtos)
print(total)

if total >= 500:
    print(f'10% de desconto')
    desconto = total * 0.10
    valor_final = total - desconto
    print(f'Total: {total}')
    print(f'Desconto: {desconto}')
    print(f'Valor final: {valor_final}')

else:
    print(f'Nenhum desconto aplicado.')