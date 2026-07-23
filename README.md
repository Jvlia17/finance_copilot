# Finance Copilot – LLM-Powered Text-to-SQL Assistant

End-to-end AI project that enables users to query a financial database using natural language.

The project demonstrates how Large Language Models (LLMs) can be integrated with relational databases to translate business questions into SQL queries, execute them, and deliver data-driven insights.

The system implements a Text-to-SQL financial analytics assistant capable of answering questions about customers, accounts, transactions, and investments.

---

# 🔷 Project Overview

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

---

# 🎯 Business Problem

Business users often need insights from databases but extracting information requires SQL knowledge.

The goal of this project is to reduce the gap between business questions and database access by allowing users to query financial data using natural language.

Potential applications:

- Self-service analytics tools
- Banking dashboards
- Financial reporting assistants
- Business intelligence automation

---

# 🗄️ Database Design

The project uses a PostgreSQL relational database representing a financial institution.

The database contains the following entities:

## Customers

Stores customer information:

- Customer ID
- Name
- Country
- Risk level
- Account creation date

## Accounts

Contains customer banking accounts:

- Account ID
- Customer ID
- Account type
- Balance
- Opening date

## Transactions

Stores account activity:

- Transaction ID
- Account ID
- Transaction date
- Transaction type
- Amount
- Currency

## Investments

Contains customer investment data:

- Investment ID
- Customer ID
- Asset ID
- Quantity
- Purchase price
- Purchase date

## Assets

Stores financial instruments:

- Asset name
- Asset class
- Sector

---

# 🧠 Natural Language Processing Pipeline

The system performs:

```text
User Question
      |
      v
Context Injection (Database Schema + Instructions)
      |
      v
SQL Generation
      |
      v
Query Execution
      |
      v
Result Retrieval
```

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

# 🧪 Technologies Used

## Programming
- Python
- SQL

## Database
- PostgreSQL

## AI / LLM
- Groq API
- Large Language Models (LLMs)
- Prompt Engineering
- Text-to-SQL generation

## Python Libraries
- pandas
- psycopg2
- python-dotenv

## Development Tools
- Git
- PyCharm

---

# 📊 Evaluation Dataset

To measure SQL generation quality, an evaluation dataset was created.

The dataset contains:

- Natural language questions
- Expected SQL queries
- Different difficulty levels

---

# 📈 Model Evaluation

The Text-to-SQL assistant was evaluated using a custom benchmark dataset containing 20 natural language queries.

The evaluation uses an execution-based approach: generated SQL queries are executed against the PostgreSQL database, and results are compared with the expected outputs.

This approach allows evaluation of query correctness based on actual database results rather than exact SQL string matching.

## 📊 Evaluation Coverage

The benchmark includes different levels of SQL complexity:

- Basic SQL queries
- Intermediate analytical queries
- Advanced financial analytics queries

The evaluation dataset covers:

- Aggregations (`COUNT`, `SUM`, `AVG`, `MAX`)
- Filtering conditions (`WHERE`)
- Sorting and limiting results (`ORDER BY`, `LIMIT`)
- `GROUP BY` operations
- Multi-table joins
- Financial calculations

---

## 🧪 Evaluation Results

| Difficulty | Passed | Total | Accuracy |
|------------|--------|-------|----------|
| Basic | 10/10 | 10 | 100% |
| Intermediate | 4/6 | 6 | 67% |
| Advanced | 2/4 | 4 | 50% |
| **Overall** | **16/20** | **20** | **80%** |

Overall accuracy:

**80%**

---

## 🔍 Evaluation Insights

The model achieved strong performance on basic analytical queries involving:

- Data aggregation
- Filtering conditions
- Simple database lookups
- Single-table SQL operations

Most failures occurred in scenarios requiring more complex SQL reasoning, including:

- Multi-table joins and understanding relationships between database entities
- Aggregations combined with sorting and ranking logic
- Identifying missing relationships using `LEFT JOIN` and `NULL` filtering
- Translating business questions into precise SQL operations

The results show that the model can reliably handle common analytical queries, while more complex tasks requiring multi-step reasoning and deeper understanding of relational structures remain challenging.

---

# 📁 Project Structure

```text
finance_copilot/
│
├── python/
│ ├── sql_agent.py
│ ├── evaluate.py
│ └── data_generator.py
│
├── sql/
│ └── create_tables.sql
│
├── data/
│ └── evaluation_dataset.json
│
├── config/
│ └── database_schema.json
│
├── results/
│ └── evaluation_results.json
│
├── requirements.txt
├── README.md
└── .env # Environment variables (not included)
```

---

# 🚀 How to Run the Project

1. Clone the repository

Clone the project from GitHub:
```bash
git clone <repository-url>
cd finance_copilot
```

2. Install dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

3. Configure environment variables

Create a .env file in the project root directory:

```bash
GROQ_API_KEY=your_api_key
```

The API key is required to connect the Large Language Model used for SQL generation.

4. Set up PostgreSQL database

Create the database tables by executing:

Run sql/create_tables.sql in PostgreSQL to create database tables.

Generate synthetic financial data:

```bash
cd python
python data_generator.py
```

5. Run the Text-to-SQL assistant

Start the application:

```bash
python sql_agent.py
```

Example:

Ask a database question:
- What is the average account balance by country?

The assistant will:

- Process the natural language question
- Generate SQL using the LLM
- Execute the query against PostgreSQL
- Return the database result

6. Run evaluation

Evaluate SQL generation performance:

```bash
python evaluate.py
```

The evaluation script:

- Loads benchmark questions from data/evaluation_dataset.json
- Generates SQL queries
- Executes queries against PostgreSQL
- Compares generated results with expected outputs
- Calculates accuracy

---

# 🔮 Future Improvements

Potential improvements:

- Add automatic SQL validation before execution
- Improve prompt engineering for complex joins
- Add conversational memory for multi-step questions
- Add query explanation functionality
- Support larger real-world financial datasets
