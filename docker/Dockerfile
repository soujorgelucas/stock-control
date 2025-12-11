# Usar Python 3.11 como base
FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY . .

# Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expor porta da aplicação
EXPOSE 5000

# Comando para rodar a API
CMD ["python", "app/app.py"]
