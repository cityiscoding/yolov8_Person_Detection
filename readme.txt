Chương trình YOLO v8 này được sử dụng để phát hiện và theo dõi các đối tượng người trong các video hình ảnh. Nó sử dụng mô hình YOLO v8 được đào tạo trên tập dữ liệu COCO(Common Objects in Context là tập dữ liệu phát hiện, phân đoạn và tạo phụ đề đối tượng quy mô lớn. Tập dữ liệu chứa 91 lớp, bao gồm 250.000 người với những điểm chính. Kích thước tải xuống của nó là 37,57 GiB. Nó chứa 80 loại đối tượng. Trong tập dữ liệu đã kèm theo Giấy phép Apache 2.0.)

Chương trình bao gồm các thành phần sau:

Tải mô hình YOLO v8: Chương trình sử dụng thư viện TensorFlow để tải mô hình YOLO v8 từ file frozen_inference_graph.pb.

Phát hiện đối tượng: Chương trình sử dụng mô hình YOLO v8 để phát hiện các đối tượng trong các khung hình video. Các hộp giới hạn và nhãn đối tượng được trả về bởi mô hình YOLO v8.
Theo dõi đối tượng: Chương trình sử dụng thuật toán Kalman để theo dõi các đối tượng trong các khung hình video tiếp theo.

Xuất đầu ra: Chương trình hiển thị các hộp giới hạn của các đối tượng được phát hiện và theo dõi trên màn hình.
Dưới đây là một số chi tiết về cách thức hoạt động của chương trình:

Tải mô hình YOLO v8: Chương trình sử dụng hàm tf.saved_model.load() để tải mô hình YOLO v8 từ file frozen_inference_graph.pb. Mô hình YOLO v8 được lưu trữ ở định dạng Protocol Buffers(Protobuf)

Phát hiện đối tượng: Chương trình sử dụng hàm tf.compat.v1.Session.run() để chạy mô hình YOLO v8 trên các khung hình video. Các hộp giới hạn và nhãn đối tượng được trả về bởi mô hình YOLO v8.

Theo dõi đối tượng: Chương trình sử dụng thuật toán Kalman để theo dõi các đối tượng trong các khung hình video tiếp theo. Thuật toán Kalman sử dụng các thông tin từ các khung hình trước đó để dự đoán vị trí của các đối tượng trong khung hình hiện tại.

Xuất đầu ra: Chương trình sử dụng thư viện OpenCV để hiển thị các hộp giới hạn của các đối tượng được phát hiện và theo dõi trên màn hình.
