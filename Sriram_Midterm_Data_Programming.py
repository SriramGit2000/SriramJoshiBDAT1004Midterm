#!/usr/bin/env python
# coding: utf-8

# In[11]:


#1

import math
 
class Point:
    def __init__(self, y=0, x=0):
        self.y_coordinate = y
        self.x_coordinate = x
 
class Segment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
 
    def calculate_length(self):

        length = math.sqrt((self.point2.y_coordinate - self.point1.y_coordinate) ** 2 + (self.point2.x_coordinate - self.point1.x_coordinate) ** 2)
        print("The length of the segment is: ", length)
 
    def calculate_slope(self):
    
        slope = (self.point2.y_coordinate - self.point1.y_coordinate) / (self.point2.x_coordinate - self.point1.x_coordinate)
        print("The slope of the segment is: ", slope)
 
if __name__ == "__main__":
    print("When initializing a Point object, provide (y-coordinate, x-coordinate)")
    point1 = Point(3, 4)
    point2 = Point(0, 0)
    segment = Segment(point1, point2)
    segment.calculate_length()
    segment.calculate_slope()
    


# In[7]:


#2

import sqlite3

database_connection = sqlite3.connect("test.db")

db_cursor = database_connection.cursor()

db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY,
        record_date DATE,
        temperature INTEGER
    )
''')

data_to_insert = [
    (1, '2015-01-01', 10),
    (2, '2015-01-02', 25),
    (3, '2015-01-03', 20),
    (4, '2015-01-04', 30)
]

insert_query = "INSERT INTO weather_data (id, record_date, temperature) VALUES (?, ?, ?)"
db_cursor.executemany(insert_query, data_to_insert)


database_connection.commit()

select_query = "SELECT * FROM weather_data"
print("Printing the contents of the 'weather_data' table")
db_cursor.execute(select_query)
data_records = db_cursor.fetchall()


for data_record in data_records:
    print(data_record)


select_query = """SELECT t1.id FROM weather_data t1
                    LEFT JOIN weather_data t2 ON t1.record_date = DATE(t2.record_date, '+1 days')
                    WHERE t1.temperature > t2.temperature
                    """
db_cursor.execute(select_query)
result_records = db_cursor.fetchall()

print("Printing the results")

for result_record in result_records:
    print(result_record)


db_cursor.close()
database_connection.close()


# In[10]:


#3
def f(indent, num):
    if num>0:
        f(indent, num//2);
        print(" "*indent + "*"*num);
        f(indent + num//2, num//2)
f(0,0)
print("\n\n\n\n\n\n\n")
f(0,1)
print("\n\n\n\n\n\n\n")
f(0,2)
print("\n\n\n\n\n\n\n")
f(0,4)

        
        


# In[ ]:




