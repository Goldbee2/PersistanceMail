from email.header import decode_header, make_header
from email.parser import HeaderParser
import imaplib
from collections import deque
import getpass
import sys


class EmailQueue:
    'Collection of tools for accessing emails.'
    __user = 'USER_EMAIL'
    __password = 'USER_PASSWORD'
    email_queue = deque() # deque chosen as stack implementation for O(1) runtime on pop
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    search_type = '[REVERSE] DATE'

    # logs in
    def login(self):
        print('logging in as', self.__user)
        try:
            self.mail.login(self.__user, self.__password)
        except: print('invalid credentials.')

    def select_inbox(self):
        self.mail.select('inbox')

    # sets private variable user
    def set_username_and_password(self):
        user = input("please enter your username:")
        self.__user = user
        password = input("please enter your password:")
        self.__password = password

        # populates the queue with the n most recent emails
    def initialize_queue(self, queue_length):
        emails = self.get_emails(self, queue_length)
        for message in emails:
            self.email_queue.append(message)

    def get_emails(self, count):
        emails = []
        for item in self.latest_n_emails(self, count):
            data = self.mail.fetch(item, '(BODY[HEADER])')
            header_data = data[1][0][1]
            header_data = header_data.decode("utf-8")
            parser = HeaderParser()
            message = parser.parsestr(header_data)
            decoded_header = make_header(decode_header(message['subject']))
            emails.append(str(decoded_header))
        return emails

        # gets latest n emails from the mailbox =
    def latest_n_emails(self, count):
        typ, data = self.mail.search(None, 'ALL')
        message_list = data[0].split()
        emails = message_list[-1 * count:]
        return emails



    def update_queue(self, email_queue, imap):
        most_recent_email = self.get_emails(1)
        if most_recent_email != email_queue[-1]:
            email_queue.append(most_recent_email)