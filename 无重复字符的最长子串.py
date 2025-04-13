
class table:
    def __init__(self):
        self.value: dict[str, int] = {}
        self.repeat: int = 0
    
    def no_repeat(self) -> bool:
        return self.repeat == 0
    
    def push(self, char: str):
        if char not in self.value:
            self.value[char] = 1
            return
        if self.value[char] == 1:
            self.repeat += 1
        self.value[char] += 1
    
    def pop(self, char: str):
        assert char in self.value and self.value[char] > 0
        if self.value[char] == 2:
            self.repeat -= 1
        self.value[char] -= 1

class window:
    def __init__(self, s: str):
        self.t = table()
        self.s = s
        self.width = 0
        self.index = 0
    
    def set(self, index: int, width: int):
        self.t = table()
        self.index = index
        self.width = width
        for char in self.s[self.index: self.index + self.width]:
            self.t.push(char)
    
    def move_right(self):
        self.t.pop(self.s[self.index])
        self.t.push(self.s[self.index + self.width])
        self.index += 1
    
    def move_left(self):
        self.index -= 1
        self.t.pop(self.s[self.index + self.width])
        self.t.push(self.s[self.index])
    
    def pop_right(self):
        self.width -= 1
        self.t.pop(self.s[self.index + self.width])
    def pop_left(self):
        self.width -= 1
        self.t.pop(self.s[self.index])
        self.index += 1
    
    def push_right(self):
        self.t.push(self.s[self.index + self.width])
        self.width += 1
    
    def is_on_right(self) -> bool:
        return self.index + self.width == len(self.s)
    
    def is_on_left(self) -> bool:
        return self.index == 0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = window(s)
        w.set(0, 0)
        max_width = 0
        while True:
            if w.is_on_right():
                break
            w.push_right()
            if w.t.no_repeat():
                max_width = max(max_width, w.width)
                continue
            w.pop_right()
            w.move_right()
            max_width = max(max_width, w.width)
        return max_width
            
                
s = Solution()

print(s.lengthOfLongestSubstring(" "))