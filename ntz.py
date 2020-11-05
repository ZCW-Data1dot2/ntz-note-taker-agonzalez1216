#!/usr/bin/env python3
import os
import sqlite3
from sys import argv

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
  c.execute(sql, (note_name,))

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
  c.execute(select_sql, (note_name,))
  result = c.fetchone()
  print(result[1])
  note_data = str(result[1] + " " + note_data)
  print(note_data)
  update_sql = "UPDATE NTZ_NOTES SET NOTE_CONTENT =? WHERE NOTE_NAME =?"
  c.execute(update_sql, (note_data, note_name))
  conn.commit()
def cli():
#command = input('Input command, r, c, f, e or x for clear:\n')
  if argv[1] == 'r':
    new_note_data = ((argv[2], argv[3]))
    remember(new_note_data)
  elif argv[1] == 'e':
    edit(argv[2], argv[3])
  elif argv[1] == 'f':
    forget(argv[2])
  elif argv[1] == 'clear':
    clear()
  elif argv[1] == 'ntz':
    retrieve_all()
def get_args():
   return argv
  
# run the main function
cli()

