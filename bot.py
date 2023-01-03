from telethon import TelegramClient, client, events
from telethon.tl.functions.messages import SendMessageRequest
import re 

token = '5802676518:AAHKrAZltr9uIBpzAGJDKKuhLmSOLHV8dMo'
api_id = 15443592
api_hash = "4765a38d2895fcc169c7ce2452c7ebd9"
client = TelegramClient('session_read',api_id,api_hash)


'''async def gamersOutlet(event,message_text):
    ref = "?tracking=hwo"

    if "https://www.gamers-outlet.net/" in message_text:

        refcompleto = message_text + ref
        
        sus=event.chat.id
        messaggioId=event.message.id
        username = event.sender.username
        first_name = event.sender.first_name
        last_name = event.sender.last_name

        access = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)
        short_url = access.shorten(refcompleto)

        
        
        return short_url['url']
    else:
            return None

'''


#2031158106:AAH3HjnbQST6cH3mLfwf8NveROwACW7Rlmg 


@client.on(events.NewMessage)
async def main(event):
    message = event.text
    reply = await event.get_reply_message()
    print(reply)
    if reply!= None:
        messaggio_reply = reply.message
    message_return = []
    chat_id=event.chat.id
    messaggioId=event.message.id
    username = event.sender.username
    phone = event.sender.phone
    first_name = event.sender.first_name
    last_name = event.sender.last_name
    sender = await event.get_sender()
    print(sender)      
    print(phone)
    print(message)
    print(chat_id)
    if len(message)>0:
        controllo = False
        if username != None:  
            commentoSussyBaka = f"Messaggio inviato da (@{username}) \n\n{message}"
            controllo = True
        elif phone != None:
            commentoSussyBaka = f"Messaggio inviato da (+{phone}) (#{chat_id}) \n\n{message}"
            controllo = True
        else:
            commentoSussyBaka = f"Messaggio inviato da ({first_name}) (#{chat_id}) \n\n{message}"
            controllo = True
        '''else:
            await client.send_message(chat_id,"Per parlare con l'assistenza aggiungere un username al vostro account Telegram o cambiare la privacy del numero di telefono in PUBBLICO") '''
        
        if chat_id != 1881287074 and controllo:
            await client.send_message(1881287074,commentoSussyBaka) 
        elif chat_id == 1881287074 and reply.sender.id==5802676518: 
            cleaned_string_chiocciola = re.compile("@(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
            message_text_c = cleaned_string_chiocciola.findall(messaggio_reply)
            if len(message_text_c)>0:
                messaggio_admin = message.replace(message_text_c[0],'')
                message_text_c[0] = message_text_c[0].replace(')','')
                await client.send_message(message_text_c[0], message)
            else:
                cleaned_string_cancelletto = re.compile("#(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
                message_text_cancelletto = cleaned_string_cancelletto.findall(messaggio_reply)
                if len(message_text_cancelletto)>0:
                    tag = message_text_cancelletto[0][1:]
                    print("cancelletto: "+tag)
                    tag = tag.replace(')','')
                    await client.send_message(int(tag), message)



        #await client.delete_messages(chat_id,messaggioId)
        



client.start()
client.run_until_disconnected() 