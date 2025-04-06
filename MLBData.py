def main():
  myFile = open("MLB_Pitching.csv", 'r')
  team_data = []

  for line in myFile:
    info = line.split(",")
    name = info[0]
    runs_allowed = info[3]
    wins = info[4]
    losses = info[5]
    era = info[7]

    team_data.append([name, "" ,runs_allowed, wins, losses, era])
  
  myFile.close()

  hitting = open("MLB_Hitting.csv", 'r')

  teamCount = 0
  for line in hitting:
    info = line.split(",")
    runs_scored = info[3]
    #print(runs_scored)

    team_data[teamCount][1] = runs_scored
    #print(team_data[teamCount])

    teamCount = teamCount + 1

  hitting.close()

  outFile = open("mlb_output.csv", 'w')

  for line in team_data:
    output = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "\n"
    outFile.write(output)

  outFile.close()

if __name__ == '__main__':
  main()