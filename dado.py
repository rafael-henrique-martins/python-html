import json

def enviar_html(data, context):
    # Dicionário com os dados que serão inseridos no HTML

    # HTML template com placeholders para os dados
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Layout Horizontal</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Roboto', sans-serif;  /* Fonte moderna */
                background-color: #f4f4f9;          /* Fundo claro */
                border: 1px solid #ccc;             /* Borda suave */
                border-radius: 10px;                /* Borda arredondada */
                padding: 20px;                      /* Espaçamento dentro da borda */
                margin: 20px auto;
                max-width: 800px;                   /* Limitar a largura do conteúdo */
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);  /* Sombra para elegância */
            }}
            .header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px;
                border-bottom: 1px solid #ddd;
            }}
            .header img {{
                height: 50px;
            }}
            .header img.left {{
                height: 80px;
                margin-right: 20px;
            }}
            .header img.right {{
                margin-top: -30px;
                margin-left: 20px;
            }}
            .header-text {{
                font-size: 28px;
                color: #333;
            }}
            .hipoteses-list {{
                margin: 20px 15px;
                font-size: 18px;
                margin-top: 30px;
            }}
            .hipoteses-list div {{
                display: block;
                margin-bottom: 10px;
                background-color: #fff;
                padding: 10px;
                border-radius: 5px;
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
            }}
            .hipoteses-list div i {{
                color: #007bff;  /* Azul para ícones */
                margin-right: 10px;
            }}
            .footer-icons {{
                margin-top: 50px;
                text-align: right;
            }}
            .footer-icons h6 {{
                margin-bottom: 15px;
                font-size: 16px;
                color: #666;
            }}
            .footer-icons .icon-container {{
                display: flex;
                justify-content: flex-end;
                align-items: center;
                margin-bottom: 10px;
                transition: all 0.3s ease;
            }}
            .footer-icons .icon-container:hover {{
                transform: scale(1.05);  /* Efeito de hover para ícones */
            }}
            .footer-icons i {{
                font-size: 20px;
                color: #666;
                margin-right: 10px;
            }}
            .footer-icons .icon-description {{
                font-size: 14px;
                color: #333;
            }}

            /* Responsividade */
            @media (max-width: 600px) {{
                .header {{
                    flex-direction: column;
                    text-align: center;
                }}
                .header img {{
                    margin-bottom: 10px;
                }}
                .header-text {{
                    font-size: 24px;
                }}
                .footer-icons {{
                    text-align: center;
                }}
            }}
        </style>
    </head>
    <body>

        <div class="header">
            <img src="img_1.png" alt="Imagem Esquerda" class="left">
            <div class="header-text" id="textoSNS">{data['texto_sns']}</div>
            <img src="img.png" alt="Imagem Direita" class="right">
        </div>

        <div class="hipoteses-list">
            <div id="headerText" style="font-size: 20px; margin-bottom: 40px; margin-top: 30px;">gameday agendado para o dia 1/1/21 na sigla {data['sigla']}, para a conta {data['nome_produto']}</div>
            <h2>Hipóteses:</h2>
            <div id="hipotesesList">
                {''.join([f'<div><i class="fa fa-question-circle"></i> {data["nome_produto"]} {hipotese["hipotese"]}</div>' for hipotese in data['hipoteses']])}
            </div>
        </div>

        <div class="footer-icons">
            <h6>Legendas</h6>

            <div class="icon-container">
                <i class="fa fa-exclamation-triangle"></i>
                <div class="icon-description">Não executado</div>
            </div>

            <div class="icon-container">
                <i class="fa fa-check-circle"></i>
                <div class="icon-description">Finalizado com desvio</div>
            </div>

            <div class="icon-container">
                <i class="fa fa-info-circle"></i>
                <div class="icon-description">Finalizado com sucesso</div>
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
    response = enviar_html(data, context=None)
    # Salvar o HTML gerado em um arquivo
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(response['body'])

    print("HTML gerado e salvo em index.html")
