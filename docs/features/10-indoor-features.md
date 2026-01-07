# Indoor Features

> Comprehensive indoor mapping, navigation, and wayfinding features.

## Basic Indoor Mapping

| Feature Group | Feature Name | Short Description | Detailed Description | Why This Feature is Needed | Implementation Phase |
|--------------| -------------- |------------|----------------|---------------------------|---------------------|
| Indoor Mapping | Indoor Mode Toggle | Chuyển chế độ trong nhà | Chuyển đổi giữa chế độ bản đồ ngoài trời và trong nhà theo tòa nhà | Cung cấp trải nghiệm khác biệt cho điều hướng trong nhà | Phase 2 |
| Indoor Mapping | Building Selector | Chọn tòa nhà | Chọn tòa nhà trong khu phức hợp (campus, khu công nghiệp, v.v.) | Điều hướng giữa nhiều tòa nhà trong cùng khu vực | Phase 2 |
| Indoor Mapping | Floor Selector | Chọn tầng | Bộ chọn tầng trực quan (floor picker) với hiển thị số tầng và tên | Điều hướng giữa các tầng trong tòa nhà | Phase 2 |
| Indoor Mapping | Room Highlighting | Tô sáng phòng | Tô sáng phòng và hiển thị thuộc tính phòng (tên, số, loại, chức năng) | Giúp người dùng dễ dàng xác định vị trí phòng cần tìm | Phase 2 |
| Indoor Mapping | Indoor POI Layer | Lớp POI trong nhà | Hiển thị các điểm quan tâm trong nhà: cửa, quầy lễ tân, toilet, tiện ích, v.v. | Cung cấp thông tin đầy đủ cho người dùng trong tòa nhà | Phase 2 |
| Indoor Mapping | Indoor Labels | Nhãn trong nhà | Nhãn hiển thị theo tầng cho phòng, hành lang, khu vực | Định hướng rõ ràng trong không gian phức tạp | Phase 2 |
| Indoor Mapping | Indoor Visibility Rules | Quy tắc hiển thị | Tự động ẩn các tầng không liên quan để giảm nhiễu thông tin | Tập trung vào tầng đang xem, tránh rối mắt | Phase 2 |
| Indoor Mapping | Stairs/Elevator Connectors | Kết nối cầu thang/thang máy | Hiển thị các điểm kết nối đứng giữa các tầng (cầu thang, thang máy, thang cuốn) | Điều hướng giữa các tầng một cách chính xác | Phase 2 |
| Indoor Mapping | Indoor Accessibility Tags | Nhãn hỗ trợ tiếp cận | Đánh dấu các điểm hỗ trợ tiếp cận (thang máy cho xe lăn, dốc, toilet cho người khuyết tật) | Hỗ trợ người khuyết tật di chuyển trong nhà | Phase 2 |
| Indoor Mapping | Indoor Mini-Map | Bản đồ mini trong nhà | Mini-map hiển thị vị trí hiện tại trên tầng để định hướng nhanh | Giúp người dùng luôn biết vị trí của mình | Phase 2 |
| Indoor Mapping | Indoor Routing | Định tuyến trong nhà | Tìm đường trong nhà giữa phòng/POI qua nhiều tầng | Điều hướng chính xác trong các tòa nhà phức tạp | Phase 2 |
| Indoor Mapping | Door-to-Door Routing | Định tuyến liền mạch | Ghép tuyến ngoài trời + trong nhà liền mạch (từ cửa tòa nhà vào phòng) | Trải nghiệm điều hướng toàn diện không gián đoạn | Phase 2 |
| Indoor Mapping | Indoor Search | Tìm kiếm trong nhà | Tìm kiếm phòng, POI trong nhà theo tên hoặc số | Tìm nhanh vị trí trong tòa nhà lớn (văn phòng, bệnh viện, trung tâm thương mại) | Phase 2 |
| Indoor Mapping | 3D Indoor Visualization | Hiển thị 3D trong nhà | Hiển thị nội thất 3D của tòa nhà, phòng, hành lang | Trải nghiệm trực quan hơn, dễ định hướng | Phase 3 |
| Indoor Mapping | Indoor Geofencing | Geofencing trong nhà | Tạo geofence cho các khu vực trong nhà (phòng họp, kho, khu hạn chế) | Quản lý an ninh, kiểm soát ra vào | Phase 2 |
| Indoor Mapping | Indoor Heatmap | Bản đồ nhiệt trong nhà | Hiển thị mật độ người, nhiệt độ, hoặc các metric khác theo phòng | Phân tích sử dụng không gian, quản lý năng lượng | Phase 3 |
| Indoor Mapping | Emergency Exit Routes | Lối thoát hiểm | Hiển thị lối thoát hiểm và điểm tập trung khi khẩn cấp | An toàn cho người dùng trong tình huống khẩn cấp | Phase 2 |
| Indoor Mapping | Indoor Location Sharing | Chia sẻ vị trí trong nhà | Chia sẻ vị trí chính xác (tầng + phòng) với đồng đội | Hợp tác và hội họp trong tòa nhà lớn | Phase 2 |
| Indoor Mapping | BIM Integration | Tích hợp BIM | Tích hợp dữ liệu Building Information Modeling (IFC, Revit) | Sử dụng dữ liệu kiến trúc có sẵn, tiết kiệm chi phí | Phase 3 |
| Indoor Mapping | Indoor Analytics | Phân tích trong nhà | Phân tích lưu lượng, thời gian lưu trú trong các khu vực | Tối ưu hóa bố trí không gian, hiệu quả vận hành | Phase 3 |
## Indoor Navigation & Advanced Features
> Advanced features and implementation details for indoor navigation & mapping.

| Feature Group | Feature Name | Short Description | Detailed Description | Why This Feature is Needed | Implementation Phase |
|--------------| -------------- |------------|----------------|---------------------------|---------------------|
| Core - Indoor - Core | Floor Selector | Tính năng floor selector | Tính năng floor selector | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Level Auto-Detect | Tính năng indoor level auto-detect | Tính năng indoor level auto-detect | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor POI List | Tính năng indoor poi list | Tính năng indoor poi list | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Room Highlight | Tính năng indoor room highlight | Tính năng indoor room highlight | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Routing A->B | Tính năng indoor routing a->b | Tính năng indoor routing a->b | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Vertical Transitions Support | Tính năng vertical transitions support | Tính năng vertical transitions support | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Accessibility Routing | Tính năng indoor accessibility routing | Tính năng indoor accessibility routing | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Wayfinding Arrows | Tính năng indoor wayfinding arrows | Tính năng indoor wayfinding arrows | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Map Styling | Tính năng indoor map styling | Tính năng indoor map styling | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Labeling Rules | Tính năng indoor labeling rules | Tính năng indoor labeling rules | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Search Scoped | Tính năng tìm kiếm và tra cứu nâng cao | Tính năng tìm kiếm và tra cứu nâng cao | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Occupancy Layer (View) | Quản lý và điều khiển indoor occupancy layer (view) | Quản lý và điều khiển indoor occupancy layer (view) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Access Control Zones | Tính năng indoor access control zones | Tính năng indoor access control zones | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Emergency Exits Layer | Quản lý và điều khiển indoor emergency exits layer | Quản lý và điều khiển indoor emergency exits layer | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Navigation Voice Prompts (Basic) | Tính năng indoor navigation voice prompts (basic) | Tính năng indoor navigation voice prompts (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Route Re-route | Tính năng indoor route re-route | Tính năng indoor route re-route | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor POI Categories Filter | Tính năng indoor poi categories filter | Tính năng indoor poi categories filter | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Building Selector | Tính năng indoor building selector | Tính năng indoor building selector | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor-to-Outdoor Transition | Tính năng indoor-to-outdoor transition | Tính năng indoor-to-outdoor transition | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Blue Dot Positioning (Basic) | Tính năng indoor blue dot positioning (basic) | Tính năng indoor blue dot positioning (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Calibration UI (Basic) | Tính năng indoor calibration ui (basic) | Tính năng indoor calibration ui (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor POI Details Panel | Tính năng indoor poi details panel | Tính năng indoor poi details panel | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Crowd-safe Route (Optional) | Tính năng indoor crowd-safe route (optional) | Tính năng indoor crowd-safe route (optional) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Route Print View | Tính năng indoor route print view | Tính năng indoor route print view | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Level Transition Animation | Tính năng indoor level transition animation | Tính năng indoor level transition animation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Layer Isolation | Quản lý và điều khiển indoor layer isolation | Quản lý và điều khiển indoor layer isolation | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Door/Entrance Graph | Tính năng indoor door/entrance graph | Tính năng indoor door/entrance graph | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Network Debug Overlay | Tính năng indoor network debug overlay | Tính năng indoor network debug overlay | Hỗ trợ troubleshooting và phân tích vấn đề | Phase 1 |
| Core - Indoor - Core | Indoor Navigation Events | Tính năng indoor navigation events | Tính năng indoor navigation events | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Core - Indoor - Core | Indoor Route Accessibility Annotations | Tính năng indoor route accessibility annotations | Tính năng indoor route accessibility annotations | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
