# Gemini Telegram AI Chatbot

An intelligent Telegram bot powered by Google Gemini AI, featuring multi-language support, interactive settings menus, tone customization, and conversation memory.

## Features
- 🤖 **Google Gemini AI Integration**: Context-aware conversational responses.
- ⚙️ **Settings Button & Inline Menus**: Easily change bot language and AI tone on the fly.
- 🌐 **Multi-Language Support**: English, Spanish, French, German, Russian, and Chinese.
- 🎭 **AI Tone Customization**: Switch between Friendly, Professional, and Concise tones.
- 🔄 **Conversation Memory & Reset**: Context retention per user with reset capabilities.

## Setup Instructions

1. **Clone or navigate to the project directory**:
   ```bash
   cd telegrambot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**:
   Open or create `.env` and configure your keys:
   ```env
   TELEGRAM_BOT_TOKEN=8512305919:AAGQsQVHm-10FuOeJefecmCwluYNjoRqzoI
   GEMINI_API_KEY=your_google_gemini_api_key
   ```

4. **Run the Bot**:
   ```bash
   python main.py
   ```
