import sqlite3
from random import randint, choice
from faker import Faker
import pandas as pd

conn = sqlite3.connect('social_network.db')

#creating a query to get list of all married couples as asked in the lab 
married_couple = """ 
   SELECT person1.name, person2_name, beginning_date
   FROM relationships
   JOIN people person1 ON person1_id = person1.id
   JOIN people person2 ON person2_id = person2.id
   WHERE Relationship_type = 'spouse' 
"""
c = conn.cursor()
c.execute(married_couple)

# Using pandas package to generate a CSV file

Output = c.fetchall()
Table = pd.DataFrame(Output, columns=['Person1', 'Person2', 'beginning_date'])
Table.to_csv('married_couples.csv', index=False)

conn.close()