import pandas as pd
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname='dvdrental',    
    user='postgres',          
    password='0099',  
    host='localhost',        
    port='5432'              
)
# Read the movie titles in ascending order into a DataFrame using pandas
df = pd.read_sql_query("SELECT title FROM film ORDER BY title ASC", conn)

# Display the DataFrame with movie titles
print(df)

# Close the connection
conn.close()
