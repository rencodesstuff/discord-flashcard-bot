import aiosqlite
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_NAME = os.getenv('DATABASE_NAME', 'flashcards.db')

async def init_db():
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                category TEXT NOT NULL,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        ''')
        await db.commit()

async def add_flashcard(user_id: int, category: str, question: str, answer: str):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute('INSERT INTO flashcards (user_id, category, question, answer) VALUES (?, ?, ?, ?)',
                         (user_id, category, question, answer))
        await db.commit()

async def get_flashcards(user_id: int, category: str = None):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        if category:
            async with db.execute('SELECT question, answer FROM flashcards WHERE user_id = ? AND category = ?', (user_id, category)) as cursor:
                return await cursor.fetchall()
        else:
            async with db.execute('SELECT question, answer FROM flashcards WHERE user_id = ?', (user_id,)) as cursor:
                return await cursor.fetchall()

async def get_categories(user_id: int):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        async with db.execute('SELECT DISTINCT category FROM flashcards WHERE user_id = ?', (user_id,)) as cursor:
            categories = await cursor.fetchall()
            return [category[0] for category in categories]

async def delete_flashcard(user_id: int, question: str):
    async with aiosqlite.connect(DATABASE_NAME) as db:
        await db.execute('DELETE FROM flashcards WHERE user_id = ? AND question = ?', (user_id, question))
        await db.commit()