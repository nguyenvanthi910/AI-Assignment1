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


Game code:
1. 780464
2. 290299
3. 918660
4. 520967
5. 028431
6. 524383
7. 189493
8. 499707
9. 074355
10. 300590
11. 291709
12. 958640
13. 448106
14. 210362
15. 098598
16. 000241
17. 003596
18. 284933
19. 119785
20. 543019
21. 728724
22. 987319
23. 293486
24. 088198
25. 250453
26. 426429
27. 660141
28. 769721
29. 691859
30. 280351
31. 138620
32. 079021
33. 614955