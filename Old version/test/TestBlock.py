import unittest
from src.Elements import Block
from src.Elements import Node

class TestBlock(unittest.TestCase):
    #Test sau khi di chuyển các khối chồng nhau, block điều khiển 2 khối
    def test_moveup(self):
        a = Node("a", 0, 0)
        b = Node("b", 0, 1)
        block = Block(a,b)

        block.moveup()
        self.assertTrue(a.top(b))

    def test_movedown(self):
        a = Node("a", 0, 0)
        b = Node("b", 0, 1)
        block = Block(a,b)

        block.movedown()
        self.assertTrue(a.top(b))

    def test_moveright(self):
        a = Node("a", 0, 0)
        b = Node("b", 1, 0)
        block = Block(a,b)

        block.moveright()
        self.assertTrue(a.top(b))

    def test_moveleft(self):
        a = Node("a", 0, 0)
        b = Node("b", 1, 0)
        block = Block(a,b)

        block.moveleft()
        self.assertTrue(a.top(b))

    #Test1 sau khi di chuyển trạng thái vẫn như cũ, block điều khiển 2 khối
    def test_moveup1(self):
        a = Node("a", 0, 0)
        b = Node("b", 1, 0)
        block = Block(a,b)

        self.assertTrue(a.isLeft(b))
        block.moveup()
        self.assertTrue(a.isLeft(b))

    def test_movedown1(self):
        a = Node("a", 0, 0)
        b = Node("b", 1, 0)
        block = Block(a,b)
        self.assertTrue(b.isRight(a))
        block.movedown()
        self.assertTrue(a.isLeft(b))

    def test_moveright1(self):
        a = Node("a", 0, 0)
        b = Node("b", 0, 1)
        block = Block(a,b)
        self.assertTrue(a.isDown(b))
        block.moveright()
        self.assertTrue(b.isUp(a))

    def test_moveleft1(self):
        a = Node("a", 0, 0)
        b = Node("b", 0, 1)
        block = Block(a,b)
        self.assertTrue(a.isDown(b))
        block.moveleft()
        self.assertTrue(b.isUp(a))

    #Test2 sau khi di chuyển điều khiển chuyển sang 2 khối
    #Hiện tại điều khiển là khối A
    def test_moveup2(self):
        a = Node("a", 1, 0)
        b = Node("b", 0, 1)
        block = Block(a,b)
        block.control = a

        self.assertFalse(b.isLeft(a))
        block.moveup()
        self.assertTrue(b.isLeft(a))

    def test_movedown2(self):
        a = Node("a", 0, 1)
        b = Node("b", 1, 0)
        block = Block(a,b)
        block.control = a

        self.assertFalse(a.isLeft(b))
        block.movedown()
        self.assertTrue(a.isLeft(b))

    def test_moveright2(self):
        a = Node("a", 0, 1)
        b = Node("b", 1, 0)
        block = Block(a,b)
        block.control = a

        self.assertFalse(a.isDown(b))
        block.moveright()
        self.assertTrue(a.isUp(b))

    def test_moveleft2(self):
        a = Node("a", 1, 0)
        b = Node("b", 0, 1)
        block = Block(a,b)
        block.control = a

        self.assertFalse(a.isDown(b))
        block.moveleft()
        self.assertTrue(a.isDown(b))

    #Test3 chuyển điều khiển giữa 2 khối với nhau
    def test_toggle_control(self):
        a = Node("a", 0, 0)
        b = Node("b", 3, 0)
        block = Block(a, b, a)

        block.moveright()

        block.changeControl()

        block.moveleft()

        self.assertEqual(block.control, None)


if __name__ == '__main__':
    unittest.main()