# Automotive Core (ADAS & Fleet)

> Consolidated from: Automotive ADAS, Automotive Fleet

| Feature Group | Feature Name | Short Description | Detailed Description | Why This Feature is Needed | Implementation Phase |
|--------------|--------------|------------|----------------|---------------------------|---------------------|
| Automotive ADAS | Lane-Level Mapping | Bản đồ cấp làn đường | Mapping chi tiết từng làn đường với geometry chính xác | Cần thiết cho hỗ trợ lái xe và xe tự lái | Phase 3 |
| Automotive ADAS | 3D Lane Visualization | Hiển thị làn 3D | Render làn đường 3D với vạch kẻ, overpass, tunnel | Hướng dẫn trực quan hơn cho người lái | Phase 3 |
| Automotive ADAS | HD Road Geometry | Hình học đường độ chính xác cao | Road geometry với độ chính xác cm-level | Quan trọng cho autonomous driving | Phase 3 |
| Automotive ADAS | E-Horizon System | Hệ thống e-horizon | Cung cấp thông tin đường phía trước ngoài tầm cảm biến | Cho phép xe dự đoán điều kiện phía trước | Phase 3 |
| Automotive ADAS | Curvature Information | Thông tin độ cong đường | Cung cấp radius và độ cong từng đoạn đường | Điều chỉnh tốc độ tự động khi vào cua | Phase 3 |
| Automotive ADAS | Slope Information | Thông tin độ dốc | Độ dốc chính xác cho từng đoạn đường | Tối ưu động cơ và phanh trên dốc | Phase 3 |
| Automotive ADAS | Road Sign Mapping | Mapping biển báo | Vị trí và loại biển báo trên từng đoạn đường | Cảnh báo và tuân thủ biển báo tự động | Phase 2 |  
| Automotive ADAS | Traffic Light Phase | Pha đèn giao thông | Dữ liệu pha đèn và countdown đèn tín hiệu | Tối ưu tốc độ đến giao lộ | Phase 3 |
| Automotive ADAS | Junction Complexity Level | Mức độ phức tạp ngã tư | Phân loại độ phức tạp của giao lộ | Điều chỉnh mức cảnh báo cho tài xế | Phase 2 |
| Automotive ADAS | Behavioral Maneuver Prediction | Dự đoán  hanh vi lái | AI dự đoán hành vi lái phù hợp cho đoạn đường | Lái xe mượt mà và tự nhiên hơn | Phase 3 |
| Automotive ADAS | Automated Driving Zone | Vùng lái tự động | Định nghĩa vùng cho phép/không cho phép autonomous | Tuân thủ quy định về xe tự lái | Phase 3 |
| Automotive ADAS | Parking Space Detection | Phát hiện chỗ đỗ | Phát hiện chỗ đậu xe khả dụng từ camera | Hỗ trợ đậu xe tự động | Phase 3 |
| Automotive ADAS | V2X Communication Integration | Tích hợp giao tiếp V2X | Tích hợp với Vehicle-to-Everything communication | Tương lai của giao thông thông minh | Phase 3 |
| Automotive ADAS | Sensor Fusion Mapping | Bản đồ fusion cảm biến | Kết hợp dữ liệu từ camera, LiDAR, radar | Bản đồ chính xác cao cho ADAS | Phase 3 |
| Automotive ADAS | Over-the-Air Map Updates | Cập nhật bản đồ OTA | Push updates bản đồ realtime qua mạng | Luôn có dữ liệu bản đồ mới nhất | Phase 2 |
| Automotive ADAS | Road Condition Reporting | Báo cáo tình trạng đường | Crowdsource tình trạng đường (ổ gà, công trường) | Cải thiện an toàn và comfort | Phase 2 |
| Automotive Fleet | Commercial Vehicle Routing | Định tuyến xe thương mại | Route cho xe tải với hạn chế tải trọng, chiều cao | Tuân thủ quy định về xe tải | Phase 2 |
| Automotive Fleet | Dangerous Goods Routing | Định tuyến hàng nguy hiểm | Route tránh khu dân cư cho xe chở hàng nguy hiểm | An toàn và tuân thủ pháp luật | Phase 2 |
| Automotive Fleet | Multi-Trailer Configuration | Cấu hình nhiều rơ moóc | Tính route cho xe đầu kéo với nhiều rơ moóc | Đặc thù logistics container | Phase 3 |
| Automotive Fleet | Weigh Station Locations | Vị trí trạm cân | Database và routing qua trạm cân xe tải | Tuân thủ quy định kiểm tra tải trọng | Phase 2 |
