alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = alt * lar
tinta = area / 2
print(f'A área da parede é igual a {area}m².')
print(f'Serão necessários {tinta:.1f}L de tinta para pintar a parede inteira.')
