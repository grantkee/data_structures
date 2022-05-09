import unittest

class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, item):
        return self.q.append(item)

    def dequeue(self):
        if self.size < 1:
            return None
        return self.q.pop(0)

    def display(self):
        return self.q

    def size(self):
        return len(self.q)

class TestStack(unittest.TestCase):
    def test_init(self):
        s = Queue()
        self.assertAlmostEqual([], s.q)

    def test_is_empty(self):
        s1 = Queue()
        s2 = Queue()
        s2.push("test")
        self.assertAlmostEqual(True, s1.is_empty())
        self.assertAlmostEqual(False, s2.is_empty())

    def test_push(self):
        s = Queue()
        s.push("test")
        s.push("test2")
        self.assertAlmostEqual("test", s.q[0])
        self.assertAlmostEqual(2, len(s.q))

    def test_pop(self):
        s = Queue()
        s.push("test")
        s.push("test2")
        self.assertAlmostEqual("test2", s.pop())
        self.assertAlmostEqual(1, len(s.q))

    def test_peek(self):
        s = Queue()
        s.push("test")
        s.push("test2")
        self.assertAlmostEqual("test2", s.peek())
        self.assertAlmostEqual(2, len(s.q))

    def test_size(self):
        s = Queue()
        s.push("test")
        s.push("test2")
        self.assertAlmostEqual(2, s.size())

if __name__ == "__main__":
    unittest.main()
