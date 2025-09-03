USE portfolio_min;

-- Datos de ejemplo
INSERT INTO customers (full_name, email) VALUES
('Ana García', 'ana@example.com'),
('Pedro Martínez', 'pedro@example.com');

INSERT INTO products (name, price, stock) VALUES
('Cadena 11v', 19990, 40),
('Cámara 29"', 4990, 100),
('Llave dinamométrica', 45990, 8);

-- Pedido de Ana
INSERT INTO orders (customer_id, status)
VALUES ((SELECT customer_id FROM customers WHERE email='ana@example.com'), 'PENDING');

SET @order_id := LAST_INSERT_ID();

-- Items del pedido (precios copiados como snapshot)
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
(@order_id, (SELECT product_id FROM products WHERE name='Cadena 11v' LIMIT 1), 2, 19990),
(@order_id, (SELECT product_id FROM products WHERE name='Cámara 29"' LIMIT 1), 3, 4990);

-- Ejemplos DML (manipulación)
-- UPDATE: cambia stock de un producto
UPDATE products SET stock = stock - 2 WHERE name='Cadena 11v' AND stock >= 2;

-- DELETE: elimina un producto que aún no ha sido vendido
DELETE p FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.product_id
WHERE p.name='Llave dinamométrica' AND oi.product_id IS NULL
LIMIT 1;
