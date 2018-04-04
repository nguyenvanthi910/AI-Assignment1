from src import Elements

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def readFrom(filename):
    """
    Format file:
    Tên map
    num1 num2 : Số hàng và số cột
    Ma trận num1 x num2
    ### Thông tin khác
    SH w x y
    <danh sách tọa độ>
    HI w x y
    <danh sách tọa độ>
    TG w x y
    <Danh sách tọa độ>
    SP w x y
    <Danh sách tọa độ, control được xét cho tọa độ đầu tiên>
    IN
    <Danh sách tọa độ>
    EN
    <Danh sách tọa độ>
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        name = next(file)
        r, c = [int(x) for x in next(file).split()]
        matrix = list()
        blockarr = []
        isMatrix = True
        for line in file:
            if line.startswith("###"): isMatrix = False
            if isMatrix:
                matrix.append([Elements.Point(int(x)) for x in line.split()])
            elif line.startswith("SH"):#Show
                tmp = line.split()
                tmp.pop(0)
                w, x, y = [int(i) for i in tmp]
                nextline = [int(x) for x in next(file).split()]
                sh = Elements.Button(Elements.SHOWBTN, w, [])
                for i, j in pairwise(nextline):
                    sh.lsPoint.append(matrix[i][j])
                matrix[x][y] = sh
            elif line.startswith("HI"):#Hide
                tmp = line.split()
                tmp.pop(0)
                w, x, y = [int(i) for i in tmp]
                nextline = [int(x) for x in next(file).split()]
                sh = Elements.Button(Elements.HIDEBTN, w, [])
                for i, j in pairwise(nextline):
                    sh.lsPoint.append(matrix[i][j])
                matrix[x][y] = sh
            elif line.startswith("TG"):#Toggle
                tmp = line.split()
                tmp.pop(0)
                w, x, y = [int(i) for i in tmp]
                nextline = [int(x) for x in next(file).split()]
                sh = Elements.Button(Elements.TOGGLEBTN, w, [])
                for i, j in pairwise(nextline):
                    sh.lsPoint.append(matrix[i][j])
                matrix[x][y] = sh
            elif line.startswith("SP"):#split
                tmp = line.split()
                tmp.pop(0)
                w, x, y = [int(i) for i in tmp]
                nextline = [int(x) for x in next(file).split()]
                sh = Elements.Button(Elements.SPLITBTN, w, [])
                for i, j in pairwise(nextline):
                    sh.lsPoint.append(matrix[i][j])
                matrix[x][y] = sh
            elif line.startswith("EN"):#GOAL
                nextline = [int(x) for x in next(file).split()]
                for i, j in pairwise(nextline):
                    matrix[i][j] = Elements.Button(Elements.GOAL, 3, [])
            elif line.startswith("IN"):#Init Block
                blockarr = [int(x) for x in next(file).split()]

        map = Elements.Map(name, r, c, matrix)
        a = Elements.Node("a", blockarr[0], blockarr[1])
        b = Elements.Node("b", blockarr[2], blockarr[3])
        block = Elements.Block(a, b, a)
    file.close()
    return (map, block)