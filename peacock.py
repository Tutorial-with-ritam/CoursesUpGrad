import re
class Solution(object):
    def isNumber(self, s):
        pattern=re.compile(r'^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$')
        return pattern.match(s.strip())
