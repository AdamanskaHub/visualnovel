
# import pygame
# from pygame.locals import *
#
# pygame.init()
# thebg = pygame.image.load(bg club)
# thebg = pygame.transform.scale(thebg, (1920, 1080))
###### CHARACTERS ######
define m = Character("[MainCharacter]")
define a = Character("Alistair")
define l = Character("Leo")
define c = Character("Cassandra")
define mi = Character("Mirna")
define rm = Character("The Royal Messenger")
define d = Character("Duchess of ")
#define med = Character("Rexxar")
define someelf = Character("Some elf")
define merchant = Character("Merchants Guild Representant")
define noble = Character("Nobles Guild Representant")
define elf = Character("Elven Representant")
define warrior = Character("Warriors Guild Representant")
define religious = Character("Priestress of the Order")
define med = Character("Alchemists Guild Representant")

###### IMAGES ######
# image main = "main.jpg"
image bg room = "bg room.jpg"
image bg throne ="bg throne.jpg"
image bg house ="images/bg house.jpg"
image bg library ="bg library.jpg"
image alistair normal ="alistair normal.png"
image alistair angry ="alistair angry.png"
image mirna normal ="mirna normal.png"
image mirna shy ="mirna shy.png"
image mirna smile ="mirna smile.png"

label start:

    ###### MOVEMENTS ######
    transform righto:
        xalign 0.65
        yalign 1.0
    transform lefto:
        xalign 0.20
        yalign 1.0

    ###### BASE VALUES ######
    default approval = 60
    default gender = ""
    default genderf = False
    default paragon = 0
    default renegade = 0
    default randomness = 0
    ##### Chosen #####
    default cassandraChosen = False
    default alistairChosen = False
    default leoChosen = False
    default mirnaChosen = False
    default diseaseCause = False #when false = cure
    ### people's points
    default alistairpoints = 0
    default mirnapoints = 0
    default cassandrapoints = 0
    default leopoints = 5
    default elfpoints = 0
    default merchantspoints = 0
    default noblespoints = 0
    default warriorspoints = 0
    default medspoints = 0
    default religiouspoints = 0
    ### knowledge
    default militaryknowledge = 0
    default internalknowledge = 0
    default foreignknowledge = 0
    default religiousknowledge = 0
    default scienceknowledge = 0
    default elfknowledge = 0
    ### dates
    default leodatenum = 0
    default mirnadatenum = 0
    default cassandradatenum = 0
    default alistairdatenum = 0
    ##### MATHS #####
    default datecounter = 0
    #default mirnapercent = mirnapoints*10/12
    #default alistairpercent = alistairpoints*10/12
    #default cassandrapercent = cassandrapoints*10/12
    #default leopercent = leopoints*10/12
    ##### OTHER ######
    default increaseArmy = False
    default mercenaries = False
    default dukepayfast = False
    default scandale1posleo = False
    default gavetwomonths = False
    default getrecordstraight = True
    default trainingarmy = False
    default armystarving = False
    default draft = False
    default spiesSent = False
    default patrolsSent = False
    default protestInfo = False
    default protestInfoSuccess = False
    default protestInfoAlistair = False
    default protestInfoMirna = False
    default protestInfoLeo = False
    default protestInfoCassandra = False

    default choseDemonize = False
    default choseUnity = False
    default unitySuccess = False
    default demonizeSuccess = False
    default choseLetter = False
    default choseWitness = False
    default fakeLetterSuccess = False
    default fakeWitnessSuccess = False

    default choseWeaponry = False
    default choseAlliance = False
    default weaponrySuccess = False
    default allianceSuccess = False
    default choseWhataboutism = False
    default choseFakenews = False
    default whataboutsimSuccess = False
    default fakenewsSuccess = False



    #=======================================================#
    #===================###### START ######=================#
    scene bg house
    pause 1

    "Knock knock"
    "Who on earth could this be waking me up at such an ungodly hour?!"

    show alistair normal

    "???" "My apologies for barging into your house so early."
    "???" "Are you related to Sir Eidola?"

    menu:
        "Yes, I'm his son.":
            jump genderdone

        "Yes, I'm his daughter.":
            jump genderf


    label genderf:
        $ gender = "female"
        jump genderdone

    label genderdone:
    #$ if _preferences.language == "spanish" and gender == "female":
    #$ renpy.change_language("spanish_f")

    #$ if _preferences.language == "english" and gender == "female":
    #$ renpy.change_language("english_f")

    "May I ask for your name Sir ?"

    "???" "I am Alistair Halestorm, our ruler's right arm man."

    "You" "My name is..."

    python:
        MainCharacter = renpy.input("What is your name?")
        MainCharacter = MainCharacter.strip()

        if not MainCharacter:
            MainCharacter = "Rowan"

    "[MainCharacter]."

    a "It is a pleasure to meet you [MainCharacter]. I look forward to knowing more about you."

    a "You are the next person in line to the throne and I came to bring you back to the castle. Your reign, may it be long and just, starts now."

    m "..."
    m "What?"

    a "As I said, you are the next person in line..."
    with hpunch
    m "Stop stop right there!"
    m "There must be a terrible mistake! What about my cousin Red?"

    a "Oh... You have not heard? She passed away. Hunting accident."

    m "...What about my cousin Raj?"

    a "He joined the Order."

    m "To not inherit the throne probably! What about Genma?"

    a "She left the kingdom."

    m "Fled the kingdom you mean."

    a "Did you plan to get out of it as well?"

    menu:
        "(lie) No no. I am ready.":
            jump firstquestionlie

        "Definitely, but I thought I had more time":
            jump firstquestiontruth

    label firstquestionlie:
        a "I hope you are for both our sakes."
        $ alistairpoints += 1
        jump firstquestiondone
    label firstquestiontruth:
        a "That's honest."
        $ alistairpoints += 2
        jump firstquestiondone
    label firstquestiondone:
        a "No need to grab anything, a footman will come later. Let us make haste."

    ######## CASTLE #######

    hide alistair with easeoutleft
    show bg throne with dissolve(1)

    "I was supposed to have a nice day out today and here I am. In the castle, as the ruler of the kingdom!"
    "Duty to rule should never have come down as far as me. I'm a distant cousin."

    show alistair normal with dissolve

    a "[MainCharacter], let me explain a few things to you."
    a "As you know, once a ruler passes away, whoever is next in line must rise to the throne."
    m "Unless they fled, joined the Order or had a tragic hunting accident."
    a "Indeed."
    a "You probably know as well that the newly appointed ruler has 3 months to prove their worth."
    m "If they fail they get beheaded. No surprise all my cousins found a way to get out of it!"
    m "Can't I just be exiled if I fail?"
    m "Beheading seems a bit..."
    menu:
        "Radical":
            jump beheading
        "Completely insane":
            $ alistairpoints += -1
            jump beheading
    label beheading:
        a "It is necessary. The ruler during those 3 months wields a great power and has access to critical information."
    a "We do not want it to fall in the hands of our enemies."
    pause 1
    a "I know this is a lot all of sudden, but I feel that you have what it takes."
    m "I hope so cause I'd rather not have my head rolling in 3 months!"

    show alistair normal at righto with moveinright
    show mirna normal at lefto with moveinleft

    "Woman" "Alistair, you called me?"
    a "[MainCharacter], let me introduce you to Mirna. She is your advisor on all matters of magic, faith and science."
    mi "It's a pleasure to meet you."
    m "The pleasure is mine."
    menu:
        "I hope you can help me to build better relationships with the Order.":
            $ mirnapoints += -1
            jump mirnaintro
        "I hope you can help me to learn more about science.":
            $ mirnapoints += 1
            jump mirnaintro
    label mirnaintro:
        mi "I'll be happy to help."
        m "Thanks, I'll take all the help I can to keep my head on my shoulders."
        a "I need to go and attend to a meeting with the nobles. I will spare you that on your first day."
        mi "Go ahead I'll explain the state of the kingdom."
        a "Thank you."
        hide alistair with dissolve(0.5)
        show mirna normal center
    menu:
        "Thank you for not abandonning me.":
            jump mirnastay
        "Are you trying to get out of that meeting?":
            $ mirnapoints += 1
            jump mirnaescape

    label mirnaescape:
        show mirna shy
        mi "Hahaha... Well yes"
        m "It's ok, you're helping me and Alistair seems big enough to handle a couple of nobles."
        show mirna normal
        mi "I was never a big fan of nobles."
        jump mirnastay

    label mirnastay:
        mi "Anyway, let me tell you more about the current state of the kingdom."
        mi "On our West border the kingdom of XXX is going through a civil war and we don't know yet how this is going to evolve."
        mi "I have also heard rumours of a strange disease in a nearby village."
        mi "Should I spend a few days there and try to gather information?"
        "If she goes she will be unavailable for a couple of days and what if she catches the disease!"
        "On the other hand, she might gather critical information."
        $ gonetothevillage_flag = False
    menu:
        "Alright, go there and be careful.":
            jump mirnagoes
        "Let's see how it develops and I will need those first days.":
            jump mirnadoesntgo
    label mirnagoes:
        $ gonetothevillage_flag = True
        show mirna smile
        mi "Thank you, I'm looking forward to what I will learn."
        $ mirnapoints += 1
        mi "I will go now and I should be back soon."
        m "Be careful."
        hide mirna
        jump mirnadone
    label mirnadoesntgo:
        show mirna sad
        mi "Well... I'll keep an ear out for any news."
        mi "Now, if you'd excuse me, I need to go to the royal library."
        m "Thank you for your help."
        hide mirna
        jump mirnadone
    label mirnadone:
        "Ok now what?"
        "I should have asked Mirna where my room is from here."
    menu:
        "I think I came from the left.":
            jump left
        "No I came from the right... I think.":
            jump right
    label right:
        scene bg room
        "I was right, here is my room. Time to sleep."
        "...As the ruler of this kingdom!"
        jump daytwo
    label left:
        "I'm completely lost! I can't believe it. I just want to go to sleep."
        m "Excuse me Sir."
        show brother surprised
        hide brother with moveoutright
        "He just fled!"
        "Whatever! I'll wander some more, I should eventually recognise a corridor."
        pause 2
        scene bg room
        "Finally!"
        "I'm exhausted."
        "Zzzzzz"
        jump daytwo

    ###### DAY TWO ######

    label daytwo:
        "Knock Knock"
        m "..."
        m "...Wh..? Is this...?"
        "Knock Knock"
        m "Oh right! Ruling, castle, advisors..."
        m "I need to get ready."
        m "Some pants. Over here!"
        "KNOCK KNOCK"
        m "Come in."
        show Leo smile
        "Man" "Good morning your Grace."
        "Man" "I hope I didn't wake you up?"
    menu:
        "Absolutely not. I was absorbed in a book.":
            $ leopoints += 1
            jump leointro
        "I was about to get out of bed.":
            jump leointro
    label leointro:
        show leo normal
        "Man" "Excellent, I would want to make a poor impression for my first encounter with you."
        "Man" "Allow me to introduce myself, Leo Tirvante. Adviser of foreign affairs. At your service."
        m "It's a pleasure to meet you."
        l "Alistair wanted to come and wake you up, but I thought it would be better if I went. A great opportunity to meet the new ruler."
        show leo smile
        l "Also, Alistair is not... As patient as I am."
        show leo normal
        l "Anyway, he is waiting for you in the throne room."
        m "Thank you Leo, I'll go."
        m "Are you not coming ?"
        l "Sadly I will have to pass. I must ran to some urgent errand."
    menu:
        "I hope I will see you again soon.":
            $ leopoints += 1
            jump leointrodone
        "I guess I will see you at the next meeting.":
            jump leointrodone

    label leointrodone:
        if gonetothevillage_flag == True:
            l "By the way, I heard that you sent Mirna away to investigate."
            show Leo smile
            l "It's nice to see you taking control already."
            l "Enjoy your first meeting."
        hide leo
        pause 1
        show bg throne
        show alistair normal
        a "Ah, [MainCharacter]. Good day."
        m "Good day."
        a "Let me introduce you to Cassandra."
        show alistair at righto
        show cassandra at lefto with moveinleft
        c "It's a pleasure to meet you."
        c "I'm Cassandra, your military advisor and General of the Royal Army."
        m "The pleasure is mine."
        c "I hope you'll fare better than your predecessor."
    menu:
        "I'd rather not be beheaded.":
            jump cassintro
        "It would be better for the kingdom and for myself":
            $ cassandrapoints += 1
            jump cassintro
    label cassintro:
        c "Indeed..."
        c "I must go to the barracks, but I look forward to seeing what you're made of."
        hide cassandra
        a "She is actually nicer than she seems. Don't worry."
        a "Now, as a noble you must have had a speciality when you studied. What was it?"
    menu:
        "Military strategy for cavalry":
            $ militaryknowledge += 2
            jump paststudies
        "Diplomacy with other nations":
            $ foreignknowledge += 2
            jump paststudies
        "Elven Kingdoms":
            $ elfknowledge += 2
            jump paststudies
        "Modern medicine":
            $ scienceknowledge += 2
            jump paststudies
        "xxx history of the last 500 years":
            $ internalknowledge += 2
            jump paststudies
        "New and ancient divinities":
            $ religiousknowledge += 2
            jump paststudies
    label paststudies:
        a "Very well. It might have seem useless to you at the time, but maybe, as a ruler, you will find this knowledge useful."
        a "Knowledge is critical for your success. Whether you succeed or fail will depend on your ability to make the right decision."
        a "Something more critical: information."
        a "This is the real power you will wield, for good or bad."
        a "It might as well be used against you."
        m "This all sounds dangerous."

    ###### DAY THREE ######

    call study from _call_study
    #label study1:
    "Continue"
    "scienceknowledge [scienceknowledge] religiousknowledge [religiousknowledge] internalknowledge [internalknowledge]"

    show bg throne
    show alistair normal
    a "Your Highness, the faction of the Merchants and that of the Nobles are here to submit an issue to your judgement."
    a "They do not seem to be able to get along (as usual)."
    m "Alright, let's do this."
    hide alistair
    show noble at righto
    show merchant at lefto
    noble "It's an honour to meet our new ruler. I am Frey Svertssion, I represent the Nobles' Guild."
    merchant "Your Highness, my name is Leya Hildr. I am sure you can help us resolve this conflict in a wise and just manner."
    noble "Let me explain the issue."
    show merchant angry
    noble "The title of noble is only given to people meeting certain criteria, such as exploits in battle, honorable deed for the Kingdom or inherited."
    show merchant normal
    show noble angry
    merchant "Or for those who manage to accumulate enough Gold."
    noble "As I was saying..."
    show noble normal
    noble "The title is full of meaning and not anyone can have access to it."
    merchant "The rule is clear your Highness : if a family maintain a fortune of 20000 Gold for two generations, then they can claim the title of noble."
    merchant "A feat not easily acheive, even for the best of merchants."
    noble "The rule however also stipulate that the pretendant must have an estate."
    merchant "This rule was added later as a way to prevent merchants from becoming nobles!"
    show noble angry
    noble "That does not make that rule invalid."
    show merchant angry
    merchant "But merchants are always following their caravans, the estate would be empty."
    a "You've been heard."
    hide noble
    hide merchant
    show alistair
    a "There is really no simple resolution of this problem. No obvious truth."
    a "What do you think ?"
    if internalknowledge >= 1:
        $ renpy.notify('Internal affairs knowledge check passed')
        "This new rule was indeed added pretty recently to prevent merchants to be nobles."
    elif internalknowledge >=3:
        $ renpy.notify('Internal affairs knowledge check passed')
        "This new rule was indeed added pretty recently to prevent merchants to be nobles."
        "The noble are a tight group. Having them as enemies is not a smart move. On the other hand, added some 'fresh blood' among the nobles might lessen their power."
    elif internalknowledge <1:
        $ renpy.notify('Internal affairs knowledge check failed')
    menu:
        "Accumulating that much Gold for two generations is impressive and some nobles have less than that. Merchants should be able to get the title without an estate.":
            $ merchantspoints += 1
            $ noblespoints += -1
            jump issueOneMerchants
        "The rule is the rule. Nobles have had to accomplish honourable deeds to get their title. It cannot simply be obtained with money.":
            $ merchantspoints += -1
            $ noblespoints += 1
            jump issueOneNobles

    label issueOneNobles:
        show merchant angry at lefto
        show noble at righo
        hide alistair
        merchant "Is this fair?..."
        hide merchant dissolve(1)
        noble "Thank you your Highness, the nobles will be pleased to see that you recognise the importance of such a title."
        hide noble
        jump issueOneResolved
    label issueOneMerchants:
        show noble angry at righto
        show merchant at lefto
        hide alistair
        noble "..."
        hide noble dissolve(1)
        merchant "Thank you your Highness! I knew you would be fair. The Merchants Guild won't forget that."
        hide merchant
        jump issueOneResolved
    label issueOneResolved:
        show alistair normal
        a "Well done. In cases like this there is not really any right or wrong."
        show alistair at lefto
        show leo at righto with moveinright
        l "Nicely done. That's one of those case where you can't please everyone."
        a "Leo, you returned."
        l "Yes, I was visiting the Duke of Noremberg. He had some issues with neighbouring Dwarves and wanted my help."
        show alistair suspicious
        a "..."
        a "That is all that required your attention today [MainCharacter]."
        hide alistair
        hide leo
        show bg room
        "This went ok."
        "So far it doesn't seem too complicated."

        ##### DAY FOUR #####

        call study from _call_study_1

        "I have nothing planned this afternoon. I could go and see one of the advisors."

        call adviserchat from _call_adviserchat

        ##### DAY FIVE #####

        call study from _call_study_2

        show bg throne
        show cassandra normal

        c "You've met the nobles, now let me introduce you to the 'Warriors'."
        show cassandra whatever
        c "That's what they call themselves. I would call them expansionist nobles. That's more accurate."
        c "They are not worse than the 'regular' nobles though, simply different."
        m "I can't wait to meet them. I remember hear my father talk about them."
        hide cassandra with moveoutright
        pause 0.5
        show noble at lefto
        show warrior at righto
        warrior "Your Highness, I am glad to finally see you. I am sure you will see how reasonable my proposal is."
        noble "A rather unreasonable proposal in my opinion."
        m "Let's hear it."
        warrior "As you know your Highness, there is a limit to the size of the army we can have."
        if militaryknowledge == 0:
            "I didn't know that..."
        elif militaryknowledge > 0:
            m "Yes, depending on the population of the Duchy."
            warrior "Indeed."
        warrior "However, we think this rule is not taking into account something very important : if the Duchy shares border with a foreign kingdom."
        warrior "Those of us next to other kingdoms are at a higher risk og being invaded, we need to be able to defend ourselves."
        noble "And increasing your military at the border is exactly what will start a conflict."
        noble "Maybe that is actually what you want, so you can fight back and get some extra piece of land to add to yours."
        warrior "This idea is preposterous! We are not blood thirsty as you like to portray us. We are on the front line in case of invasion and would like to be able to fight back."
        warrior "If we can better defend ourselves, we can better defend the Kingdom."
        c "We heard you."
        hide noble
        hide warrior
        c "What do you think?"
        if militaryknowledge >= 1:
            $ renpy.notify('Military knowledge check passed')
            m "Instead of increasing their army they could hire mercenaries."
            c "That's a possibility."
        if militaryknowledge >= 2:
            $ renpy.notify('Military knowledge check passed')
            m "The neighbouring countries will feel threatened. Not all of them, but some definitely won't be happy about that."
            c "True, but what they say about how reninforcing their army helps the whole Kingdom is true."
        if militaryknowledge == 0:
            $ renpy.notify('Military knowledge check failed')
        "I need a crystal ball to make those decisions!"
        c "What do you think we should do ?"
        m "What do YOU think ? You're my military advisor after all, you know better than me."
        c "True. But, as the other advisers, I want to see what you're made of to see if you are a worthy ruler."
        menu:
            "That's not very smart, I might make all sort of wrong decisions.":
                $ cassandrapoints += -1
                jump notverysmart
            "You're the one who will suffer the consequences if I make a mistake.":
                jump notverysmart
            "Be prepared to be impressed.":
                $ cassandrapoints += 1
                jump notverysmart
    label notverysmart:
        c "What will you tell them ?"
        show noble at lefto
        show warrior at righto
        "This will come back to bite me in the butt..."
        menu:
            "You can increase the size of your army.":
                $ warriorspoints += 1
                $ increaseArmy = True
                jump issueTwoWarriors
            "You can get mercenaries if you need them.":
                $ mercenaries = True
                jump issueTwoResolved
            "You cannot increase the size of your army.":
                $ warriorspoints += -1
                $ noblespoints += 1
                jump issueTwoNobles
    label issueTwoWarriors:
        hide noble
        show warrior smiling
        warrior "The Warrior Guild is pleased to see that you understand how important the security of the Kingdom is."
        jump doneWithIssueTwo
    label issueTwoResolved:
        show noble
        show warrior
        noble "That's an interesting decision."
        warrior "This will increase our military costs, mercenaries are not cheap."
        warrior "I hope you will change your mind and authorize an increase in the size of armies."
        jump doneWithIssueTwo
    label issueTwoNobles:
        show warrior angry
        warrior "Then pray that no one will ever be tempted to invade us!"
        hide warrior
        show noble smiling
        noble "I'm glad you see how preserving the peace is most important your Highness."
        jump doneWithIssueTwo
label doneWithIssueTwo:
    hide noble
    hide warrior
    show cassandra smiling
    c "That went alright."
    hide cassandra
    show bg room
    "I need to learn more! When I don't have the knowledge my decisions are just shots in the dark."
    hide cassandra
    #Transition
    if gonetothevillage_flag == True:
        show bg room
        "Knock knock... Knock"
        m "Yes?"
        mi "It's Mirna, I'm back from the village."
        show mirna normal
        m "How was the trip?"
        mi "There is a strange disease, the rumours are right. People start coughing, they become very pale, after a week or so they are bedridden. Some survive, but the weakest die."
        m "How contagious is this?"
        mi "Hard to say..."
        menu:
            "You should study what causes it.":
                $ diseaseCause = True
                jump tostudydisease
            "You should study how to cure it.":
                jump tostudydisease
    label tostudydisease:
        mi "I will do that."
        show mirna shy
        mi "Ah and... Thank you for trusting me with this."
        hide mirna
        #Transition

###### DAY SIX #######

    call study from _call_study_3
    #Transition
    call adviserchat from _call_adviserchat_1

    show bg throne
    a "The Royal Messenger is here."
    a "He is carrying different information to you. As I told you, information is critical."
    hide alistair
    show dagon
    rm "It's an honour to meet you. I will serve as best as I can."
    m "Thank you."
    rm "I was in the castle of the Duke of Wincort."
    if internalknowledge > 1:
        $ renpy.notify('Internal Affairs knowledge check passed')
        "The Duke is a very disorganised man who prefers to be away hunting and leaves the duties to his wife."
    if internalknowledge <= 1:
        $ renpy.notify('Internal Affairs knowledge check failed')
    rm "He announced that he would not be paying his taxes."
    show dagon at lefto
    show alistair worried at righto
    a "That is... A problem."
    rm "What will be your answer?"
    "I thought the day was going to be nice. Why?!"
    menu:
        "Send a tax collector and tell him he has 5 days to pay.":
            $ dukepayfast = False
            jump fakenews1
        "Send a tax collector and an armed escort and tell him he must pay immediately.":
            $ dukepayfast = True
            jump fakenews1
label fakenews1:
    rm "At once."
    hide rm
    pause 0.5
    show alistair suspicious
    a "The Duke is not the kind of man looking for conflicts, quite the contrary."
    "I hope I made the right decision..."

###### DAY SEVEN ######

    # Transition
    call study from _call_study_4

    show bg throne
    show leo
    l "[MainCharacter], I just witnessed something that will prove quite problematic for you."
    m "Go ahead, being a ruler seems to be all about problems anyway. I better get used to it."
    l "A man, that happened to be your uncle, or so he said, was telling the people on the street that you were actually a bastard child and had no place on the throne."
    m "By the gods! That's a lie! Why would he do that?"
    l "I believe you, but people were listening."
    l "Also, allow me to remind you that at any time, if most of the people in the city agree that you are 'not fit' to be their ruler and they vote..."
    l "You know what happens."
    m "The whole beheading thing. Yes. Don't worry I won't forget it."
    m "We need to do something about it."
    l "You need information. That's what you will use to fight back."
    l "We can try to find some way to blackmail him."
    show leo at lefto
    show alistair at righto with moveinright
    a "That is one way. Not my favourite I must say."
    m "Do you have another solution?"
    a "Why not try to find why he is lying?"
    "I need to send my advisers to take care of that. I'm pretty sure that motivation plays a role in increasing or decreasing the chances of success."
    "The more an adviser trust me, the more effort they will put."
    hide leo
    hide alistair
    hide dagon
    "I need someone to look for clues as to why he is doing this."
    menu:
        "Send Mirna \(68\% \chances\)":
            default scandale1posmirna = False
            $ randomness = renpy.random.randint(1, 100)
            if 68+mirnapoints*10/12 >=randomness:
                $ scandale1posmirna = True
            jump scandale1posmirna
        "Send Leo \(72\% \chances\)":
            $ randomness = renpy.random.randint(1, 100)
            if 72+leopoints*10/12>=randomness:
                $ scandale1posleo = True
            jump scandale1posleo
        "Send Alistair \(70\% \chances\)":
            default scandale1posalistair = False
            $ randomness = renpy.random.randint(1, 100)
            if 70+alistairpoints*10/12>=randomness:
                $ scandale1posalistair = True
            jump scandale1posalistair
        "Send Cassandra \(71\% \chances\)":
            default scandale1poscassandra = False
            $ randomness = renpy.random.randint(1, 100)
            if 71+cassandrapoints*10/12>=randomness:
                $ scandale1poscassandra = True
            jump scandale1poscassandra

label scandale1poscassandra:
    show cassandra normal
    $ cassandraChosen = True
    c "cassandrapoints [cassandrapoints] and is passed? [scandale1poscassandra] VS [randomness]"
    c "Alright. I'll get to it. [scandale1poscassandra]"
    hide cassandra
    jump scandale1posdone
label scandale1posleo:
    show leo normal
    $ leoChosen = True
    l "[leopoints] and [scandale1posleo] and [randomness]"
    l "Alright. I'll get to it. [scandale1posleo]"
    hide leo
    jump scandale1posdone
label scandale1posmirna:
    show mirna normal
    $ mirnaChosen = True
    m "[mirnapoints] and [mirnaNum] and [scandale1posmirna] and [randomness]"
    m "Alright. I'll get to it. [scandale1posmirna]"
    hide mirna
    jump scandale1posdone
label scandale1posalistair:
    show alistair normal
    $ alistairChosen = True
    a "[alistairpoints] and [alistairpercent] and [scandale1posalistair] and [randomness]"
    a "Alright. I'll get to it. [scandale1posalistair]"
    hide alistair
    jump scandale1posdone

label scandale1posdone:
    menu:
        "And someone to look about blackmailing him."
        "Send Mirna \(75\% \chances\)" if mirnaChosen == False :
                default scandale1negmirna = False
                $ randomness = renpy.random.randint(1, 100)
                if 75+mirnapoints*10/12>=randomness:
                    $ scandale1negmirna = True
                jump scandale1negmirna
        "Send Alistair \(71\% \chances\)" if alistairChosen == False :
                default scandale1negalistair = False
                $ randomness = renpy.random.randint(1, 100)
                if 71+alistairpoints*10/12>=randomness:
                    $ scandale1negalistair = True
                jump scandale1negalistair
        "Send Leo \(77\% \chances\)" if leoChosen == False :
                default scandale1negleo = False
                $ randomness = renpy.random.randint(1, 100)
                if 77+leopoints*10/12>=randomness:
                    $ scandale1negleo = True
                jump scandale1negleo
        "Send Cassandra \(72\% \chances\)" if cassChosen == False :
                default scandale1negcassandra = False
                $ randomness = renpy.random.randint(1, 100)
                if 72+cassandrapoints*10/12>=randomness:
                    $ scandale1negcassandra = True
                jump scandale1negcassandra

label scandale1negleo:
    show leo normal
    $ leoChosen = True
    l "I will look into it. [scandale1negleo]"
    hide leo
    jump scandale1Done
label scandale1negcassandra:
    show cassandra normal
    $ cassandraChosen = True
    c "I will look into it. [scandale1negcassandra]"
    hide cassandra
    jump scandale1Done
label scandale1negalistair:
    show alistair normal
    $ alistairChosen = True
    a "I will look into it. [scandale1negalistair]"
    hide alistair
    jump scandale1Done
label scandale1negmirna:
    show mirna normal
    $ mirnaChosen = True
    m "I will look into it. [scandale1negmirna]"
    hide mirna
    jump scandale1Done

label scandale1Done:
    #Transition
    show bg room
    "Who could want to get rid of me?"
    "I have no known enemies."
    "The next person in line after me is my cousin Nadia and she absolutely doesn't want to rule."
    "I should be careful..."


###### DAY EIGHT ######

    # Transition
    call study #from _call_study_4
    call adviserchat #from _call_adviserchat_2

    show bg throne
    show mirna normal
    mi "The Duke of Wincort seems quite angry and would like an audience immediately."
    m "Where is he?"
    m "We only sent the message two days ago."
    with hpunch #shake
    hide mirna with moveoutright
    show duke
    "Duke of Wincort" "I cannot believe this!"
    "Duke of Wincort" "I demand an extra month to pay the taxes - Taxes that I always paid on time!"
    if dukepayfast == True :
        "Duke of Wincort" "And I get {b}a threat{/b} and an order to pay at once?!"
    elif dukepayfast == False :
        "Duke of Wincort" "And I get {b}a threat{/b} and an order to pay in five days?!"
    "Duke of Wincort" "What kind of tyrant is now sitting on the throne!"
    m "You asked for an extra month to pay your taxes?"
    "Duke of Wincort" "Indeed."
    menu:
        "I'm sorry that this happened."
        "Let me give you two months to pay the taxes.":
            $ gavetwomonths = True
            jump dukeovertwo
        "We will exceptionnally allow you one month to pay.":
            jump dukeoverone
label dukeovertwo:
    "Duke of Wincort" "Hmph. Fair enough."
    jump dukedone
label dukeoverone:
    "Duke of Wincort" "I think it is the minimum to agree to that considering the trouble I just went through."
    jump dukedone
label dukedone:
    hide duke
    show mirna shy
    mi "The Duke was quite angry..."
    show mirna shy at lefto with moveinleft
    show leo smiling at righto with moveinright
    l "That's the least we could say."
    l "Don't worry [MainCharacter], he'll get over it."
    if gavetwomonths == True:
        l "It was generous of you to give two months."
        l "He didn't show it but he was pleased."
    elif gavetwomonths == False:
        l "In the end you gave him what he wanted."
        l "Maybe throwing a little present his way, for the trouble, might have been nice."
    hide mirna
    show cassandra suspicious at lefto with moveinleft
    c "What is strange is how we ended up with another message."
    show leo normal
    l "It happens I guess."
    hide mirna with dissolve
    hide leo with dissolve

    if mercenaries == True:
        show cassandra normal with dissolve
        c "By the way, I came to tell you that authorizing mercenaries might not have been the wisest of decision."
        m "Alright, I'm ready, one more mistake."
        c "The mercenaries in two Duchies pillaged and left."
        m "That's bad, but not my problem."
        c "It is your problem actually. The two nobles to whom it happened blamed it on you and the fact that you {i}forced{/i} them to have mercenaries instead of an army. And the army would have created jobs said some."
        m "I see how that {b}is{/b} my problem."
        c "Those Duchies are pretty far away so news won't travel to fast and too much, but we can be pretty sure your reputation among the masses will drop."
        m "Anything we can do?"
        c "We could tell the nobles to correct those rumours. That will work fine if it does, but if it doesn't, it will even more damage your reputation."
        c "Or we could try our own rumours about how the mercenaries were only authorised in times of war. It's easier to do and there are no consequences in case of failure, but it would also have a weaker impact."
        c "What do you think?"
        menu:
            "Tell the nobles to get the record straight \(unknown \chances\)":
                $ randomness = renpy.random.randint(1, 100)
                if 50+cassandrapoints*10/12>=randomness:
                    $ getrecordstraight = False
                jump mercenariesdone
            "Counter rumour seems better \(unknown \chances\)":
                $ randomness = renpy.random.randint(1, 100)
                if 80+cassandrapoints*10/12>=randomness:
                    $ getrecordstraightrumour = True
                jump mercenariesdone
    label mercenariesdone:
        hide cassandra with dissolve
        if getrecordstraight = True:
            $ approval += 10
        if getrecordstraight = False:
            $ approval -= 10
    if increaseArmy == True:
        show cassandra normal with dissolve
        c "You remember how you authorised the nobles to increase the size of their armies?"
        m "I do... Don't tell me it was a mistake."
        c "I would not say that, more that it has consequences, negative ones."
        m "..."
        c "The Duchess of Lwara increased her army's size by quite a lot. She more than doubled it. Her neighbours, the Elven kingdom of Nerina and Gilden are not pleased about this."
        m "She more than doubled it?!"
        c "They fear that the Duchess is preparing to invade."
        m "We need to stop this before it gets out of hand."
        c "How, that's the question."
        c "We could somehow tell the Duchess that keeping such a big army is not good."
        m "...Yes, I think I know how."
        c "Or we could try to reassure the kingdoms of Nerina and Gilden on the intent of the Duchess."
        c "We could say she is training this new part of the army for another kingdom."
        m "Is that true?"
        c "Well if there is a war she will have to give part of her army to the kingdom attacked as stipulates in our code of war."
        c "What do you want to do? The rumour seems more likely to fail but would be much more efficient."
        menu:
            "Spread a rumour among the troops that because of the bad harvest they won't be paid \(unknown \chances\)":
                $ randomness = renpy.random.randint(1, 100)
                if 70+cassandrapoints*10/12>=randomness:
                    $ armystarving = True
                jump increasedarmydone
            "Send a messenger to the Elven kingdoms to tell them that the army is just being trained there \(unknown \chances\)":
                $ randomness = renpy.random.randint(1, 100)
                if 90+cassandrapoints*10/12>=randomness:
                    $ trainingarmy = True
                jump incresedarmydone
    label increasedarmydone:
        hide cassandra with dissolve
        if armystarving = True:
            $ approval += 10
        if armystarving = False:
            $ approval -= 10
        if trainingarmy = True:
            $ approval += 5
        if trainingarmy = False:
            $ approval -= 3

###### DAY NINE ######

    # Transition
    call study #from _call_study_5

    show bg throne with dissolve
    pause 1
    show mirna normal with dissolve

    mi "Good afternoon."
    mi "It seems that today the nobles are back with a new problem."
    show mirna at lefto
    show cassandra normal at righto with moveinright
    c "I wonder what they want this time."
    m "Bring them, I'm ready."
    hide cassandra with moveoutright
    hide mirna with moveoutleft
    show warrior with easeinleft
    show religious with easeinright
    religious "Your Highness, I am Serva Lakam, High Priestress of the Order."
    religious "The Order is certain you will help us settle this dispute the right way."
    warrior "In the right way indeed."
    m "I will. What is your issue?"
    religious "As you know, the Orders army is made from military men and women of the different kingdoms. It has been like so for hundreds of years."
    warrior "Except that now, some of the nobles are rejecting the principles of the Order."
    warrior "Should they still have to give their soldiers to a faith they don't believe in?"
    religious "Yes, they should. Let's not forget that the Divine Army is sent accross the kingdom to help the people."
    warrior "And preach..."
    religious "You mean share its wisdoms with the good people?"
    hide warrior with easeoutleft
    hide religious with easeoutright
    pause 0.5
    show cassandra normal with dissolve
    c "Alright alright. We will see what to do about this."
    show cassandra at lefto with easeinleft
    show mirna at righto with easeinright
    mi "Most people still believe in the Order."
    if religiousknowledge < 2:
        $ renpy.notify('Religious knowledge check failed')
    if religiousknowledge >= 2:
        $ renpy.notify('Religious knowledge check passed')
        m "The ones who don't believe in the Order are usually forest people who believe in the Spirits."
        mi "Yes, it's unlikely that those nobles converted."
        m "They might say that just to keep their soldiers to themselves."
    if internalknowledge < 2:
        $ renpy.notify('Internal affairs knowledge check failed')
    if internalknowledge >= 2:
        $ renpy.notify('Internal affairs knowledge check passed')
        m "While they do try to propagate their religion, the Divine Army does help a lot the people."
    mi "What will you tell them?"
    menu:
        "The Divine army is helpful, let's keep it" if internalknowledge >= 2:
            $ warriorspoints -= 7
            $ religiouspoints += 8
            $ stillDrafting = True
            jump draft
        "The Order has been respected so far, we should keep it that way":
            $ warriorspoints -= 10
            $ religiouspoints += 10
            $ stillDrafting = True
            jump draft
        "The nobles who don't follow the Order should be exempt":
            $ warriorspoints += 10
            $ religiouspoints -= 10
            jump noDraft
    label draft:
        show religious with dissolve
        religious "A wise decision. Tonight the Chant will be in your honour."
        hide religious with dissolve (1)
        jump draftingDone
    label noDraft:
        show warrior normal at lefto with easeinleft
        show religious sad at righto with easeinright
        religious "My child... The light seems to have abandonned you."
        hide religious with dissolve
        show warrior smiling at center
        warrior "I think the light is just fine and you made some nobles quite happy."
        hide warrior
        jump draftingDone
    label draftingDone:
        show mirna normal
        mi "I suppose that's settled."
        mi "The Royal Messenger has been waiting with some news."
        hide mirna with dissolve
        "It just never ends..."
        show dagon with dissolve
        rm "Your Highness, I bear news from our informants in the Duchy of Kalimos."
        m "What are the news?"
        rm "Groups of elves have been seen meeting at night, clearly preparing something."
        rm "There are rumours of a rebellion."

        if internalknowledge < 5:
            $ renpy.notify('Internal affairs knowledge check failed')
        if internalknowledge >= 5:
            $ renpy.notify('Internal affairs knowledge check checked')
            "The Duchy of Kalimos is known to have a very important population of elves."
        if elfknowledge < 5:
            $ renpy.notify('Elf knowledge check failed')
        if elfknowledge >= 5:
            $ renpy.notify('Elf knowledge check checked')
            "Elves in Kalimos are almost exclusively wood elves, they are the most peaceful of people on this continent."
        rm "What do you want to do?"
        menu:
            "Send spies to keep a close eye on those meetings":
                $ spiesSent = True
                jump spiesSent
            "Have patrols on the street to show them":
                $ patrolsSent = True
                jump spiesSent
    label spiesSent:
        rm "I will carry your message immediately."
        hide dagon
        mi "I guess that's it for the day then."

###### DAY TEN ######

    # Transition
    call study #from _call_study_6
    call adviserchat #from _call_adviserchat_3

    show throne with dissolve (1)
    show alistair at lefto with easeinleft
    show leo at righto with easeinright
    l "[MainCharacter], have you been outside of the castle today?"
    m "No... What's happening?"
    l "People are protesting on the main plaza."
    m "Protesting?!"
    m "Why?"
    l "Because you want to increase taxes on the people."
    m "WHAT?!" with hpunch
    l "Someone is trying to ruin your reputation with a disinformation campaign."
    a "I agree that this is the second time and it's suspicious, but it might still be a coincidence."
    l "Really? You don't think someone is doing this on purpose."
    m "But why would anyone do that?"
    a "A great question, but the more pressing matter is what should we do about this. It needs to be handled before it gets out of hand."

    "My popularity with the people must be dropping as we speak, I must do something!"
    a "We could try to inform the people about the tax system. Once they have access to the right information they should understand."
    l "It could work..."
    a "Do you have a better idea?"
    l "It's not so much about the taxes and more about the image."
    show alistair angry
    l "If the people saw their ruler helping the poor and while doing so someone can do some counter propaganda and help people forget about this taxes mess."
    a "..."
    "Which one is the best approach?"
    menu:
        "I'm sure if we inform the people they will understand that there was no reason to protest":
            jump protestInfo
        "We need to rebuild my image":
            jump protestComm

    label protestInfo:
        l "That might be less risky sure, but probably harder to get any results."
        a "Good choice, who should take care of this?"
        menu:
            "Send Mirna \(65\% \chances\)":
                $ randomness = renpy.random.randint(1, 100)
                $ protestInfoMirna = True
                if 65+mirnapoints*10/12 >=randomness:
                    $ protestInfoSuccess = True
                jump protestInfoDone
            "Send Leo \(64\% \chances\)":
                $ randomness = renpy.random.randint(1, 100)
                $ protestInfoLeo = True
                if 64+leopoints*10/12>=randomness:
                    $ protestInfoSuccess = True
                jump protestInfoDone
            "Send Alistair \(72\% \chances\)":
                $ randomness = renpy.random.randint(1, 100)
                $ protestInfoAlistair = True
                if 72+alistairpoints*10/12>=randomness:
                    $ protestInfoSuccess = True
                jump protestInfoDone
            "Send Cassandra \(69\% \chances\)":
                $ randomness = renpy.random.randint(1, 100)
                $ protestInfoCassandra = True
                if 69+cassandrapoints*10/12>=randomness:
                    $ protestInfoSuccess = True
                jump protestInfoDone

    label protestComm:
        if protestInfoLeo == False:
            l "A wise choice, it's all about your popularity after all."
        if protestInfoAlistair == False:
            a "I suppose it matters..."
        if protestInfoLeo == False:
            l "Who will you send?"
        else:
            a "Who will you send?"
        menu:
            "Send Mirna \(75\% \chances\)" if protestInfoMirna == False :
                $ randomness = renpy.random.randint(1, 100)
                $ protestCommMirna = True
                if 75+mirnapoints*10/12 >=randomness:
                    $ protestCommSuccess = True
                jump protestCommDone
            "Send Leo \(72\% \chances\)"if protestInfoLeo == False :
                $ randomness = renpy.random.randint(1, 100)
                $ protestCommLeo = True
                if 72+leopoints*10/12>=randomness:
                    $ protestCommSuccess = True
                jump protestCommDone
            "Send Alistair \(69\% \chances\)" if protestInfoAlistair == False :
                $ randomness = renpy.random.randint(1, 100)
                $ protestCommAlistair = True
                if 69+alistairpoints*10/12>=randomness:
                    $ protestCommSuccess = True
                jump protestCommDone
            "Send Cassandra \(73\% \chances\)" if protestInfoCassandra == False :
                $ randomness = renpy.random.randint(1, 100)
                $ protestCommCassandra = True
                if 73+cassandrapoints*10/12>=randomness:
                    $ protestCommSuccess = True
                jump protestCommDone
    label protestCommDone:
        if protestInfoLeo == False:
            l "This should prove useful."
        else:
            m "This should help. If it works..."
        m "Now we will have to wait and hope for the best."

###### DAY ELEVEN #######

    # Transition
    call study #from _call_study_7

    show bg throne with dissolve(1)
    pause (0.5)
    show cassandra normal at lefto
    show alistair normal at righto
    a "The Duchess of XXX is waiting for her audience with you."
    c "She's part of the Warriors. One of their most prominent figures."
    m "Let's do this. Bring her in."
    show duchess with dissolve
    d "Your Highness, I'm the Duchess of XXX, it's an honour."
    d "I've requested an audience and traveled far from my duchy today because I am in a dire situation."
    d "I should like to get straight to the point: I need to declare war to Advena, the Northern neighbouring kingdom of Dwarves."
    if militaryknowledge >= 5:
        $ renpy.notify('Military knowledge check passed')
        "But the Duchess needs a valid reason to go to war. There are none."
    if militaryknowledge < 5:
        $ renpy.notify('Military knowledge check failed')
    if internalknowledge >= 6:
        $ renpy.notify('Military knowledge check passed')
        "Her duchy has been trying to find a reason to expand their border for quite some time. Her father tried before her."
    if militaryknowledge < 6:
        $ renpy.notify('Military knowledge check failed')
    menu:
        "May I know why?":
            $ duchesspoints +=1
            jump duchessOne
        "Are you serious?":
            $ duchesspoints -=2
            jump duchessOne
    label duchessOne:
        d "My kingdom has been attacked over 30 times those last three months."
        if militaryknowledge >= 7:
            $ renpy.notify('Military knowledge check passed')
            "Advena has a small army and has problem at their northern border. They would not want to divide their forces fighting on their South border..."
        if militaryknowledge < 7:
            $ renpy.notify('Military knowledge check failed')
        c "The army of Advena is attacking you?"
        d "Their people are your Grace. I cannot tolerate this any longer. They need to be shown that pillaging our ressources, terrorizing our people and generating chaos is not without consequences."
        d "I came to request your assistance. I wish you would send troops to help me fight this threat."
        d "If you choose not to however, I would solely request your permission to go to war against them to protect my people and land."
    menu:
        "I will consider your proposition":
            $ duchesspoints +=1
            jump duchessTwo
        "I'll summon you when I've reached a decision":
            $ duchesspoints -=1
            jump duchessTwo
    label duchessTwo:
        d "I am sure you will consider the suffering people of Advena."
        hide duchess with dissolve
        pause 1.5

        m "We need to analyse this situation carefully. We are talking about war here! As if I didn't have enough on my plate already !"
        if militaryknowledge >= 8:
            $ renpy.notify('Military knowledge check passed')
            "A war would have costly consequences that simply can't be estimated properly."
        if militaryknowledge < 8:
            $ renpy.notify('Military knowledge check failed')
        m "Cassandra, as my military advisor what is your opinion?"
        c "If we ally the force of the castle army with that of the Duchess we would win without a shadow of a doubt."
        m "What if we help the Duchess? What about the cost for the kingdom?"
        c "The kingdom's army loss would be small. But the troops would not be interested in going to war with a country that we have nothing against."
        pause 1
        m "..."
        m "What if we refuse to help?"
        c "The Duchy of xxxx could win without our help."
        if militaryknowledge < 5:
            $ renpy.notify('Military knowledge check failed')
        if militaryknowledge >= 5:
            $ renpy.notify('Military knowledge check passed')
            m "But with our help they would crush them and suffer little loss."
            c "And still they ask for help."
        if militaryknowledge >= 6:
            $ renpy.notify('Military knowledge check passed')
            m "Could we compromise and send half of our forces?"
            c "If we just sent half the troops we would definitely win, but we would have significant losses."
        if militaryknowledge < 6:
            $ renpy.notify('Military knowledge check failed')

        pause 1
        l "Going to war would have important repercussions."
        l "We would have other duchies asking to do the same."
        if internalknowledge >= 5:
            $ renpy.notify('Internal affairs knowledge check passed')
            m "The Duke of Telsna has been eyeing Dwarves ressources for a long time and would want to go against them."
            L "Indeed, and that would mean full out war with the Dwarves."
        if internalknowledge < 5:
            $ renpy.notify('Internal affairs knowledge check failed')
        l "We will also have to face the wrath of the Dwarves Kingdom for the attack of the Duchess, which could mean severe penalties on import/export."
        m "I'd rather not have to deal with a war. That would not help my popularity."
        pause 1
        m "So if we help the Duchess we are making a big mistake?"
        l "We would acquire ressources. The duchy is next to ressources of myrthril."
        l "Needless to say that it would be {b}very{/b} valuable. We could then increase her taxes, produce new goods and export them."
        m "What if we tell her not to do anything?"
        l "She might still go and that would be a big problem."
        m "She's giving me a headache."
        l "If she doesn't do anything though... We might use this to our advantage."
        pause 1
        m "..?"
        pause 0.5
        m "..??"
        pause 0.5
        m "Are you going to say how?"
        l "I like to build suspense, sorry."
        l "She wants to go to war, fine. We could help the Dwarves in their current war on their northern border."
        c "We would double their forces. The victory would be guaranteed."
        l "But we need a deal with the Dwarves, a sort of alliance, the agreement of the Duchess and we need it fast before she can cause chaos on her own."

        pause 1
        m "Alright. I think I have all the information I need."
        c "What's your choice?"

        menu:
            "Better a swift war":
                $ renegade += 2
                jump toWar
            "We need to stop her":
                $ paragon += 2
                jump toPeace
    label toWar:
        m "Time to increase the riches of the castle. A swift war, little losses, big rewards."
        c "Some practice for our royal troops."
        l "And lots of money coming our way."
        pause 0.5
        c "We need to motivate our troops first."
        m "Propaganda?"
        c "Yes, the moral of the troops is critical."
        c "For propaganda to work we need our soldiers to identify themselves with the cause."
        c "They must be certain that our cause is just. They must believe we can win."
        c "And finally there is a need for discipline and unity. I will do the discipline part."
        m "We will say that we are coming to the rescue of the Duchess that has been {b}harassed incessantly{/b} by the Dwarves."
        m "We could demonize the enemy, promoting an idea about the Dwarves being threatening evil aggressor with only destructive objectives."
        c "That could work."
        m "Or we could reinforce the feeling of unity across the kingdom. Attacking the Duchess is attacking the whole kingdom."
        c "That would create unity indeed."
        menu:
            "Demonize the enemy \(78\% \chances\)":
                $ renegade += 1
                $ choseDemonize = True
                $ randomness = renpy.random.randint(1, 100)
                if 78+cassandrapoints*10/12>=randomness:
                    $ demonizeSuccess = True
                jump toWarOne
            "Attacking them is attacking us \(73\% \chances\)":
                $ paragon += 1
                $ choseUnity = True
                $ randomness = renpy.random.randint(1, 100)
                if 73+cassandrapoints*10/12>=randomness:
                    $ unitySuccess = True
                jump toWarOne

    label toWarOne:
        l "That's not all. We also need to make sure the other Nobles understand that it's an exception."
        m "We must tell the nobles that the Duchess is not attacking but defending."
        l "Indeed. But the nobles might have access to information though and know that she's not in any real danger."
        m "we could fabricate proof that it's something much bigger. Fake witnesses."
        l "Or fake news at the court."
        l "One way or another we can manipulate people by feeding them made up information."
        l "The truth is what they'll believe."
        l "So how do you want to do this?"
        m "Either we forge a letter send by an anonymous counselor of the Duchess asking various nobles for help in this dire, sinister, tragic situation."
        m "Or we have witnesses coming to testify at the court a day when many nobles are present."
        menu:
            "Fake witness \(76\% \chances\)":
                $ choseWitness = True
                $ randomness = renpy.random.randint(1, 100)
                if 76+leppoints*10/12>=randomness:
                    $ fakeWitnessSuccess = True
                jump toWarTwo
            "Fake letter \(74\% \chances\)":
                $ choseLetter = True
                $ randomness = renpy.random.randint(1, 100)
                if 74+leopoints*10/12>=randomness:
                    $ fakeLetterSuccess = True
                jump toWarTwo


    label toPeace:
        m "Let's try to see if we can stop her and turn this whole thing around."
        c "I can help the Duchess' General."
        l "We will need to be careful, I'll help."
        m "First step, we need the Duchess to agree."
        m "She should come to the conclusion that it is not wise to go to war."
        c "We could pretend that the Dwarves have a new advance weapon that would swing the ties of battle..."
        l "...Via a forged letter from her spy in XXX."
        l "Or we could have a fake spy tell [MainCharacter] at the assembly that the Dwarves are making an alliance with Domiyos, therefore more than doubling the size of their army."
        c "Many nobles will be there, especially the Duchess."
        c "Which do you think is the best course of action?"
        menu:
            "Threat of weaponry \(74\% \chances\)":
                $ choseWeaponry = True
                $ randomness = renpy.random.randint(1, 100)
                if 74+leopoints*10/12>=randomness:
                    $ weaponrySuccess = True
                jump toPeaceTwo
            "Threat of alliance \(71\% \chances\)":
                $ choseAlliance = True
                $ randomness = renpy.random.randint(1, 100)
                if 71+leopoints*10/12>=randomness:
                    $ allianceSuccess = True
                jump toPeaceTwo

    label toPeaceTwo:
        c "That's a good first step, but we also need to make sure the Dwarves agree to a deal with the Duchess about her coming with her army to help on the northern border and getting in exchange a piece of their land with some myrthril to exploit."
        l "Not easy, but feasible."
        m "The Dwarves must believe that the Duchess wanted to help all long."
        show cassandra whatever
        c "Hmph!"
        l "It's all a matter of story telling."
        show cassandre normal
        l "It's all a {i}big mistake{/i}. The Duchess getting ready to invade is fake news from the kingdom of Djaar they are already at war with."
        l "They wanted to demoralise the troops and divide the army."
        c "Actually that would be solid enough. They could have done that."
        c "We could also use whataboutism."
        l "It's an idea."
        m "What is that?"
        c "We discredit the Dwarves' position by accusing them of hypocrisy without directly disproving the fact that the Duchess is preparing for war."
        m "Oh... I see."
        c "Those are not very noble ways to reach peace, but I guess the end justifies the means."
        m "Yes, therefore I will go with..."
        menu:
            "Fake news of fake news \(69\% \chances\)":
                $ choseFakenews = True
                $ randomness = renpy.random.randint(1, 100)
                if 69+cassandrapoints*10/12>=randomness:
                    $ fakenewsSuccess = True
                jump toWarTwo
            "Whataboutism \(73\% \chances\)":
                $ choseWhataboutism = True
                $ randomness = renpy.random.randint(1, 100)
                if 73+cassandrapoints*10/12>=randomness:
                    $ whataboutsimSuccess = True
                jump toWarTwo

    label toWarTwo:
        c "Then this is it."
        c "Now we can only wait and hope that everything will work."


###### DAY TEN ######

    # Transition
    call study #from _call_study_8
    call adviserchat #from _call_adviserchat_4
    # patrolsSent // spiesSent

    show bg throne with dissolve
    show mirna normal at righto with dissolve
    pause(0.3)
    show alistair suspicious at lefto with dissolve
    pause(0.3)
    if patrolsSent==True:
        mi "Your Highness, the patrols didn't have the expected effect."
        mi "The Elves felt threatened and a few confrontations between patrols and Elves happened."
    if spiesSent==True:
        mi "Your Highness, the spies didn't have the expected effect."
        mi "The Elves saw them and felt threatened. Multiple protests happened."
    a "Actually, the Elves had been meeting to prepare their festival of the Sacred Tree..."
    m "Who reported those meetings through the Royal Messenger?"
    mi "A minor noble by the name of Friilevan."
    a "A minor noble no one ever heard of..."
    mi "Maybe they were from another Kingdom?"
    a "Maybe..."
    m "That's strange."
    m "Keep your eyes peeled. This mustn't happen again."

#====================================================================#
#=========================== MONTH TWO ==============================#
#====================================================================#

###### DAY THIRTEEN ######

    # Transition
    call study #from _call_study_9

    show bg throne with dissolve
    show mirna normal at righto with dissolve
    show alistair normal at lefto with dissolve
    mi "Do you remember that disease in a village from almost a month ago?"
    m "Yes."
    mi "It has propagated to another village now."
    mi "Of course that village has been quarantined. But it's still disturbing."
    a "In any case, the dispute today brings the Order against the Alchemists."
    m "Bring them in."
    hide alistair with easeoutleft
    hide mirna with easeoutright
    pause 0.5
    show religious normal at righto with dissolve
    show med normal at lefto with dissolve
    if stillDrafting:
        religious "Your Highness, it is a pleasure to see you again. I hope your judgment will be as just as last time."
    if noDraft:
        religious "Your Highness. I hope your judgment will be fairer than last time."
    med "Your Highness, I'm Archibald Lohgos, representant of the Alchemists Guild."
    m "Tell me what brings you here."
    religious "The Alchemists wish to disturb the dead and bring forth the Wrath of the Lady upon us."
    med "We are worried about this disease in the villages."
    med "We lost one of our own who was trying to help someone with the disease."
    med "To better understand the disease we need to see what it does inside the body of those it has taken."
    religious "They mean to disturb the rest of the dead. That is blasphemy."
    m "What if they examine the body of people who are not believer of the Order?"
    med "We already so that in some case. But those village people are all very religious."
    med "This needs to be done. The disease keeps propagating."
    religious "You do not even know for certain if you will find your answer by profaning bodies."
    med "At the very least clues."
    religious "If you disturb the bodies instead of sending their ashes to the wind then do not be surprised when the wrath of the Lady is upon you."
    m "Thank you, I will "
    hide med with easeoutleft
    hide religious with easeoutright
    pause 0.5
    show mirna normal with dissolve
    mi "What she said is true."
    mi "The simple folks from the village might believe that, if the disease keeps spreading and the Alchemists have dissected bodies, it is a punishment from the Lady."
    mi "On the other hand, it is true as well that dissection can provide critical clues."
    if mirnagoes:
        mi "When I was there I observed some of the contaminated people. It is a totally unknown disease."
    m "It's not easy being a ruler..."
    m "Tell them to come back, I'm ready."
    hide mirna with dissolve
    pause 0.3
    show med with easeinleft at lefto
    show religious with easeinright at righto
    med "What have you decided?"
    menu:
        "Dissect the bodies":
            $ dissection = True
            $ religiouspoints -= 1
            $ medspoints += 1
            jump toDissectionDone
        "Don't dissect the bodies":
            $ religiouspoints += 1
            $ medspoints -= 1
            jump toDissectionDone
    label toDissectionDone:
        if dissection:
            religious "This is unacceptable!"
            religious "Be ready to face the wrath of the Lady."
            hide religious with dissolve
            show med smiling at center
            med "This will no doubt help us to find a cure."
            med "Thank you."
            hide med with dissolve
        if dissection == False:
            med "Then let us hope that the disease doesn't contaminate another village."
            hide med with dissolve
            show religious smiling at center
            if stillDrafting:
                religious "Once more you have proven an ally of the faithful and an excellent judge."
            else:
                religious "I am glad you understood how important it is to allow the voyage of the souls to the Lady."
            religious "You made the right choice."
            hide religious with dissolve
        "I hope this disease won't reach another village, otherwise that will be {b}more{/b} trouble for me."

###### DAY FOURTEEN ######

    # Transition
    call study #from _call_study_10
    call adviserchat

    show bg throne with dissolve
    show dagon
    rm "Your Highness, I bring you news from the city."
    rm "The Alchemist Sera Marnia has contaminated on purpose a clothier by the name of Drumqar Latso."
    if scienceknowledge >= 3:
        $ renpy.notify('Science knowledge check passed')
        "Sera Marnia is a well known Alchemist."
    else:
        $ renpy.notify('Science knowledge check failed')
    m "Why would she do that?"
    rm "For an experiment Latso claimed."
    if scienceknowledge >= 5:
        $ renpy.notify('Science knowledge check passed')
        "Alchemists do test on people, but never contaminate them on purpose."
    else:
        $ renpy.notify('Science knowledge check failed')
    rm "He wants to see justice brought to her."
    hide rm with dissolve
    show cassandra normal with easeinright at righto
    show mirna normal with easeinleft at lefto
    mi "More trouble for the Alchemists."
    c "Justice in that case would be exile. It's against the Order as well as our laws."
    mi "It's also against the code of the Alchemists."
    m "It has to be an accident."
    c "If you let this go unpunished your reputation will suffer."
    mi "If you exile her and she is not guilty though..."
    m "This problems seem to get trickier by the day."
    hide cassandra with dissolve
    hide mirna with dissolve
    pause 0.3
    show dagon with dissolve
    rm "Your Highness, here is a testimony written and signed by Latso"
    m "Let's see..."
    "..."
    "It seems true."
    rm "Here are the notes from the Alchemist herself on Latso."
    m "...The patient has now little appetite, sunken eyes, tears of blood, nose bleeds everyday, loses weight fast... Chances of death very high... New disease very interesting..."
    "This doesn't look good. "
    m "Alright."
    menu:
        "Exile her"
            $ exiled = True
            jump toExileDone
        "Give her a pardon"
            jump toExileDone
    label toExileDone:
        rm "I will let her know."
        hide dagon
        "I hope this will go well."

###### DAY FITHTEEN ######

    # Transition
    call study #from _call_study_12
    call adviserchat

    show bg throne
    show alistair with dissolve at righto
    show mirna with dissolve at lefto
    a "A new dispute for you to resolve."
    a "The Elves and the Alchemists."
    m "Them again."
    mi "It's about market control as well as remedies."
    m "I'm ready."
    hide alistair
    hide mirna
    pause 0.3
    show med with dissolve at righto
    show elf with dissolve at lefto














    label toGameOver:
        "G A M E   O V E R"



    return # This ends the game.
