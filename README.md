# Pure Element ETL Pipeline
Automated inventory management system for a luxury jewelry brand (PURE ELEMENT).

## Tech Stack
- **Python**: Core logic and automation.
- **Pandas**: Data transformation and categorization.
- **PostgreSQL**: Production database for sales records.
- **SQLAlchemy**: Database connection and management.

## Features
- **Security**: Secure credential management using `.env` to protect database secrets.
- **Automation**: Automated item categorization (Luxury Timepieces vs Fine Jewelry) using Python logic.
- **Scalability**: Seamless data loading from flat CSV files into a relational SQL environment.

## Data Validation
I use **DBeaver Community Edition** as my primary Database Administration tool to verify successful ETL runs. This allows me to:
* Run SQL audits to ensure data integrity.
* Visualize the `vault_sales` schema.
* Execute complex queries to track high-value inventory performance.

<img width="1279" height="804" alt="image" src="https://github.com/user-attachments/assets/518ec8b8-317a-4fd0-879c-1344aeb1c49b" />

## Setup & Usage
1. **Clone the repository** to your local machine.
2. **Create a local `.env` file** and add your `DB_PASSWORD`.
3. **Install dependencies** by running:  
   `pip install -r requirements.txt`
4. **Trigger the pipeline** by executing:  
   `python main.py`

   
