from random import randint

class ask:
\tdef __init__(self):
\t\tself.good = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."] # 1 2 3 5 4 3 6 3 4 1 2
\t\tself.maybe = ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again."] # 5 5 3 10 1
\t\tself.no = ["My reply is no.", "My sources say no.", "Outlook not so good.", "Don't count on it.", "Very doubtful."] # 2 2 4 5 7
\tdef choose(self):
\t\tchoice = randint(0, 2)
\t\tif choice == 0:
\t\t\toption = randint(0, 34)
\t\t\tif option == 0:
\t\t\t\treturn(self.good[0])
\t\t\telif option >= 1 and option <= 2:
\t\t\t\treturn(self.good[1])
\t\t\telif option >= 3 and option <= 5:
\t\t\t\treturn(self.good[2])
\t\t\telif option >= 6 and option <= 9:
\t\t\t\treturn(self.good[3])
\t\t\telif option >= 10 and option <= 14:
\t\t\t\treturn(self.good[4])
\t\t\telif option >= 15 and option <= 18:
\t\t\t\treturn(self.good[5])
\t\t\telif option >= 19 and option <= 21:
\t\t\t\treturn(self.good[6])
\t\t\telif option >= 22 and option <= 27:
\t\t\t\treturn(self.good[7])
\t\t\telif option >= 28 and option <= 30:
\t\t\t\treturn(self.good[8])
\t\t\telif option >= 31 and option <= 34:
\t\t\t\treturn(self.good[9])
\t\t\telse:
\t\t\t\tprint("Error. 8 Ball is out of service.")
\t\t\t\texit()
\t\telif choice == 1:
\t\t\toption = randint(0, 23)
\t\t\tif option >= 0 and option <= 4:
\t\t\t\treturn(self.maybe[0])
\t\t\telif option >= 5 and option <= 9:
\t\t\t\treturn(self.maybe[1])
\t\t\telif option >= 10 and option <= 12:
\t\t\t\treturn(self.maybe[2])
\t\t\telif option >= 13 and option <= 22:
\t\t\t\treturn(self.maybe[3])
\t\t\telif option == 23:
\t\t\t\treturn(self.maybe[4])
\t\t\telse:
\t\t\t\tprint("Error. 8 Ball is out of service.")
\t\t\t\texit()
\t\telif choice == 2:
\t\t\toption = randint(0, 19)
\t\t\tif option >= 0 and option <= 1:
\t\t\t\treturn(self.no[0])
\t\t\telif option >= 2 and option <= 3:
\t\t\t\treturn(self.no[1])
\t\t\telif option >= 4 and option <= 7:
\t\t\t\treturn(self.no[2])
\t\t\telif option >= 8 and option <= 12:
\t\t\t\treturn(self.no[3])
\t\t\telif option >= 13 and option <= 19:
\t\t\t\treturn(self.no[4])
\t\t\telse:
\t\t\t\tprint("Error. 8 Ball is out of service.")
\t\t\t\texit()
