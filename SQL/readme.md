# Portfolio DB –  (MySQL)

Este proyecto demuestra, con el caso más simple posible, el uso de **bases de datos relacionales**: modelo ER, **DDL**, **DML** y **consultas SQL** (`SELECT / JOIN / GROUP BY`) usando 4 tablas: `customers`, `products`, `orders`, `order_items`.

## Contenido del repositorio
- `ddl.sql` → Crea la base de datos `portfolio_min` y las tablas con claves primarias/foráneas.
- `dml.sql` → Inserta datos de ejemplo y muestra operaciones **INSERT/UPDATE/DELETE**.
- `consultas.sql` → Consultas de lectura con **JOIN** y **GROUP BY** (pedidos por cliente, totales, top productos).
- `erd_min.drawio` → Diagrama Entidad–Relación para abrir en [diagrams.net](https://app.diagrams.net/).

## Requisitos
- **MySQL 8.0+** (o MariaDB 10.6+), motor **InnoDB**
- Charset recomendado: `utf8mb4`

## Cómo ejecutar (rápido)
```bash
# 1) Crear DB y tablas (DDL)
mysql -u root -p < ddl.sql

# 2) Insertar datos y ejecutar DML (INSERT/UPDATE/DELETE)
mysql -u root -p < dml.sql

# 3) Probar consultas con JOIN/GROUP BY
mysql -u root -p < consultas.sql
