import imaplib
import email
import pyttsx3
engine=pyttsx3.init()
voiceId="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice',voiceId)
engine. setProperty("rate", 135)
server="imap.gmail.com"
username='botpython261@gmail.com'
password='RDTLm2cxWPFsU4X'
mail=imaplib.IMAP4_SSL(server)
mail.login(username,password)
mail.select("inbox")
_, search_data=mail.search(None,"SEEN")
for num in search_data[0].split():
    _,data=mail.fetch(num,'(RFC822)')
    _,b=data[0]
    email_message=email.message_from_bytes(b)
    engine.say(f"You've got a new mail from {email_message['from']}")
    engine.say(f"The subject is : {email_message['subject']}")
    engine.runAndWait()

