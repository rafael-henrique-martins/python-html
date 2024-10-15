import json


def enviar_html(data, context):
    # HTML template com placeholders para os dados
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Layout Email</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                font-family: Arial, sans-serif;
            }}
            .container {{
                width: 100%;
                max-width: 800px;  /* Aumentado para 800 pixels */
                margin: 0 auto;
                background-color: #ffffff;
                border: 1px solid #ddd;
                border-radius: 5px;
                overflow: hidden;
            }}
            .header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px;
                border-bottom: 1px solid #ddd;
            }}
            .header img {{
                max-height: 80px;
                width: auto;
            }}
            .header-text {{
                font-size: 24px;
                text-align: center; /* Centraliza o texto */
                flex: 1; /* Permite que o texto ocupe o espaço disponível */
                margin: 0 20px; /* Margem lateral */
                color: #333333;
            }}
            .content {{
                padding: 20px;
            }}
            .content h2 {{
                font-size: 20px;
                margin-bottom: 10px;
            }}
            .hipoteses-list {{
                padding: 0;
                list-style-type: none;
            }}
            .hipoteses-list li {{
                background-color: #f9f9f9;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 4px;
                font-size: 16px;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 12px;
                color: #888888;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <img src="img_1.png" alt="Imagem Esquerda" />
                <div class="header-text">{data['texto_sns']}</div>
                <img src="img.png" alt="Imagem Direita" />
            </div>

            <div class="content">
                <p><strong>Gameday agendado:</strong> para o dia 1/1/21 na sigla <strong>{data['sigla']}</strong>, para a conta <strong>{data['nome_produto']}</strong></p>

                <h2>Hipóteses:</h2>
                <ul class="hipoteses-list">
                    {''.join([f'<li>{hipotese["hipotese"]}</li>' for hipotese in data['hipoteses']])}
                </ul>
            </div>

            <div class="footer">
                <p><strong>Legendas:</strong></p>
                <p>⏲️ Aguardando execução | ⚠️ Finalizado com desvio | ✔️ Aprovado</p>

            </div>
        </div>
    </body>
    </html>
    """

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
        },
        'body': html_content
    }


if __name__ == "__main__":
    data = {
        "nome_produto": "exemplo_produto",
        "texto_sns": "IUChaos Gameday, resiliência, fv4, contas a pagar - teste do tamanho do nome da coisa",
        "sigla": "ABC",
        "hipoteses": [
            {"hipotese": "exemplo para lambda 1"},
            {"hipotese": "exemplo para lambda 2"},
            {"hipotese": "exemplo para lambda 3"}
        ]
    }

    # Chamando a função para gerar o HTML
    response = enviar_html(data, context=None)

    # Salvar o HTML gerado em um arquivo
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(response['body'])

    print("HTML gerado e salvo em index.html")
