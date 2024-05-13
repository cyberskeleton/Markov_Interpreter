class Rule:
    def __init__(self, rule_string):
        self.is_terminal = False
        self.pattern, self.replacement = self.get_pattern_replacement(rule_string)

    # Return true if there are only whitespace characters in the string and there is at least one character,
    # false otherwise.
    def is_space(self, rule_string):
        return rule_string.isspace()

    def get_pattern_replacement(self, rule_string):
        split_string = rule_string.split(" -> ")
        pattern_temp, replacement_temp = split_string[0].strip(), split_string[1].strip()
        if replacement_temp[:1] == ".":
            self.is_terminal = True
            replacement_temp = replacement_temp[1:]
        return pattern_temp, replacement_temp

    def show(self):
        print(self.pattern, "->", self.replacement)
