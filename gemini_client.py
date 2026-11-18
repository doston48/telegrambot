import os
import logging
from config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

# Try importing the new google-genai SDK, fallback to google.generativeai if needed
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

    def generate_response(self, prompt: str, language: str = "en", tone: str = "friendly", history: list = None) -> str:
        if not self.api_key or (not self.client and not HAS_NEW_SDK):
            return "⚠️ Gemini API key is missing. Please set GEMINI_API_KEY in your .env file."

        try:
            system_instruction = (
                f"You are a helpful AI assistant in a Telegram bot. "
                f"You must respond in the language code '{language}'. "
                f"Your conversation tone should be '{tone}'."
            )

            model_name = "gemini-3.5-flash-lite"

            if HAS_NEW_SDK:
                # Build contents with history if available
                contents = []
                if history:
                    contents.extend(history)
                contents.append(prompt)

                response = self.client.models.generate_content(
                    model=model_name,
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.7,
                    )
                )
                return response.text
            else:
                # Older generativeai SDK fallback
                model = genai.GenerativeModel(
                    model_name="gemini-3.5-flash-lite",
                    system_instruction=system_instruction
                )
                chat = model.start_chat(history=history or [])
                response = chat.send_message(prompt)
                return response.text

        except Exception as e:
            logger.error(f"Gemini generation error: {e}")
            return f"⚠️ Error communicating with Gemini AI: {str(e)}"

gemini_client = GeminiClient()
