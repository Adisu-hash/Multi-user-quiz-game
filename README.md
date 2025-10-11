# 🧠 Multi-User Quiz Game (Python)

A **console-based**, **multi-user** quiz game written in Python. Each player answers randomized multiple-choice questions; the game tracks scores, ranks players from highest to lowest, and reports the **average score** at the end. Built as part of my masters module to demonstrate Python fundamentals, input handling, and simple game logic.

---

## ✨ Features
- Multiple players in one session (sequential turns)
- 10 questions with **4 options** each (A/B/C/D)
- **Randomized question order** per player (`random` module)
- Per-player scoring + final **leaderboard**
- **Average score** across all players
- Simple, interactive console UI

---

## 📦 Project Structure

├── src/
│ main.py # or quiz_game.py – game’s entry point
├── docs/
│ How_to_Play.txt # full “how to play” instructions
├── media/
│ demo_link.txt # link to screen-recorded demo (or demo.mp4 if <25MB)
└── README.md

> If your entry file is named differently (e.g., `quiz_game.py`), update the commands below.

---

## ▶️ How to Run
**Requirements:** Python 3.9+ (no external packages required — uses only the standard library)

```bash
# from the repository root
python src/main.py
# or
python3 src/main.py
You’ll be prompted for a player name, then to answer each question by typing A / B / C / D (uppercase).
At the end, add another player (y) or finish (n) to see the ranked results and average score.
🎮 How to Play (quick guide)

Run the program — you’ll be prompted to enter your name.

For each question, type A, B, C, or D (uppercase) and press Enter.

The game tells you if your answer is correct or incorrect, then moves to the next question.

After 10 questions, you’ll be asked if another player wants to play (y/n).

When everyone is finished, the game prints a sorted scoreboard (highest to lowest) and the average score.

Full instructions: see docs/How_to_Play.txt.
🎥 Demo

A narrated walkthrough of the code and gameplay is available here:
media/demo_link.txt → add your LinkedIn/YouTube/Vimeo URL inside that file.
🧩 Design Notes

Uses Python random to shuffle question order per player

Clean separation of game loop, question bank, and scoring

Input validation for A/B/C/D answers

Clear end-of-game prompts to add players and exit
# Future Improvements

Persist scores to a file/SQLite and show a historical leaderboard

Add timers, difficulty levels, categories, or a question editor

Convert to a web UI (Flask/Streamlit) or GUI (Tkinter)

Add unit tests (e.g., scoring, answer checking, input validation)
📚 License

Personal academic project. You may read and run locally for learning.
👤 Author

Name Adisu Genbez

LinkedIn: LinkedIn URL

Email: email
