class Question:
    def __init__(self, quest = "", opts = ["", "", "", ""], ans = ""):
        self.question = quest
        self.answer = ans
        self.options = {
            "a": opts[0],
            "b": opts[1],
            "c": opts[2],
            "d": opts[3]
        }

    def add_option(self, choice, option):
        self.options[choice] = option

    def print(self, number = -1):
        if number != -1:
            print(str(number) + ". ", end = "")
        print("Question: ", self.question)
        for letter in self.options:
            print("  " + letter + ". " + self.options[letter])
        print("  Answer: " + self.answer) 

class Quiz:
    def __init__(self, path):
        self.file_path = path
        self.questions = []
        self.items = 0
    
    def append(self, Question quest):
        if not quest.ans in quest.options.keys(): return False
        self.questions.append(quest)
        self.write_to_file([quest])
        self.items += 1
        return True

    def add(self):
        stop_query = "save"
        quests_to_add = []
        while(True):
            print("Question", self.items + 1, ": Input \"" + stop_query + "\" in question to record inputs")

            #QUESTION INPUTS
            temp = Question()
            temp.question = input("Input Question: ")

            if temp.question == stop_query: break

            #OPTIONS INPUTS
            for letter in temp.options:
                option = input("Input option " + letter + " : ")
                temp.add_option(letter, option)

            #ANSWER INPUTS
            ans = ""
            while(not(ans in temp.options.keys())):
                ans = input("Input correct option: ")
            temp.answer = ans

            self.questions.append(temp)
            quests_to_add.append(temp)
            self.items += 1
        self.write_to_file(quests_to_add)
        
    def write_to_file(self, questions):
        file = open(self.file_path, 'a')
        block = " " * 4
        inp_txt = []
        
        for item in questions:
            inp_txt.append("{")
            inp_txt.append(block + "\"Question\": " + item.question)
            inp_txt.append(block + "{")
            for letter in item.options:
                inp_txt.append(block * 2 + "\"" + letter + "\": " + item.options[letter])
            inp_txt.append(block + "}")
            inp_txt.append(block + "\"Answer\": " + item.answer)
            inp_txt.append("}")

            if item != questions[-1]:
                inp_txt[-1] += ","
            
        for txt in inp_txt:
            file.write(txt + "\n")
        
        file.close()

    def print(self):
        for idx in range(len(self.questions)):
            self.questions[idx].print(idx + 1)
            
if __name__ == "__main__":
    file_path = "quiz_data.txt"
    quiz = Quiz(file_path)
    quiz.add()
    
