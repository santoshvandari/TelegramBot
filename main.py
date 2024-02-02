import psycopg2,datetime,asyncio,telegram

bot = telegram.Bot(token='6959113117:AAFPVCjeu_ZN4hwwIDHW09NpqNyEVCSnMG4')
channel_id = '-1002109629328'

# Connecting to the Database
connectionString = "postgres://postgres.xirdbhvrdyarslorlufu:9XEq4EPhvJzDXfA7@aws-0-ap-south-1.pooler.supabase.com:5432/postgres"
# pwd = 9XEq4EPhvJzDXfA7
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
    message = f"Today is the Last Day to apply IPO of {companyname}. Please Don't miss the chance to apply.\n\nIPO Information:\nCompany Name: {companyname}\nSymbol: {symbol}\nTotal Unit: {totalunit}\nIssue Type: {issuetype}\nIssue Manager: {issuemanager}\nOpening Date: {openingdate}\nClosing Date: {closingdate}"
    # Send a text message
    await send_message(message)

# Reading the Data from the Database for opening date
date = datetime.datetime.now().date()
# query = f"select * from ipoinfodetails where openingdate='{date}';"
query = f"select * from ipoinfodetails;"
cursor.execute(query)
result = cursor.fetchall()
loop = asyncio.get_event_loop()
if result:
    print("For Opening IPO")
    for row in result:
        loop.run_until_complete(OpeningIpo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print("opening Message Sent")

# # Reading the Data from the Database for closing date
query = f"select * from ipoinfodetails where closingdate='{date}';"
query = f"select * from ipoinfodetails;"
cursor.execute(query)
result = cursor.fetchall()
if result:
    print("For Closing IPO")
    for row in result:
        loop.run_until_complete(ClosingIpo(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        print("Closing Message Sent")

connection.commit()
