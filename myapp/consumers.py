import json
from channels.generic.websocket import AsyncWebsocketConsumer
from myapp.langflow_tool import run_langflow

class LangflowConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        question = text_data_json.get('question')
        if question:
            # Use Langflow to get the response
            response_data = await run_langflow(question)
            print(question)
            # Send the response back to the client
            await self.send(text_data=json.dumps({
                'response': response_data
            }))
        else:
            await self.send(text_data=json.dumps({
                'response': "Invalid input"
            }))