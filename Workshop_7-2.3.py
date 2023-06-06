with open("check_quotes.txt", "r") as line:
    def check_quotes(line):
        single_quotes = 0
        double_quotes = 0
        for char in line:
            if char == "":
                single_quotes += 1
            elif char == "":
                double_quotes += 1
        if single_quotes % 2 == 0 and double_quotes % 2 == 0:
            return True
        else:
            return False