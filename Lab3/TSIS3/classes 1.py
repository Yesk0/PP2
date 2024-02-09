class GetString1:
    def __init__(self):
        self.x = ""

    def get_string(self):
        self.x = input()

    def to_up(self):
        self.x = self.x.upper()

    def print_str(self):
        print(self.x)

string_print = GetString1()

string_print.get_string()

string_print.to_up()

string_print.print_str()





