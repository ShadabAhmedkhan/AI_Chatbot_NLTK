from database.connection import get_sql_connection
from ml.ml_bot import get_bot_response

def get_bot_reply(message: str, current_user: dict):
    bot_reply = get_bot_response(message.lower()) or "Sorry, I didn't understand that."

    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_history (user_id, user_message, bot_reply) VALUES (?, ?, ?)",
        current_user["id"], message.lower(), bot_reply
    )
    conn.commit()
    conn.close()

    return {"reply": bot_reply}

def get_chat_history(current_user: dict):
    conn = get_sql_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT user_message, bot_reply, timestamp FROM chat_history WHERE user_id = ?",
        current_user["id"]
    )
    rows = cursor.fetchall()
    conn.close()

    return [{"user_message": row[0], "bot_reply": row[1], "timestamp": row[2]} for row in rows]
