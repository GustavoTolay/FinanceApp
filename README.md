# Personal Finance Management API

The Personal Finance Management API is a tool built using Python and FastAPI that allows users to efficiently manage their personal finances by interacting with an SQLite database. This API provides a set of endpoints to perform various financial transactions, retrieve financial summaries, and track expenses. Whether you're an individual looking to track your expenses or a developer aiming to integrate financial management into an application, this API is designed to streamline these tasks.

## Features

- **Transaction Management:** Perform various financial transactions such as adding income, recording expenses, and more.

- **Expense Tracking:** Keep a record of your expenses by categorizing them, adding descriptions, and attaching relevant details.

- **Account Management:** Create and manage different financial accounts such as savings, checking, credit cards, and more.

- **Financial Summaries:** Retrieve summaries of your financial activities, including account balances, expense breakdowns, income sources, and net worth.

- **Secure Authentication:** Utilize token-based authentication to ensure secure access to your financial data.

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/GustavoTolay/FinanceApp.git
   ```

2. Navigate to the project directory.

   ```bash
   cd FinanceApp
   ```

3. Create a virtual environment and activate it.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

5. Run the API server.

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

6. The API will be accessible at `http://localhost:8000`.

## API Endpoints/Docs

The API documentation will be available at "http://localhost:8000/docs"

## Database

The API uses an SQLite database to store financial data. The database schema includes tables for transactions, accounts, categories, and more. You can find the database file named `record.db` in the project directory.

## Authentication

To access the API, you need to obtain an authentication token by making a POST request to `/token` with your username and password. Include the token in the headers of subsequent requests using the format `Authorization: Bearer <token>`.

Please note that this README provides a general and altered overview of the Personal Finance Management API. Some of the features listed above might not be true at all. Ty for reading <3
