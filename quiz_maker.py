class Question:
    def __init__(self, quest, opts = [], ans = ""):
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
        temp = 0

    def new(self, file_path):
        file = open(file_path, 'w')
        file.close()
    
    def add(self, file_path):
        file = open(file_path, 'a')

        while(True):
            pass
        
        file.close()

if __name__ == "__main__":
    quiz = Quiz()
    
