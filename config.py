import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Supported languages
LANGUAGES = {
    "en": "English",
    "es": "Español",
    "fr": "Français",
    "de": "Deutsch",
    "ru": "Русский",
    "zh": "中文"
}

# Localization dictionary
LOCALES = {
    "en": {
        "welcome": "Hello! I am your AI assistant powered by Google Gemini. Send me a message or use the buttons below.",
        "help": "🤖 *Gemini AI Bot Help*\n\n- Send any text message to chat with Gemini.\n- Use ⚙️ *Settings* to change language or AI tone.\n- Use 🔄 *Reset* to clear conversation memory.",
        "settings_title": "⚙️ *Bot Settings*\n\nSelect an option below to customize your experience:",
        "lang_select": "🌐 Please choose your language:",
        "lang_changed": "✅ Language successfully changed to *{lang}*.",
        "tone_select": "🎭 Please choose AI conversation tone:",
        "tone_changed": "✅ AI tone successfully changed to *{tone}*.",
        "reset_success": "🔄 Conversation memory has been reset.",
        "btn_chat": "💬 Chat",
        "btn_settings": "⚙️ Settings",
        "btn_reset": "🔄 Reset",
        "btn_help": "❓ Help",
        "btn_lang": "🌐 Change Language",
        "btn_tone": "🎭 AI Tone",
        "btn_back": "« Back to Menu",
        "error_api": "⚠️ Error communicating with Gemini AI. Please check your API key or try again later.",
        "error_general": "⚠️ An unexpected error occurred. Please try again."
    },
    "es": {
        "welcome": "¡Hola! Soy tu asistente de IA impulsado por Google Gemini. Envíame un mensaje o usa los botones de abajo.",
        "help": "🤖 *Ayuda del Bot de IA Gemini*\n\n- Envía cualquier mensaje de texto para chatear con Gemini.\n- Usa ⚙️ *Configuración* para cambiar el idioma o el tono de la IA.\n- Usa 🔄 *Reiniciar* para borrar la memoria de la conversación.",
        "settings_title": "⚙️ *Configuración del Bot*\n\nSelecciona una opción para personalizar tu experiencia:",
        "lang_select": "🌐 Por favor elige tu idioma:",
        "lang_changed": "✅ Idioma cambiado exitosamente a *{lang}*.",
        "tone_select": "🎭 Por favor elige el tono de la IA:",
        "tone_changed": "✅ Tono de IA cambiado exitosamente a *{tone}*.",
        "reset_success": "🔄 La memoria de la conversación ha sido reiniciada.",
        "btn_chat": "💬 Chat",
        "btn_settings": "⚙️ Configuración",
        "btn_reset": "🔄 Reiniciar",
        "btn_help": "❓ Ayuda",
        "btn_lang": "🌐 Cambiar Idioma",
        "btn_tone": "🎭 Tono de IA",
        "btn_back": "« Volver al Menú",
        "error_api": "⚠️ Error al comunicarse con Gemini AI. Verifica tu clave API o inténtalo más tarde.",
        "error_general": "⚠️ Ocurrió un error inesperado. Por favor inténtalo de nuevo."
    },
    "fr": {
        "welcome": "Bonjour ! Je suis votre assistant IA propulsé par Google Gemini. Envoyez-moi un message ou utilisez les boutons ci-dessous.",
        "help": "🤖 *Aide du Bot IA Gemini*\n\n- Envoyez n'importe quel message texte pour discuter avec Gemini.\n- Utilisez ⚙️ *Paramètres* pour changer la langue ou le ton.\n- Utilisez 🔄 *Réinitialiser* pour effacer la mémoire.",
        "settings_title": "⚙️ *Paramètres du Bot*\n\nSélectionnez une option ci-dessous :",
        "lang_select": "🌐 Veuillez choisir votre langue :",
        "lang_changed": "✅ Langue changée avec succès en *{lang}*.",
        "tone_select": "🎭 Veuillez choisir le ton de l'IA :",
        "tone_changed": "✅ Ton de l'IA changé avec succès en *{tone}*.",
        "reset_success": "🔄 La mémoire de la conversation a été réinitialisée.",
        "btn_chat": "💬 Discuter",
        "btn_settings": "⚙️ Paramètres",
        "btn_reset": "🔄 Réinitialiser",
        "btn_help": "❓ Aide",
        "btn_lang": "🌐 Changer de Langue",
        "btn_tone": "🎭 Ton de l'IA",
        "btn_back": "« Retour au Menu",
        "error_api": "⚠️ Erreur de communication avec Gemini AI. Veuillez vérifier votre clé API.",
        "error_general": "⚠️ Une erreur inattendue s'est produite."
    },
    "de": {
        "welcome": "Hallo! Ich bin dein KI-Assistent, angetrieben von Google Gemini. Sende mir eine Nachricht oder nutze die Buttons unten.",
        "help": "🤖 *Gemini KI Bot Hilfe*\n\n- Sende eine Nachricht, um mit Gemini zu chatten.\n- Nutze ⚙️ *Einstellungen*, um Sprache oder Tonfall zu ändern.\n- Nutze 🔄 *Zurücksetzen*, um den Verlauf zu löschen.",
        "settings_title": "⚙️ *Bot-Einstellungen*\n\nWähle eine Option:",
        "lang_select": "🌐 Bitte wähle deine Sprache:",
        "lang_changed": "✅ Sprache erfolgreich zu *{lang}* geändert.",
        "tone_select": "🎭 Bitte wähle den KI-Tonfall:",
        "tone_changed": "✅ KI-Tonfall erfolgreich zu *{tone}* geändert.",
        "reset_success": "🔄 Der Konversationsverlauf wurde zurückgesetzt.",
        "btn_chat": "💬 Chat",
        "btn_settings": "⚙️ Einstellungen",
        "btn_reset": "🔄 Zurücksetzen",
        "btn_help": "❓ Hilfe",
        "btn_lang": "🌐 Sprache ändern",
        "btn_tone": "🎭 KI-Tonfall",
        "btn_back": "« Zurück zum Menü",
        "error_api": "⚠️ Fehler bei der Kommunikation mit Gemini AI.",
        "error_general": "⚠️ Ein unerwarteter Fehler ist aufgetreten."
    },
    "ru": {
        "welcome": "Привет! Я ваш ИИ-ассистент на базе Google Gemini. Отправьте мне сообщение или используйте кнопки ниже.",
        "help": "🤖 *Справка по боту Gemini AI*\n\n- Отправьте текстовое сообщение для общения с Gemini.\n- Используйте ⚙️ *Настройки* для смены языка или тона.\n- Используйте 🔄 *Сброс* для очистки истории.",
        "settings_title": "⚙️ *Настройки бота*\n\nВыберите опцию ниже:",
        "lang_select": "🌐 Пожалуйста, выберите язык:",
        "lang_changed": "✅ Язык успешно изменен на *{lang}*.",
        "tone_select": "🎭 Пожалуйста, выберите тон ИИ:",
        "tone_changed": "✅ Тон ИИ успешно изменен на *{tone}*.",
        "reset_success": "🔄 История разговора сброшена.",
        "btn_chat": "💬 Чат",
        "btn_settings": "⚙️ Настройки",
        "btn_reset": "🔄 Сброс",
        "btn_help": "❓ Помощь",
        "btn_lang": "🌐 Изменить язык",
        "btn_tone": "🎭 Тон ИИ",
        "btn_back": "« Назад в меню",
        "error_api": "⚠️ Ошибка связи с Gemini AI. Проверьте ваш API ключ.",
        "error_general": "⚠️ Произошла непредвиденная ошибка."
    },
    "zh": {
        "welcome": "你好！我是由 Google Gemini 驱动的 AI 助手。发送消息或使用下方按钮开始。",
        "help": "🤖 *Gemini AI 机器人帮助*\n\n- 发送任意文本消息与 Gemini 对话。\n- 使用 ⚙️ *设置* 更改语言或 AI 语气。\n- 使用 🔄 *重置* 清除对话记忆。",
        "settings_title": "⚙️ *机器人设置*\n\n请选择以下选项来自定义您的体验：",
        "lang_select": "🌐 请选择您的语言：",
        "lang_changed": "✅ 语言已成功更改为 *{lang}*。",
        "tone_select": "🎭 请选择 AI 语气：",
        "tone_changed": "✅ AI 语气已成功更改为 *{tone}*。",
        "reset_success": "🔄 对话记忆已重置。",
        "btn_chat": "💬 聊天",
        "btn_settings": "⚙️ 设置",
        "btn_reset": "🔄 重置",
        "btn_help": "❓ 帮助",
        "btn_lang": "🌐 更改语言",
        "btn_tone": "🎭 AI 语气",
        "btn_back": "« 返回菜单",
        "error_api": "⚠️ 与 Gemini AI 通信时出错，请检查 API 密钥或稍后重试。",
        "error_general": "⚠️ 发生意外错误，请重试。"
    }
}

AI_TONES = {
    "friendly": {"en": "Friendly & Casual", "es": "Amistoso y Casual", "fr": "Amical et Décontracté", "de": "Freundlich & Locker", "ru": "Дружелюбный", "zh": "友善休闲"},
    "professional": {"en": "Professional & Formal", "es": "Profesional y Formal", "fr": "Professionnel et Formel", "de": "Professionell & Formell", "ru": "Профессиональный", "zh": "专业正式"},
    "concise": {"en": "Short & Concise", "es": "Corto y Conciso", "fr": "Court et Concis", "de": "Kurz & Prägnant", "ru": "Краткий", "zh": "简洁明了"}
}

def get_text(lang: str, key: str, **kwargs) -> str:
    lang_dict = LOCALES.get(lang, LOCALES["en"])
    text = lang_dict.get(key, LOCALES["en"].get(key, key))
    if kwargs:
        text = text.format(**kwargs)
    return text
