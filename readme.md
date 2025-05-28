# Vexus Data Pipeline
Automated Data Pipeline with Airflow, Python, and SQL Server


## Description

This project implements an automated pipeline for generating, ingesting, and storing simulated sales order data for a fictitious clothing store called Vexus. It uses Python to create the data and send it to the database, Apache Airflow for orchestration, and SQL Server for storage and querying.

## Features

- Daily generation of simulated data based on real products from the SQL Server database.
- Storage of data in CSV files organized by date.
- Automatic ingestion of CSV files into the SQL Server database.
- Data validation to avoid duplication and ensure integrity.
- Pipeline orchestrated and scheduled via Apache Airflow.

## Technologies Used

- Python
- Apache Airflow
- SQL Server
- pandas
- pyodbc

## Project Structure
- scripts
  - `__init__.py`
  - `db_utils.py`
  - `fake_data_generator.py`
  - `ingestion.py`
  - .env
- airflow
- raw_data
- .gitignore
- readme.md
- requirements.txt

## How to Run

### 1. Create and configure the `.env` file with your database credentials:

```env
DB_SERVER=your_server
DB_DATABASE=your_database
DB_USER=your_user
DB_PASSWORD=your_password 
```

### 2. Inside your project folder, create and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
.\venv\Scripts\activate        # Windows
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
### 4. Inside the virtual environment, run Airflow:
```bash
airflow standalone
```

## 🚀 Next Steps
🔁 Integration with Jenkins for automated deployment (CI/CD)

✅ Ensure idempotency in executions

🔍 Implement data quality and consistency checks

📈 Monitoring and alerting for pipeline failures

--------------------

## 📢 Contribution
Feel free to open issues or submit PRs with improvements, ideas, or fixes.

## 🧑‍💻 Author
Developed by __Gabriel Paliato__

# 📲 Connect with me on LinkedIn
I am always open to exchanging experiences, sharing knowledge, and exploring new opportunities in Data Engineering, Infrastructure, and DevOps.

Let's connect!
https://www.linkedin.com/in/gabriel-paliato-49467b211/

