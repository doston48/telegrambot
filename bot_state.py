class UserState:
    def __init__(self):
        self.language = "en"
        self.tone = "friendly"
        self.history = []  # List of message dicts or chat history objects

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def get_user_state(self, user_id: int) -> UserState:
        if user_id not in self.sessions:
            self.sessions[user_id] = UserState()
        return self.sessions[user_id]

    def reset_user(self, user_id: int):
        if user_id in self.sessions:
            self.sessions[user_id].history = []

# Global session manager instance
session_manager = SessionManager()
