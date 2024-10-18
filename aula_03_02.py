# Dados de roubos, furtos e recuperações
roubos = [100, 90, 80, 120, 110, 90, 70]
furtos = [80, 60, 70, 60, 100, 50, 30]
recuperacoes = [70, 50, 90, 80, 100, 70, 50]

# Cálculos
total_diario = [r + f for r, f in zip(roubos, furtos)]
taxas_recuperacao = [rec / r if r > 0 else 0 for rec, r in zip(recuperacoes, roubos)]

# Resultados
print("Quantidade de roubos + furtos diários nos últimos 7 dias:")
for dia, total in enumerate(total_diario, start=1):
    print(f"Dia {dia}: {total}")

print("\nTaxa de recuperação de automóveis diária nos últimos 7 dias:")
for dia, taxa in enumerate(taxas_recuperacao, start=1):
    print(f"Dia {dia}: {taxa:.2%}")  # Formata como porcentagem
