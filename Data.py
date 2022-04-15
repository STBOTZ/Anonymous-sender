from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nSend me anything and I'll send it back after removing the forwarded tag. \n\nBy @STBOTZ ♥"

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @STBOTZ

Source Code : [Click Here](https://github.com/STBOTZ/Anonymous-sender)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @STBOTZ
    """

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Remove Caption Button
    remove_button = [InlineKeyboardButton("� Remove Caption �", callback_data="remove")]

    # Add caption button
    add_button = [InlineKeyboardButton("💬 Re-Add Caption 💬", callback_data="add")]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("🎪 About The Bot 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Support Channel ♥", url="https://t.me/STBOTZ")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/ST_BOTZ")],
    ]
