import psycopg2,datetime
import asyncio
import telegram

bot = telegram.Bot(token='6959113117:AAFPVCjeu_ZN4hwwIDHW09NpqNyEVCSnMG4')
channel_id = '-1002109629328'


# For Opening IPO
async def OpeningIpo(name,totalunit):
    message = f"New IPO of {name} is opening from Today with total unit {totalunit}. Please Don't miss the chance to apply"
    # Send a text message
    await bot.send_message(chat_id=channel_id, text=message)

# Run the coroutine asynchronously
# asyncio.run(send_message())


# For Closing IPO
async def ClosingIpo(name,totalunit):
    message = f"Today is the Last Day to apply the IPO of {name} with total unit {totalunit}. Please Don't miss the chance to apply"
    # Send a text message
    await bot.send_message(chat_id=channel_id, text=message)


# Connecting to the Database
connectionString = "postgresql://postgres:rnR0uiDqNVWiBL1C@db.xirdbhvrdyarslorlufu.supabase.co:5432/postgres"
try:
    connection = psycopg2.connect(connectionString)
    cursor = connection.cursor()
    print("Connected to PostgreSQL database successfully!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)


# for reading the data according to the opening date of the IPO
# Reading the Data from the Database
date = datetime.datetime.now().date()
# date = '2019-12-12'
# print(date)
# query=f"select * from ipodetails where openingdate='{date}';"
query=f"select * from ipodetails;"
print(query)
cursor.execute(query)
result = cursor.fetchall()
print(result)
if result:
    for row in result:
        asyncio.run(OpeningIpo(row[0],row[1]))
connection.commit()




# for Reading the data according to the closing date fo the ipo 
# Reading the Data from the Database
date = datetime.datetime.now().date()
print(date)
# query=f"select * from ipodetails where closingdate='{date}';"
query=f"select * from ipodetails;"
print(query)
cursor.execute(query)
result = cursor.fetchall()
print(result)
if result:
    for row in result:
        asyncio.run(ClosingIpo(row[0],row[1]))
connection.commit()