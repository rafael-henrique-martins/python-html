from jinja2 import Template

# Dados de exemplo com a nova estrutura
diretorias = [
    {
        'squad': 'SO1234',
        'dados': [
            {'conta': 'sonserina',  'score': 22},
            {'conta': 'iuconfia', 'score': 52},
            {'conta': 'iuchaos',  'score': 90},
            {'conta': 'contabilidadeIuchaos', 'score': 100}
        ]
    },
    {
        'squad': 'SO999098',
        'dados': [
            {'conta': 'escritorio',  'score': 22},
            {'conta': 'consultoriadigital',  'score': 22}
        ]
    },
    {
        'squad': 'SO190987856',
        'dados': [
            {'conta': 'dadosdebanco',  'score': 96},
            {'conta': 'mq2',  'score': 80},
            {'conta': 'servicenow',  'score': 60},
            {'conta': 'maximoltda',  'score': 22},
            {'conta': 'performace',  'score': 22},
            {'conta': 'resiliencilambda',  'score': 22}
        ]
    },{
        'squad': 'SO190987856',
        'dados': [
            {'conta': 'dadosdebanco',  'score': 96}

        ]
    },{
        'squad': 'SO190987856',
        'dados': [
            {'conta': 'dadosdebanco',  'score': 96}
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
       <p style="background: rgba(0, 123, 255, 0.1); padding: 10px; border-radius: 5px; font-weight: bold; width: fit-content; margin-left: 10px;">
   Código Squad ({{ diretoria.squad }})
</p>
        <div style="display: flex; flex-direction: column; gap: 10px; padding: 10px;">
            {% for squad in diretoria.dados %}
            <div style="background: blue; padding: 1px; border-radius: 8px; 
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1); 
            display: flex; align-items: center; width: 90%; min-width: 500px;">

                <p style="margin: 5px 0; font-weight: bold; flex: 1; text-align: left;gap: 5px;margin-left:4px">{{ squad.conta }}</p>

                <span style="width: 20px; height: 20px; border-radius: 50%; display: inline-block; margin: 5px;
                    {% if squad.score > 94 %} background: green;
                    {% elif squad.score > 80 %} background: blue;
                    {% elif squad.score > 51 %} background: orange;
                    {% else %} background: red;
                    {% endif %}">
                </span>
                <p style="margin: 5px; flex: 1; text-align: right;">{{ squad.score }}%</p>
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