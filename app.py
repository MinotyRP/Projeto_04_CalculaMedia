
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f"\nMédia final: {media:.2f}")

if media >= 7.0:
    print("Situação: Aprovado(a) ✅")
elif media >= 5.0:
    print("Situação: Recuperação ⚠️")
else:
    print("Situação: Reprovado(a) ❌")