import matplotlib.pyplot as plt

# Dados para o gráfico
labels = ['arroz', 'proteina', 'vegetais', 'feijão']
sizes = [30, 25, 20, 25]  # Porcentagens
colors = ['blue', 'yellow', 'green', 'red']
explode = (0.1, 0, 0, 0)  # Destacar a primeira fatia

# Criando o gráfico de pizza
plt.figure(figsize=(12, 6))  # dimenssoes do grafioc, largura x altura
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Adicionando um título
plt.title('Distribuição de Alimentos')
plt.axis('equal')  # Para garantir que o gráfico seja um círculo

# Exibir o gráfico
plt.show()
