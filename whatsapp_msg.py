from twilio.rest import Client
import pendulum
from datetime import datetime

account_sid = ''  # Twilio auth sid
auth_token = ''  # Twilio auth token
client = Client(account_sid, auth_token) 

def send_whatsapp_msg(num_likes, num_matches):
    # Get Time
    ist = pendulum.timezone('Asia/Calcutta')
    today = datetime.now(ist)
    today = today.strftime("%a, %B %d %Y, %H:%M")
    try:
        if num_matches > 0:
            msg = 'Wohoo!!! You got '+str(num_matches)+' matche! You swiped '+str(num_likes)+' times at '+today

        else:
            msg = 'Swiped '+str(num_likes)+' Times, at '+today
    except Exception as e:
        print("\n\n\nException in Whatsapp msg formation: ",e, "\n\n")
    
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=msg,
            to='whatsapp: #Your Number'
            )
        print("\nWhatsapp msg ID: ", message.sid, "\n")
    except Exception as e:
        print("\n\n\nException in Whatsapp msg sending: ",e,"\n\n")