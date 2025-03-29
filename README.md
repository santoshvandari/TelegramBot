# IPO Notification Bot

This is a Python script that connects to a PostgreSQL database to fetch IPO details and sends notifications to a Telegram channel when an IPO opens or closes.

## Features
- Connects to a PostgreSQL database to fetch IPO details.
- Sends messages to a Telegram channel when an IPO opens or closes based on the Information stored in DB.
- Runs automatically by using GitHub Actions.


## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/santoshvandari/telegrambot.git
   cd ipo-notification-bot
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a `.env` file in the root directory and add:
   ```sh
   TELEGRAM_BOT_TOKEN=your_bot_token
   CHANNEL_ID=your_channel_id
   DATABASE_URL=your_postgresql_database_url
   ```

## Database Schema
Ensure your PostgreSQL database has the following table:
```sql
CREATE TABLE ipodetails (
    companyname VARCHAR(255),
    symbol VARCHAR(50),
    issuetype VARCHAR(100),
    issuefor VARCHAR(100),
    totalunit INT,
    issuemanager VARCHAR(255),
    openingdate DATE,
    closingdate DATE
);
```

## Usage
Run the script using:
```sh
python main.py
```

## How It Works
- The script fetches the current date and checks if it is a Saturday.
- If not, it queries the database for IPOs opening or closing on the current date.
- If an IPO is found, it sends a message to the specified Telegram channel.

## Contributing
We welcome contributions! If you'd like to contribute to this Script, please send the PR.

## License
This project is licensed under the MIT [License](LICENSE).
