larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
qtd_tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'
      '\nPara pintar essa parede, você precisará de {:.2f}l de tinta'.format(larg, alt, area, qtd_tinta))
