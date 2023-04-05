class LFA_Automaton:
    def __init__(self):
        self.state = 0
        self.counter = 0


    def process_input(self, char):
        if self.state == 0:
            if char == 'L':
                self.state = 1
                self.counter += 1

        elif self.state == 1:
            if char == 'F':
                self.state = 2
                self.counter += 1
            else:
                self.state = 0
        elif self.state == 2:
            if char == 'A':
                self.state = 3
                self.counter += 1
            else:
                self.state = 0
        elif self.state == 3:
            self.counter += 1

    def reset(self):
            self.state = 0
            self.counter = 0

def find_lfa(string):
    automaton = LFA_Automaton()
    for char in string:
        automaton.process_input(char)
    count = automaton.counter
    automaton.reset()
    return count    

#coloque no string o input
string = "LFALFA"
count = find_lfa(string)
print(count)