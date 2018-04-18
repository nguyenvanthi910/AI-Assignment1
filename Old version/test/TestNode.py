from src import Elements
import unittest

class TestNode(unittest.TestCase):

    def test_moveright(self):
        a = Elements.Node("a", 0, 0)
        b = Elements.Node("b", 0, 0)
        a.moveright()
        self.assertTrue(a.isRight(b))

    def test_moveleft(self):
        a = Elements.Node("a", 0, 0)
        b = Elements.Node("b", 0, 0)
        a.moveleft()
        self.assertTrue(a.isLeft(b))

    def test_moveup(self):
        a = Elements.Node("a", 0, 0)
        b = Elements.Node("b", 0, 0)
        a.moveup()
        self.assertTrue(a.isUp(b))

    def test_movedown(self):
        a = Elements.Node("a", 0, 0)
        b = Elements.Node("b", 0, 0)
        a.movedown()
        self.assertTrue(a.isDown(b))

    def test_movedown(self):
        a = Elements.Node("a", 0, 0)
        b = Elements.Node("b", 0, 0)

        self.assertTrue(a.top(b))

if __name__ == '__main__':
    unittest.main()