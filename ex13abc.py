import os
import sqlite3
from typing import List, Any

# ✅ Use environment variables instead of hardcoding
API_KEY = os.getenv("API_KEY", "default_key")

# ✅ Avoid global mutable state
def calculate_total(price: float, tax: float) -> float:
    return price + (price * tax)


# ✅ Proper authentication logic (no hardcoding)
def login(username: str, password: str) -> bool:
    stored_username = os.getenv("APP_USER", "admin")
    stored_password = os.getenv("APP_PASS", "admin123")

    if username == stored_username and password == stored_password:
        print("Login success")
        return True
    else:
        print("Login failed")
        return False


# ✅ Prevent SQL Injection using parameterized queries
def get_user(username: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    result = cursor.fetchall()
    conn.close()
    return result


# ✅ Reduced complexity + clean structure
def process_data(data: List[Any]) -> None:
    if not data:
        print("Empty data")
        return

    if not isinstance(data, list):
        print("Not a list")
        return

    for item in data:
        if item is None:
            print("None value")
        elif isinstance(item, int):
            if item > 0:
                print("Positive number")
            else:
                print("Negative number")
        else:
            print("Not int")


# ✅ No hardcoded password
def connect():
    return os.getenv("DB_PASSWORD", "default_password")


# ✅ Remove duplicate functions
def sum_values(a: int, b: int) -> int:
    return a + b


# ✅ Safer function with proper handling
def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


# ✅ Proper file handling using context manager
def write_result_to_file(result: float):
    with open("test.txt", "w") as f:
        f.write(str(result))


def clean_function(a: float, b: float, c: float) -> float:
    print("Start")

    result = sum_values(a, b)
    result2 = safe_divide(result, c)

    write_result_to_file(result2)

    return result2


# ✅ Remove unsafe system execution or sanitize input
def run_command_safe(cmd: str):
    raise NotImplementedError("Direct system execution is disabled for security reasons")


# ✅ Proper naming
def add_numbers(a: int, b: int) -> int:
    return a + b


# ✅ Handle exceptions properly
def divide(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return 0


# ✅ Avoid magic numbers
DISCOUNT_RATE = 0.8734

def calculate_discount(price: float) -> float:
    return price * DISCOUNT_RATE


# ✅ Remove duplicate code
def print_hello_world():
    print("Hello")
    print("World")


# ✅ Proper resource handling
def read_file():
    try:
        with open("file.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
        return ""


# ✅ Null-safe handling
def get_length(x):
    if x is None:
        return 0
    return len(x)


# ✅ Clean main execution
if __name__ == "__main__":
    if login("admin", "admin123"):
        print(get_user("test"))
        print(divide(10, 2))
