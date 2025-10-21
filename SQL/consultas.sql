USE portfolio_min;

-- 1) Pedidos de un cliente específico (por email)
SELECT o.order_id, o.order_date, o.status
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
WHERE c.email = 'ana@example.com'
ORDER BY o.order_date DESC;

-- 2) Detalle de un pedido con totales por línea
-- (usa el último pedido insertado como ejemplo)
SET @sample_order := (SELECT MAX(order_id) FROM orders);

SELECT
  oi.order_id,
  p.name AS product_name,
  oi.quantity,
  oi.unit_price,
  (oi.quantity * oi.unit_price) AS line_total
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
WHERE oi.order_id = @sample_order;

-- 3) Total del pedido (suma de líneas)
SELECT
  oi.order_id,
  SUM(oi.quantity * oi.unit_price) AS order_total
FROM order_items oi
WHERE oi.order_id = @sample_order
GROUP BY oi.order_id;

-- 4) Total comprado por cada cliente (JOIN + GROUP BY)
SELECT
  c.customer_id,
  c.full_name,
  SUM(oi.quantity * oi.unit_price) AS total_spent
FROM customers c
JOIN orders o       ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
GROUP BY c.customer_id, c.full_name
ORDER BY total_spent DESC;

-- 5) Top productos por unidades vendidas
SELECT
  p.product_id,
  p.name,
  SUM(oi.quantity) AS units_sold
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
GROUP BY p.product_id, p.name
ORDER BY units_sold DESC;
