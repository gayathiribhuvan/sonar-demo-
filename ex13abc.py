# ===============================
# BAD CODE FOR SONARQUBE TESTING
# ===============================

import os
import sqlite3

# ❌ HARD CODED SECRET (VULNERABILITY)
API_KEY = "123456789SECRET"

# ❌ GLOBAL VARIABLE MISUSE
user_data = {}

# ❌ DUPLICATE FUNCTION 1
def calculate_total(price, tax):
    total = price + (price * tax)
    return total

# ❌ DUPLICATE FUNCTION 2 (same logic)
def calculate_total_duplicate(price, tax):
    total = price + (price * tax)
    return total


# ❌ FUNCTION WITH MULTIPLE ISSUES
def login(username, password):
    # ❌ hardcoded credentials
    if username == "admin" and password == "admin123":
        print("Login success")
    else:
        print("Login failed")

    # ❌ unused variable
    temp = 12345

    # ❌ empty catch block (code smell)
    try:
        x = 10 / 0
    except:
        pass

    return True  # ❌ always returns true (logic bug)


# ❌ SQL INJECTION VULNERABILITY
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ directly injecting user input
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result


# ❌ VERY COMPLEX FUNCTION (CODE SMELL)
def process_data(data):
    if data:
        if isinstance(data, list):
            for i in range(len(data)):
                if data[i] is not None:
                    if type(data[i]) == int:
                        if data[i] > 0:
                            print("Positive number")
                        else:
                            print("Negative number")
                    else:
                        print("Not int")
                else:
                    print("None value")
        else:
            print("Not a list")
    else:
        print("Empty data")


# ❌ HARDCODED PASSWORD AGAIN
def connect():
    password = "root123"
    return password


# ❌ DUPLICATE LOGIC AGAIN
def sum_values(a, b):
    return a + b

def sum_values_copy(a, b):
    return a + b


# ❌ FUNCTION WITH TOO MANY RESPONSIBILITIES
def messy_function(a, b, c):
    print("Start")

    # calculation
    result = a + b

    # ❌ possible crash
    result2 = result / c

    # file handling without closing properly
    f = open("test.txt", "w")
    f.write(str(result2))

    # ❌ debug print (code smell)
    print("DEBUG:", result2)

    return result2


# ❌ DEAD CODE
def unused_function():
    print("This function is never used")


# ❌ INSECURE OS COMMAND
def run_command(cmd):
    os.system(cmd)  # command injection risk


# ❌ BAD NAMING + STYLE ISSUES
def X(a,b):
 return a+b


# ❌ NO ERROR HANDLING
def divide(a, b):
    return a / b


# ❌ MAGIC NUMBERS
def calculate_discount(price):
    return price * 0.8734


# ❌ REPEATED CODE BLOCK
def repeated1():
    print("Hello")
    print("World")

def repeated2():
    print("Hello")
    print("World")


# ❌ IMPROPER RESOURCE HANDLING
def read_file():
    f = open("file.txt", "r")
    data = f.read()
    return data


# ❌ POTENTIAL NULL ISSUE
def get_length(x):
    return len(x)


# ❌ MAIN EXECUTION (bad practice)
if __name__ == "__main__":
    login("admin", "admin123")
    print(get_user("test' OR '1'='1"))
    divide(10, 0)
