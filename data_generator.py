from faker import Faker
import pandas as pd
from sqlalchemy import create_engine
import random


fake = Faker()


engine = create_engine(
    "postgresql://postgres:YOUR_PASSWORD@localhost:5432/finance_copilot"
)


# -----------------------------
# CUSTOMERS
# -----------------------------

def create_customers(n=1000):

    data = []

    for _ in range(n):
        data.append({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "country": random.choice(
                ["Canada", "USA", "UK", "Germany", "Poland"]
            ),
            "risk_level": random.choice(
                ["Low", "Medium", "High"]
            ),
            "created_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            )
        })

    return pd.DataFrame(data)



# -----------------------------
# ASSETS
# -----------------------------

def create_assets():

    data = [
        ["Apple Inc.", "Stock", "Technology"],
        ["Microsoft", "Stock", "Technology"],
        ["Tesla", "Stock", "Automotive"],
        ["S&P 500 ETF", "ETF", "Index"],
        ["US Treasury Bond", "Bond", "Government"],
        ["Gold ETF", "ETF", "Commodity"]
    ]

    return pd.DataFrame(
        data,
        columns=[
            "asset_name",
            "asset_class",
            "sector"
        ]
    )



# -----------------------------
# ACCOUNTS
# -----------------------------

def create_accounts(customer_ids, n=2000):

    data = []

    for _ in range(n):
        data.append({
            "customer_id": random.choice(customer_ids),
            "account_type": random.choice(
                ["Checking", "Savings", "Investment"]
            ),
            "balance": round(
                random.uniform(1000, 200000),
                2
            ),
            "opened_date": fake.date_between(
                start_date="-10y",
                end_date="today"
            )
        })

    return pd.DataFrame(data)



# -----------------------------
# TRANSACTIONS
# -----------------------------

def create_transactions(account_ids, n=50000):

    data = []

    for _ in range(n):

        data.append({
            "account_id": random.choice(account_ids),
            "transaction_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            ),
            "transaction_type": random.choice(
                ["Deposit", "Withdrawal", "Payment"]
            ),
            "amount": round(
                random.uniform(10,10000),
                2
            ),
            "currency": "USD"
        })

    return pd.DataFrame(data)



# -----------------------------
# INVESTMENTS
# -----------------------------

def create_investments(customer_ids, asset_ids, n=10000):

    data = []

    for _ in range(n):

        data.append({
            "customer_id": random.choice(customer_ids),
            "asset_id": random.choice(asset_ids),
            "quantity": round(
                random.uniform(1,100),
                2
            ),
            "purchase_price": round(
                random.uniform(20,500),
                2
            ),
            "purchase_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            )
        })

    return pd.DataFrame(data)



# =============================
# PIPELINE
# =============================

print("Creating customers...")

customers = create_customers()

customers.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False
)


customer_ids = pd.read_sql(
    "SELECT customer_id FROM customers",
    engine
)["customer_id"].tolist()



print("Creating assets...")

assets = create_assets()

assets.to_sql(
    "assets",
    engine,
    if_exists="append",
    index=False
)


asset_ids = pd.read_sql(
    "SELECT asset_id FROM assets",
    engine
)["asset_id"].tolist()



print("Creating accounts...")

accounts = create_accounts(customer_ids)

accounts.to_sql(
    "accounts",
    engine,
    if_exists="append",
    index=False
)


account_ids = pd.read_sql(
    "SELECT account_id FROM accounts",
    engine
)["account_id"].tolist()



print("Creating transactions...")

transactions = create_transactions(account_ids)

transactions.to_sql(
    "transactions",
    engine,
    if_exists="append",
    index=False
)



print("Creating investments...")

investments = create_investments(
    customer_ids,
    asset_ids
)

investments.to_sql(
    "investments",
    engine,
    if_exists="append",
    index=False
)


print("DONE! Finance database created.")