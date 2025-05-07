# ITS_212_Final
ITS 212 Final Project
# Dodger Game with Power-Up Orbs

This is a Python-based arcade-style game where players dodge falling baddies and collect goodies and power-up orbs. The game uses object-oriented programming with the Pygame and Pygwidgets libraries.

## Features

- Mouse-controlled player movement
- Baddies fall from the top – avoid them
- Goodies fall too – collect them for points
- Power-Up Orbs:
  - Speed Orb: Temporarily increases player speed and slows down baddies
  - Shield Orb: Grants a visible blue shield that prevents death on collision once
  - Slow-Motion Orb: Temporarily slows down all baddies
- Score tracking and high score system
- Clean UI with buttons and background music

## Controls

- Move: Move the mouse to control the player
- Click: Use UI buttons to start a new game, quit, or view high scores

## Requirements

- Python 3.10+
- `pygame-ce`
- `pygwidgets`
- `pyghelpers`

Install dependencies:
```bash
pip install pygame-ce pygwidgets pyghelpers
