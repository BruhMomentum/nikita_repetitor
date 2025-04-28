from database import get_db_connection

connection = get_db_connection()
cursor = connection.cursor()
# script1 = """CREATE TABLE author
# (
#   author_id INTEGER PRIMARY KEY,
#   name_author text
# );"""

# script2 = """INSERT INTO author(author_id, name_author)
# VALUES (1, 'Булгаков М.А.'),
#        (2, 'Достоевский Ф.М.'),
#        (3, 'Есенин С.А.'),
#        (4, 'Пастернак Б.Л.'),
#        (5, 'Лермонтов М.Ю.');
# """ #create

# script3 = """
# SELECT * FROM author WHERE name_author LIKE '%ов%';
# """ #read

# script4 = """
# INSERT INTO author(author_id, name_author)
# VALUES (6, 'Пушкин И.И.')
# """

# new_author = 'Толстой Л.Н.'
# script5 =  f"UPDATE author SET name_author = '{new_author}' WHERE author_id = 6"

script6 = """
DELETE FROM author WHERE author_id = 6 
"""

cursor.execute(script6)
connection.commit()
#print(cursor.fetchall()[-1])
# print(cursor.fetchmany(2))
# print(cursor.fetchone())
# print(cursor.fetchone())