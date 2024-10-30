# This is main.py
from fastapi import FastAPI, Form
import logging
from utils.database import DatabaseManager, Message
from utils.credential_management import load_credentials
from utils.message_processing import LLMManager,ToolManager
from openai import OpenAI
from utils.twilio_management import TwilioManager

credentials = load_credentials()

openai_client = OpenAI(api_key=credentials['openai']['api_key'])

app = FastAPI()

database_manager = DatabaseManager(
    url=credentials['supabase']['url'],
    key=credentials['supabase']['key']
)

llm_manager = LLMManager(client=openai_client)

twilio_manager = TwilioManager(
    account_sid=credentials['twilio']['account_sid'],
    auth_token=credentials['twilio']['auth_token']
)

tool_list = [
    {
        "type": "function",
        "function": {
            "name": "send_tv_image",
            "description": "Manda una imágen de la televisión en existencias",
            "parameters": {
                "type": "object",
                "properties": {
                    "body": {
                        "type": "string",
                        "description": "Agrega aquí una descripción de la televisión"
                    }
                },
                "required": ["body"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_perfume_image",
            "description": "Manda una imágen del perfume en existencias",
            "parameters": {
                "type": "object",
                "properties": {
                    "body": {
                        "type": "string",
                        "description": "Agrega aquí una descripción del perfume"
                    }
                },
                "required": ["body"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_blouse_image",
            "description": "Manda una imágen de la blusa en existencias",
            "parameters": {
                "type": "object",
                "properties": {
                    "body": {
                        "type": "string",
                        "description": "Agrega aquí una descripción de la blusa"
                    }
                },
                "required": ["body"]
            }
        }
    }
]



@app.get("/")
async def get_root():
    return {"SofIA systems status: Online"}

@app.post("/whatsapp")
async def submit_form(
    SmsMessageSid: str = Form(...),
    NumMedia: int = Form(...),
    ProfileName: str = Form(...),
    MessageType: str = Form(...),
    SmsSid: str = Form(...),
    WaId: str = Form(...),
    SmsStatus: str = Form(...),
    Body: str = Form(...),
    To: str = Form(...),
    NumSegments: int = Form(...),
    ReferralNumMedia: int = Form(...),
    MessageSid: str = Form(...),
    AccountSid: str = Form(...),
    From: str = Form(...),
    ApiVersion: str = Form(...)
):
    logging.info("Received message from %s: %s", WaId, Body)
    message = Message(
        sms_message_sid=SmsMessageSid,
        num_media=NumMedia,
        profile_name=ProfileName,
        message_type=MessageType,
        sms_sid=SmsSid,
        wa_id=WaId,
        sms_status=SmsStatus,
        body=Body,
        num_segments=NumSegments,
        referral_num_media=ReferralNumMedia,
        message_sid=MessageSid,
        account_sid=AccountSid,
        from_=From,
        api_version=ApiVersion,
        client='demo',
        is_assistant=False
    )


    def send_tv_image(body: str) -> str:
        twilio_manager.send_message_media("whatsapp:+" + WaId, "whatsapp:+" + "17727580952",
                                                 body, "https://bigbox.rw/wp-content/uploads/2023/12/SANO-SMART-TV-43-inches-1-1200x900-1.jpg")
        
        return body

    def send_perfume_image(body: str) -> str:
        twilio_manager.send_message_media("whatsapp:+" + WaId, "whatsapp:+" + "17727580952",
                                                 body, "https://abscents.com.mx/cdn/shop/files/845_8yngbx_n5_eau_premiere_720-fotor-20240323162113.jpg")
        return body

    def send_blouse_image(body: str) -> str:
        twilio_manager.send_message_media("whatsapp:+" + WaId, "whatsapp:+" + "17727580952",
                                                 body, "https://www.elpalaciodehierro.com/on/demandware.static/-/Sites-palacio-master-catalog/default/dwf73a7b5e/images/41234224/amarillo/large/41234225_AMARILLO_x1.jpg")
        return body

    tool_manager = ToolManager(tool_dict=tool_list, functions={"send_tv_image": send_tv_image,
                                                               "send_perfume_image": send_perfume_image,
                                                               "send_blouse_image": send_blouse_image})
    logging.info("Inserting user message")
    response = database_manager.insert_message(message)
    logging.info("User message inserted")
    
    if response is None:
        logging.error("Error inserting user message")
        return {"status": "error"}
    
    logging.info("Getting messages")
    message_list = database_manager.get_messages(WaId)
    logging.info("Messages retrieved")

    if message_list is None:
        logging.error("Error getting messages")
        return {"status": "error"}

    logging.info("Getting system prompt") 
    system_prompt = database_manager.get_system_prompt("demo")
    logging.info("System prompt retrieved") 
    
    logging.info("Generating answer") 
    assistant_response:str = llm_manager.generate_answer(Body, [{"role":"system", "content":system_prompt}] + message_list, 
                                                         role='user',tools=tool_manager,debug=False)
    logging.info("Answer generated")

    if response is None:
        logging.error("Error generating answer")
        return {"status": "error"}

    logging.info("Inserting assistant message")
    response = database_manager.insert_message(
        Message(
        sms_message_sid=SmsMessageSid,
        num_media=0,
        profile_name=ProfileName,
        message_type=MessageType,
        sms_sid=SmsSid,
        wa_id=WaId,
        sms_status=SmsStatus,
        body=assistant_response,
        num_segments=1,
        referral_num_media=0,
        message_sid=MessageSid,
        account_sid=AccountSid,
        from_=From,
        api_version=ApiVersion,
        client='demo',
        is_assistant=True
    ))    
    logging.info("Assistant message inserted")

    if response is None:
        logging.error("Error inserting assistant message")
        return {"status": "error"}
    
    logging.info("Sending message")
    if "foto del producto" not in assistant_response:
        response = twilio_manager.send_message(
            to="whatsapp:+" + WaId,
            from_="whatsapp:+" + "17727580952",
            body=assistant_response
        )
    logging.info("Message sent")

    if response is None:
        logging.error("Error sending message")
        return {"status": "error"}

    return {"status": "success"}