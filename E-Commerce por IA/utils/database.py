from supabase import create_client as create_supabase_client
from supabase import Client as SupabaseClient

from pydantic import BaseModel
from typing import List
from postgrest import APIResponse
from typing import Optional, TypeAlias
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Type Alias for APIResponse
DBResponse: TypeAlias = Optional[APIResponse]

class Message(BaseModel):
    sms_message_sid: str
    num_media: int
    profile_name: str
    message_type: str
    sms_sid: str
    wa_id: str
    sms_status: str
    body: str
    num_segments: int
    referral_num_media: int
    message_sid: str
    account_sid: str
    from_: str
    api_version: str
    client: str
    is_assistant: bool

class DatabaseManager:
    """
    A class to manage the database connection and operations.
    """

    def __init__(self, url: str, key: str) -> None:
        """
        Initializes the DatabaseManager class.

        Parameters
        ----------
        url : str
            The URL of the Supabase project.
        key : str
            The Supabase project key.
        """
        self.url: str = url
        self.key: str = key
        self.client: SupabaseClient = create_supabase_client(self.url, self.key)
    
    def insert_message(self, message: Message) -> DBResponse:
        """
        Inserts a message into the database.

        Parameters
        ----------
        message : Message
            The message to be inserted.

        Returns
        -------
        DBResponse
            The response from the database, or None if an error occurred.
        """
        try:
            response = self.client.table('messages').insert({
                "wa_id": message.wa_id,
                "client": message.client,
                "is_assistant": message.is_assistant,
                "body": message.body,
            }).execute()
            return response
        except Exception as e:
            logger.error("Error inserting message: %s", e)
            return None
    
    def format_messages(self, messages: list) -> list:
        """
        Formats the messages retrieved from the database.

        Parameters
        ----------
        messages : list
            The messages to be formatted.

        Returns
        -------
        list
            The formatted messages.
        """
        formatted_messages = []
        for message in messages:
            formatted_message = {
                "role": "assistant" if message['is_assistant'] else "user",
                "content": message['body'],
            }
            formatted_messages.append(formatted_message)
        return formatted_messages

    def get_messages(self, wa_id:str) -> List[dict]:
        """
        Retrieves messages from the database for a given wa_id.

        Parameters
        ----------
        wa_id : str
            The WhatsApp ID to retrieve messages for.

        Returns
        -------
        List[dict]
            The list of messages retrieved from the database formatted in OpenAI format.
        """
        try:
            response = self.client.from_('messages').select('*').eq('wa_id', wa_id).execute()
            formatted_messages = self.format_messages(response.data)

            return formatted_messages
        except Exception as e:
            logger.error("Error retrieving messages: %s", e)
            return None
        
    def get_system_prompt(self, client: str) -> str:
        """
        Retrieves the system prompt from the database.

        Parameters
        ----------
        client : str
            The client to retrieve the system prompt for.

        Returns
        -------
        str
            The system prompt retrieved from the database.
        """
        try:
            response = self.client.from_('system_settings').select('*').eq('client', client).execute()
            return response.data[0]['system_prompt']
        except Exception as e:
            logger.error("Error retrieving system prompt: %s", e)
            return None