# Finance Database Schema

## customers

Stores customer information.

Columns:

- customer_id:
  Unique identifier for each customer.

- first_name:
  Customer first name.

- last_name:
  Customer last name.

- country:
  Customer country.

- risk_level:
  Customer risk category:
  Low, Medium, High.

- created_date:
  Date when customer profile was created.


---

## accounts

Stores customer bank accounts.

Columns:

- account_id:
  Unique identifier.

- customer_id:
  Foreign key referencing customers.

- account_type:
  Type of account:
  Checking, Savings, Investment.

- balance:
  Current account balance.

- opened_date:
  Account opening date.


Relationship:

accounts.customer_id → customers.customer_id


---

## assets

Stores financial instruments.

Columns:

- asset_id:
  Unique identifier.

- asset_name:
  Name of asset.

Examples:
Apple Inc., Tesla, S&P 500 ETF.

- asset_class:
  Stock, ETF, Bond.

- sector:
  Technology, Government, Commodity, etc.


---

## transactions

Stores account transactions.

Columns:

- transaction_id:
  Unique identifier.

- account_id:
  Related bank account.

- transaction_date:
  Date of transaction.

- transaction_type:
  Deposit, Withdrawal, Payment.

- amount:
  Transaction value.

- currency:
  Transaction currency.


Relationship:

transactions.account_id → accounts.account_id


---

## investments

Stores customer investments.

Columns:

- investment_id:
  Unique identifier.

- customer_id:
  Investor.

- asset_id:
  Purchased asset.

- quantity:
  Number of units.

- purchase_price:
  Price per unit.

- purchase_date:
  Investment date.


Relationship:

investments.customer_id → customers.customer_id

investments.asset_id → assets.asset_id