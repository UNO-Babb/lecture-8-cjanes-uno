import csv
#I was getting frustrated with the double quotes so I looked into the csv module.
#This means that the structure doesn't follow the myFile = open(ufo_sightings.csv)
#Hope that was okay. Sourced reference: http://docs.python.org/3/library/csv.html#csv.reader

def main():
    target_state = "DC"
    sightings_by_state = {}

    with open("ufo_sightings.csv", 'r', newline='', encoding='utf-8') as file:
        ufo_sightings_csv = csv.reader(file)
        next(ufo_sightings_csv)  #Supposed to skip the header row; helpful to mask/hide for troubleshooting

        print("UFO Sightings in", target_state + ":") #Meant to provide descriptor for this section
        for row in ufo_sightings_csv:
            if len(row) < 9:
                continue  #Supposed to skip bad rows or rows with missing information

            state = row[1].upper() #Preserve the uppercase use of state abbreviations
            shape = row[3]
            year = row[8]

            #To count sightings by state
            if state in sightings_by_state:
                sightings_by_state[state] = sightings_by_state[state] + 1
            else:
                sightings_by_state[state] = 1

            #To print individual NE sightings
            if state == target_state:
                print("There was a", shape, "shaped UFO sighted/seen in", state, "during", year + ".")

    #To print total sightings per state
    print("\nUFO Sightings by State:") #Figured out this should be printed on a new/separate line.
    for state, count in sightings_by_state.items():
        print(state, ":", count)

if __name__ == '__main__':
    main()