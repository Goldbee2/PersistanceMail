import email
import imaplib
from collections import deque


class Email:
    __user = 'USER_EMAIL'
    __password = 'USER_PASSWORD'
    email_queue = deque() # deque chosen as stack implementation for O(1) runtime on pop
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(__user, __password)
    mail.select('inbox')

    # sets private variable user
    def set_user(self, user):
        __user = user

    # sets private variable password
    def set_password(self, password):
        __password = password

    # populates the queue with the n most recent emails
    def initialize_queue(self, queue, n, imap):

        # gets last n emails and fills queue.
        # self.email_queue.append()

    def update_queue(self, email_queue, imap):
        # gets most recent
        # if not same as email_queue[-1]:
        #   append
        #   email_queue.pop() Popular repositories



    # def __get_subject(self, message):
    #     return message.get('subject')


