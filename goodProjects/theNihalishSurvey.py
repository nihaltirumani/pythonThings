#The Nihal-ish survey
print("This the Nihal-ish survey!!!")
print("To know how much are you like me.")

#varibles
user_answer = ""
survey_score = 0
question_no = 0

#question maker
def makeq(question, answer):
    global user_answer, survey_score, question_no

    question_no += 1
    question = question + "\n" 

    print("Question number", question_no)
    user_answer = input(question)

    if user_answer.lower() == answer:
        survey_score += 1
    
#questions
makeq("Do you like python?", "yes")
makeq("Do you like making games?", "yes")
makeq("What color do you like?", "yellow")
makeq("Do you like to eat curd?", "yes")
makeq("What is your favourite number?", "2")
makeq("What is the most irritating thing in Python?", "classes")
makeq("What is your favourite subject?", "maths")
makeq("What is your fovourite sport?", "basketball")
makeq("What Python module do you like?", "pygame")

#result
nihalishPercentage = str(round((survey_score / question_no) * 100)) + "%"
print("Your survey score:", str(survey_score) + "/" + str(question_no))
print("Nihal-ish percentage:", nihalishPercentage)

if nihalishPercentage == "100%":
    print("Wow, your purely nihal-ish!!")