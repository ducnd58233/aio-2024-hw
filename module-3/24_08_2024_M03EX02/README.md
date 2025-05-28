# K-Nearest Neighbors
- K-Nearest Neighbors (KNN) là một trong những thuật toán học máy có giám sát cơ bản. 
- KNN còn được gọi là Lazy Learning, Memory-Based Learning,... 
- Với bước huấn luyện mô hình, chỉ đơn giản là lưu trữ lại giá trị của dữ liệu huấn luyện, vì vậy KNN là phương pháp học máy không tham số (Non-Parametric). 
- Ở bước dự đoán, mô hình sẽ dử dụng các độ đo khoảng cách để tìm các hàng xóm lân cận.
- 1 số độ đo thường được sử dụng trong KNN:
    - Euclidean Distance
    - Chebyshev Distance
    - Manhattan Distance
    - Minkowski Distance
    - Tanimoto Coefficient Distance
- Các độ đo này tính toán dữ liệu dự đoán với các điểm dữ liệu khác được lưu trữ trong mô hình huấn luyện. Từ đó xếp hạng và tìm ra K điểm dữ liệu huấn luyện có kết quả gần với dữ liệu dự đoán nhất.
- Cuối cùng dựa vào phương pháp biểu quyết của các dữ liệu hàng xóm trong tập huấn luyện để đưa ra kết quả dự đoán.
- Sử dụng rộng rãi cho các ứng dụng Classification (phân loại) và Regression (dự đoán).

# KMean
- Thuật toán K-Means là một thuật toán phân cụm phổ biến và được sử dụng rộng rãi trong các bài toán học máy (machine learning) và khai phá dữ liệu (data mining). 
- Mục tiêu của K-Means là phân chia n điểm dữ liệu thành k cụm sao cho các điểm trong cùng một cụm có độ tương đồng cao nhất.
- K-Means là một thuật toán không giám sát (unsupervised learning).
- Quy trình cơ bản:
1. Khởi tạo: Chọn ngẫu nhiên k điểm dữ liệu làm tâm cụm (centroids) ban đầu.
2. Gán nhãn: Với mỗi điểm dữ liệu, tính khoảng cách từ điểm đó tới mỗi tâm cụm và gán nó vào cụm có tâm gần nhất. Khoảng cách thường được đo bằng khoảng cách Euclid, được tính như sau:
    $$d(x_i, c_i) = \sqrt{\sum_{l=1}^{m} (x_{il} - c_{jl})^2}$$
    - Trong đó:
        - $x_i$ là điểm dữ liệu thứ i.
        - $c_j$ là tâm cụm thứ j.
        - $m$ là số chiều của dữ liệu.

3. Cập nhật tâm cụm: Tính toán lại tâm cụm dựa trên các điểm dữ liệu đã được gán nhãn.
    $$c_j=\frac{1}{N_j}\sum_{x_i \in C_j}x_i$$
    - Trong đó:
        - $c_j$ là tâm cụm thứ j.
        - $C_j$ là tập các điểm dữ liệu thuộc cụm thứ j.
        - $N_j$ là số điểm dữ liệu trong cụm thứ j.

4. Lặp lại: Lặp lại quá trình gán nhãn và cập nhật tâm cụm cho đến khi không có sự thay đổi nào trong các cụm.

Thuật toán K-Means có độ phức tạp tính toán là $O(n \times k \times t \times m)$, trong đó $t$ là số lần lặp và $m$ là số chiều của dữ liệu. K-Means thường được sử dụng vì tính đơn giản và hiệu quả của nó trong việc phân cụm dữ liệu lớn, mặc dù nó có thể không tìm được nghiệm tối ưu toàn cục (global optimization) do phụ thuộc vào việc khởi tạo các tâm cụm ban đầu.









