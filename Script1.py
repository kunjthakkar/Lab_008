import sqlite3
from faker import Faker 
from random import randint, choice


conn = sqlite3.connect('social_network.db')
c = conn.cursor()

# A query that adds a row of data in the relationships table 
relationships_tbl = """
  CREATE TABLE IF NOT EXISTS relationships
  (
      id INTEGER PRIMARY KEY,
      person1_id INTERGER NOT NULL,
      person2_id INTEGER NOT NULL,
      type TEXT NOT NULL,
      start_date DATE NOT NULL,
      FOREIGN KEY (person1_id) REFERENCES people (id),
      FOREIGN KEY (person2_id) REFERENCES people (id)
  );
"""
#Executing the Table 
c.execute(relationships_tbl)

#Generating 100 relationshipss with use of faker and inserting them into the relationships
add_releating_query = """
    INSERT INTO relationships
    (
        person1_id,
        person2_id,
        type,
        start_date
    )
    VALUES (?,?,?,?);
"""
fake = Faker()
for i in range(100):
  person1_id = randint(1,100)
  person2_id = randint(1,100)
while person2_id == person1_id:
    person2_id = randint(1,100)
#Now we will select the relationship type randomly 
Relationship_type = choice(['friend', 'spouse', 'relative', 'child'])

beginning_date = fake.date_between(start_date='-50y', end_date='today')

new_connection = (person1_id, person2_id, Relationship_type, beginning_date)

c.execute(add_releating_query,new_connection )   
conn.commit()
conn.close()

