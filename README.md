# Discord Flashcard Bot

<p align="center">
<p align="center">
  <img src="./images/Artboard 3.png" alt="Flash Study: Card Wisdom" width="300"/>
</p></p>

Discord Flashcard Bot is a powerful and user-friendly tool designed to help students and learners create, manage, and study flashcards directly within Discord. With features like categorization, study sessions, and easy card management, it's the perfect companion for effective learning.

## Features

- **📚 Create Flashcards**: Easily add new flashcards with questions and answers.
- **🗂️ Categorize**: Organize your flashcards into different categories or subjects.
- **📖 Study Sessions**: Start interactive study sessions with randomized card order.
- **📊 Progress Tracking**: Keep track of your correct and incorrect answers during study sessions.
- **🔍 List and Search**: View your flashcards and search through categories.
- **🗑️ Easy Management**: Delete flashcards you no longer need.

## Commands

- `!add <category> <question> | <answer>`: Add a new flashcard to a category
- `!list [category]`: List all flashcards, optionally filtered by category
- `!categories`: List all your flashcard categories
- `!delete [category]`: Delete a flashcard, optionally from a specific category
- `!study [category]`: Start a study session, optionally for a specific category
- `!commands`: Show all available commands

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/your-username/discord-flashcard-bot.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your Discord bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   DATABASE_NAME=flashcards.db
   ```

4. Run the bot:
   ```
   python bot.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Discord.py library for making bot creation easier.
- Inspired by the need for an effective study tool within Discord.

---

<p align="center">
  Made with ❤️ by rencodesstuff
</p>