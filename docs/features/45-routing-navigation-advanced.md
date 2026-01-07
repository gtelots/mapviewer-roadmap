# Advanced Routing & Navigation

> Advanced features and implementation details for advanced routing & navigation.

## 📋 Overview

**Total Features**: ~19

**Categories**: 2

---

## Core - Routing - Outdoor


**20 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F341 Route A->B Basic |  | What: Tính tuyến đường 2 điểm. | Why: Use-case cốt lõi. | Criteria: Set A/B → route shown; distance/time displayed. |
| 2 | F342 Route Multi-Stop |  | What: Thêm điểm dừng C,D… | Why: Đi tuyến giao hàng. | Criteria: Add stop reorder; route recompute. |
| 3 | F343 Travel Mode Profiles |  | What: Car/Walk/Bike (tuỳ data). | Why: Đúng nghiệp vụ. | Criteria: Switch profile changes route; UI indicates restric |
| 4 | F344 Avoid Options |  | What: Tránh toll/ferry/highway (optional). | Why: Tùy chọn. | Criteria: Toggle avoid → route changes; if impossible show m |
| 5 | F345 Route Turn-by-Turn List |  | What: Danh sách hướng dẫn từng bước. | Why: Dễ theo dõi. | Criteria: Steps shown; click step zoom segment. |
| 6 | F346 Route ETA Live Update |  | What: Cập nhật ETA theo tốc độ giả định/traffic (if any) | Why: Thông tin tốt hơn. | Criteria: ETA updates; traffic optional; fallback to static. |
| 7 | F347 Route Preview Style |  | What: Tùy style polyline, arrows. | Why: Rõ ràng. | Criteria: Route line visible; contrast ok; zoom independent  |
| 8 | F348 Route Alternatives |  | What: Hiển thị 2-3 phương án tuyến. | Why: Lựa chọn tối ưu. | Criteria: Alternatives list; select changes highlight. |
| 9 | F349 Route Snap to Road |  | What: Snap điểm đầu/cuối vào đường. | Why: Đúng tuyến. | Criteria: Drop point near road → snaps; show snap indicator. |
| 10 | F350 Route Export |  | What: Gửi route ra GPX/GeoJSON/URL. | Why: Chia sẻ/thiết bị khác. | Criteria: Export works; link restores route. |
| 11 | F351 Route Avoid Polygons |  | What: Tránh vùng cấm do user vẽ. | Why: Tác nghiệp. | Criteria: Draw avoid area → route detours; if impossible war |
| 12 | F352 Route Elevation Profile |  | What: Profile độ cao theo tuyến. | Why: Phân tích (xe đạp/đi bộ). | Criteria: Chart shows; togglable; uses terrain. |
| 13 | F353 Route Recompute on Drag |  | What: Kéo điểm route để đổi tuyến. | Why: Tương tác tốt. | Criteria: Drag waypoint → recompute; undo supported. |
| 14 | F354 Route Cost Breakdown |  | What: Hiển thị cost (distance, time, toll). | Why: Minh bạch. | Criteria: Cost table present; missing fields hidden. |
| 15 | F355 Route Corridor Buffer |  | What: Hành lang route (buffer) để phân tích. | Why: An toàn/ảnh hưởng. | Criteria: Generate corridor polygon; width input; export. |
| 16 | F356 Route Incident Markers |  | What: Marker cảnh báo (construction, block) (if data). | Why: An toàn. | Criteria: Incidents show; click opens details; toggle layer. |
| 17 | F357 Route Accessibility Mode |  | What: Tuyến phù hợp xe lăn (if data). | Why: Phục vụ A11y. | Criteria: Mode on changes route; if unavailable show reason. |
| 18 | F358 Route Matrix (Basic) |  | What: Ma trận thời gian/độ dài giữa N điểm (small N). | Why: Logistics sơ bộ. | Criteria: Input N<=10 → matrix computed; errors handled. |
| 19 | F359 Isochrone (Basic) |  | What: Vùng đi được trong T phút (if supported). | Why: Quy hoạch/tiếp cận. | Criteria: Select origin+time → polygon shown; export. |
| 20 | F360 Route Save & Load |  | What: Lưu tuyến theo tên. | Why: Dùng lại. | Criteria: Save/load works; metadata includes profile & stops |

---

---

## Navigation & Camera


**4 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

