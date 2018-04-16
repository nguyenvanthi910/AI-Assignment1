#Mô tả những thành phần chính trong game

class Node:
    """
    Mô tả trạng thái của một khối lập phương\n
    name: Tên khối\n
    w: là khối lượng của khối lập phương đó. Mặc định là 1\n
    x: là hoành độ của khối\n
    y: là tung độ\n
    """
    def __init__(self, name, x, y):
        self.name = name
        self.w = 1
        self.x = x
        self.y = y

    def nextTo(self, other):
        """
        Kiểm tra xem có gần khối khác hay không\n
        :return True nếu gần nhau không thì False
        """
        return self.isLeft(other) or self.isRight(other) \
               or self.isUp(other) or self.isDown(other)

    #Kiểm tra nằm bên trái
    def isLeft(self, other):
        return self.x + 1 == other.x and self.y == other.y

    #Kiểm tra nằm bên phải
    def isRight(self, other):
        return self.x - 1 == other.x and self.y == other.y

    #kiểm tra nằm bên trên
    def isUp(self, other):
        return self.y + 1 == other.y and self.x == other.x

    #Kiểm tra nằm bên dưới
    def isDown(self, other):
        return self.y - 1 == other.y and self.x == other.x

    #Kiểm tra xem có nằm chông lên khối khác không
    def top(self, other):
        return self.x == other.x and self.y == other.y

    #Di chuyển lên trên
    def moveup(self, step = 1):
        self.y += step

    #Di chuyển xuống
    def movedown(self, step = 1):
        self.y -= step

    #Di chuyển sang trái
    def moveleft(self, step = 1):
        self.x -= step

    #Di chuyển sang phải
    def moveright(self, step = 1):
        self.x += step

    def __eq__(self, other):
        return other != None and self.top(other)

    def __repr__(self):
        return "%s(%d,%d)" % (self.name, self.x, self.y)

    def _toStringForTest(self):
        return self.name + "(" + str(self.x) + "," + str(self.y) + ")"

class Block:
    """Gồm 2 khối (Node) gộp lại"""
    def __init__(self, node1, node2, control = None):
        """
        A, B : Khối node A và B
        control : Điều khiển hiện tại của khối.
            Mặc định là None cho điều khiển 2 khối cùng lúc.
            A nếu điều khiển A và tương tự B.
        """
        self.A = node1
        self.B = node2
        self.control = control
        self.autoControl()

    def split(self, xA, yA, xB, yB, control):
        """Tách khối liền nhau thành 2 khối và xét điều khiển cho khối"""
        self.A.x = xA
        self.A.y = yA
        self.B.x = xB
        self.B.y = yB
        self.control = control

    def seclectControl(self, x, y):
        """Chọn control bằng tọa độ"""
        tmp = Node("tmp", x, y)
        if tmp == self.A:
            return self.A
        else: return self.B

    def changeControl(self):
        """
        Chuyển điều kiển nếu mà A B kề nhau thì điều khiển là None
        Nếu điều khiển đang là A thì chuyển cho B và ngược lại"""
        if self.A.nextTo(self.B) or self.A.top(self.B):
            self.control = None
        elif self.control == self.A:
            self.control = self.B
        else: self.control = self.A

    def autoControl(self):
        """
        Kiểm tra vị trí A B và tự động chuyển điều khiển nếu cần thiết
        """
        if self.A.nextTo(self.B) or self.A.top(self.B):
            self.control = None

    def getCtrString(self):
        ctr = "both"
        if self.control == None:
            ctr = "both"
        elif self.control is self.A:
            ctr = self.A.name
        else: ctr = self.B.name
        return ctr

    def moveup(self):
        """Di chuyển lên trên"""
        if self.control == None:
            if self.A.isLeft(self.B) or self.A.isRight(self.B):#2 khối nằm ngang
                self.A.moveup()
                self.B.moveup()
            else: #2 khối nằm dọc
                if self.A.isUp(self.B): #A nằm phía trên B
                    self.A.moveup()
                    self.B.moveup(2)
                elif self.A.isDown(self.B):
                    self.A.moveup(2)
                    self.B.moveup()
                else:#Hai khối chông nhau
                    self.A.moveup(2)
                    self.B.moveup()
        elif self.control == self.A: #Điều khiển cho A
            self.A.moveup()
            self.autoControl() #Kiểm tra lại điều khiển
        else: #Điều khiển cho B
            self.B.moveup()
            self.autoControl()

    #Di chuyển xuống
    def movedown(self):
        if self.control == None:
            if self.A.isLeft(self.B) or self.A.isRight(self.B):#2 khối nằm ngang
                self.A.movedown()
                self.B.movedown()
            else: #2 khối nằm dọc
                if self.A.isUp(self.B): #A nằm phía trên B
                    self.A.movedown(2)
                    self.B.movedown()
                elif self.A.isDown(self.B):
                    self.A.movedown(1)
                    self.B.movedown(2)
                else:#2 khối chồng nhau
                    self.A.movedown(2)
                    self.B.movedown()
        elif self.control == self.A: #Điều khiển cho A
            self.A.movedown()
            self.autoControl() #Kiểm tra lại điều khiển
        else: #Điều khiển cho B
            self.B.movedown()
            self.autoControl()

    #Di chuyển sang trái
    def moveleft(self):
        if self.control == None:
            if self.A.isUp(self.B) or self.A.isDown(self.B): #2 khối nằm dọc
                self.A.moveleft()
                self.B.moveleft()
            else: #2 khối nằm ngang
                if self.A.isLeft(self.B):
                    self.A.moveleft()
                    self.B.moveleft(2)
                elif self.A.isRight(self.B):
                    self.A.moveleft(2)
                    self.B.moveleft()
                else: #2 khối chồng nhau
                    self.A.moveleft(2)
                    self.B.moveleft()
        elif self.control == self.A:
            self.A.moveleft()
            self.autoControl()
        else:
            self.B.moveleft()
            self.autoControl()

        #Di chuyển sang trái

    def moveright(self):
        if self.control == None:
            if self.A.isUp(self.B) or self.A.isDown(self.B): #2 khối nằm dọc
                self.A.moveright()
                self.B.moveright()
            else: #2 khối nằm ngang
                if self.A.isLeft(self.B):
                    self.A.moveright(2)
                    self.B.moveright()
                elif self.A.isRight(self.B):
                    self.A.moveright()
                    self.B.moveright(2)
                else: #2 khối chồng nhau
                    self.A.moveright(2)
                    self.B.moveright()
        elif self.control == self.A:
            self.A.moveright()
            self.autoControl()
        else:
            self.B.moveright()
            self.autoControl()

    def weight(self):
        """Khối lượng của tại block nếu nằm kể là 1 và chồng lên nhau là 2"""
        if self.A.top(self.B):
            return 2
        else: return 1

    def __eq__(self, other):
        """hai Block bằng nhau khi vị trí của các node bằng nhau"""
        return self.A.top(other.A) and self.B.top(other.B)

    def __repr__(self):
        return "[%s(%s %s]" % (self.getCtrString(), self.A, self.B)

    def _toStringForTest(self):
        return "[" + str(self.A._toStringForTest()) + " ; " + str(self.B._toStringForTest()) + "]"

class Point:
    """
    Điểm trên bản đồ\n
    w: trọng số chịu tải khối lượng hiện tại.
    wBefore: trọng số chịu tải trước đó. Lưu nếu toggle sẽ restore lại
    """
    def __init__(self, w, wBefore = 2):
        self.w = w
        self.wBefore = wBefore

    def toggle(self):
        if self.w == self.wBefore:
            self.w = 0
        else: self.w = self.wBefore

    def hide(self):
        self.w = 0

    def show(self):
        self.w = self.wBefore

    def isValid(self, w):
        return self.w >= w

    def __repr__(self):
        return "%d\t\t" % (self.w)


#Mô tả nút nhấn trên bản đồ (map)
#Có những loại nút nhân sau
#Toggle: Đó là mỗi lần nhấn nó tắt/hiện thêm ô cho map.
    #Ngoài ra nó còn có trọng số khối lượng. Ví dụ có nút nhấn
    #phãi 2 ô chồng nhau mới có tác  dụng.
#Show: Đó là khi nhấn vào nó sẽ hiện thêm ô cho map và nhấn lần nữa nó sẽ không có tác dụng
    #Nó cũng có trọng số khối lượng như Toggle.
#Hide: Tương tự như Up nhưng nó ẩn ô trên map
#Split: Nút này có tác dụng chia đôi Block thành 2 khối lập phương. Cũng có trọng số khối lượng.
#Đây là key để phân biệt các loại button
TOGGLEBTN = 'TG'
SHOWBTN = 'SH'
HIDEBTN = 'HI'
SPLITBTN = 'SP'
GOAL = 'GL'

class Button(Point):
    """
    Nút nhấn có trên bản đồ\n
    type: là 1 trong 4 loại được mô tả ở trên\n
    lsPoint: là danh sách các điểm mà nó có tác dụng.
    """
    def __init__(self, type, w, lsPoint):
        self.type = type
        self.lsPoint = lsPoint
        self.w = w

    def enable(self, block):
        if block.weight() >= self.w:
            if self.type == TOGGLEBTN:
                for i in self.lsPoint:
                    i.toggle()
            elif self.type == SHOWBTN:
                for i in self.lsPoint:
                    i.show()
            elif self.type == HIDEBTN:
                for i in self.lsPoint:
                    i.hide()
            elif self.type == SPLITBTN:
                block.split(self.lsPoint[0].x, self.lsPoint[0].y,
                            self.lsPoint[1].x, self.lsPoint[1].y,
                            block.seclectControl(self.lsPoint[0].x, self.lsPoint[0].y))
##
    def isGoal(self):
        return type == GOAL

    def __repr__(self):
        return "%d(%s)\t" % (self.w, self.type)

class Map:
    """
    Chứa ma trận Point
    """
    def __init__(self, name, row, col, matrix):
        self.name = name
        self.row = row
        self.col = col
        self.matrix = matrix

    def __isOnMap(self, x, y):
        return x >= 0 and y >= 0 and x < self.col and y < self.row

    def isOnMap(self, block):
        return self.__isOnMap(block.A.x, block.A.y) and \
               self.__isOnMap(block.B.x, block.B.y)


    def isValid(self, block):
        if self.isOnMap(block):
            A = block.A
            B = block.B
            if type(self.matrix[A.x][A.y]) is Point and \
               self.matrix[A.x][A.y].isValid(block.weight()) and \
               type(self.matrix[B.x][B.y]) is Point and \
                self.matrix[B.x][B.y].isValid(block.weight()):
                return True
        return False
    def isGoal(self, block):
        A = block.A
        return block.weight() == 2 and self.matrix[A.x][A.y].isGoal()

    def enableButton(self, block):
        A = block.A
        B = block.B
        if A.top(B) :
            if type(self.matrix[A.x][A.y]) is Button :
                self.matrix[A.x][A.y].enable(block)
        else :
            if(type(self.matrix[A.x][A.y]) is Button):
                self.matrix[A.x][A.y].enable(block)
            if(type(self.matrix[B.x][B.y]) is Button):
                self.matrix[B.x][B.y].enable(block)

    def __repr__(self):
        return "\t%s\nSize: %d x %d\n\n" % (self.name, self.row, self.col) + "\n".join(str(i) for i in self.matrix)



