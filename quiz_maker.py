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
    def __init__(self):
        self.temp = 0
        self.items = 0

    def new(self, file_path):
        file = open(file_path, 'w')
        file.close()
    
    def add(self, file_path):
        file = open(file_path, 'a')

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


            file.write(temp.question)
            for idx in range(4):
                letter = chr(code_a + idx)
                file.write(letter + " " + temp.options[letter])
            file.write(ans)


            self.items += 1
        
        file.close()

if __name__ == "__main__":
    file_path = "quiz_data.txt"
    quiz = Quiz()
    quiz.add(file_path)
