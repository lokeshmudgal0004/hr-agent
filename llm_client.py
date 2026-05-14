import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"

llm_client = InferenceClient(
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)