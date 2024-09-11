import os
import psycopg2
import allure

@allure.feature('Database Tests')
def test_database_connection():
    with allure.step("Connect to the database"):
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        assert conn is not None
        conn.close()

@allure.feature('Database Tests')
def test_insert_data():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    cursor = conn.cursor()

    with allure.step("Create table if not exists"):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT
            );
        """)

    with allure.step("Insert data into users table"):
        cursor.execute("INSERT INTO users (name, age) VALUES ('John Doe', 30);")
        conn.commit()

    cursor.close()
    conn.close()

@allure.feature('Database Tests')
def test_select_data():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    cursor = conn.cursor()

    with allure.step("Select data from users table"):
        cursor.execute("SELECT name, age FROM users WHERE name = 'John Doe';")
        result = cursor.fetchone()
        assert result == ('John Doe', 30)

    cursor.close()
    conn.close()

@allure.feature('Database Tests')
def test_update_data():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    cursor = conn.cursor()

    with allure.step("Update data in users table"):
        cursor.execute("UPDATE users SET age = 31 WHERE name = 'John Doe';")
        conn.commit()

    with allure.step("Select updated data"):
        cursor.execute("SELECT age FROM users WHERE name = 'John Doe';")
        result = cursor.fetchone()
        assert result[0] == 31

    cursor.close()
    conn.close()

@allure.feature('Database Tests')
def test_delete_data():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    cursor = conn.cursor()

    with allure.step("Delete data from users table"):
        cursor.execute("DELETE FROM users WHERE name = 'John Doe';")
        conn.commit()

    with allure.step("Verify data deletion"):
        cursor.execute("SELECT * FROM users WHERE name = 'John Doe';")
        result = cursor.fetchone()
        assert result is None

    cursor.close()
    conn.close()
