INSERT INTO customers (id, name, city) VALUES
(1, 'Arun', 'Chennai'),
(2, 'Priya', 'Coimbatore'),
(3, 'Karthik', 'Madurai'),
(4, 'Divya', 'Trichy'),
(5, 'Vignesh', 'Salem');

INSERT INTO orders (id, customer_id, product_name, quantity, total_amount, order_date) VALUES
(1, 1, 'Laptop', 1, 55000, '2026-06-10'),
(2, 1, 'Mouse', 2, 1200, '2026-06-11'),
(3, 2, 'Keyboard', 1, 1800, '2026-06-12'),
(4, 3, 'Monitor', 1, 14000, '2026-06-13'),
(5, 2, 'Headset', 1, 2500, '2026-06-14'),
(6, 4, 'Printer', 1, 9000, '2026-06-14'),
(7, 5, 'Webcam', 2, 3200, '2026-06-15');