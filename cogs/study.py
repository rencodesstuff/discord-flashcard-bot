from discord.ext import commands
import random

class Study(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def study(self, ctx):
        """Start a study session"""
        flashcards = self.bot.get_cog('Flashcards').flashcards
        if not flashcards:
            await ctx.send("No flashcards available to study.")
            return
        question = random.choice(list(flashcards.keys()))
        await ctx.send(f"Question: {question}")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        msg = await self.bot.wait_for('message', check=check)
        if msg.content.lower() == flashcards[question].lower():
            await ctx.send("Correct!")
        else:
            await ctx.send(f"Incorrect. The correct answer is: {flashcards[question]}")

async def setup(bot):
    await bot.add_cog(Study(bot))