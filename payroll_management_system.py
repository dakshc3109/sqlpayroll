import mysql.connector
from mysql.connector import Error
import datetime

def setup_database():

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678"
        )

        cursor = con.cursor()

        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS payroll_db"
        )
        cursor.execute(
            "USE payroll_db"
        )

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS EMPLOYEE (
                EMP_ID INT PRIMARY KEY AUTO_INCREMENT,
                NAME VARCHAR(50) NOT NULL,
                DESIGNATION VARCHAR(50),
                DEPARTMENT VARCHAR(50),
                BASIC_SALARY FLOAT NOT NULL,
                DA FLOAT DEFAULT 0,
                STOCK_BONUS FLOAT DEFAULT 0,
                PF FLOAT DEFAULT 0,
                PHONE VARCHAR(15),
                EMAIL VARCHAR(50)
            )
        """)

        con.commit()

        cursor.close()
        con.close()

        print("\nDatabase and table are ready!\n")
        return True

    except Error as e:
        print("Database setup error:", e)
        return False


def connect_db():

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="payroll_db"
        )

        return con

    except Error as e:
        print("Database connection error:", e)
        return None

def add_employee():

    con = connect_db()

    if con is None:
        return

    cursor = con.cursor()

    try:

        print("\n---------- ADD NEW EMPLOYEE ----------")

        name = input("Enter Employee Name: ")
        designation = input("Enter Designation: ")
        department = input("Enter Department: ")

        basic = float(input("Enter Basic Salary: "))
        da = float(input("Enter DA: "))
        stock_bonus = float(input("Enter Stock Bonus: "))
        pf = float(input("Enter PF Deduction: "))

        phone = input("Enter Phone Number: ")
        email = input("Enter Email ID: ")
        if len(phone)<10:
            print("\nPlease enter a valid phone number.")
            if "@" not in email or ".com" not in email:
                    print("Also Please enter a valid email address.\n")
                    return
            return
        if "@" not in email or ".com" not in email:
                print("\nPlease enter a valid email address.\n")
                return
        

        query = """
            INSERT INTO EMPLOYEE
            (
                NAME,
                DESIGNATION,
                DEPARTMENT,
                BASIC_SALARY,
                DA,
                STOCK_BONUS,
                PF,
                PHONE,
                EMAIL
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            name,
            designation,
            department,
            basic,
            da,
            stock_bonus,
            pf,
            phone,
            email
        )

        cursor.execute(query, values)

        con.commit()

        print("\nEmployee added successfully!")
        print("Employee ID:", cursor.lastrowid)

    except ValueError:
        print("\nPlease enter valid numbers.")

    except Error as e:
        print("Error while adding employee:", e)

    finally:
        cursor.close()
        con.close()

def view_all_employees():

    con = connect_db()

    if con is None:
        return

    cursor = con.cursor()

    try:

        cursor.execute(
            "SELECT * FROM EMPLOYEE"
        )

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("\nNo records found.\n")
            return

        print("\n")
        print("=" * 120)
        print("                                                    ALL EMPLOYEES")
        print("=" * 120)

        print(
            "ID     NAME                 DESIGNATION          "
            "DEPARTMENT           BASIC        DA        BONUS          PF"
        )

        print("-" * 120)

        for row in rows:

            print(
                str(row[0]) + "      " +
                str(row[1]) + " " * (21 - len(str(row[1]))) +
                str(row[2]) + " " * (21 - len(str(row[2]))) +
                str(row[3]) + " " * (21 - len(str(row[3]))) +
                str(row[4]) + " " * (13 - len(str(row[4]))) +
                str(row[5]) + " " * (10 - len(str(row[5]))) +
                str(row[6]) + " " * (15 - len(str(row[6]))) +
                str(row[7])
            )

        print("=" * 120)
        print()

    except Error as e:
        print("Error while viewing employees:", e)

    finally:
        cursor.close()
        con.close()

def search_employee():

    con = connect_db()

    if con is None:
        return

    cursor = con.cursor()

    try:

        emp_id = int(
            input("\nEnter Employee ID to search: ")
        )

        query = """
            SELECT *
            FROM EMPLOYEE
            WHERE EMP_ID = %s
        """

        cursor.execute(query, (emp_id,))

        row = cursor.fetchone()

        if row is None:
            print("\nNo employee found with this ID.\n")
            return

        print("\n---------- EMPLOYEE DETAILS ----------")

        print("Employee ID:", row[0])
        print("Name:", row[1])
        print("Designation:", row[2])
        print("Department:", row[3])
        print("Basic Salary:", row[4])
        print("DA:", row[5])
        print("Stock Bonus:", row[6])
        print("PF:", row[7])
        print("Phone:", row[8])
        print("Email:", row[9])

        net_salary = (
            row[4]
            + row[5]
            + row[6]
            - row[7]
        )

        print("Net Salary:", net_salary)
        print()

    except ValueError:
        print("\nPlease enter a valid Employee ID.\n")

    except Error as e:
        print("Error while searching employee:", e)

    finally:
        cursor.close()
        con.close()

def update_payroll():

    con = connect_db()

    if con is None:
        return

    cursor = con.cursor()

    try:

        emp_id = int(
            input("\nEnter Employee ID to update: ")
        )

        query = """
            SELECT BASIC_SALARY, DA, STOCK_BONUS, PF
            FROM EMPLOYEE
            WHERE EMP_ID = %s
        """

        cursor.execute(query, (emp_id,))

        row = cursor.fetchone()

        if row is None:
            print("\nNo employee found with this ID.\n")
            return

        print("\n---------- CURRENT PAYROLL ----------")

        print("Basic Salary:", row[0])
        print("DA:", row[1])
        print("Stock Bonus:", row[2])
        print("PF:", row[3])

        print("\nEnter new value.")
        print("Press ENTER to keep the old value.")

        basic = input("New Basic Salary: ")

        if basic == "":
            new_basic = row[0]
        else:
            new_basic = float(basic)

        da = input("New DA: ")

        if da == "":
            new_da = row[1]
        else:
            new_da = float(da)

        stock = input("New Stock Bonus: ")

        if stock == "":
            new_stock = row[2]
        else:
            new_stock = float(stock)

        pf = input("New PF: ")

        if pf == "":
            new_pf = row[3]
        else:
            new_pf = float(pf)

        query = """
            UPDATE EMPLOYEE
            SET BASIC_SALARY = %s,
                DA = %s,
                STOCK_BONUS = %s,
                PF = %s
            WHERE EMP_ID = %s
        """

        values = (
            new_basic,
            new_da,
            new_stock,
            new_pf,
            emp_id
        )

        cursor.execute(query, values)

        con.commit()

        net_salary = (
            new_basic
            + new_da
            + new_stock
            - new_pf
        )

        print("\nPayroll updated successfully!")

        print("Basic Salary:", new_basic)
        print("DA:", new_da)
        print("Stock Bonus:", new_stock)
        print("PF:", new_pf)
        print("Net Salary:", net_salary)

        print()

    except ValueError:
        print("\nPlease enter valid numbers.\n")

    except Error as e:
        print("Error while updating payroll:", e)

    finally:
        cursor.close()
        con.close()


def delete_employee():

    con = connect_db()

    if con is None:
        return

    cursor = con.cursor()

    try:

        emp_id = int(
            input("\nEnter Employee ID to delete: ")
        )

        cursor.execute(
            "SELECT * FROM EMPLOYEE WHERE EMP_ID = %s",
            (emp_id,)
        )

        row = cursor.fetchone()

        if row is None:
            print("\nNo employee found with this ID.\n")
            return

        confirm = input(
            "Are you sure you want to delete? (y/n): "
        )

        if confirm.lower() == "y":

            cursor.execute(
                "DELETE FROM EMPLOYEE WHERE EMP_ID = %s",
                (emp_id,)
            )

            con.commit()

            print("\nRecord deleted successfully!\n")

        else:

            print("\nDeletion cancelled.\n")

    except ValueError:
        print("\nPlease enter a valid Employee ID.\n")

    except Error as e:
        print("Error while deleting employee:", e)

    finally:
        cursor.close()
        con.close()

def generate_payslip():

    con = connect_db()

    if con is None:
        return

    try:

        emp_id = int(
            input(
                "\nEnter Employee ID to generate payslip: "
            )
        )

        row, net_salary = calculate_net_salary(
            emp_id,
            con
        )

        if row is None:
            print("\nNo employee found with this ID.\n")
            return

        today = datetime.date.today()

        payslip = f"""
========================================
              PAYSLIP
========================================
Date            : {today}
Employee ID     : {row[0]}
Name            : {row[1]}
Designation     : {row[2]}
Department      : {row[3]}
----------------------------------------
Basic Salary    : Rs. {row[4]}
DA              : Rs. {row[5]}
Stock Bonus     : Rs. {row[6]}
PF Deduction    : Rs. {row[7]}
----------------------------------------
NET SALARY      : Rs. {net_salary}
========================================
"""

        print(payslip)

        filename = "payslip_" + str(row[0]) + ".txt"

        with open(filename, "w") as file:
            file.write(payslip)

        print("Payslip saved as:", filename)
        print()

    except ValueError:
        print("\nPlease enter a valid Employee ID.\n")

    except OSError as e:
        print("Error while saving payslip:", e)

    except Error as e:
        print("Database error:", e)

    finally:
        con.close()

def calculate_net_salary(emp_id, con):

    cursor = con.cursor()

    query = """
        SELECT *
        FROM EMPLOYEE
        WHERE EMP_ID = %s
    """

    cursor.execute(query, (emp_id,))

    row = cursor.fetchone()

    cursor.close()

    if row is None:
        return None, None

    basic = row[4]
    da = row[5]
    stock_bonus = row[6]
    pf = row[7]

    net_salary = (
        basic
        + da
        + stock_bonus
        - pf
    )

    return row, net_salary

def department_wise_report():

    con = connect_db()

    if con is None:
        return

    cursor = con.cursor()

    try:

        query = """
            SELECT
                DEPARTMENT,
                COUNT(*),
                SUM(
                    BASIC_SALARY
                    + DA
                    + STOCK_BONUS
                    - PF
                )
            FROM EMPLOYEE
            GROUP BY DEPARTMENT
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        if len(rows) == 0:
            print("\nNo employee records found.\n")
            return

        print(
            "\n---------- DEPARTMENT-WISE REPORT ----------"
        )

        print(
            "DEPARTMENT | EMPLOYEES | TOTAL PAYOUT"
        )

        print("-" * 50)

        for row in rows:

            print(
                row[0],
                "|",
                row[1],
                "|",
                row[2]
            )

        print()

    except Error as e:
        print(
            "Error while generating report:",
            e
        )

    finally:
        cursor.close()
        con.close()

def highest_paid_employee():

    con = connect_db()

    if con is None:
        return

    cursor = con.cursor()

    try:

        query = """
            SELECT
                NAME,
                DESIGNATION,
                BASIC_SALARY
                + DA
                + STOCK_BONUS
                - PF
            FROM EMPLOYEE
            ORDER BY
                BASIC_SALARY
                + DA
                + STOCK_BONUS
                - PF DESC
            LIMIT 1
        """

        cursor.execute(query)

        row = cursor.fetchone()

        if row is None:
            print("\nNo records found.\n")
            return

        print(
            "\n---------- HIGHEST PAID EMPLOYEE ----------"
        )

        print("Name:", row[0])
        print("Designation:", row[1])
        print("Net Salary:", row[2])

        print()

    except Error as e:
        print(
            "Error while finding highest paid employee:",
            e
        )

    finally:
        cursor.close()
        con.close()

def main_menu():

    while True:

        print("""
====================================================
          PAYROLL MANAGEMENT SYSTEM
====================================================

1. Add New Employee
2. View All Employees
3. Search Employee by ID
4. Update Employee Payroll
5. Delete Employee Record
6. Generate Payslip
7. Department-wise Salary Report
8. Show Highest Paid Employee
9. Exit

====================================================
""")

        choice = input(
            "Enter your choice (1-9): "
        )

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_all_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_payroll()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            generate_payslip()

        elif choice == "7":
            department_wise_report()

        elif choice == "8":
            highest_paid_employee()

        elif choice == "9":

            print(
                "\nThank you for using "
                "Payroll Management System!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter 1 to 9.\n"
            )


if setup_database():
    main_menu()
else:
    print("\nProgram could not start.")
