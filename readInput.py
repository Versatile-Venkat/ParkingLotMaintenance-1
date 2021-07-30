class ReadInput:
  #opens the input file in the same environment and converts it into a list of commands
    def getInput(self):
      lines=[]
      with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
      return lines