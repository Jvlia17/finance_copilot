# Finance Copilot – LLM-Powered Text-to-SQL Assistant

End-to-end AI project that enables users to query a financial database using natural language.

The project demonstrates how Large Language Models (LLMs) can be combined with relational databases to automatically generate SQL queries from user questions, execute them, and return business insights.

The system simulates a financial analytics assistant capable of answering questions about customers, accounts, transactions, and investments.

---

# 🔷 Project Overview

Accessing business data often requires SQL knowledge, which creates a barrier for non-technical users.

The goal of this project is to build a Natural Language to SQL assistant that allows users to interact with structured financial data by simply asking questions in plain English.

Example:

User:
> "What is the average account balance by country?"

AI-generated SQL:

```sql
SELECT 
    c.country,
    AVG(a.balance)
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id
GROUP BY c.country;
```

The project combines:

Large Language Models (LLMs) for SQL generation
PostgreSQL for structured data storage
Python for database interaction and automation
Prompt engineering for reliable SQL generation
Evaluation datasets for measuring model performance.

---

# 🎯 Business Problem

Many organizations store valuable information in relational databases, but extracting insights often requires technical SQL expertise.

The objective of this project is to create an AI-powered analytics assistant that allows business users to interact with financial data using natural language.

Potential applications:

Banking analytics assistants
Self-service BI tools
Customer support analytics
Financial reporting automation

---

# 🗄️ Database Design

The project uses a PostgreSQL relational database simulating a financial institution.

The database contains:

Customers

Stores customer information:

Customer ID
Name
Country
Risk level
Account creation date
Accounts

Contains customer banking accounts:

Account ID
Customer ID
Account type
Balance
Opening date
Transactions

Stores account activity:

Transaction ID
Account ID
Transaction date
Transaction type
Amount
Currency
Investments

Contains customer investment data:

Investment ID
Customer ID
Asset ID
Quantity
Purchase price
Purchase date
Assets

Stores financial instruments:

Asset name
Asset class
Sector

---

# ⚙️ System Architecture

The application follows a Text-to-SQL pipeline:

User Question
      |
      v
LLM Prompt
      |
      v
SQL Generation
      |
      v
PostgreSQL Database
      |
      v
Query Execution
      |
      v
Business Result

---

# 🧠 Natural Language Processing Pipeline

The system performs:

1. User Input Processing

Example:

"What is the total transaction volume by country?"

↓

2. Context Injection

The LLM receives:

Database schema
Table relationships
Column descriptions
SQL generation instructions

↓

3. SQL Generation

The model creates a PostgreSQL query.

↓

4. Query Execution

Generated SQL is executed against the database.

↓

5. Result Retrieval

The user receives the requested information.

---

# 🤖 Large Language Model Integration

The project uses an LLM-based Text-to-SQL pipeline to translate natural language requests into PostgreSQL queries.

The model is responsible for:

- Understanding user intent
- Mapping questions to database entities
- Generating SQL syntax
- Applying correct joins, aggregations, and filtering logic

The system uses prompt engineering techniques to improve:

- SQL generation accuracy
- Schema understanding
- Query reliability
- Consistency of generated outputs

---

# 📊 Evaluation Dataset

To measure SQL generation quality, an evaluation dataset was created.

The dataset contains:

Natural language questions
Expected SQL queries
Different difficulty levels

Examples:

Easy:

"How many customers are in the database?"

Medium:

"What is the average account balance by country?"

Advanced:

"Rank customers by total investment value."

The evaluation dataset allows:

Testing model performance
Comparing different LLMs
Improving prompts
Detecting SQL generation errors

---

# 📈 Model Evaluation

The Text-to-SQL assistant was evaluated using a custom benchmark dataset containing 20 natural language queries.

The evaluation focuses on whether the generated SQL query produces the same results as the expected SQL query when executed against the PostgreSQL database.

Evaluation categories:

- Basic SQL queries
- Intermediate analytical queries
- Advanced financial analytics queries

The benchmark covers:

- Aggregations (`COUNT`, `SUM`, `AVG`, `MAX`)
- Filtering conditions
- Sorting and limiting results
- `GROUP BY` operations
- Table joins
- Financial calculations


## Evaluation Results

Initial evaluation results:

| Difficulty | Passed | Total | Accuracy |
|------------|--------|-------|----------|
| Basic | 10/10 | 10 | 100% |
| Intermediate | 4/6 | 6 | 67% |
| Advanced | 2/4 | 4 | 50% |
| **Overall** | **16/20** | **20** | **80%** |


Overall accuracy:

**80%**


## Evaluation Insights

The model achieved strong performance on basic analytical queries involving:

- Data aggregation
- Filtering
- Simple database lookups

Most failures occurred in scenarios requiring more complex SQL reasoning, including:

- Multi-table joins and understanding relationships between database entities
- Aggregations combined with sorting and ranking logic
- Identifying missing relationships using LEFT JOIN and NULL filtering
- Translating business questions into precise SQL operations

The model performed well on basic retrieval and aggregation tasks, but showed limitations when queries required deeper understanding of table relationships and multi-step reasoning.