import boto3
import re

# Configurações do bucket e arquivo
bucket_name = 'nome-do-seu-bucket'
file_key = 'caminho/do/seu/arquivo.html'

# Inicializa o cliente S3
s3 = boto3.client('s3')


# Função para baixar o arquivo HTML do bucket S3
def download_html_file():
    s3.download_file(bucket_name, file_key, 'arquivo_local.html')
    with open('arquivo_local.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content


# Função para editar o conteúdo HTML usando expressões regulares
def edit_html_content(html_content):
    # Conteúdo que queremos adicionar ao HTML
    new_content = "<p>Conteúdo adicionado com Python!</p>"

    # Padrão para localizar a tag onde inserir o novo conteúdo
    # Exemplo: insere logo após uma div com id="inserir-aqui"
    pattern = r'(<div id="inserir-aqui">)'

    # Substitui a tag alvo, adicionando o novo conteúdo logo após ela
    updated_html_content = re.sub(pattern, f'\\1{new_content}', html_content)

    return updated_html_content


# Função para fazer o upload do arquivo HTML atualizado para o bucket S3
def upload_updated_html(updated_html_content):
    with open('arquivo_local.html', 'w', encoding='utf-8') as file:
        file.write(updated_html_content)

    s3.upload_file('arquivo_local.html', bucket_name, file_key)


# Processo completo: baixar, editar e enviar de volta
html_content = download_html_file()
updated_content = edit_html_content(html_content)
upload_updated_html(updated_content)

print("Arquivo atualizado com sucesso no S3!")
