# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 20:25:56 2023

@author: Deenen Manikion, Anant Manoj Dwivedi, Daniil Rudkovskyi, Karam Mu Ness Qasem Obeidat, Luigi Moretti, Philip Effa
"""        
# Create the class for team overview 
class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.points = 0

#Print out the name of a Team
    def __str__(self):
        return self.name
    
#Create the groups for the Group Stage
class Group:
    def __init__(self, name):
        self.name = name
        self.group = []

# Allow to add the teams to the Groups
    def add_team(self, team):
        self.group.append(team)

# Print the teams
    def print_teams(self):
        liste1 = []
        for team in self.group:
            liste1.append(team.name)
        return liste1

# Play the match one by one by taking the two team and asking for the scores            
    def play_match(self, team1, team2):
        score1, score2 = map(int, input("Enter the score of " + str(team1) + " vs " + str(team2) + " separated by a space: ").split())
        team1.points += 3 if score1 > score2 else (1 if score1 == score2 else 0)
        team2.points += 3 if score2 > score1 else (1 if score1 == score2 else 0)
        
        team1.wins += 1 if score1 > score2 else 0
        team2.wins += 1 if score2 > score1 else 0
        
        team1.losses += 1 if score1 < score2 else 0
        team2.losses += 1 if score2 < score1 else 0
        
        team1.draws += 1 if score1 == score2 else 0
        team2.draws += 1 if score2 == score1 else 0

# Allow to sort the groups by the amount of points, wins, losses and Draws
    def sort_teams(self):
        self.group.sort(key=lambda x: (-x.points, -x.wins, x.name))
        self.group.pop()
        self.group.pop()

# Allow to play all the matches in a group directly without repeating them manually
    def play_all_matches(self):
        for i in range(len(self.group)):
            for j in range(i+1, len(self.group)):
                team1 = self.group[i]
                team2 = self.group[j]
                self.play_match(team1, team2)
    
# Initializing the Round of 16 through the class
class Round16:
    def __init__(self):
        self.matches = []
# Allow to add the teams to a list so we know which team playing who
    def add_match(self, team1, team2):
        self.matches.append(team1)
        self.matches.append(team2)
# Allow to play the matches and ask for the score of team1 and team2 and automatically eliminate the who lost from the list
    def play_match(self):
        
        score1, score2 = map(int, input("Enter the score of " + self.matches[0] + " vs " + self.matches[1] + " separated by a space: ").split())
        
        if score1 > score2:
            self.matches.pop(1)
        else:  
            self.matches.pop(0)
# Allow to print the two opposite teams in a list
    def print_teams(self):
        liste1 = []
        for team in self.matches:
            liste1.append(team)
        return liste1

# Initializing the Quarter Final through the class
class QuarterFinal: 
    def __init__(self):
        self.matches = []
# Allow to add the teams to a list so we know which team playing who
    def add_match(self, team1, team2):
        self.matches.append(team1)
        self.matches.append(team2)
# Allow to play the matches and ask for the score of team1 and team2 and automatically take out the team who lost
    def play_match(self):
        
        score1, score2 = map(int, input("Enter the score of " + self.matches[0] + " vs " + self.matches[1] + " separated by a space: ").split())
        
        if score1 > score2:
            self.matches.pop(1)
        else:  
            self.matches.pop(0)
# Initializing the Semi Final through the class
class SemiFinal:
    def __init__(self):
        self.matches = []
# Allow to add the teams to a list so we knoe which team playing who
    def add_match(self, team1, team2):
        self.matches.append(team1)
        self.matches.append(team2)
# Allow to play the matches and ask for the score of team1 and team2 and automatically take out the team who lost
    def play_match(self):
        score1, score2 = map(int, input("Enter the score of " + self.matches[0] + " vs " + self.matches[1] + " separated by a space: ").split())
        
        if score1 > score2:
            self.matches.pop(1)
        else:  
            self.matches.pop(0)
            
# Initializing the Final through the Final
class Final:
    def __init__(self):
        self.matches = []
# Allow to add the team to a list so we know which teams are in the final
    def add_match(self, team1, team2):
        self.matches.append(team1)
        self.matches.append(team2)
# Allow to play the match and ask for the score of team1 and team2 and automatically take the team who lost
    def play_match(self):
        score1, score2 = map(int, input("Enter the score of " + self.matches[0] + " vs " + self.matches[1] + " separated by a space: ").split())
        
        if score1 > score2:
            self.matches.pop(1)
        else:  
            self.matches.pop(0)









#teams=[]
#for _ in range(32):
#    team_name = input("Enter the name of the team: ")
#    team = Team(team_name)
#    teams.append(team)
#    locals()[team_name] = team

#Create the teams 32
Argentina = Team("Argentina")
Netherlands = Team("Netherlands")
Senegal = Team("Senegal")
Ecuador = Team("Ecuador")
Qatar = Team("Qatar")
England = Team("England")
USA = Team("USA")
Iran = Team("Iran")
Wales  = Team("Wales")
Poland = Team("Poland")
Mexico = Team("Mexico")
Saudi_Arabia = Team("Saudi Arabia")
France = Team("France")
Australia = Team("Australia")
Tunisia = Team("Tunisia")
Denmark = Team("Denmark")
Japan = Team("Japan")
Spain = Team("Spain")
Germany = Team("Germany")
Costa_rica = Team("Costa Rica")
Morocco = Team("Morocco")
Croatia = Team("Croatia")
Belgium = Team("Belgium")
Canada = Team("Canada")
Brazil = Team("Brazil")
Switzerland = Team("Switzerland")
Cameroon = Team("Cameroon")
Serbia = Team("Serbia")
Portugal = Team("Portugal")
South_Korea = Team("South Korea")
Uruguay = Team("Uruguay")
Ghana = Team("Ghana")

#Create the Groups (8)
GroupA = Group("A")
GroupB = Group("B")
GroupC = Group("C")
GroupD = Group("D")
GroupE = Group("E")
GroupF = Group("F")
GroupG = Group("G")
GroupH = Group("H")

#Put the Teams inside the groups
GroupA.add_team(Netherlands)
GroupA.add_team(Senegal)
GroupA.add_team(Ecuador)
GroupA.add_team(Qatar)

GroupB.add_team(England)
GroupB.add_team(USA)
GroupB.add_team(Iran)
GroupB.add_team(Wales)

GroupC.add_team(Argentina)
GroupC.add_team(Poland)
GroupC.add_team(Mexico)
GroupC.add_team(Saudi_Arabia)

GroupD.add_team(France)
GroupD.add_team(Australia)
GroupD.add_team(Tunisia)
GroupD.add_team(Denmark)

GroupE.add_team(Japan)
GroupE.add_team(Spain)
GroupE.add_team(Germany)
GroupE.add_team(Costa_rica)

GroupF.add_team(Morocco)
GroupF.add_team(Croatia)
GroupF.add_team(Belgium)
GroupF.add_team(Canada)

GroupG.add_team(Brazil)
GroupG.add_team(Switzerland)
GroupG.add_team(Cameroon)
GroupG.add_team(Serbia)

GroupH.add_team(Portugal)
GroupH.add_team(South_Korea)
GroupH.add_team(Uruguay)
GroupH.add_team(Ghana)



# print the current groups without any matches
print("All the teams from the Stage Group:")
print("                          ")
print(GroupA.print_teams())
print(GroupB.print_teams())
print(GroupC.print_teams())
print(GroupD.print_teams())
print(GroupE.print_teams())
print(GroupF.print_teams())
print(GroupG.print_teams())
print(GroupH.print_teams())

# For more space in the console
print("                          ")
print("                          ")
print("                          ")



# Play all the match in each group
print("Enter the Scores for all the matches in the Stage Groups:")
print("                          ")
GroupA.play_all_matches()
GroupB.play_all_matches()
GroupC.play_all_matches()
GroupD.play_all_matches()
GroupE.play_all_matches()
GroupF.play_all_matches()
GroupG.play_all_matches()
GroupH.play_all_matches()


# sort the match and eliminate automatically the two unecessary teams
GroupA.sort_teams()
GroupB.sort_teams()
GroupC.sort_teams()
GroupD.sort_teams()
GroupE.sort_teams()
GroupF.sort_teams()
GroupG.sort_teams()
GroupH.sort_teams()

# For more space in the console
print("                          ")
print("                          ")
print("                          ")

# Print out all the teams send to the next stage Round of 16
print("Team send to the round of 16: ")
print(GroupA.print_teams())
print(GroupB.print_teams())
print(GroupC.print_teams())
print(GroupD.print_teams())
print(GroupE.print_teams())
print(GroupF.print_teams())
print(GroupG.print_teams())
print(GroupH.print_teams())

# For more space in the console
print("                          ")
print("                          ")
print("                          ")

#Create the different groups for the Round of 16
one = Round16()
two = Round16()
three =Round16()
four=Round16()
five=Round16()
six=Round16()
seven=Round16()
eight=Round16()

# Add the two teams inside the groups
one.add_match(str(GroupA.group[0]), str(GroupB.group[1]))
two.add_match(str(GroupA.group[1]), str(GroupB.group[0]))
three.add_match(str(GroupC.group[0]), str(GroupD.group[1]))
four.add_match(str(GroupC.group[1]), str(GroupD.group[0]))
five.add_match(str(GroupE.group[0]), str(GroupF.group[1]))
six.add_match(str(GroupE.group[1]), str(GroupF.group[0]))
seven.add_match(str(GroupG.group[0]), str(GroupH.group[1]))
eight.add_match(str(GroupG.group[1]), str(GroupH.group[0]))

# Play the matches in each groups and eliminating automatically the lossing team
print("Enter the scores for the Round of 16:")
print("                    ")
one.play_match()
two.play_match()
three.play_match()
four.play_match()
five.play_match()
six.play_match()
seven.play_match()
eight.play_match()

# For more space in the console
print("                          ")
print("                          ")
print("                          ")



# Print the winning teams from the Round of 
print("The winning Teams from Round of 16: ")
print(one.matches[0])
print(two.matches[0])
print(three.matches[0])
print(four.matches[0])
print(five.matches[0])
print(six.matches[0])
print(seven.matches[0])
print(eight.matches[0])

# For more space in the console
print("                          ")
print("                          ")
print("                          ")


# Create the groups for the Quarter Final
Quarter_1 = QuarterFinal()
Quarter_2 =  QuarterFinal()
Quarter_3 =  QuarterFinal()
Quarter_4 = QuarterFinal()

# Add the two respective teams inside the groups
Quarter_1.add_match(one.matches[0], two.matches[0])
Quarter_2.add_match(three.matches[0], four.matches[0])
Quarter_3.add_match(five.matches[0], six.matches[0])
Quarter_4.add_match(seven.matches[0], eight.matches[0])

# Play the match in each group and take out automatically the losing team
print("Enter the scores for the Quarter Final:")
print("                          ")
Quarter_1.play_match()
Quarter_2.play_match()
Quarter_3.play_match()
Quarter_4.play_match()

#For more space inside the console
print("                          ")
print("                          ")
print("                          ")

#Print the winning team from the Quarter Final
print("The winning Teams from the Quarter Final:")
print(Quarter_1.matches[0])
print(Quarter_2.matches[0])
print(Quarter_3.matches[0])
print(Quarter_4.matches[0])

# For more space in the console
print("                          ")
print("                          ")
print("                          ")

#Create the groups for the SemiFinal, the list
Semi_1 = SemiFinal()
Semi_2 = SemiFinal()

#Add the teams inside each respective group
Semi_1.add_match(Quarter_1.matches[0], Quarter_2.matches[0])
Semi_2.add_match(Quarter_3.matches[0], Quarter_4.matches[0])

#Play all the match and eliminate automatically the losing team
print("Enter the scores for the Semi Final:")
print("                          ")
Semi_1.play_match()
Semi_2.play_match()

# For more space inside the console
print("                          ")
print("                          ")
print("                          ")



# Print the winning team from the Semi Final
print("The winning Teams from the Semi Final:")
print(Semi_1.matches[0])
print(Semi_2.matches[0])

# For more space in the console
print("                          ")
print("                          ")
print("                          ")


# Create the group for the Final, the list
Final = Final()

# Add the winning team from semi final to final
Final.add_match(Semi_1.matches[0], Semi_2.matches[0])

# play the match and automatically eliminate the losing team
print("Enter the scores for the Final:")
print("                          ")
Final.play_match()

# For more space inside the console
print("                          ")

# Print out the world cup winner
print("The world cup winner is: ",Final.matches[0])
