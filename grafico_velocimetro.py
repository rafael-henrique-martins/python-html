import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge


def plot_speedometer(value, min_val=0, max_val=100):
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw={'projection': 'polar'})

    # Ajuste da visualização do gráfico polar
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['polar'].set_visible(False)

    # Definindo os ângulos para os setores do gráfico
    angles = np.linspace(np.pi, 0, 5)  # Dividir em 4 setores (0, 1, 2, 3)

    # Definindo as cores com base no intervalo
    if value < 51:
        color = 'red'  # Vermelho para valores menores que 51
    elif value >= 51 and value < 81:
        color = 'yellow'  # Amarelo para valores entre 51 e 80
    elif value >= 81 and value < 94:
        color = 'blue'  # Azul para valores entre 81 e 93
    else:
        color = 'green'  # Verde para valores acima de 94

    # Cor do restante do gráfico (cinza) preenchendo primeiro
    gray_angle = np.pi - (value / max_val) * np.pi  # O restante do gráfico
    ax.barh(1, width=gray_angle, left=0, color='gray', height=1)

    # Cor do gráfico até o valor inserido
    red_angle = np.pi - gray_angle  # Ângulo até o valor fornecido
    ax.barh(1, width=red_angle, left=gray_angle, color=color, height=1)

    # Ajustando a posição do valor no centro (agora corretamente no sistema polar)
    ax.text(0, 0.25, f'{value} km/h', horizontalalignment='center', verticalalignment='center', fontsize=16,
            color='black')

    # Título principal e subtítulo acima do gráfico, alinhados à esquerda
    ax.text(-np.pi / 2, 1.2, 'Score de Chaos', horizontalalignment='left', verticalalignment='center', fontsize=18,
            fontweight='bold', color='black')
    ax.text(-np.pi / 2, 1.05, 'Pontuação geral composta de gamedays', horizontalalignment='left',
            verticalalignment='center', fontsize=12, color='black')

    plt.show()


# Exemplo de uso
plot_speedometer(60)  # Teste com valo60

criar circolos
<div style="font-family: Arial, sans-serif; text-align: center;">
  <span style="color: red; font-size: 24px;">●</span> <strong>Crítico</strong>
  <span style="color: orange; font-size: 24px;">●</span> <strong>Médio</strong>
  <span style="color: blue; font-size: 24px;">●</span> <strong>Bom</strong>
  <span style="color: green; font-size: 24px;">●</span> <strong>Ótimo</strong>
  <br>
  <span style="margin-right: 30px;">&lt;51</span>
  <span style="margin-right: 30px;">&lt;81</span>
  <span style="margin-right: 30px;">&lt;94</span>
  <span>&gt;94</span>
</div>


