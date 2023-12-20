import psycopg2,datetime
import asyncio
import telegram

bot = telegram.Bot(token='6959113117:AAFPVCjeu_ZN4hwwIDHW09NpqNyEVCSnMG4')
channel_id = '-1002109629328'


# Getting the data from the database
async def SendMessage(message):
    try:
        await bot.send_message(chat_id=channel_id, text=message)
    except Exception as e:
        print(f"Error sending message: {e}")


# Connecting to the Database
connectionString = "postgresql://postgres:rnR0uiDqNVWiBL1C@db.xirdbhvrdyarslorlufu.supabase.co:5432/postgres"
try:
    connection = psycopg2.connect(connectionString)
    cursor = connection.cursor()
    print("Connected to PostgreSQL database successfully!")
    SendMessage("Connected to PostgreSQL database successfully!")
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit(1)



for i in range(1, 5):
    try:
        print("Sending message...")
        asyncio.run(SendMessage(f'Hello World! {i}'))
    except Exception as e:
        print(f"Error sending message: {e}")

for i in range(1,5):
    try:
        print("Sending message...")
        asyncio.run(SendMessage(f'Hello Universe! {i}'))
    except Exception as e:
        print(f"Error sending message: {e}")
