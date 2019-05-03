import smtplib
from os import path
import config

from string import Template

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


MY_ADDRESS = 'stockmarketsubscription@gmail.com'
PASSWORD = 'ajdn2019seniorproject'


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def integrated_test():

    basepath = path.dirname(__file__)
    contact_path = path.abspath(path.join(basepath, "contacts.txt"))

    message_path = path.abspath(path.join(basepath, "report_test.txt"))

    image_path = path.abspath(path.join(basepath, "graph.png"))
    image1 = "graph.png"

    names, emails = get_contacts(contact_path)  # read contacts
    message_template = read_template(message_path)

    report_file = open('E81WN.html')
    html = report_file.read()

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Your Personalized Weekly Stock Research"

        # add in the message body
        msg.attach(MIMEText(html, 'html'))
        # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText('<br><img src="cid:image1"><br>One Year Price Chart', 'html')
        msg.attach(msgText)

        # This example assumes the image is in the current directory
        fp = open(image_path, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        # msg.attach(msgImage)

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    #main()
    integrated_test()