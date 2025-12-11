#!/usr/bin/env bash
set -euo pipefail

# scripts/up.sh
# Script helper para subir os containers do projeto a partir da raiz

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "[scripts/up.sh] Diretório do projeto: $ROOT_DIR"

echo "[scripts/up.sh] Subindo containers com Docker Compose..."
docker compose -f docker/docker-compose.yml up -d --build

if [ "${1:-}" = "import-db" ]; then
  echo "[scripts/up.sh] Importando schema SQL para o container MySQL..."
  # Espera o MySQL ficar pronto
  for i in {1..30}; do
    if docker exec estoque_mysql mysql -uroot -proot -e "SELECT 1" >/dev/null 2>&1; then
      echo "[scripts/up.sh] MySQL está pronto"
      break
    fi
    echo "[scripts/up.sh] Aguardando MySQL... ($i/30)"
    sleep 2
  done

  if docker ps --format '{{.Names}}' | grep -q '^estoque_mysql$'; then
    docker cp sql/schema.sql estoque_mysql:/schema.sql
    docker exec -i estoque_mysql sh -c 'mysql -u root -proot < /schema.sql'
    echo "[scripts/up.sh] Schema importado com sucesso."
  else
    echo "[scripts/up.sh] Container 'estoque_mysql' não encontrado. Verifique se os containers estão rodando." >&2
    exit 1
  fi
fi

echo "[scripts/up.sh] Pronto. A API deve estar disponível em http://localhost:5000"
