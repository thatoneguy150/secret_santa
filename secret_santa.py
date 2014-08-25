import smtplib
import random

def send_message(recv, recip):
    sender = "thatoneguy150@gmail.com"
    receiver = [recv]
    message = "Ho ho ho!\nIt's time for this years Secret Santa. Your recipient this year is " + recip + ". Happy gift giving!\n-Santa"

    try:
        session = smtplib.SMTP('smtp.gmail.com',587)
        session.ehlo()
        session.starttls()
        session.ehlo()
        session.login(sender,'Hammerofdawn5')
        session.sendmail(sender,recv,message)
        session.quit()
    except smtplib.SMTPException:
        print('Error sending message to' + recv)

def create_list():
    people = {'Aaron': '3143655388@tmomail.net', 'Josh': '3145997638@mms.att.net', 'Sam': '3146055163@mms.att.net', 'Denis': '3147045371@messaging.sprintpcs.com', 'Nicole': '3149203310@mms.att.net', 'Joel': '3149601696@mms.att.net', 'Mike': '6366923583@mms.att.net'}

    givers = people.keys()
    receivers = people.keys()
    pairs = {}
    
    for g in givers:
        recip = g
        num = -1
        while g == recip:
            num = random.randint(0, len(receivers) - 1)
            recip = receivers[num]
        del receivers[num]
        pairs[g] = recip
        send_message(people[g], pairs[g])

    f = open('secret_santa_list.txt', 'w')
    f.write(str(pairs))

create_list()    
