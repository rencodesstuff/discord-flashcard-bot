import asyncio
import random
from discord.ext import commands
from utils.database import add_flashcard, get_flashcards, get_categories, delete_flashcard

class Flashcards(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, category, *, content):
        """Adds a new flashcard to a category. Usage: !add category question | answer"""
        try:
            question, answer = content.split('|', 1)
            question = question.strip()
            answer = answer.strip()
            if not question or not answer:
                raise ValueError
        except ValueError:
            await ctx.send("Invalid format. Please use: !add category question | answer")
            return

        await add_flashcard(ctx.author.id, category, question, answer)
        await ctx.send(f"Flashcard added to category '{category}':\nQ: {question}\nA: {answer}")

    @commands.command()
    async def list(self, ctx, category=None):
        """Lists all your flashcards, optionally filtered by category"""
        flashcards = await get_flashcards(ctx.author.id, category)
        if not flashcards:
            await ctx.send("You have no flashcards" + (f" in category '{category}'" if category else "") + ".")
            return
        flashcard_list = "\n".join([f"{i+1}. Q: {q} A: {a}" for i, (q, a) in enumerate(flashcards)])
        await ctx.send(f"Your Flashcards" + (f" in category '{category}'" if category else "") + ":\n{flashcard_list}")

    @commands.command()
    async def categories(self, ctx):
        """Lists all your flashcard categories"""
        categories = await get_categories(ctx.author.id)
        if not categories:
            await ctx.send("You have no categories.")
            return
        await ctx.send(f"Your categories: {', '.join(categories)}")

    @commands.command()
    async def delete(self, ctx, category=None):
        """Displays flashcards and allows deletion by number, optionally filtered by category"""
        flashcards = await get_flashcards(ctx.author.id, category)
        if not flashcards:
            await ctx.send("You have no flashcards" + (f" in category '{category}'" if category else "") + " to delete.")
            return

        flashcard_list = "\n".join([f"{i+1}. Q: {q} A: {a}" for i, (q, a) in enumerate(flashcards)])
        await ctx.send(f"Your Flashcards" + (f" in category '{category}'" if category else "") + ":\n{flashcard_list}\n\nEnter the number of the flashcard you want to delete:")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=30.0)
            index = int(msg.content) - 1
            if 0 <= index < len(flashcards):
                question, _ = flashcards[index]
                await delete_flashcard(ctx.author.id, question)
                await ctx.send(f"Flashcard deleted: Q: {question}")
            else:
                await ctx.send("Invalid number. No flashcard deleted.")
        except asyncio.TimeoutError:
            await ctx.send("Deletion cancelled due to timeout.")
        except ValueError:
            await ctx.send("Invalid input. Please enter a number.")

    @commands.command()
    async def study(self, ctx, category=None):
        """Start a study session, optionally for a specific category"""
        flashcards = await get_flashcards(ctx.author.id, category)
        if not flashcards:
            await ctx.send("You have no flashcards" + (f" in category '{category}'" if category else "") + " to study.")
            return

        random.shuffle(flashcards)
        correct = 0
        total = len(flashcards)

        for question, answer in flashcards:
            await ctx.send(f"Question: {question}")
            await ctx.send("Type your answer, or 'skip' to move to the next card.")

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                msg = await self.bot.wait_for('message', check=check, timeout=30.0)
                if msg.content.lower() == 'skip':
                    await ctx.send(f"Skipped. The correct answer was: {answer}")
                elif msg.content.lower() == answer.lower():
                    await ctx.send("Correct!")
                    correct += 1
                else:
                    await ctx.send(f"Incorrect. The correct answer was: {answer}")
            except asyncio.TimeoutError:
                await ctx.send(f"Time's up! The correct answer was: {answer}")

        await ctx.send(f"Study session complete! You got {correct} out of {total} correct.")

async def setup(bot):
    await bot.add_cog(Flashcards(bot))