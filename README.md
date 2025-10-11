# 🧠 Multi-User Quiz Game (Python)

A **console-based**, **multi-user** quiz game written in Python. Each player answers randomized multiple-choice questions; the game tracks scores, ranks players from highest to lowest, and reports the **average score** at the end. Built as part of the CETM73 module to demonstrate Python fundamentals, input handling, and simple game logic.

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

🕹️ Gameplay Rules

10 multiple-choice questions per player

Answer with A, B, C, or D

Correct answer = +1 point

Scores are shown immediately after each answer (optional) and summarized at the end

Final output:

Leaderboard: highest → lowest

Average score across all players

For detailed instructions, see docs/How_to_Play.txt.
.

🎥 Demo

A narrated walkthrough of the code and gameplay is available here:
media/demo_link.txt → add your LinkedIn/YouTube/Vimeo URL inside that file.
🧩 Design Notes

Uses Python random to shuffle question order per player

Clean separation of game loop, question bank, and scoring

Input validation for A/B/C/D answers

Clear end-of-game prompts to add players and exit
Future Improvements

Persist scores to a file/SQLite and show a historical leaderboard

Add timers, difficulty levels, categories, or a question editor

Convert to a web UI (Flask/Streamlit) or GUI (Tkinter)

Add unit tests (e.g., scoring, answer checking, input validation)
📚 License

Personal academic project. You may read and run locally for learning.
👤 Author

Your Name

LinkedIn: add your LinkedIn URL

Email: add your email

4) Scroll down and **Commit changes → Commit directly to the main branch → Commit**.

Please reply **“GitHub Step 4 done”** once you’ve updated the README.  
Then we’ll do **Step 5** (make repo public + pin) and **Step 6** (update your LinkedIn project to link to this repo).
