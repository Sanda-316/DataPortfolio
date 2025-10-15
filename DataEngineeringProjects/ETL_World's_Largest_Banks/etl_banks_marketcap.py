#import libraries
import pandas as pd
import numpy as np
import sqlite3
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os

#define Attributes

url = 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name','MC_USD_Billion']
table_name = 'Largest_Banks'
db_name = 'Banks.db'
csv_path = './Largest_banks_data.csv'



#Task 1 Write a function log_progress() to log the progress of the code at different stages in a file code_log.txt. Use the list of log points provided to create log entries as every stage of the code.

def log_progress(message):
    timestamp_format = '%Y-%h-%d %H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("./code_log.txt", "a") as f :
        f.write(timestamp + ' : ' + message + '\n')

#Task 2 Extract the tabular information from the given URL under the heading 'By market capitalization' and save it to a dataframe.

def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'lxml')
    Data_list = []
    tables= data.find_all('tbody')
    rows = tables[0].find_all('tr') # its the first table in the webpage
    for row in rows[1:]: # skip the header row
        col = row.find_all('td')
        if len(col) >= 3: #ensuring there are enough columns
           if col[1].find('a') is not None:
                market_cap = float(col[2].get_text(strip=True).replace(',',''))
                Data_list.append ({"Bank_Name": col[1].get_text(strip=True),
                             "MC_USD_Billion": market_cap})
    df = pd.DataFrame(Data_list)
    return df

#Task 3 Transform the data 

def transform(df):

    # Get the folder where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, "exchange_rate.csv")
    exchange_df = pd.read_csv(csv_path)
    exchange_rate = exchange_df.set_index(exchange_df.columns[0]).to_dict()[exchange_df.columns[1]]

     # Add new columns by multiplying MC_USD_Billion with exchange rates
    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['MC_USD_Billion']]
    return df

#Task 4 , Load to CSV
def load_to_csv(df,path):
    df.to_csv(path, index= False)
    log_progress(f"Data saved to CSV at {path}")

#Task 5 Load to DB

# Function to load DataFrame to database
def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)
    log_progress(f"Data loaded to database '{db_name}' in table '{table_name}'.")

#Task 6 , Run queries

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement,sql_connection)
    print(query_output)
    print("\n") # Print a newline for better readability


#Log progress
#ETL operations and log progress
log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df)
log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('Banks.db')

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Executing queries')

query1 = f"SELECT * from Largest_Banks"
query2 = f"SELECT AVG(MC_GBP_Billion) FROM Largest_Banks"
query3 = f"SELECT Bank_Name from Largest_Banks LIMIT 5"

run_query(query1, sql_connection)
run_query(query2, sql_connection)
run_query(query3, sql_connection)


log_progress('Process Complete.')

sql_connection.close()

log_progress('Server Connection closed. ETL process finished.')

