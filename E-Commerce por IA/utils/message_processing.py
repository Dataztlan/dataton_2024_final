import logging
from openai import OpenAI
from typing import List, Union
from openai import OpenAI
import json


tools = [
  {
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA",
          },
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        },
        "required": ["location"],
      },
    }
  }
]

class ToolManager:
    """
    Class to manage the tools used in the completions
    """

    def __init__(self, tool_dict: dict, functions: dict) -> None:
        """
        Initialize the ToolManager class
        
        Parameters
        ----------
        tool_dict : dict
            The dictionary of tools to use in the completions
        functions : dict[str,function]
            The list of functions to use in the completions
        """
        self.tool_dict = tool_dict
        self.functions = functions
    
class LLMManager:
    """
    Class to manage the interaction with the OpenAI API
    """

    def __init__(self, client: OpenAI, model: str = "gpt-4o-mini") -> None:
        """
        Initialize the LLMManager class
        
        Parameters
        ----------
        client : OpenAI
            The OpenAI client to interact with the API
        model : str
            The model to use for the completions
        """
        self.client: OpenAI = client
        self.model = model

    def generate_answer(self, content: str, message_list: List[dict], 
                        role: str = 'user', tools: ToolManager = None,debug: bool = False) -> Union[dict, tuple, None]:
        """
        Generate a response to a message
        
        Parameters
        ----------
        content : str
            The content of the message to generate a response to
        message_list : List[dict]
            The list of previous messages
        role : str
            The role of the user sending the message
        tools : ToolManager
            The tools to use in the completions
        debug : bool
            Whether to return the full response or just the content of the message
        
        Returns
        -------
        Union[dict, str, None]
            The response from the API, or just the content of the message, or None in case of error
        """
        if not isinstance(content, str) or not content:
            logging.error("Invalid content: %s", content)
            return None

        if not isinstance(message_list, list) or not all(isinstance(message, dict) for message in message_list):
            logging.error("Invalid message_list: %s", message_list)
            return None

        if role not in ['user', 'system']:
            logging.error("Invalid role: %s", role)
            return None

        if not isinstance(debug, bool):
            logging.error("Invalid debug: %s", debug)
            return None

        try:
            if tools:
                logging.info("Generating answer with tools")
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=message_list + [{"role": role, "content": content}],
                    tools=tools.tool_dict,
                    tool_choice="auto",
                )

                logging.info("Calling tool")
                if response.choices[0].finish_reason == "tool_calls":
                    function_name = response.choices[0].message.tool_calls[0].function.name
                    arguments = json.loads(response.choices[0].message.tool_calls[0].function.arguments)

                    if function_name in tools.functions:
                        logging.info("Calling function: %s", function_name)
                        function_response = tools.functions[function_name](**arguments)
                        response = "[foto del producto]\n" + function_response
                        logging.info("Function response: %s", function_response)
                        """ message_list.append(function_call_result_message)

                        logging.info("Generating answer with tool response")
                        response = self.client.chat.completions.create(
                            model=self.model,
                            messages=message_list
                        )
                        logging.info("Answer generated with tool response") """
                    
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=message_list + [{"role": role, "content": content}],
                )
        except Exception as e:
            logging.error("Error generating answer: %s", str(e))
            return None

        if debug:
            return response, ToolManager!=None
        else:
            if type(response) == str:
                return response
            else:
                return response.choices[0].message.content
