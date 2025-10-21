-- Base mínima (MySQL 8+)
CREATE DATABASE IF NOT EXISTS portfolio_min
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE portfolio_min;

-- CLIENTES
CREATE TABLE customers (
  customer_id   INT AUTO_INCREMENT PRIMARY KEY,
  full_name     VARCHAR(120) NOT NULL,
  email         VARCHAR(150) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- PRODUCTOS
CREATE TABLE products (
  product_id    INT AUTO_INCREMENT PRIMARY KEY,
  name          VARCHAR(120) NOT NULL,
  price         DECIMAL(10,2) NOT NULL,
  stock         INT NOT NULL DEFAULT 0
) ENGINE=InnoDB;

-- PEDIDOS
CREATE TABLE orders (
  order_id      INT AUTO_INCREMENT PRIMARY KEY,
  customer_id   INT NOT NULL,
  order_date    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  status        ENUM('PENDING','PAID','CANCELLED') NOT NULL DEFAULT 'PENDING',
  CONSTRAINT fk_orders_customer
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- ITEMS DEL PEDIDO (tabla puente M:N)
CREATE TABLE order_items (
  order_id      INT NOT NULL,
  product_id    INT NOT NULL,
  quantity      INT NOT NULL,
  unit_price    DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (order_id, product_id),
  CONSTRAINT fk_oi_order
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
    ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT fk_oi_product
    FOREIGN KEY (product_id) REFERENCES products(product_id)
    ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

-- Índices simples
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_oi_product ON order_items(product_id);
