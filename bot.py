import os
import discord

# Put the target user's numeric ID here (example: 123456789012345678)
TARGET_USER_ID = int(os.environ["TARGET_USER_ID"])

# Your custom message (the bot will ping the user, then add this text)
REPLY_TEXT = os.environ.get("REPLY_TEXT", "I saw your message.")

intents = discord.Intents.default()
intents.message_content = True  # you enabled this in the Developer Portal

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (id: {client.user.id})")

@client.event
async def on_message(message: discord.Message):
    # Ignore messages from bots (including itself)
    if message.author.bot:
        return

    # Only react to the one specific user
    if message.author.id != TARGET_USER_ID:
        return

    # Send a normal message mention so it actually pings
    # Mentions inside embeds do NOT notify; keep it as plain text.
    await message.channel.send(
        content=f"<@{TARGET_USER_ID}> {REPLY_TEXT}",
        allowed_mentions=discord.AllowedMentions(users=True)
    )

client.run(os.environ["DISCORD_BOT_TOKEN"])
