from jinja2 import Template

# Dados de exemplo com a nova estrutura
diretorias = [
    {
        'diretoria': 'Diretoria A',
        'squads': [
            {'time': 'sonserina', 'valor': 13, 'score': 10},
            {'time': 'iuconfia', 'valor': 13, 'score': 52},
            {'time': 'iuchaos', 'valor': 13, 'score': 90},
            {'time': 'timao', 'valor': 13, 'score': 100}
        ]
    },
    {
        'diretoria': 'Diretoria B',
        'squads': [
            {'time': 'seil la', 'valor': 13, 'score': 22},
            {'time': 'parmera', 'valor': 13, 'score': 22}
        ]
    },
    {
        'diretoria': 'Diretoria C',
        'squads': [
            {'time': 'ma oi', 'valor': 13, 'score': 96},
            {'time': 'oi só', 'valor': 13, 'score': 80},
            {'time': 'ma oi', 'valor': 13, 'score': 60},
            {'time': 'oi só', 'valor': 13, 'score': 22},
            {'time': 'ma oi', 'valor': 13, 'score': 22},
            {'time': 'oi só', 'valor': 13, 'score': 22}
        ]
    }
]

# Template HTML
html_template = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Diretorias</title>
</head>
<body>

    <h2>Relatório de Diretorias</h2>
    {% for diretoria in diretorias %}
        <h3>{{ diretoria.diretoria }}</h3>
        <table border="1" cellpadding="8" cellspacing="0">
            <thead>
                <tr>
                    <th>Nome Time</th>
                    <th>Cor</th>
                    <th>Valor</th>
                    <th>Score</th>
                </tr>
            </thead>
            <tbody>
                {% for squad in diretoria.squads %}
                    <tr>
                        <td>{{ squad.time }}</td>
                        <td>
                            {% if squad.score > 94 %}
                                <span style="color:green;">●</span>
                            {% elif squad.score > 80 %}
                                <span style="color:blue;">●</span>
                            {% elif squad.score > 51 %}
                                <span style="color:orange;">●</span>
                            {% else %}
                                <span style="color:red;">●</span>
                            {% endif %}
                        </td>
                        <td>{{ squad.valor }}</td>
                        <td>{{ squad.score }}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    {% endfor %}

</body>
</html>
"""

# Cria o template Jinja2
template = Template(html_template)

# Renderiza o HTML com os dados
html_output = template.render(diretorias=diretorias)

# Salva o HTML gerado em um arquivo
with open("relatorio_diretorias.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print("Arquivo HTML gerado com sucesso: relatorio_diretorias.html")
