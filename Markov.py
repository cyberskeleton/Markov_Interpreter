from Rule import Rule


def create_ruleset(rules):
    ruleset = []
    for s in rules:
        ruleset.append(Rule(s))
    return ruleset


def replace_pattern(string, pattern, replacement):
    return replacement.join(string.split(pattern, 1))


def markov(input_string, ruleset):
    ruleset_length = len(ruleset)
    i = 0
    rules_apply = ruleset_length
    while True:
        rule = ruleset[i]
        if rule.pattern in input_string:
            input_string = replace_pattern(input_string, rule.pattern, rule.replacement)
            i = 0
            rules_apply = ruleset_length
            if rule.is_terminal:
                return input_string
        else:
            rules_apply -= 1
            i += 1
        if rules_apply == 0:
            return input_string
