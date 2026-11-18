import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from config import get_text, LANGUAGES, AI_TONES
from bot_state import session_manager
from gemini_client import gemini_client

logger = logging.getLogger(__name__)

def get_main_keyboard(lang: str) -> ReplyKeyboardMarkup:
    keyboard = [
        [get_text(lang, "btn_chat"), get_text(lang, "btn_settings")],
        [get_text(lang, "btn_reset"), get_text(lang, "btn_help")]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def get_settings_inline_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton(get_text(lang, "btn_lang"), callback_data="menu_lang")],
        [InlineKeyboardButton(get_text(lang, "btn_tone"), callback_data="menu_tone")],
    ]
    return InlineKeyboardMarkup(keyboard)

def get_languages_inline_keyboard() -> InlineKeyboardMarkup:
    keyboard = []
    for code, name in LANGUAGES.items():
        keyboard.append([InlineKeyboardButton(name, callback_data=f"set_lang_{code}")])
    keyboard.append([InlineKeyboardButton("« Back", callback_data="menu_settings")])
    return InlineKeyboardMarkup(keyboard)

def get_tones_inline_keyboard(lang: str) -> InlineKeyboardMarkup:
    keyboard = []
    for tone_key, tone_names in AI_TONES.items():
        name = tone_names.get(lang, tone_names["en"])
        keyboard.append([InlineKeyboardButton(name, callback_data=f"set_tone_{tone_key}")])
    keyboard.append([InlineKeyboardButton(get_text(lang, "btn_back"), callback_data="menu_settings")])
    return InlineKeyboardMarkup(keyboard)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    state = session_manager.get_user_state(user.id)
    lang = state.language
    
    welcome_text = get_text(lang, "welcome")
    reply_markup = get_main_keyboard(lang)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode="Markdown")

async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    state = session_manager.get_user_state(user.id)
    lang = state.language
    
    text = get_text(lang, "settings_title")
    reply_markup = get_settings_inline_keyboard(lang)
    
    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    state = session_manager.get_user_state(user.id)
    lang = state.language
    
    help_text = get_text(lang, "help")
    reply_markup = get_main_keyboard(lang)
    
    await update.message.reply_text(help_text, reply_markup=reply_markup, parse_mode="Markdown")

async def reset_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    session_manager.reset_user(user.id)
    state = session_manager.get_user_state(user.id)
    lang = state.language
    
    await update.message.reply_text(get_text(lang, "reset_success"), reply_markup=get_main_keyboard(lang))

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    user = update.effective_user
    state = session_manager.get_user_state(user.id)
    lang = state.language
    data = query.data
    
    if data == "menu_settings":
        text = get_text(lang, "settings_title")
        reply_markup = get_settings_inline_keyboard(lang)
        await query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")
        
    elif data == "menu_lang":
        text = get_text(lang, "lang_select")
        reply_markup = get_languages_inline_keyboard()
        await query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")
        
    elif data == "menu_tone":
        text = get_text(lang, "tone_select")
        reply_markup = get_tones_inline_keyboard(lang)
        await query.message.edit_text(text, reply_markup=reply_markup, parse_mode="Markdown")
        
    elif data.startswith("set_lang_"):
        new_lang = data.split("_")[2]
        if new_lang in LANGUAGES:
            state.update_settings(language=new_lang)
            success_msg = get_text(new_lang, "lang_changed", lang=LANGUAGES[new_lang])
            await query.message.reply_text(success_msg, reply_markup=get_main_keyboard(new_lang), parse_mode="Markdown")
            try:
                await query.message.delete()
            except Exception:
                pass
                
    elif data.startswith("set_tone_"):
        new_tone = data.split("_")[2]
        if new_tone in AI_TONES:
            state.update_settings(tone=new_tone)
            tone_name = AI_TONES[new_tone].get(lang, AI_TONES[new_tone]["en"])
            success_msg = get_text(lang, "tone_changed", tone=tone_name)
            await query.message.edit_text(success_msg, reply_markup=get_settings_inline_keyboard(lang), parse_mode="Markdown")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
        
    text = update.message.text
    user = update.effective_user
    state = session_manager.get_user_state(user.id)
    lang = state.language
    
    # Check reply keyboard buttons
    if text == get_text(lang, "btn_settings") or text == "⚙️ Settings":
        await settings_command(update, context)
        return
    elif text == get_text(lang, "btn_reset") or text == "🔄 Reset":
        await reset_command(update, context)
        return
    elif text == get_text(lang, "btn_help") or text == "❓ Help":
        await help_command(update, context)
        return
    elif text == get_text(lang, "btn_chat") or text == "💬 Chat":
        await update.message.reply_text("💬 Send me any question or prompt and I will answer with Gemini AI!", reply_markup=get_main_keyboard(lang))
        return
        
    # Otherwise, query Gemini AI using native chat session
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    
    response_text = gemini_client.send_message(state.chat, text)
    
    await update.message.reply_text(response_text, reply_markup=get_main_keyboard(lang), parse_mode="Markdown")
