#Example Questions for Testing, 0-4 where 0 is s disagree, 2 is indifferent, 4 is s agree
#1. Dogs are better than cats 0-4
#2. I like to bang regularly 0-4
#3. Donald Trump MAGA 0-4
#4. Greek Life Affiliation 0-4
#5. My fav rap song is EZ MONEY 0-4



#Person Object
class Person:
    def __init__(self, name, gender, answers):
        self.name = name
        self.gender = gender
        self.answers = answers
        self.preferenceList = []

#Parse CSV file (example people for now)
p1 = Person("graham", "male", [4, 4, 0, 0, 4])
p2 = Person("matthew", "male", [4, 4, 4, 2, 4])
p3 = Person("dylan", "male", [2, 4, 0, 1, 2])
p4 = Person("liam", "male", [3, 2, 4, 0, 0])
p5 = Person("horace", "male", [1, 3, 2, 0, 4])
p6 = Person("irene", "female", [2, 1, 0, 2, 2])
p7 = Person("jessica", "female", [3, 3, 2, 3, 2])
p8 = Person("cat", "female", [1, 4, 1, 3, 1])
p9 = Person("lior", "female", [0, 4, 2, 2, 2])
p10 = Person("exene", "female", [2, 2, 2, 2, 3])

men = [p1, p2, p3, p4, p5]
women = [p6, p7, p8, p9, p10]

#Stable marriage algorithm, remember to RIG for JESSICA and EXENE before shipping

#Build preference lists
#Subtract score for each question and add total, sort least to greatest

#men
for x in range(0, len(men)):
        preferenceList = []
        mAnswers = men[x]
        for y in range(0, len(women)):
            wAnswers = women[y].answers
            total = 0
            for z in range(0, len(mAnswers)):
                total = total + (abs(mAnswers[z]-wAnswers[z]))
            preferenceList.append({women[y], total})
        men[x].preferenceList = preferenceList
#sort
for x in range(0, len(men)):
    men[x].preferenceList = sorted(men[x].preferenceList, key=lambda y: y[1])

#women
for x in range(0, len(women)):
        preferenceList = []
        wAnswers = women[x]
        for y in range(0, len(men)):
            mAnswers = men[y].answers
            total = 0
            for z in range(0, len(wAnswers)):
                total = total + (abs(wAnswers[z]-mAnswers[z]))
            preferenceList.append({men[y], total})
        men[x].preferenceList = preferenceList
#sort
for x in range(0, len(men)):
    women[x].preferenceList = sorted(women[x].preferenceList, key=lambda y: y[1])



