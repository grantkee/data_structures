import unittest

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        return self.stack.insert(0, item)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

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
        self.assertAlmostEqual(1, len(s.stack))

    def test_pop(self):
        s = Stack()
        s.push("test")
        self.assertAlmostEqual("test", s.pop())
        self.assertAlmostEqual(0, len(s.stack))

    def test_peek(self):
        s = Stack()
        s.push("test")
        self.assertAlmostEqual("test", s.peek())
        self.assertAlmostEqual(1, len(s.stack))

    def test_size(self):
        s = Stack()
        s.push("test")
        s.push("test2")
        self.assertAlmostEqual(2, s.size())

if __name__ == "__main__":
    unittest.main()
