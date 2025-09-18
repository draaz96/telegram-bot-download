from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from environment variables
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
bot_token = os.getenv('BOT_TOKEN')

# Initialize the client
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply('Hello! I am your video download bot. Send me a video file to get started.')

@bot.on(events.NewMessage(func=lambda e: e.message.media))
async def handle_media(event):
    try:
        # Reply to let user know download is starting
        await event.reply("Processing your video file...")
        
        # Download the file
        downloaded_file = await event.message.download_media(file="downloads/")
        
        if downloaded_file:
            await event.reply(f"File downloaded successfully!\nPath: {downloaded_file}")
        else:
            await event.reply("Sorry, there was an error downloading the file.")
            
    except Exception as e:
        await event.reply(f"An error occurred: {str(e)}")

def main():
    print("Bot is running...")
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()