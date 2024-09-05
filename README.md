# Welcome to Aidandle, Mobile Edition!

With *Aidandle, Mobile Edition* you can play my fantastic game on your own computer terminal! Let the game proctor enter the answer and start the game, and you may begin! More functionality will be available like personal stats tracking and automatic
word updates. 

## Requirements

- Python 3
- git
- bash, zsh, or unix terminal
- Willingness to play this game

## Installation

In your terminal clone the repository,

```
git clone https://github.com/berres2002/aidandle.git
```

## Gameplay

To start the game, a word needs to be input (ask game proctor), then you can type,

```
python game.py
```

The rules of wordle apply, six guesses to guess a word. Colors represent the guess,

- White, incorrect letter, not in the answer word
- Yellow, correct letter, found in the answer word but not in the correct placement
- Green, correct letter placement, found in the answer word and in the correct placement to the answer

The goal is to have all the letters become green, with the correct guess, within six tries.

**Good Luck!**

