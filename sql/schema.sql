-- ===============================
-- Banco de Dados: Estoque
-- ===============================
CREATE DATABASE IF NOT EXISTS estoque;
USE estoque;

-- ===============================
-- Tabela: Categoria
-- ===============================
CREATE TABLE IF NOT EXISTS categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255)
);

-- ===============================
-- Tabela: Fornecedor
-- ===============================
CREATE TABLE IF NOT EXISTS fornecedor (
    id_fornecedor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cnpj VARCHAR(20),
    telefone VARCHAR(20),
    email VARCHAR(100)
);

-- ===============================
-- Tabela: Produto
-- ===============================
CREATE TABLE IF NOT EXISTS produto (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    descricao VARCHAR(255),
    id_categoria INT,
    id_fornecedor INT,
    quantidade_atual INT DEFAULT 0,
    preco_custo DECIMAL(10,2) DEFAULT 0.00,
    preco_venda DECIMAL(10,2) DEFAULT 0.00,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria) ON DELETE SET NULL,
    FOREIGN KEY (id_fornecedor) REFERENCES fornecedor(id_fornecedor) ON DELETE SET NULL
);

-- ===============================
-- Tabela: Movimentacao
-- ===============================
CREATE TABLE IF NOT EXISTS movimentacao (
    id_movimentacao INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    tipo_movimentacao ENUM('entrada', 'saida') NOT NULL,
    quantidade INT NOT NULL,
    data_movimentacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    observacao VARCHAR(255),
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto) ON DELETE CASCADE
);

-- ===============================
-- Inserts de exemplo
-- ===============================

INSERT INTO categoria (nome, descricao) VALUES
('Eletrônicos', 'Produtos eletrônicos diversos'),
('Alimentos', 'Produtos alimentícios'),
('Limpeza', 'Produtos de limpeza');

INSERT INTO fornecedor (nome, cnpj, telefone, email) VALUES
('Fornecedor A', '12.345.678/0001-90', '1111-2222', 'fornecedorA@email.com'),
('Fornecedor B', '98.765.432/0001-10', '3333-4444', 'fornecedorB@email.com');

INSERT INTO produto (nome, descricao, id_categoria, id_fornecedor, quantidade_atual, preco_custo, preco_venda) VALUES
('Notebook', 'Notebook Intel i5 8GB', 1, 1, 10, 2500.00, 3000.00),
('Arroz', 'Arroz 5kg', 2, 2, 50, 20.00, 30.00),
('Detergente', 'Detergente líquido 500ml', 3, 2, 30, 3.50, 5.00);

INSERT INTO movimentacao (id_produto, tipo_movimentacao, quantidade, observacao) VALUES
(1, 'entrada', 10, 'Estoque inicial'),
(2, 'entrada', 50, 'Estoque inicial'),
(3, 'entrada', 30, 'Estoque inicial');
