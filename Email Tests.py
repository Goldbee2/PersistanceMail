from Email import *


class EmailQueueTests:

    def test_get_emails(self):
        test_mail = EmailQueue
        test_mail.set_username_and_password(test_mail)
        test_mail.login(test_mail)
        test_mail.select_inbox(test_mail)
        test_mail.get_emails(test_mail, 5)
        while len(test_mail.email_queue) > 0:
            print(test_mail.email_queue.pop())

    def test_update_queue(self):
        pass





test = EmailQueueTests
test.test_get_emails(test)
test.test_update_queue(test)




