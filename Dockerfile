FROM python:3.10-slim

WORKDIR /app

# Instala dependências do sistema operacional necessárias para compilar pacotes se houver
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala os pacotes do requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia todo o ecossistema do projeto para dentro do container
COPY . .

# Expõe a porta padrão que o servidor Uvicorn vai rodar
EXPOSE 8000

# Inicializa o Uvicorn apontando para a aplicação de forma irrestrita na nuvem
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
