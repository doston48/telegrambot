from gemini_client import gemini_client

class UserState:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.language = "en"
        self.tone = "friendly"
        self.chat = gemini_client.create_chat(self.language, self.tone)

    def update_settings(self, language: str = None, tone: str = None):
        if language:
            self.language = language
        if tone:
            self.tone = tone
        # Recreate chat session with updated system instructions and preserve or start fresh
        self.chat = gemini_client.create_chat(self.language, self.tone)

    def reset(self):
        self.chat = gemini_client.create_chat(self.language, self.tone)

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def get_user_state(self, user_id: int) -> UserState:
        if user_id not in self.sessions:
            self.sessions[user_id] = UserState(user_id)
        return self.sessions[user_id]

    def reset_user(self, user_id: int):
        state = self.get_user_state(user_id)
        state.reset()

# Global session manager instance
session_manager = SessionManager()
