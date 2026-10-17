"""World Cup tournament simulator (2022 format: 32 teams, 8 groups, knockouts).

Run interactively and type in every score:
    python world_cup_tournament.py

Or let the computer play random scores (handy for testing):
    python world_cup_tournament.py --auto

Author: Retimane.
Refactored from the original "Power Rangers" group project by Deenen Manikion,
Anant Manoj Dwivedi, Daniil Rudkovskyi, Karam Mu Ness Qasem Obeidat,
Luigi Moretti and Philip Effa.
"""

import random
import sys
from dataclasses import dataclass
from itertools import combinations

GROUPS = {
    "A": ["Netherlands", "Senegal", "Ecuador", "Qatar"],
    "B": ["England", "USA", "Iran", "Wales"],
    "C": ["Argentina", "Poland", "Mexico", "Saudi Arabia"],
    "D": ["France", "Australia", "Tunisia", "Denmark"],
    "E": ["Japan", "Spain", "Germany", "Costa Rica"],
    "F": ["Morocco", "Croatia", "Belgium", "Canada"],
    "G": ["Brazil", "Switzerland", "Cameroon", "Serbia"],
    "H": ["Portugal", "South Korea", "Uruguay", "Ghana"],
}

# Round of 16 in FIFA bracket order (matches 49, 50, 53, 54, 51, 52, 55, 56).
# Pairing neighbours in each round then reproduces the real 2022 bracket.
# Each entry is (group, finishing position) with position 0 = winner, 1 = runner-up.
ROUND_OF_16 = [
    (("A", 0), ("B", 1)),
    (("C", 0), ("D", 1)),
    (("E", 0), ("F", 1)),
    (("G", 0), ("H", 1)),
    (("D", 0), ("C", 1)),
    (("B", 0), ("A", 1)),
    (("F", 0), ("E", 1)),
    (("H", 0), ("G", 1)),
]

ROUND_NAMES = {16: "Round of 16", 8: "Quarter-finals", 4: "Semi-finals", 2: "Final"}


# --------------------------------------------------------------------------
# Input helpers
# --------------------------------------------------------------------------

AUTO_MODE = "--auto" in sys.argv


def read_scores(team1, team2, allow_draw=True):
    """Ask for 'score1 score2' and keep asking until the input is valid."""
    if AUTO_MODE:
        while True:
            s1, s2 = random.randint(0, 4), random.randint(0, 4)
            if allow_draw or s1 != s2:
                print(f"  {team1} {s1} - {s2} {team2}")
                return s1, s2

    while True:
        raw = input(f"  {team1} vs {team2} (two scores, e.g. '2 1'): ").split()
        try:
            s1, s2 = (int(x) for x in raw)
        except ValueError:
            print("  Please enter exactly two whole numbers.")
            continue
        if s1 < 0 or s2 < 0:
            print("  Scores can't be negative.")
        elif not allow_draw and s1 == s2:
            print("  Someone has to win the shootout - scores can't be equal.")
        else:
            return s1, s2


# --------------------------------------------------------------------------
# Domain classes
# --------------------------------------------------------------------------

@dataclass
class Team:
    name: str
    wins: int = 0
    draws: int = 0
    losses: int = 0
    goals_for: int = 0
    goals_against: int = 0

    @property
    def points(self):
        return 3 * self.wins + self.draws

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against

    def record_result(self, scored, conceded):
        self.goals_for += scored
        self.goals_against += conceded
        if scored > conceded:
            self.wins += 1
        elif scored == conceded:
            self.draws += 1
        else:
            self.losses += 1

    def __str__(self):
        return self.name


class Group:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams

    def play_all_matches(self):
        for team1, team2 in combinations(self.teams, 2):
            s1, s2 = read_scores(team1, team2)
            team1.record_result(s1, s2)
            team2.record_result(s2, s1)

    def standings(self):
        """Points, then goal difference, then goals scored, then name.

        (Head-to-head and fair-play tiebreakers are not implemented.)
        """
        return sorted(
            self.teams,
            key=lambda t: (-t.points, -t.goal_difference, -t.goals_for, t.name),
        )

    def qualifiers(self):
        return self.standings()[:2]

    def print_table(self):
        print(f"Group {self.name}")
        print(f"  {'Team':<14}{'P':>3}{'W':>3}{'D':>3}{'L':>3}{'GF':>4}{'GA':>4}{'GD':>4}{'Pts':>5}")
        for t in self.standings():
            played = t.wins + t.draws + t.losses
            print(
                f"  {t.name:<14}{played:>3}{t.wins:>3}{t.draws:>3}{t.losses:>3}"
                f"{t.goals_for:>4}{t.goals_against:>4}{t.goal_difference:>4}{t.points:>5}"
            )


def play_knockout_match(team1, team2):
    """Play one knockout match and return the winner (penalties if drawn)."""
    s1, s2 = read_scores(team1, team2)
    if s1 != s2:
        return team1 if s1 > s2 else team2
    print("  Draw! Penalty shootout:")
    p1, p2 = read_scores(team1, team2, allow_draw=False)
    return team1 if p1 > p2 else team2


def play_round(pairings):
    """Play a list of (team1, team2) matches and return the winners in order."""
    return [play_knockout_match(a, b) for a, b in pairings]


def pair_up(teams):
    return list(zip(teams[::2], teams[1::2]))


# --------------------------------------------------------------------------
# Tournament flow
# --------------------------------------------------------------------------

def main():
    groups = {
        letter: Group(letter, [Team(name) for name in names])
        for letter, names in GROUPS.items()
    }

    print("=== Group stage ===")
    for group in groups.values():
        print(f"\nGroup {group.name}: {', '.join(t.name for t in group.teams)}")
        group.play_all_matches()

    print("\n=== Final group tables ===")
    for group in groups.values():
        group.print_table()
        print()

    # Build the Round of 16 from the group results.
    pairings = [
        (groups[g1].qualifiers()[p1], groups[g2].qualifiers()[p2])
        for (g1, p1), (g2, p2) in ROUND_OF_16
    ]

    winners = None
    for teams_left in (16, 8, 4, 2):
        print(f"\n=== {ROUND_NAMES[teams_left]} ===")
        winners = play_round(pairings)
        print("Advancing:" if teams_left > 2 else "Champion:",
              ", ".join(str(w) for w in winners))
        pairings = pair_up(winners)

    print(f"\nThe World Cup winner is: {winners[0]}!")


if __name__ == "__main__":
    main()
