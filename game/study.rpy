label study:

    hide leo
    hide alistair
    hide cassandra
    hide mirna
    show bg library

    menu :
        "What will I study this morning?"
        "Foreign affairs":
            $ foreignknowledge += 1
            #jump study1
        "Internal affairs":
            $ internalknowledge += 1
            #jump study1
        "Military techniques":
            $ militaryknowledge += 1
            #jump study1
        "Science":
            $ scienceknowledge +=1
            #jump study1
        "Religion":
            $ religiousknowledge += 1
            #jump study1
        "Other civilizations":
            $ elfknowledge += 1

    return
