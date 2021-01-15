rounds = int(input("No of rounds to play "))


bonusCheck=[]
bonusplayer=[]


scoresPattern={"A":5,"B":4,"C":3,"D":2,"E":1,"F":0}



teamsList={"Gyrhuna":[{"Jaons Dain":0},{"Susu":0}],
       "Achni":[{"Milog":0},{"Tianlong":0}],
       "Bathar":[{"Pakhangba":0},{"Poubi Lai Paphal":0}]}

teamno=len (teamsList)
bonusTeam={}
teamsScore={}
def winnerFunt(teamsScore):
    return [key  for (key, value) in teamsScore.items() if value == max(teamsScore.values())]


for team in teamsList:
    bonusTeam[team]=0
    teamsScore[team]=0
players=0
for i in teamsList:
    players+=len(teamsList[i])


playerscores={}

for r in range(rounds):
    for team in teamsList:

        bonusCheck=[]
        bonusplayer=[]
        teamsScore[team]=0
        for player in teamsList[team]:
            key, value = list(player.items())[0]
            temp=0
            playerscore=(input("Enter the score for " +str(key)+str(" of team ")+team+" "))
            if playerscore not in (["A","B","C","D","E","F"]):
                print("Please select the score from A-F")
                exit(0)
            bonusCheck.append(playerscore)
            bonusplayer.append(key)
            preScore=key
            if preScore  not in  playerscores:

                playerscores[preScore]=scoresPattern[playerscore]
            else:
                playerscores[preScore]+=scoresPattern[playerscore]
                temp=playerscores[preScore]
            teamsScore[team]+=playerscores[preScore]

        if(len(set(bonusCheck))==1):
            bonusTeam[team]+=2
        teamsScore[team]+=bonusTeam[team]

    scoresPattern={key:value+1 if(key!="F") else value  for key,value in(scoresPattern.items()) }

    print(playerscores)
    print(bonusTeam)
    print(teamsScore)
    print("Next Round.")

key=winnerFunt(teamsScore)[0]
print("Game over. {} won!!!".format(key))
