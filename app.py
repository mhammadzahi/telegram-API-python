from telethon.sync import TelegramClient
import asyncio
import re
import random

# Replace these values with your own
api_id = 12345
api_hash = ''
phone_number = '+971509267545'

client = TelegramClient('anon108', api_id, api_hash)

async def main():
    # Getting information about yourself
    #me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    #print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    #username = me.username
    #print(username)
    #print(me.phone)
    
    # Get information about the channel
    entity = await client.get_entity('JOBSS_AE')

    counter = 0
    maximum = 350
    email_list = []
    sleep_randoms = [19, 15, 7, 11, 18, 9, 17, 16, 20, 22, 5, 8]
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # List of messages from the channel
    async for message in client.iter_messages(entity):
        counter = counter + 1
        if counter <= maximum:
            #print(message.text)
            print(message.date)
            email = re.search(email_pattern, message.text)
            if email:
                email_list.append(email.group())

            #print(email_list)
            await asyncio.sleep(random.choice(sleep_randoms))

        else:
            print('done!')
            break


    with open('data_350.txt', 'w') as file_:
        for email_ in email_list:
            file_.write(email_ + '\n')

    # Disconnect
    await client.disconnect()

    # You can print all the dialogs/conversations that you are part of:
    #async for dialog in client.iter_dialogs():
    #    print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    #await client.send_message('me', 'Hello, myself!')
    # ...to some chat ID
    #await client.send_message(-7170321696, 'Hello, group!')
    # ...to your contacts
    #await client.send_message('+212691756830', 'Hello, friend!')
    # ...or even to any username
    #await client.send_message('username', 'Testing Telethon!')

    #You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )

    # # Sending a message returns the sent message object, which you can use
    # print(message.raw_text)

    # # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # # You can print the message history of any chat:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)

    #     # You can download media from messages, too!
    #     # The method will return the path where the file was saved.
    #     if message.photo:
    #         path = await message.download_media()
    #         print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())