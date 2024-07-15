import alpaca_trade_api as tradeapi
import mailtrap as mt
from datetime import datetime, timedelta, time
from twilio.rest import Client
import logging
import traceback
import os
import schedule
from time import sleep

# Configuration

ALPACA_API_KEY = "KEY"
ALPACA_API_SECRET = "Secret Key"
MAILTRAP_TOKEN = "KEY"
RECIPIENT_EMAIL = "email"
RECIPIENT_PHONE_NUMBER = "####"
TWILIO_ACCOUNT_SID = "Account #"
TWILIO_AUTH_TOKEN = "KEY"
TWILIO_PHONE_NUMBER = "###"

STOCK_SYMBOL = "TQQQ"
# ALPACA_API_KEY = os.getenv('ALPACA_API_KEY')
# ALPACA_API_SECRET = os.getenv('ALPACA_API_SECRET')
ALPACA_BASE_URL = 'https://paper-api.alpaca.markets'
# TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
# TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
# TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
# RECIPIENT_PHONE_NUMBER = os.getenv('RECIPIENT_PHONE_NUMBER')
BASE_INVESTMENT = 250
# MAILTRAP_TOKEN = os.getenv('MAILTRAP_TOKEN')
# RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')





# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Alpaca API
api = tradeapi.REST(ALPACA_API_KEY, ALPACA_API_SECRET, ALPACA_BASE_URL, api_version='v2')

# Function to get the 7-day moving average
def get_7_day_moving_average(symbol):
    end_date = datetime.now()-timedelta(days=3)
    start_date = end_date - timedelta(days=7)
    try:
        barset = api.get_bars(symbol, '1D', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
        prices = [bar.c for bar in barset]
        moving_average = sum(prices) / len(prices)
        return moving_average, prices[-1]  # Return moving average and the current price
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        send_email("API Error", f"An error occurred while fetching data for {symbol}: {str(e)}\n{traceback.format_exc()}", RECIPIENT_EMAIL)
        return None, None

# Function to send text messages
def send_text_message(to_number, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=to_number,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )
    logging.info(f"SMS sent: {message.sid}")

# Function to send emails
def send_email(subject, message, to_email):
    
    client = mt.MailtrapClient(MAILTRAP_TOKEN)
    try:
        msg = mt.Mail(
            sender=mt.Address(email="mailtrap@demomailtrap.com", name="Richard Cook"),
            to=[mt.Address(email=to_email)],
            subject=subject,
            text=message,
            category="Integration Test",
        )
        client.send(msg)
        logging.info("Email sent successfully")
    except Exception as e:
        logging.error("Failed to send email", exc_info=True)

def calculate_investment(current_price, moving_average, base_investment):
    def investment_amount_for_price(price):
        percentage_difference = ((price - moving_average) / moving_average) * 100
        # Adjust the multiplier based on the percentage difference
        if percentage_difference >= 0:
            # Decrease multiplier as the percentage difference increases, capped at 0.50
            multiplier = max(1.00 - (percentage_difference * 0.025), 0.50)
        else:
            # Increase multiplier as the percentage difference decreases, capped at 2.00
            multiplier = min(1.00 - (percentage_difference * 0.025), 2.00)
        return base_investment * multiplier

    # Calculate investment amounts for current, 1% higher, and 1% lower prices
    investment_amounts = {
        "current_price": investment_amount_for_price(current_price),
        "1_percent_higher": investment_amount_for_price(current_price * 1.01),
        "1_percent_lower": investment_amount_for_price(current_price * 0.99),
    }

    return investment_amounts



# Main logic
if __name__ == "__main__":


    def job():

        moving_average, current_price = get_7_day_moving_average(STOCK_SYMBOL)
        if moving_average is None or current_price is None:
            logging.info("Could not retrieve stock data.")
        else:
            # Get investment amounts for current, 1% higher, and 1% lower prices
            investment_amounts = calculate_investment(current_price, moving_average, BASE_INVESTMENT)
            
            # Round the investment amounts to the nearest dollar
            investment_amount_current_price = round(investment_amounts["current_price"])
            investment_amount_1_percent_higher = round(investment_amounts["1_percent_higher"])
            investment_amount_1_percent_lower = round(investment_amounts["1_percent_lower"])

            # Calculate the price differences in dollars
            difference_higher_in_dollars = (current_price * 1.01) - current_price
            difference_lower_in_dollars = (current_price * 0.99) - current_price

            # Calculate the investment amount differences and format them
            investment_difference_higher = investment_amount_1_percent_higher - investment_amount_current_price
            investment_difference_lower = investment_amount_1_percent_lower - investment_amount_current_price
            formatted_investment_difference_higher = f"+${investment_difference_higher}" if investment_difference_higher >= 0 else f"-${abs(investment_difference_higher)}"
            formatted_investment_difference_lower = f"+${investment_difference_lower}" if investment_difference_lower >= 0 else f"-${abs(investment_difference_lower)}"

            # Create a message with the corrected format, including rounded investment amounts and price differences
            message = (
                f"Today's Investment Analysis for {STOCK_SYMBOL}:\n\n"
                f"Current Price: ${current_price:.2f}\n"
                f"Investment at current price: ${investment_amount_current_price}\n\n"
                f"Investment if 1% higher (${current_price * 1.01:.2f}, {formatted_investment_difference_higher}): ${investment_amount_1_percent_higher}\n\n"
                f"Investment if 1% lower (${current_price * 0.99:.2f}, {formatted_investment_difference_lower}): ${investment_amount_1_percent_lower}\n"
            )
            
            # Send an email with the investment analysis
            send_email("Investment Analysis", message, RECIPIENT_EMAIL)
            
            # Optionally, send a text message with a brief note about the investment analysis
            # send_text_message(RECIPIENT_PHONE_NUMBER, "Investment analysis details sent to your email.")
        
        
    # Schedule the job to run every weekday at 08:47 AM
    schedule.every().monday.at("08:47").do(job)
    schedule.every().tuesday.at("08:47").do(job)
    schedule.every().wednesday.at("08:47").do(job)
    schedule.every().thursday.at("08:47").do(job)
    schedule.every().friday.at("08:47").do(job)
    job()

    # Run the scheduler continuously
    while True:
        schedule.run_pending()
        
