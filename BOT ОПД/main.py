from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_admin_keyboard(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="❌", callback_data=f"set_status:{user_id}:❌"),
            InlineKeyboardButton(text="✅", callback_data=f"set_status:{user_id}:✅"),
            InlineKeyboardButton(text="Очистить", callback_data=f"set_status:{user_id}:")
        ],
        [InlineKeyboardButton(text="Снять бан", callback_data=f"remove_ban:{user_id}")],
        [InlineKeyboardButton(text="Просмотреть медиа", callback_data=f"view_media:{user_id}")],
        [InlineKeyboardButton(text="Вернуться к списку пользователей", callback_data="return_to_users_list")]
    ])