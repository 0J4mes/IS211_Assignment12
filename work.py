import sqlite3

connection = sqlite3.connect('hw13.db')
cursor = connection.cursor()

# Add initial data
cursor.execute("INSERT INTO students (first_name, last_name) VALUES ('John', 'Smith');")
cursor.execute("INSERT INTO quizzes (subject, num_questions, date_given) VALUES ('Python Basics', 5, '2015-02-05');")
cursor.execute("INSERT INTO results (student_id, quiz_id, score) VALUES (1, 1, 85);")

connection.commit()
connection.close()
