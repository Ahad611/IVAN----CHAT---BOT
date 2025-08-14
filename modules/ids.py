def get_user_id(update):
    return update.message.from_user.id

def get_chat_id(update):
    return update.message.chat_id
  
