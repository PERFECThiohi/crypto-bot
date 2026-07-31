import aiosqlite


DATABASE_NAME = "crypto_bot.db"


# ==============================
# Initialize Database
# ==============================

async def init_db():
    """
    ساخت جدول‌ها در اولین اجرا
    """

    async with aiosqlite.connect(DATABASE_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            requests INTEGER DEFAULT 0,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)


        await db.commit()



# ==============================
# Add / Update User
# ==============================

async def add_user(
        user_id: int,
        username: str,
        first_name: str
):
    """
    ثبت کاربر یا افزایش تعداد درخواست
    """

    async with aiosqlite.connect(DATABASE_NAME) as db:

        await db.execute("""
        INSERT INTO users
        (
            user_id,
            username,
            first_name,
            requests
        )
        VALUES (?, ?, ?, 1)

        ON CONFLICT(user_id)
        DO UPDATE SET
        requests = requests + 1
        """,
        (
            user_id,
            username,
            first_name
        ))

        await db.commit()



# ==============================
# Get Statistics
# ==============================

async def get_users_count():

    async with aiosqlite.connect(DATABASE_NAME) as db:

        cursor = await db.execute(
            "SELECT COUNT(*) FROM users"
        )

        result = await cursor.fetchone()

        return result[0]