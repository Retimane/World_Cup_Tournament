# World Cup Tournament Simulator

A console program that simulates the 2022 FIFA World Cup format: 32 teams in 8 groups of 4, followed by the Round of 16, quarter-finals, semi-finals and final. You enter every match score yourself and the program works out the standings, who advances, and the champion.

## Requirements

Python 3.7 or newer. No external packages.

## Usage

```bash
python world_cup_tournament.py          # type in every score
python world_cup_tournament.py --auto   # random scores, for a quick demo
```

Scores are entered as two numbers separated by a space, e.g. `2 1` means the first team scored 2 and the second scored 1. Invalid input is rejected and you are asked again.

## Rules implemented

- **Group stage:** every team plays the other three once. 3 points for a win, 1 for a draw.
- **Group tiebreakers:** points, then goal difference, then goals scored, then team name. Head-to-head and fair-play tiebreakers are not implemented.
- **Knockouts:** the bracket follows the real 2022 layout (e.g. winner of 1A v 2B meets winner of 1C v 2D in the quarter-finals). A drawn match goes to a penalty shootout, where you enter the shootout score (it can't be a tie).

## Project layout

| File | Purpose |
| --- | --- |
| `world_cup_tournament.py` | The simulator |
| `Presentation.pptx` | Project presentation |

## Authors

Author: Retimane. Refactored from the original "Power Rangers" group project by Deenen Manikion, Anant Manoj Dwivedi, Daniil Rudkovskyi, Karam Mu Ness Qasem Obeidat, Luigi Moretti and Philip Effa.
