CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    country VARCHAR(50),
    risk_level VARCHAR(20),
    created_date DATE
);


CREATE TABLE assets (
    asset_id SERIAL PRIMARY KEY,
    asset_name VARCHAR(100),
    asset_class VARCHAR(50),
    sector VARCHAR(50)
);


CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    account_type VARCHAR(50),
    balance NUMERIC(12,2),
    opened_date DATE
);


CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT REFERENCES accounts(account_id),
    transaction_date DATE,
    transaction_type VARCHAR(20),
    amount NUMERIC(12,2),
    currency VARCHAR(10)
);


CREATE TABLE investments (
    investment_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    asset_id INT REFERENCES assets(asset_id),
    quantity NUMERIC(10,2),
    purchase_price NUMERIC(10,2),
    purchase_date DATE
);