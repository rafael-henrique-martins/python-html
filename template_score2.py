from jinja2 import Template

# Dados de exemplo com a nova estrutura
diretorias = [
    {
        'diretoria': 'Diretoria A',
        'squads': [
            {'time': 'sonserina', 'valor': 13, 'score': 22},
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



html_template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Diretorias</title>
</head>
<body style="font-family: Arial, sans-serif; display: flex; flex-direction: column; align-items: center; gap: 20px; padding: 20px; background-color: #f4f4f4;">

    {% for diretoria in diretorias %}
    <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); width: 100%; max-width: 700px; text-align: center;">
        <h2 style="background: red; color: white; padding: 10px; border-radius: 5px;">{{ diretoria.diretoria }}</h2>
        
        <!-- Cabeçalho dos campos -->
        <div style="display: flex; justify-content: space-between; padding: 5px 10px; font-weight: bold; 
        background: green; border-radius: 5px; margin-bottom: 5px;margin: 0 11px 5px 10px;">
            <span style="flex: 1; text-align: left;">SQUAD</span>
            <span style="flex: 1; text-align: center;">APROVADO</span>
            <span style="flex: 1; text-align: right;">SCORE</span>
        </div>

        <div style="display: flex; flex-direction: column; gap: 10px; padding: 10px;">
            {% for squad in diretoria.squads %}
            <div style="background: blue; padding: 10px; border-radius: 8px; box-shadow: 0 0 5px rgba(0, 0, 0, 0.1); display: flex; align-items: center; justify-content: space-between;">
                <p style="margin: 5px 0; font-weight: bold; flex: 1; text-align: left;">{{ squad.time }}</p>
                <span style="width: 20px; height: 20px; border-radius: 50%; display: inline-block; margin: 5px;
                    {% if squad.score > 94 %} background: green;
                    {% elif squad.score > 80 %} background: blue;
                    {% elif squad.score > 51 %} background: orange;
                    {% else %} background: red;
                    {% endif %}">
                </span>
                <p style="margin: 5px; flex: 1; text-align: right;">{{ squad.score }}</p>
            </div>
            {% endfor %}
        </div>
    </div>
    {% endfor %}

</body>
</html>



"""

# Cria o template Jinja2
template = Template(html_template)

# Renderiza o HTML com os dados
html_output = template.render(diretorias=diretorias)

# Salva o HTML gerado em um arquivo
with open("relatorio_diretorias2.html", "w", encoding="utf-8") as file:
    file.write(html_output)

print("Arquivo HTML gerado com sucesso: relatorio_diretorias.html")