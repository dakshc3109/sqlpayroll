💼 Payroll Management System
A robust, menu-driven Payroll Management System built with Python and MySQL, designed to streamline employee record management, salary structures, deductions, and payroll processing. Developed as part of Computer Science project work.
🚀 Features
  Employee Management: Seamlessly add, view, update, and delete employee profiles (names, departments, employment types, etc.).
  Salary & Compensation Tracking: Manage base salary rates, bonuses, and allowances efficiently.
  Deductions Calculator: Track statutory and internal deductions (tax, insurance, loans, provident funds).
  Automated Payroll Processing: Compute net pay accurately by processing gross earnings against total deductions.
  Relational Database Backend: Securely stores and queries all data using MySQL for persistent and reliable record-keeping.
  Interactive Interface: Clean, user-friendly command-line interface (CLI) driven by Python.
🛠️ Tech Stack
  Programming Language: Python 3.x
  Database Management System: MySQL
  Python Connectivity: mysql-connector-python
📁 Project Structure
  sqlpayroll/
  │
  ├── database/
  │   └── schema.sql            # MySQL database schema and initial dump
  │
  ├── main.py                   # Main application execution & navigation menu
  ├── db_config.py              # Database connection handler
  ├── requirements.txt          # Python dependencies
  └── README.md                 # Project documentation
⚙️ Installation & Setup Guide
  Prerequisites
  Ensure you have the following installed on your machine:
  Python (v3.8 or higher)
  MySQL Server (or XAMPP / MySQL Workbench)
  Step 1: Clone the Repository
    git clone https://github.com/dakshc3109/sqlpayroll.git
    cd sqlpayroll
  Step 2: Install Python Dependencies
    Install the required packages using pip:
    pip install -r requirements.txt
  Step 3: Set Up the Database
    Open your MySQL terminal or GUI client (like MySQL Workbench or phpMyAdmin).
    Create the database:
    CREATE DATABASE payroll;
    USE payroll;
    Import the tables and sample data using the provided SQL scripts in the database/ directory.
  Step 4: Configure Database Credentials
    Update your MySQL host, username, and password in db_config.py:
    DB_CONFIG = {
      'host': 'localhost',
      'user': 'root',
      'password': 'YOUR_MYSQL_PASSWORD',
      'database': 'payroll'
    }
  Step 5: Run the Application
    Execute the main script to start the program:
    python main.py
📊 Database Schema Design
  employee: Stores core personnel details (emp_id, fname, lname, gender, emp_type, division).
  salary: Manages pay grades and base compensation rates (salary_id, salary_rate).
  deductions: Tracks individual deductions like insurance, taxes, and loans.
  user: Handles secure admin authentication and login credentials.
💡 Future Enhancements
  [ ] Implement a graphical user interface (GUI) using Tkinter.
  [ ] Add support for generating downloadable PDF payslips.
  [ ] Enhance reporting features for monthly payroll summaries.
👨‍💻 Author
  Daksh Chaudhary
  GitHub: @dakshc3109
📜 License
  This project is open-source and available under the MIT License.
