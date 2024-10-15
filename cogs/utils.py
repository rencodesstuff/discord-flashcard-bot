from discord.ext import commands
import discord

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='commands')
    async def show_commands(self, ctx):
        """Displays all available commands and their descriptions"""
        embed = discord.Embed(title="Flashcard Bot Commands", 
                              description="Here are all the available commands:",
                              color=discord.Color.blue())
        
        command_list = [
            ("!add", "Adds a new flashcard to a category. Usage: !add category question | answer"),
            ("!list", "Lists all your flashcards. Usage: !list [category]"),
            ("!categories", "Lists all your flashcard categories"),
            ("!delete", "Displays flashcards and allows deletion by number. Usage: !delete [category]"),
            ("!study", "Starts a study session. Usage: !study [category]"),
            ("!commands", "Shows this list of commands")
        ]
        
        for cmd, description in command_list:
            embed.add_field(name=cmd, value=description, inline=False)
        
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utils(bot))