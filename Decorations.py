import re
def validate_email(func):
    def wrapper(self, value):
        pattern = r'\w+@\w+\.\w+' 
        rule = re.compile(pattern)
        valid = rule.search(value)
        print(valid)
        func(self, value)
    return wrapper
        