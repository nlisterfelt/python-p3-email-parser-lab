import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        patternSplit = re.compile(r'[ \,]+')
        patternFilter = re.compile(r'[a-z\.]+\@\w+\.com')
        emailList = sorted(re.split(patternSplit, self.emails))
        return [x for x in emailList if re.match(patternFilter, x)]
