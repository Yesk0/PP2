import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345678"
)

cur = conn.cursor()

def inputData():
    name = input("Hello input your name: ")
    number = input("Input your phone number: ")
    cur.execute('INSERT INTO phone_book("PersonName", "PhoneNumber") VALUES(%s, %s);', (name, number))

csv_file_path = r"C:\Users\Asus\Desktop\github\PP2\Lab12\phonebook\info.csv"

def importFromCSV():
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            personName, phoneNumber = row
            cur.execute('INSERT INTO phone_book("PersonName", "PhoneNumber") VALUES(%s, %s);', (personName, phoneNumber))

def update_contact(personName, phoneNumber):
    cur.execute('UPDATE phone_book SET "PhoneNumber" = %s WHERE "PersonName" = %s;', (phoneNumber, personName))

def queryData():
    cur.execute('SELECT * FROM phone_book;')
    data = cur.fetchall()
    path = r"C:\Users\Asus\Desktop\github\PP2\Lab12\phonebook\queredData.txt"

    with open(path, "w") as f:
        for row in data:
            f.write("Name: " + str(row[1]) + "\n" + "Number: " + str(row[2]) + "\n")

def deleteData():
    print("Which name do you want to delete?\n")
    personName = input()
    cur.execute('DELETE FROM phone_book WHERE "PersonName" = %s;', (personName,))

def deleteAllData():
    cur.execute('DELETE FROM phone_book;')

def query_all_records():
    cur.execute("SELECT * FROM phone_book1")
    rows = cur.fetchall()
    return rows

def create_insert_or_update_user_function(person_name, last_name, phone_number):
    sql_query = """
    CREATE OR REPLACE FUNCTION insert_or_update_user(
        person_name VARCHAR,
        last_name VARCHAR,
        phone_number VARCHAR
    ) RETURNS VOID AS $$
    BEGIN
        IF EXISTS (SELECT 1 FROM phone_book1 WHERE PersonName = person_name AND LastName = last_name) THEN
            UPDATE phone_book1 
            SET PhoneNumber = phone_number
            WHERE PersonName = person_name AND LastName = last_name;
        ELSE
            INSERT INTO phone_book1 (PersonName, LastName, PhoneNumber)
            VALUES (person_name, last_name, phone_number);
        END IF;
    END;
    $$ LANGUAGE plpgsql;
    """
    cur.execute(sql_query)
    conn.commit()
    conn.close()

def insert_many_users(user_list):
    sql_query = """
    CREATE OR REPLACE FUNCTION insert_many_users(
    user_list VARCHAR[][],
    OUT incorrect_data VARCHAR[][]
) RETURNS SETOF VARCHAR[][] AS $$
DECLARE
    user_record RECORD;
BEGIN
    FOR user_record IN SELECT UNNEST(user_list) LOOP
        IF LENGTH(user_record[2]) != 10 OR NOT user_record[2] ~ '^[0-9]+$' THEN
            incorrect_data := ARRAY_APPEND(incorrect_data, user_record);
        ELSE
            INSERT INTO phone_book1 (PersonName, LastName, PhoneNumber)
            VALUES (user_record[1], user_record[2], user_record[3]);
        END IF;
    END LOOP;
    RETURN;
END;
$$ LANGUAGE plpgsql;
    """
    cur.execute(sql_query)
    conn.commit()
    conn.close()

def query_users(limit, offset):
    cur.execute("SELECT * FROM phone_book1 LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    conn.close()
    return rows

# Procedure to delete data from the users table by username or phone
def delete_user(identifier):
    cur.execute("DELETE FROM phone_book1 WHERE PersonName = %s OR PhoneNumber = %s", (identifier, identifier))
    conn.commit()
    conn.close()

done = False
while not done:
    print("What do you want to do?\n\
          1. Input data from console\n\
          2. Upload from csv file\n\
          3. Update existing contact\n\
          4. Query data from the table\n\
          5. Delete data from table by person name\n\
          6. Delete all data from table\n\
          7. Query records by pattern\n\
          8. Create insert or update user function\n\
          9. Insert many users\n\
          10. Query users\n\
          11. delete user\n\
          12. Exit")
    print("Enter number 1-7")
    x = int(input())
    if x == 1:
        inputData()
    elif x == 2:
        importFromCSV()
    elif x == 3:
        print("Which number do you want to update? Enter name and new number: ")
        name = input()
        newNumber = input()
        update_contact(name, newNumber)
    elif x == 4:
        queryData()
    elif x == 5:
        deleteData()
    elif x == 6:
        deleteAllData()
    elif x == 7:
        records = query_all_records()
        for record in records:
            print(record)
    elif x == 8:
        person_name = input("Enter person's name: ")
        last_name = input("Enter person's last name: ")
        phone_number = input("Enter person's phone number: ")
        create_insert_or_update_user_function(person_name, last_name, phone_number)
    elif x == 9:    
        user_input = input("Enter user data (name, last name, phone number), separated by commas: ")
        user_list = [tuple(user.strip() for user in user_input.split(','))]
        incorrect_data = insert_many_users(user_list, conn, cur)
        print("Incorrect data:", incorrect_data)
    elif x == 10:
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        rows = query_users(limit, offset)
        print("Query result:", rows)
    elif x == 11:
        identifier = input("Enter name or phone number to delete: ")
        delete_user(identifier, conn, cur)
    elif x == 12:
        done = True
    conn.commit()

cur.close()
conn.close()