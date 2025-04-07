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
        code_a = ord('a')
        if number != -1:
            print(str(number) + ". ", end = "")
        print("Question: ", self.question)
        for idx in range(4):
            letter = chr(code_a + idx)
            print("  " + letter + ". " + self.options[letter])
        print("  Answer: " + self.answer) 

class Quiz:
    def __init__(self, path):
        self.file_path = path
        self.questions = []
        self.items = 0
    
    def add(self):
        stop_query = "save"
        quests_to_add = []
        code_a = ord('a')
        while(True):
            print("Question", self.items + 1, ": Input \"" + stop_query + "\" in question to record inputs")

            #QUESTION INPUTS
            temp = Question()
            temp.question = input("Input Question: ")

            if temp.question == stop_query: break

            #OPTIONS INPUTS
            for idx in range(4):
                letter = chr(code_a + idx)
                option = input("Input option " + letter + " : ")
                temp.add_option(letter, option)

            #ANSWER INPUTS
            ans = ""
            while(not(ans in ['a', 'b', 'c', 'd'])):
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
        code_a = ord('a')
        
        for item in questions:
            inp_txt.append("{")
            inp_txt.append(block + "\"Question\": " + item.question)
            inp_txt.append(block + "{")
            for idx in range(4):
                letter = chr(code_a + idx)
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
            self.questions[idx + 1].print(idx)
            
if __name__ == "__main__":
    file_path = "quiz_data1.txt"
    quiz = Quiz(file_path)
    quiz.add()
    quiz.print()
