code_a = ord('a')

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

class Quiz:
    def __init__(self, path):
        self.file_path = path
        self.items = 0
    
    def add(self):
        questions = []
        while(True):
            print("Question", self.items + 1, ": Input --1 in question to stop")
        
            temp = Question()
            temp.question = input("Input Question: ")

            if temp.question == "--1": break
            
            for idx in range(4):
                letter = chr(code_a + idx)
                option = input("Input option " + letter + " :")
                temp.add_option(letter, option)

            ans = ""
            while(not(ans in ['a', 'b', 'c', 'd'])):
                ans = input("Input correct option: ")
            temp.answer = ans

            questions.append(temp)
            self.items += 1
        self.write_to_file(questions)
        
    def write_to_file(self, questions):
        file = open(self.file_path, 'a')
        block = " " * 4
        inp_txt = []
        
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
            
            
        for txt in inp_txt:
            file.write(txt + "\n")
        
        file.close()
                    
if __name__ == "__main__":
    file_path = "quiz_data.txt"
    quiz = Quiz(file_path)
    quiz.add()
