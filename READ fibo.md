# Fibonacci 2048 Console Game

A Python implementation of the classic 2048 puzzle game featuring a custom mathematical twist: instead of powers of 2, tile combinations follow the Fibonacci sequence.

## 📌 Project Overview
This project is a fully-featured terminal-based game built from scratch using pure Python. It features state persistence (save/load functionality), custom algorithmic rules for tile merging based on Fibonacci numbers, and dynamic console formatting to ensure a clean layout as numbers grow.

---

## 🚀 Key Features
- **Fibonacci Game Logic:** Tiles merge if they are consecutive numbers in the Fibonacci sequence (or two 1s), offering a unique mathematical puzzle dynamic.
- **Matrix Transformation:** Utilizes matrix transposition to efficiently handle up, down, left, and right slide mechanics without code duplication.
- **State Persistence:** Allows players to save their current board state to a text file (`tablero.txt`) and reload it seamlessly.
- **Dynamic Console Formatting:** Automatically aligns numbers of varying digit lengths to maintain a clean, grid-like visual presentation in the terminal.
- **Intelligent Move Validation:** Detects valid moves to trigger random tile generation or trigger game-over/victory states (reaching 2584).

---

## 🛠️ Tech Stack
- **Python 3.11+**
- **Standard Libraries:** `random`, `math` (Zero external dependencies required!).

---

## 📦 Project Structure
```text
├── practica_2048.py    # Main game script, logic, and state management
└── tablero.txt         # Auto-generated save file for game persistence