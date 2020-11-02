# add your code in this file
import os
import sqlite3

conn = sqlite3.connect('notes.db')
c = conn.cursor()

# conn.execute('''CREATE TABLE NTZ_NOTES
#          (NOTE_NAME VARCHAR(50) PRIMARY KEY     NOT NULL,
#          NOTE_CONTENT   LONGTEXT);''')
# print("Table created successfully")
#
# conn.close()
# main function
def remember(new_note_data):
  sql = "INSERT INTO NTZ_NOTES(NOTE_NAME, NOTE_CONTENT) VALUES(?,?)"
  c.execute(sql, new_note_data)
  conn.commit()

def forget(note_name):
  sql = "DELETE FROM NTZ_NOTES WHERE NOTE_NAME =?"
  c.execute(sql, note_name)

def clear():
  sql = "DELETE FROM NTZ_NOTES"
  c.execute(sql)

def retrieve_all():
  sql = "SELECT * FROM NTZ_NOTES"
  c.execute(sql)
  rows = c.fetchall()
  for row in rows:
    print(row)
def edit(note_name, note_data):
  select_sql = "SELECT * FROM NTZ_NOTES WHERE NOTE_NAME =?"
  c.execute(select_sql, note_name)
  result = c.fetchone()
  new_edit = input()
  note_data = result[1] + str(new_edit)
  update_sql = "UPDATE NTZ_NOTES SET NOTE_CONTENT = ? WHERE NOTE_NAME =?"
  c.execute(update_sql,(note_name, note_data))
def cli():
  command = input('Input command, r, c, f, e or x for clear:\n')
  if command == 'r':
    note_name = input('New note name\n')
    note_content = input('add note\n')
    new_note_data = (note_name, note_content)
    remember(new_note_data)

  
# def get_args():
#    return sys.argv
  
# run the main function
cli()
