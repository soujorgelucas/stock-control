# stock-control

Projeto de protótipo de um sistema de controle de estoque desenvolvido em **Python** com **Flask**, **MySQL** e **Docker**.  
Permite gerenciar produtos, categorias, fornecedores e movimentações de estoque com controle automático.

---

## **Tecnologias Utilizadas**

- Python 3.11
- Flask
- MySQL 8.0
- Docker / Docker Compose
- MySQL Connector / Python
- Blueprint Flask para rotas organizadas

---

## **Funcionalidades**

- CRUD completo para:
  - Produtos
  - Categorias
  - Fornecedores
  - Movimentações de estoque
- Controle automático de estoque:
  - Entrada e saída de produtos
  - Validação de estoque insuficiente
- Relatórios:
  - Produtos abaixo do estoque mínimo
  - Valor total do estoque

---

## **Arquitetura do Projeto**

O projeto é organizado em módulos para facilitar manutenção e escalabilidade:

```

app/
├── app.py                  # Arquivo principal da API Flask
├── **init**.py             # Inicialização do Flask app
├── config/
│   └── database.py         # Configuração da conexão MySQL via pooling
├── models/                 # Classes representando tabelas do banco
│   ├── produto.py
│   ├── categoria.py
│   ├── fornecedor.py
│   └── movimentacao.py
├── repositories/           # CRUD direto no banco
│   ├── produto_repo.py
│   ├── categoria_repo.py
│   ├── fornecedor_repo.py
│   └── movimentacao_repo.py
├── services/               # Lógica de negócio
│   └── estoque_service.py
└── routes/                 # Endpoints da API (Blueprints)
├── produto_routes.py
├── categoria_routes.py
├── fornecedor_routes.py
└── movimentacao_routes.py
Dockerfile
docker-compose.yml
requirements.txt

```

**Fluxo do sistema:**

```

[API Flask] → [Services] → [Repositories] → [Banco MySQL]

````

- **API Flask** → Recebe requisições HTTP
- **Services** → Contém regras de negócio (controle de estoque, validações, relatórios)
- **Repositories** → CRUD no banco de dados
- **Banco MySQL** → Armazena todas as informações

---

## **Pré-requisitos**

- Docker e Docker Compose instalados
- Git (opcional)

---

## **Passo a Passo para Construção do Projeto**

1. **Clone o projeto**

```bash
git clone <url-do-repositorio>
cd nome-do-projeto
````

2. **Instale dependências (opcional, se quiser rodar localmente sem Docker)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. **Subir containers com Docker**

Recomendado: use o script helper `scripts/up.sh` a partir da raiz do projeto. Ele invoca o `docker compose` apontando para o arquivo `docker/docker-compose.yml` e, opcionalmente, importa o schema SQL.

```bash
# Torne o script executável (uma vez):
chmod +x scripts/up.sh

# Subir containers (em background):
./scripts/up.sh

# Subir containers e importar o schema SQL (após o MySQL ficar pronto):
./scripts/up.sh import-db
```

Comando alternativo (sem script):

```bash
docker compose -f docker/docker-compose.yml up --build
```

* A API estará disponível em: `http://localhost:5000`
* O MySQL estará disponível em: `localhost:3306` (usuário: root, senha: root, banco: estoque)

4. **Variáveis de ambiente usadas**

* `DB_HOST` → Host do MySQL (`mysql` no docker-compose)
* `DB_USER` → Usuário do MySQL (`root`)
* `DB_PASSWORD` → Senha do MySQL (`root`)
* `DB_NAME` → Nome do banco (`estoque`)

---

## **Estrutura do Banco de Dados (ER Simplificado)**

* **Produto**: id_produto, nome, descricao, id_categoria, id_fornecedor, quantidade_atual, preco_custo, preco_venda
* **Categoria**: id_categoria, nome, descricao
* **Fornecedor**: id_fornecedor, nome, cnpj, telefone, email
* **Movimentacao**: id_movimentacao, id_produto, tipo_movimentacao, quantidade, data_movimentacao, observacao

Relações:

* Produto → Categoria (1:N)
* Produto → Fornecedor (1:N)
* Movimentacao → Produto (N:1)

---

## **Endpoints da API**

### Produtos

| Método | Endpoint       | Descrição                |
| ------ | -------------- | ------------------------ |
| GET    | /produtos      | Listar todos os produtos |
| GET    | /produtos/<id> | Buscar produto por ID    |
| POST   | /produtos      | Criar novo produto       |
| PUT    | /produtos/<id> | Atualizar produto        |
| DELETE | /produtos/<id> | Deletar produto          |

### Categorias

| Método | Endpoint         | Descrição               |
| ------ | ---------------- | ----------------------- |
| GET    | /categorias      | Listar categorias       |
| GET    | /categorias/<id> | Buscar categoria por ID |
| POST   | /categorias      | Criar categoria         |
| PUT    | /categorias/<id> | Atualizar categoria     |
| DELETE | /categorias/<id> | Deletar categoria       |

### Fornecedores

| Método | Endpoint           | Descrição                |
| ------ | ------------------ | ------------------------ |
| GET    | /fornecedores      | Listar fornecedores      |
| GET    | /fornecedores/<id> | Buscar fornecedor por ID |
| POST   | /fornecedores      | Criar fornecedor         |
| PUT    | /fornecedores/<id> | Atualizar fornecedor     |
| DELETE | /fornecedores/<id> | Deletar fornecedor       |

### Movimentações

| Método | Endpoint            | Descrição                         |
| ------ | ------------------- | --------------------------------- |
| GET    | /movimentacoes      | Listar movimentações              |
| GET    | /movimentacoes/<id> | Buscar movimentação por ID        |
| POST   | /movimentacoes      | Criar entrada ou saída de produto |

---

## **Exemplos de Uso**

### 1. Criar um Produto

```bash
POST /produtos
Content-Type: application/json

{
  "nome": "Teclado Mecânico",
  "descricao": "Teclado RGB",
  "id_categoria": 1,
  "id_fornecedor": 1,
  "quantidade_atual": 10,
  "preco_custo": 100.0,
  "preco_venda": 150.0
}
```

### 2. Registrar Saída de Produto

```bash
POST /movimentacoes
Content-Type: application/json

{
  "id_produto": 1,
  "tipo_movimentacao": "saida",
  "quantidade": 2,
  "observacao": "Venda para cliente"
}
```

### 3. Verificar Produtos Abaixo do Estoque Mínimo

```python
from services.estoque_service import produtos_estoque_baixo
produtos_alerta = produtos_estoque_baixo(minimo=5)
for p in produtos_alerta:
    print(p.nome, p.quantidade_atual)
```

---

## **Serviços Importantes**

* `movimentar_estoque(id_produto, tipo, quantidade)` → Faz entrada ou saída de produtos.
* `produtos_estoque_baixo(minimo)` → Lista produtos com estoque baixo.
* `valor_total_estoque()` → Calcula valor total do estoque.

---

## **Contribuindo**

1. Clone o repositório
2. Faça alterações em `models/`, `repositories/`, `services/` ou `routes/`
3. Teste usando a API ou scripts Python
4. Commit e push das alterações

---

## **Autor**

* Nome: Seu Nome
* Email: [seuemail@dominio.com](mailto:seuemail@dominio.com)

---

## **Licença**

MIT License

```

---

Se você quiser, posso criar **uma versão ainda mais visual** com **diagrama da arquitetura incluído no README**, mostrando como API → Services → Repositórios → Banco interagem, tudo pronto para copiar e colar.  

Quer que eu faça essa versão visual?
```
