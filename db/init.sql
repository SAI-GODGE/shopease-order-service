CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer VARCHAR(100) NOT NULL,
    item VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    status VARCHAR(20) NOT NULL DEFAULT 'PLACED',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO orders (customer, item, quantity, status) VALUES
    ('Asha Rao', 'Wireless Mouse', 2, 'SHIPPED'),
    ('Vikram Shah', 'Mechanical Keyboard', 1, 'PACKED'),
    ('Neha Kulkarni', 'USB-C Hub', 3, 'PLACED');
