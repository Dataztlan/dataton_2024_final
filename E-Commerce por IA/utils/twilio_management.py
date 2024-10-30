from twilio.rest import Client
import logging

class TwilioManager:

    def __init__(self, account_sid: str, auth_token: str) -> None:
        """
        Initializes the TwilioManager class.

        Parameters
        ----------
        account_sid : str
            The Twilio account SID.
        auth_token : str
            The Twilio auth token.
        """
        self.account_sid: str = account_sid
        self.auth_token: str = auth_token
        self.client: Client = Client(self.account_sid, self.auth_token)

    def send_message(self, to: str, from_: str, body: str) -> dict:
        """
        Sends a message using the Twilio API.

        Parameters
        ----------
        to : str
            The recipient's phone number.
        from_ : str
            The sender's phone number.
        body : str
            The message body.
        
        Returns
        -------
        dict
            The response from the Twilio API.
        """
        try:
            response = self.client.messages.create(to=to, from_=from_, body=body)
        except Exception as e:
            logging.error("Error sending message: %s", str(e))
            return None
        return response.sid
    
    def send_message_media(self, to: str, from_: str, body: str, media_url: str) -> dict:
        """
        Sends a message with media using the Twilio API.

        Parameters
        ----------
        to : str
            The recipient's phone number.
        from_ : str
            The sender's phone number.
        body : str
            The message body.
        media_url : str
            The URL of the media to send.
        
        Returns
        -------
        dict
            The response from the Twilio API.
        """
        try:
            response = self.client.messages.create(to=to, from_=from_, body=body, media_url=[media_url])
        except Exception as e:
            logging.error("Error sending message with media: %s", str(e))
            return None
        return response.sid