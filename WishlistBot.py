#Import our libraries and config file.
import discord
from config import *
from oauth2client.service_account import ServiceAccountCredentials
import gspread

#token variables imported from config.py
#create the client for discord
Client = discord.Client()

#Setting up client credentials here.
SERVICE_ACCOUNT_FILE = ServiceAccountCredentials.from_json_keyfile_name("credentials.json")
GAuth = gspread.authorize(SERVICE_ACCOUNT_FILE)
Sheets_Client = GAuth.open(Spreadsheet_name)
Worksheet = Sheets_Client.worksheet(Worksheet_name)

#Print ready to console.
@Client.event
async def on_ready():
    print ("Ready!")

#Check if Reaction is added, check if it's sparkle heart, if so, send to the content of the message to Gsheet.
@Client.event
#If emoji is moneywings, find the message ID of the message and then delete the corresponding row from Gsheet.
async def on_raw_reaction_add(payload):
    if payload.emoji.name == "💸":
        Mess_ID = payload.message_id
        Str_Mess_ID = (str(Mess_ID))
        All_Messages = Worksheet.findall(Str_Mess_ID)

        #Next block iterates through all messages, finds the cell value and row, then if the value matches the discord message ID, deletes the row.
        #If it doesn't match, then the block passes.
        for i in All_Messages:
            Del_val, Del_row, = i.value, i.row
            if Del_val == Str_Mess_ID:
                Worksheet.delete_rows(Del_row)
            else:
                pass

# If the emoji added is sparkle heart, gets the channel id and message id of the message, fetches the body of the message (using channel ID and Message ID), user who reacted,
# and then adds them to google sheets by appending a row.
# If any other emojis are added, print a warning to console that it's the wrong emoji. Will likely change this later.
    elif payload.emoji.name == "💖":
        TextChannel = Client.get_channel(payload.channel_id)
        Mess_ID = payload.message_id
        Full_Mess = await TextChannel.fetch_message(Mess_ID)
        User_Reaction = payload.member.name
        Body = [Full_Mess.content, User_Reaction, str(Mess_ID)]
        Worksheet.append_row(Body, value_input_option="USER_ENTERED")
    else:
        pass

Client.run(discord_token)

