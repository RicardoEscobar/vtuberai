"""This module is used to read the twitch chat and send the messages to the vtuber twitch channel."""
import os
import asyncio

from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
from dotenv import load_dotenv


# load the environment variables
load_dotenv()
APP_ID = os.getenv("TWITCH_APP_ID")
APP_SECRET = os.getenv("TWITCH_APP_SECRET")
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = 'RicardoEscobar'

async def twitch_example():
    # initialize the twitch instance, this will by default also create a app authentication for you TWITCH_APP_ID and TWITCH_APP_SECRET
    twitch = await Twitch(APP_ID, APP_SECRET)
    # call the API for the data of your twitch user
    # this returns a async generator that can be used to iterate over all results
    # but we are just interested in the first result
    # using the first helper makes this easy.
    user = await first(twitch.get_users(logins=TARGET_CHANNEL))
    # print the ID of your user or do whatever else you want with it
    print(user.id)

# run this example
asyncio.run(twitch_example())