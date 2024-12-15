import sqlite3
import json

# Connecting to DB
conn = sqlite3.connect("contacts.db")
cur = conn.cursor()

# Data example
example = {
  "contacts": [
    {
      "name": "Jason",
      "phone": "999-999-9999",
      "address": "123 Wilcocks Dr"
    }
  ]
}

# Create a table in the database with the columns name, phone, and address
# make sure to run only once and then comment out the following code
# cur.execute("""
# CREATE TABLE contacts (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone TEXT,
#     address TEXT
# )
# """)

def create(data):
  for contact in data["contacts"]:
    try:
      cur.execute(f'''
                INSERT INTO contacts (name, phone, address)
                VALUES ("{contact["name"]}", "{contact["phone"]}", "{contact["address"]}")
            ''')
    except sqlite3.OperationalError as err:
      print(err)
      return
    
    conn.commit()
    print("New Recored Added!")
    return

def read(name=None):
  if not name:
    name = ""
    
  cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"')
  rows = cur.fetchall()
  records = {"results": []}
  
  for row in rows:
    record = {"name": row[1], "mobile": row[2], "home": row[3]}
    records["results"].append(record)
    
    pretty_records = json.dumps(records, indent=2)
    print(pretty_records)
    return

# Helper function
def _update_number(row):
  phone = input("Enter a new phone number (skip to leave unchanged): ")
  address = input("Enter a new address (skip to leave unchanged): ")
  
  phone = phone if phone != "" else row[2]
  address = address if address != "" else row[3]
  
  cur.execute(f'UPDATE contacts SET phone="{phone}", address="{address}" '
              f'WHERE name="{row[1]}"')
  
  conn.commit
  return
  
def update(name):
  cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"')
  rows = cur.fetchall()
  
  if len(rows) == 1:
    row = rows[0]
    _update_number(row)
  else:
    print("Multiple results were found. Select which one: ")
    for row in rows:
      print(row)
      
    _id = input("Enter number here: ")
    cur.execute(f'SELECT * FROM contacts WHERE id={_id}')
    row = cur.fetchall()[0]
    _update_number(rows)
    
  print("Number Update is Successful!")  
  
# Helper function for the delete
def _delete_number(row):
  cur.execute(f'DELETE FROM contacts WHERE id={row[0]}')
  conn.commit()
  return
  
# Delete method = Update method in terms of functionalities 
def delete(name):
  cur.execute(f'SELECT * FROM contacts WHERE "name" LIKE "%{name}%"')
  rows = cur.fetchall()
  
  if len(rows) == 1:
    row = rows[0]
    _delete_number(row)
  else:
    print("Multiple results were found. Select which one: ")
    for row in rows:
      print(row)
      
    _id = input("Enter number here: ")
    cur.execute(f'SELECT * FROM contacts WHERE id={_id}')
    row = cur.fetchall()[0]
    _delete_number(rows)
    
  print("Number Deletion is Successful!")
  

def main():
  while True:
    options = input("Select one of the following options: Create(C) Read(R) Update(U) Delete(D) or Quit(Q)")
    
    if options.lower() == "c":
        new_record = {
          "contacts": [
            {
              "name": input("Enter a name: "),
              "phone": input("Enter a phone number: "),
              "address": input("Enter a home address: ")
            }
          ]
        }
        
        create(new_record)
        
    elif options.lower() == "r":
      name = input("Enter a name: ")
      read(name)
    elif options.lower() == "u":
      name = input("Enter a name: ")
      update(name)
    elif options.lower() == "d":
      name = input("Enter a name: ")
      delete(name)
    elif options.lower() == "q":
      print("Bye Bye!")
      quit()
    else:
      print(f"No options {options} available. Try again.")

      
if __name__ == "__main__":
  main()
      
    