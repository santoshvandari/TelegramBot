import psycopg2
import datetime
import asyncio
import telegram

bot = telegram.Bot(token='6959113117:AAFPVCjeu_ZN4hwwIDHW09NpqNyEVCSnMG4')
channel_id = '-1002109629328'

# Connecting to the Database
connectionString = "postgresql://postgres:rnR0uiDqNVWiBL1C@db.xirdbhvrdyarslorlufu.supabase.co:5432/postgres"
try:
    connection = psycopg2.connect(connectionString)
    cursor = connection.cursor()
    print("Connected to PostgreSQL database successfully!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)

# Function to send messages
async def send_message(message):
    await bot.send_message(chat_id=channel_id, text=message)

# For Opening IPO
async def OpeningIpo(companyname,symbol, totalunit,issuetype,issuemanager,openingdate,closingdate):
    message = f"New IPO of {companyname} is opening for {issuetype} from Today with total unit {totalunit}. Please Don't miss the chance to apply.\n\nIPO Information:\nCompany Name: {companyname}\nSymbol: {symbol}\nTotal Unit: {totalunit}\nIssue Type: {issuetype}\nIssue Manager: {issuemanager}\nOpening Date: {openingdate}\nClosing Date: {closingdate}"
    # Send a text message
    await send_message(message)

# For Closing IPO
async def ClosingIpo(companyname,symbol, totalunit,issuetype,issuemanager,openingdate,closingdate):
    message = f"Today is the Last Day to apply IPO of {companyname}.Please Don't miss the chance to apply.\n\nIPO Information:\nCompany Name: {companyname}\nSymbol: {symbol}\nTotal Unit: {totalunit}\nIssue Type: {issuetype}\nIssue Manager: {issuemanager}\nOpening Date: {openingdate}\nClosing Date: {closingdate}"
    # Send a text message
    await send_message(message)

# Reading the Data from the Database for opening date
date = datetime.datetime.now().date()
query = f"select * from ipoinfodetails;"
print(query)
cursor.execute(query)
result = cursor.fetchall()
# print(result)

loop = asyncio.get_event_loop()

if result:
    print("For Opening IPO")
    for row in result:
        # print(f'{row[0]}\t {row[1]}\t {row[2]}\t {row[3]}\t {row[4]}\t {row[5]}\t {row[6]}\n')
        # print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        loop.run_until_complete(OpeningIpo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print("opening Message Sent")
        break


# # Reading the Data from the Database for closing date
# date = datetime.datetime.now().date()
# print(date)
# query = f"select * from ipoinfodetails;"

# cursor.execute(query)
# result = cursor.fetchall()
# # print(result)

if result:
    print("For Opening IPO")
    for row in result:
        # print(f'{row[0]}\t {row[1]}\t {row[2]}\t {row[3]}\t {row[4]}\t {row[5]}\t {row[6]}\n')
        # print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        loop.run_until_complete(ClosingIpo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print("Closing Message Sent")
        break

# connection.commit()
