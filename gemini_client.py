import os
import logging
from config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

HAS_NEW_SDK = False
try:
    from google import genai
    from google.genai import types
    HAS_NEW_SDK = True
except ImportError:
    try:
        import google.generativeai as genai
    except ImportError:
        genai = None

class GeminiClient:
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.client = None
        if not self.api_key:
            logger.warning("GEMINI_API_KEY is not set. AI responses will be simulated or return errors.")
            return

        try:
            if HAS_NEW_SDK:
                self.client = genai.Client(api_key=self.api_key)
            else:
                genai.configure(api_key=self.api_key)
        except Exception as e:
            logger.error(f"Failed to initialize Gemini client: {e}")

    def create_chat(self, language: str = "en", tone: str = "friendly"):
        if not self.api_key or (not self.client and not HAS_NEW_SDK):
            return None

        system_instruction = (
            f"You are a helpful AI assistant in a Telegram bot. "
            f"You must respond in the language code '{language}'. "
            f"Your conversation tone should be '{tone}'."
        )
        model_name = "gemini-3.5-flash-lite"

        try:
            if HAS_NEW_SDK:
                return self.client.chats.create(
                    model=model_name,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.7,
                    )
                )
            else:
                model = genai.GenerativeModel(
                    model_name="gemini-3.5-flash-lite",
                    system_instruction=system_instruction
                )
                return model.start_chat(history=[])
        except Exception as e:
            logger.error(f"Failed to create chat session: {e}")
            return None

    def send_message(self, chat, prompt: str) -> str:
        if not chat:
            return "⚠️ Gemini AI chat session is not initialized. Please check your API key in .env."
        try:
            response = chat.send_message(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini send_message error: {e}")
            return f"⚠️ Error communicating with Gemini AI: {str(e)}"

gemini_client = GeminiClient()
