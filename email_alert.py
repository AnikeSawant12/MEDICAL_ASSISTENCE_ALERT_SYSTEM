
import smtplib

def send_email(image_name, predicted_class):
    gmail_user = 'hatedkiller108@gmail.com'
    gmail_password = 'lwrm qzha xslz eqvf'

    sent_from = gmail_user
    to = ['aniket121199@gmail.com']
    subject = 'Medical Alert Message'
    
    # Determine the email body based on the predicted class
    if predicted_class in ['Angry', 'Disgust', 'Fear', 'Sad']:
        body = 'Dear Users,This is an automated alert from the Medical Assistance System.We have detected unusual activity or a potential emergency situation based on the image collected from your devices. Please take the required actions immediately Please remember that your safety and well-being are our top priorities. If you have any questions or need further assistance contact[9883546627,medicalalert@gmail.com]. Stay safe and take care. Sincerely, Medical Assistance Team'
    elif predicted_class in ['Happy', 'Neutral', 'Surprise']:
        body = 'The person seems to be happy. They may not need medical assistance.'
    else:
        # If the predicted class does not match any predefined categories
        body = 'The person\'s emotional state is uncertain. Further assessment may be needed.'
    
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong: ", ex)








