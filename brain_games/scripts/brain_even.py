#!/usr/bin/env python3

from brain_games.games import even_game
from brain_games.games import start
from brain_games.games import greeting


def main():
    greeting.greet('Answer "yes" if number even otherwise answer "no".')
    start.play(even_game.play_even)


if __name__ == "__main__":
    main()
