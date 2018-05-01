# AI-Assignment1
Hiện thực solution cho game block and hole

## Cấu trúc thư mục
    src Chứa tất cả source code
    test Chứa tất cả testcase
    document chứa tài liệu tham khảo cũng như report
    
## Mô hình hoạt động 
### Các đối tượng
    - Point: Mô tả một điểm trên bản đồ. Điểm này có trọng số chịu  tải
    khối lượng. Nếu điểm này mà Block có thể đứng được thì nó có trọng số 
    khối lượng là dương (điểm 'nền'). Điểm nền có thể có 2 giá trị là 1 hoặc 
    2 (1 thì cho phép 1 Node đứng trên nó, 2 cho phép 2 block). Còn các điểm 
    còn lại không cho phép block đứng trên nó đều có trọng số là 0. Đối với
    điểm kết thúc thì có trọng số là 3.
    
    - Map: 
        - Là ma trận các điểm (Point)
    
    - Node: Mô tả một khối lập phương có khối lượng mặc định là 1, và vị trí 
    của khối này trên bản đồ.
    
    - Block: Mô tả hình hộp chữ nhật gồm 2 Node gộp lại. Trên mỗi block có phân
    chia quyền điều khiển. Nếu 2 Node hợp thành 1 thì quyền điều khiển là chung.
    Nếu nó tách ra làm 2 thì quyền điều khiển là 1 trong 2 Node.
    
    - Button: Mô tả những nút có trên bản đồ (map) ví dụ Toggle, Hihe, Show, 
    Split. Đây là đối tượng đặc biệt nằm trên bản dồ nên nó là con của đối tượng
    Point. Lúc này trọng số chịu tải khối lượng của nó dùng để áp dụng chức năng
    của nó.
        - Toggle: là nút điều khiển một số Point nào đó trên bản đồ. Khi block
        đi qua nút này thì nó ẩn/hiện 'nền' tại vị trí nó quy định (thực tế là
        toggle trọng số 0 thành 1 or 2.
        - Hide: là nút mà block đi qua thì sẽ làm ẩn một vài điểm mà nó quy định
        trên bản đò.
        - Show: Cũng như Hide mà thay vì ẩn thì nó là hiện.
        - Split: là nút tách đôi block thành 2 Node
        
        Ví dụ: Toggle có trọng số là 2 thì chức năng của nó được thực hiện khi
        block là 2 node chông lên nhau đè lên nút toggle.
    
    Đối tượng mô tả trạng thái để áp dụng giải thuật
    - State: Mô tả trạng thái của bài toán gồm có Block và parent (trạng thái trước)
    
### Mô hình
    State: Block
    Goal: Block là 2 khối chồng nhau và vị trí của nó ở vị trí Goal trên ban đồ
    Move: Thay đổi vị trí của Block trên bản đồ.
        Trạng thái hợp lệ:
            - Vị trí của các Node trong block phãi thuộc bản đồ.
            - Khi hiệu khối lượng của block và trọng số trên bản đồlà dương.
        
### Hoạt động của chương trình
    1. Load bản đồ theo fomat từ file txt vào đối tượng Map, Block
        Fomat:
        - Bản đồ là ma trận hình chữ nhật bất kì tùy theo level trong game
        - Nếu vị trí đó không phải là nền thì là 0 nếu là nền thì 1 hoặc 2
        - Nếu là Toggle là T(x) với x là trọng số 1 hoặc 2
        - Show: S(x) tương tự Toggle
        - Hide: H(x)
        - Goal: G : điểm kết thúc
        - Init: I(x) điểm bắt đầu. Nếu x là 2 thì bắt đầu là 2 khối chồng nhau và trên bản đồ chỉ có 1 I.
        Trường hợp 2 khối kề nhau thì trên bản đồ là 2 điểm I(1). Trường hợp 2 điểm I không kề nhau thì I(0)
        và I(1) với I(0) là điểm được xét điều khiển cho nó.
    2. Thực hiện việc chuyển trạng thái cho tới khi đến mục tiêu
    
### Giải thuật sử dụng
    Depth first search
    Breadth first search
    
    Cố gắng tìm ra hàm lượng giá để áp dụng heuristic


Level 01 - code : 780464    v
Level 02 - code : 290299    v
Level 03 - code : 918660    v
Level 04 - code : 520967    v
Level 05 - code : 028431    v
Level 06 - code : 524383    v
Level 07 - code : 189493    v
Level 08 - code : 499707    v
Level 09 - code : 074355    v
Level 10 - code : 300590    v
Level 11 - code : 291709    v
Level 12 - code : 958640    v
Level 13 - code : 448106    v
Level 14 - code : 210362    v
Level 15 - code : 098598    fail
Level 16 - code : 000241    fail
Level 17 - code : 683596    v
Level 18 - code : 284933    v
Level 19 - code : 119785    v
Level 20 - code : 543019    fail
Level 21 - code : 728724    v
Level 22 - code : 987319    v
Level 23 - code : 293486    fail
Level 24 - code : 088198    fail
Level 25 - code : 250453    v
Level 26 - code : 426329    fail
Level 27 - code : 660141    v
Level 28 - code : 769721    fail
Level 29 - code : 691859    fail
Level 30 - code : 280351
Level 31 - code : 138620
Level 32 - code : 879021
Level 33 - code : 614955