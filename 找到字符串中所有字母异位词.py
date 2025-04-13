from typing import List
from collections import Counter

class window:
    def __init__(self, s: str):
        self.width = 0
        self.index = 0
        self.s = s
        self.c = Counter()
    
    def set(self, index: int, width: int):
        self.index = index
        self.width = width
        self.c = Counter(self.s[self.begin():self.end()])
    
    def move_n(self, step: int):
        self.set(self.index + step, self.width)
    
    def move_right(self):
        self.c[self.s[self.begin()]] -= 1
        self.c[self.s[self.end()]] += 1
        self.index += 1
    
    def move_left(self):
        self.index -= 1
        self.c[self.s[self.begin()]] += 1
        self.c[self.s[self.end()]] -= 1
    
    def pop_right(self):
        self.c[self.s[self.end()]] -= 1
        self.width -= 1
    
    def pop_left(self):
        self.c[self.s[self.begin()]] -= 1
        self.width -= 1
        self.index += 1
    
    def push_right(self):
        self.c[self.s[self.end()]] += 1
        self.width += 1
    
    def is_on_right(self) -> bool:
        return self.end() == len(self.s)
    
    def is_on_left(self) -> bool:
        return self.index == 0
    
    def begin(self) -> int:
        return self.index
    def end(self) -> int:
        return self.index + self.width

def build_counter(s: str, cp: Counter, width: int) -> int | Counter:
    if width > len(s):
        return len(s)
    c = Counter()
    for r, char in enumerate(reversed(s[:width])):
        i = width - 1 - r
        if cp[char] == 0:
            return i + 1
        c[char] += 1
    return c
    

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cp = Counter(p)
        w = window(s)
        w.index = 0
        w.width = len(p)
        result: list[int] = []
        while True:
            if w.end() > len(s):
                return result
            ic = build_counter(s[w.index:], cp, w.width)
            if isinstance(ic, int):
                w.index += ic
                continue
            w.c = ic
            is_equal = w.c == cp
            if is_equal:
                result.append(w.index)
            while True:
                if w.end() >= len(s):
                    return result
                sb, se = s[w.begin()], s[w.end()]
                if cp[se] == 0:
                    w.index = w.end() + 1
                    break
                if sb == se:
                    w.index += 1
                    if is_equal:
                        result.append(w.index)
                    continue
                w.move_right()
                is_equal = w.c == cp
                if is_equal:
                    result.append(w.index)
        return result
        
            
print(Solution().findAnagrams("baa", "aa"))
