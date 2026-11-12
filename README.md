# 💼 Payroll Management System

A robust, menu-driven **Payroll Management System** built with **Python** and **MySQL**, designed to streamline employee record management, salary structures, deductions, and payroll processing. Developed as part of Computer Science project work.

---

## 🚀 Features

- **Employee Management:** Seamlessly add, view, update, and delete employee profiles (names, departments, employment types, etc.).
- **Salary & Compensation Tracking:** Manage base salary rates, bonuses, and allowances efficiently.
- **Deductions Calculator:** Track statutory and internal deductions (tax, insurance, loans, provident funds).
- **Automated Payroll Processing:** Compute net pay accurately by processing gross earnings against total deductions.
- **Relational Database Backend:** Securely stores and queries all data using MySQL for persistent and reliable record-keeping.
- **Interactive Interface:** Clean, user-friendly command-line interface (CLI) driven by Python.

---

## 🛠️ Tech Stack

- **Programming Language:** Python 3.x
- **Database Management System:** MySQL
- **Python Connectivity:** `mysql-connector-python`

---

## 📁 Project Structure

```text
sqlpayroll/
│
├── payroll_management_system.py # Main application script (contains logic, menu, and database connectivity)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ Installation & Setup Guide

### Prerequisites
Ensure you have the following installed on your machine:
- **Python** (v3.8 or higher)
- **MySQL Server** (or XAMPP / MySQL Workbench)

### Step 1: Clone the Repository
```bash
git clone [https://github.com/dakshc3109/sqlpayroll.git](https://github.com/dakshc3109/sqlpayroll.git)
cd sqlpayroll
```

### Step 2: Install Python Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Database
1. Open your MySQL terminal or GUI client (like MySQL Workbench or phpMyAdmin).
2. Create the database and tables required by the project:
   ```sql
   CREATE DATABASE payroll;
   USE payroll;
   ```
   *(Make sure to run your table creation queries or schema setup here).*

### Step 4: Configure Database Credentials
Open `payroll_management_system.py` and update your MySQL connection details (host, user, password, database) in the database connection block:
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="payroll"
)
```

### Step 5: Run the Application
Execute the main script to start the program:
```bash
python payroll_management_system.py
```

---

## 📊 Database Schema Design

- **`employee`**: Stores core personnel details (`emp_id`, `fname`, `lname`, `gender`, `emp_type`, `division`).
- **`salary`**: Manages pay grades and base compensation rates (`salary_id`, `salary_rate`).
- **`deductions`**: Tracks individual deductions like insurance, taxes, and loans.
- **`user`**: Handles secure admin authentication and login credentials.

---

## 💡 Future Enhancements

- [ ] Implement a graphical user interface (GUI) using `Tkinter`.
- [ ] Add support for generating downloadable PDF payslips.
- [ ] Enhance reporting features for monthly payroll summaries.

---

## 👨‍💻 Author

**Daksh Chaudhary**  
- GitHub: [@dakshc3109](https://github.com/dakshc3109)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
