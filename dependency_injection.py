import abc

class EmailSender(abc.ABC):
    @abc.abstractmethod
    def send(self, email:str, message:str):
        pass

class SendGridESender(EmailSender):
    def send(self, email:str, message:str):
        print(f"Sending {message} to {email} using Gmail")

class MailChimpSender(EmailSender):
    def send(self, email:str, message:str):
        print(f"Sending {message} to {email} using Chimp")


def send_email(email:str, message:str, sender:EmailSender):
   sender.send(email, message)

send_grid = SendGridESender()
mailchimp = MailChimpSender()

send_email("rest@gmail.com", "hello world", mailchimp)
