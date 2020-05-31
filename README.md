# Discord Swear Counter

Discord Swear Counter is a Python bot used for logging user profanity. 

Before starting, make sure you have a developer portal with bot enabled on server.

If not, this code is based off this [tutorial](https://realpython.com/how-to-make-a-discord-bot-python/) where it goes through the setup. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [discord.py](https://discordpy.readthedocs.io/en/latest/index.html) and [dotenv](https://github.com/theskumar/python-dotenv).

```bash
pip install -U discord.py
pip install -U python-dotenv
```

In the .env file, import your Discord Bot Token and Guild name.

## Usage

All you need to do from here is start it and it will connect to your discord server and run. 
```bash
python SwearBot.py
```
### Bot Activities:
Inside discord you can type specific commands in chat to check for user data as well as have the bot passively gather data on the profanity usage inside the server.
>##### **Commands List:**
>
> - !help - Provides a list of commands that can be used
> - !Total - Displays total swear count of all users
> - !D user#1234- Gives detailed account of words used by specified user (include identification number)
> - !Me - Shows detailed account of words used from caller
> - !m - Bot sends back the word "mung" in chat 

>##### **Passive logging from discord bot:**
>
> - on_message - Views message and updates swear word account from user
> - on_error - Records errors inside *err.log*

### Code:

**To edit word list:**
>Change list of words in the swearList to match your server. Adding or removing words does not require method changes. 

This program stores data with the data.txt file as a hash-table object by default. 

**To use alternative storage:**
>Update the loadData, storeData and swearCount methods in order to change from local storage to a database or another kind of file.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
None, do whatever you want
