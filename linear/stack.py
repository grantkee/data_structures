import unittest

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        return self.stack.insert(0, item)

    def pop(self):
        result = None
        if not self.is_empty():
            result = self.stack.pop(0)
        return result

    def peek(self):
        result = None
        if not self.is_empty():
            result = self.stack[0]
        return result

    def size(self):
        return len(self.stack)

class TestStack(unittest.TestCase):
    def test_init(self):
        s = Stack()
        self.assertAlmostEqual([], s.stack)

    def test_is_empty(self):
        s = Stack()
        self.assertAlmostEqual(True, s.is_empty())

    def test_push(self):
        s = Stack()
        s.push("test")
        s.push("test2")
        self.assertAlmostEqual(2, len(s.stack))
        self.assertAlmostEqual("test2", s.stack[0])

    def test_pop(self):
        s1 = Stack()
        s2 = Stack()
        s1.push("test")
        s1.push("test2")
        self.assertAlmostEqual("test2", s1.pop())
        self.assertAlmostEqual(1, len(s1.stack))
        self.assertAlmostEqual(None, s2.pop())

    def test_peek(self):
        s1 = Stack()
        s2 = Stack()
        s1.push("test")
        s1.push("test2")
        self.assertAlmostEqual("test2", s1.peek())
        self.assertAlmostEqual(2, len(s1.stack))
        self.assertAlmostEqual(None, s2.peek())

    def test_size(self):
        s1 = Stack()
        s2 = Stack()
        s1.push("test")
        s1.push("test2")
        self.assertAlmostEqual(2, s1.size())
        self.assertAlmostEqual(0, s2.size())

if __name__ == "__main__":
    unittest.main()
