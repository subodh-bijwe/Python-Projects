class Node:
    def __init__(self) -> None:
        self.links = [None] * 26
        self.flag = False
        self.meaning = ""
        
    def containsKey(self, ch):
        return self.links[ord(ch) - ord("a")] is not None
    
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node 
    
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    
    def setEnd(self, meaning):
        self.flag = True
        self.meaning = meaning
        
    def isEnd(self):
        return self.flag, self.meaning

class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word, type, meaning):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
        node.setEnd(meaning)
    
    def search(self, word):
        node = self.root 
        for ch in word:
            if not node.containsKey(ch):
                return False, ""
            node = node.get(ch)
        return node.isEnd()
    
    def startsWith(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True
  

import csv

class WordTraversal:
    def __init__(self) -> None:
        self.trie = Trie()
        self.process_csv()
    
    def process_csv(self):
        with open('dictionary.csv', mode ='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                self.create_trie(lines)
                
    def create_trie(self, line):
        try:
            self.trie.insert(line[0].lower(), line[1], line[2])
            print("processed word: ", line[0])
        except:
            pass
    
    def search_in_trie(self, word):
        exists, meaning = self.trie.search(word.lower())
        if exists:
            return {word: meaning}
        return {word: "Apologies, word does not exists!"}
    