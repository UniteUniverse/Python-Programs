from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
import requests
# Enable logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define states for the conversation
MOBILE, ACCOUNT_STATUS, OTP, SONG_PROMPT = range(4)

# Start function - entry point for the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Please enter your mobile number to begin.",
        reply_markup=ReplyKeyboardMarkup([['Cancel']], one_time_keyboard=True)
    )
    return MOBILE  # Move to the MOBILE state

# Handler for receiving mobile number 
async def mobile_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mobile = update.message.text
    
    await update.message.reply_text(f"Received mobile number: {mobile}.")
    
    return ConversationHandler.END  # End the conversation for now

# Cancel function
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Operation canceled.")
    return ConversationHandler.END

# Updated mobile_number function to ask about account status
async def mobile_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mobile = update.message.text
    context.user_data['mobile'] = mobile  # Store mobile number for later use
    await update.message.reply_text(
        "Do you already have an account on Suno? Reply with 'yes' or 'no'."
    )
    return ACCOUNT_STATUS  # Move to the ACCOUNT_STATUS state

# New function to handle account status (sign-in/sign-up choice)
async def account_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = update.message.text.strip().lower()
    if response == 'yes':
        await update.message.reply_text("Great! I’ll direct you to sign in. Please wait...")
        
    elif response == 'no':
        await update.message.reply_text("No problem! I'll help you sign up. Please wait...")
        
    else:
        await update.message.reply_text("Please reply with 'yes' or 'no'.")
        return ACCOUNT_STATUS  # Keep the user in this state if response is invalid

    # Proceed to the next step based on the response
    return ConversationHandler.END  


# Initialize Selenium WebDriver
def initialize_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)  
    driver.get("https://suno.com")
    return driver


# Updated function to handle account status and initiate sign-in or sign-up
async def account_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = update.message.text.strip().lower()
    driver = initialize_driver()  # Start Selenium

    if response == 'yes':
        # Sign-In Process
        await update.message.reply_text("Signing you in. Please wait...")
        driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div/div/div[2]/div[1]/a").click()
        time.sleep(2)
        
        driver.find_element(By.ID, "identifier-field").send_keys(context.user_data['mobile'])
        driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div/div/div[1]/div[2]/form/button[2]/span").click()  # Click sign-in (replace IDs with actual ones)
        
    elif response == 'no':
        # Sign-Up Process
        await update.message.reply_text("Sorry this bot is for signned in users only")
        quit()
        
    else:
        await update.message.reply_text("Please reply with 'yes' or 'no'.")
        return ACCOUNT_STATUS  # Keep the user in this state if response is invalid

    # Store the driver in context to use in the next function
    context.user_data['driver'] = driver
    await update.message.reply_text("Please enter the OTP sent to your mobile number.")
    return OTP  # Move to OTP state

# New function to handle OTP entry
async def otp_entry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    otp = update.message.text
    driver = context.user_data['driver']
    driver.find_element(By.ID, "digit-0-field").send_keys(otp)
    time.sleep(2)
    await update.message.reply_text("You have been successfully signed in! Now, please enter the prompt for the song you want to generate.")
    return SONG_PROMPT  
async def song_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    driver = context.user_data['driver']
    driver = context.user_data['driver']
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/a[2]/div").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "body > div.\@container.bg-vinylBlack-darker.w-full.h-full.flex.flex-col > div.css-lb6gzl > div.css-lfs4ov > div.relative.flex.flex-1.overflow-y-hidden.overflow-x-hidden.w-full.mt-0.md\:mt-0 > div > div.w-split-pane.flex.lg\:min-w-\[570px\].flex-1.bg-vinylBlack-darker.w-full.max-w-full > div.css-6kj3y > div > div.chakra-stack.w-split-pane.css-14jdhr2 > div > div.chakra-stack.css-hxif05 > div.chakra-stack.css-1u4m72d > div > div > textarea").send_keys(prompt)
    driver.find_element(By.CSS_SELECTOR, "body > div.\@container.bg-vinylBlack-darker.w-full.h-full.flex.flex-col > div.css-lb6gzl > div.css-lfs4ov > div.relative.flex.flex-1.overflow-y-hidden.overflow-x-hidden.w-full.mt-0.md\:mt-0 > div > div.w-split-pane.flex.lg\:min-w-\[570px\].flex-1.bg-vinylBlack-darker.w-full.max-w-full > div.css-6kj3y > div > div.chakra-stack.w-split-pane.css-14jdhr2 > div > div.chakra-stack.css-hxif05 > div.chakra-stack.create-button.css-1u3er56 > button").click()
    await update.message.reply_text("Your song is being generated. Please wait...")
    time.sleep(5)
    await update.message.reply_text("Your song has been generated. Please visit your dashboard.")
    return ConversationHandler.END
# Define ConversationHandler with states
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        MOBILE: [MessageHandler(filters.TEXT & ~filters.COMMAND, mobile_number)],
        ACCOUNT_STATUS: [MessageHandler(filters.TEXT & ~filters.COMMAND, account_status)],
        OTP: [MessageHandler(filters.TEXT & ~filters.COMMAND, otp_entry)],
        SONG_PROMPT: [MessageHandler(filters.TEXT & ~filters.COMMAND, song_prompt)],
        },
    fallbacks=[CommandHandler('cancel', cancel)]
)


# Main function to start the bot
def main():
    application = Application.builder().token("7627967297:AAG7BsiLqYz7ZCP8VF7J8Y9kTA2AixHDrUE").build()

    # Add the conversation handler to the application
    application.add_handler(conv_handler)

    # Run the bot until you press Ctrl-C
    application.run_polling()

if __name__ == '__main__':
    main()
