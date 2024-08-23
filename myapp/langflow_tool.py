import requests
from langflow import CustomComponent
from langchain import LLMChain
from langchain.llms.base import LLM
from langchain.schema import LLMResult, Generation
from typing import Any, List, Mapping, Optional

class LocalLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "local_llm"

    def _call(self, question: str, stop: Optional[List[str]] = None) -> str:
        # Make an HTTP POST request to the Flask service
        response = requests.post(
            "http://llm_service:5000/generate",  # Replace with your Flask service URL
            json={"prompt": question}
        )
        response.raise_for_status()  # Ensure we notice bad responses
        return response.json().get("response", "No response")

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"name": "LocalLLM"}

    def _generate(self, questions: List[str], stop: Optional[List[str]] = None) -> LLMResult:
        return LLMResult(generations=[[Generation(text=self._call(question))] for question in questions])

class CustomLLMComponent(CustomComponent):
    display_name = "Custom LLM Component"
    description = "Process a question using a locally deployed LLM."

    def build(self):
        self.question = self.create_input("question", "Question", str)

    def process(self, question: str):
        try:
            # Initialize LocalLLM
            llm = LocalLLM()
            
            # Generate response using LocalLLM
            response = llm._call(question)
            
            return response
        except Exception as e:
            return f"Error: {str(e)}"

async def run_langflow(question: str):
    component = CustomLLMComponent()
    result = component.process(question)
    return result
