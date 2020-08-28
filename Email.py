import email
import email.header
import imaplib
from collections import deque



class EmailQueue:
    'Collection of tools for accessing emails.'
    __user = 'USER_EMAIL'
    __password = 'USER_PASSWORD'
    email_queue = deque() # deque chosen as stack implementation for O(1) runtime on pop
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    search_type = 'REVERSE DATE'

    # logs in
    def login(self):
        print(self.__user)
        print(self.__password)
        self.mail.login(self.__user, self.__password)
        self.mail.select('inbox')

    # sets private variable user
    def set_user(self, user):
        self.__user = user

    # sets private variable password
    def set_password(self, password):
        self.__password = password

    def get_emails(self, count):
            typ, data = self.search(None, self.search_type)
            for i in data[0].split():
                typ, data = self.mail.fetch(i, '(BODY[HEADER])')
                message = email.message_from_string(data[0][1])
                decode = email.header.decode_header(message['Subject'])[0]
                subject = unicode(decode[0])
                print(subject)




    # populates the queue with the n most recent emails
    def initialize_queue(self, email_queue, email_count, imap):
        pass
        # gets last n emails and fills queue.
        # self.email_queue.append()

    def update_queue(self, email_queue, imap):
        pass
        # gets most recent
        # if not same as email_queue[-1]:
        #   append
        #   email_queue.pop()

    def __get_subject(self, message):
         return message.get('subject')