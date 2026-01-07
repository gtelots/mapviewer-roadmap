# Measurement & Drawing Tools

> Advanced features and implementation details for measurement & drawing tools.

## 📋 Overview

**Total Features**: ~39

**Categories**: 2

---

## Core - Measurement & Drawing


**40 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F301 Measure Distance 2D |  | What: Đo khoảng cách trên mặt đất. | Why: Khảo sát cơ bản. | Criteria: Click points → distance; unit correct; undo point. |
| 2 | F302 Measure Distance 3D |  | What: Đo khoảng cách không gian (straight line). | Why: 3D cần độ cao. | Criteria: Shows 3D distance; includes height delta. |
| 3 | F303 Measure Area |  | What: Đo diện tích polygon. | Why: Quy hoạch/kiểm kê. | Criteria: Close polygon auto; area correct; unit m²/ha. |
| 4 | F304 Measure Height |  | What: Đo chênh cao giữa 2 điểm. | Why: Cốt lõi 3D. | Criteria: Shows height; handles no-hit gracefully. |
| 5 | F305 Measure Slope |  | What: Đo độ dốc theo line. | Why: Phân tích địa hình. | Criteria: Outputs %/degrees; uses terrain height. |
| 6 | F306 Measure Profile Chart |  | What: Biểu đồ độ cao theo tuyến. | Why: Phân tích nâng cao vừa. | Criteria: Chart renders; hover shows station/height. |
| 7 | F307 Draw Point Marker |  | What: Tạo marker point. | Why: Ghi chú vị trí. | Criteria: Add marker; edit label; delete works. |
| 8 | F308 Draw Polyline |  | What: Vẽ tuyến. | Why: Ghi chú, route plan. | Criteria: Vertex edit; snap optional; export. |
| 9 | F309 Draw Polygon |  | What: Vẽ vùng. | Why: Khoanh vùng AOI. | Criteria: Edit vertices; area shown; style config. |
| 10 | F310 Draw Rectangle Tool |  | What: Vẽ hình chữ nhật nhanh. | Why: Khoanh vùng nhanh. | Criteria: Drag to draw; resize handles. |
| 11 | F311 Draw Circle Tool |  | What: Vẽ hình tròn theo bán kính. | Why: Phạm vi ảnh hưởng. | Criteria: Center+radius; numeric input supported. |
| 12 | F312 Snap to Features |  | What: Snap tới vertex/edge của dữ liệu. | Why: Độ chính xác. | Criteria: Snap indicator; toggle; tolerance config. |
| 13 | F313 Magnet to Ground |  | What: Clamp drawing xuống ground/terrain. | Why: Đúng với 3D. | Criteria: Draw points clamp; option absolute. |
| 14 | F314 Draw in 3D Space |  | What: Vẽ polyline/polygon ở height absolute. | Why: Digital twin cơ bản. | Criteria: Height input; renders floating; edit height. |
| 15 | F315 Annotation Text |  | What: Ghi chú text/callout. | Why: Truyền đạt. | Criteria: Text editable; style basic; export. |
| 16 | F316 Markup List Panel |  | What: Danh sách markups của user. | Why: Quản lý ghi chú. | Criteria: List CRUD; zoom-to; visibility toggle. |
| 17 | F317 Markup Categories |  | What: Phân loại markup theo tag. | Why: Tổ chức tốt hơn. | Criteria: Tag filter works; multi-tag. |
| 18 | F318 Markup Import/Export |  | What: Import/export GeoJSON/KML (optional). | Why: Chia sẻ dữ liệu. | Criteria: Import validates; export matches schema. |
| 19 | F319 Markup Sharing Link |  | What: Chia sẻ markup set qua link/token. | Why: Collaboration. | Criteria: Recipient opens → sees markups; permission enforce |
| 20 | F320 Measure Unit Settings |  | What: Chọn đơn vị đo riêng cho tool. | Why: Phù hợp khách hàng. | Criteria: Change unit updates results; persisted. |
| 21 | F321 Measure Accuracy Mode |  | What: Chọn sample terrain (fast/accurate). | Why: Cân bằng perf. | Criteria: Accurate mode slower but closer; UI indicates mode |
| 22 | F322 Measurement Report Export |  | What: Xuất báo cáo đo đạc (PDF/CSV basic). | Why: Báo cáo. | Criteria: Export includes points and results; downloadable. |
| 23 | F323 Draw Style Presets |  | What: Preset màu/độ dày/opacity cho markup. | Why: Chuẩn hoá. | Criteria: Choose preset applies; persists. |
| 24 | F324 Draw Edit History |  | What: Undo/redo riêng cho 1 markup. | Why: Sửa an toàn. | Criteria: Undo works; redo works; bounded. |
| 25 | F325 Draw Constraints (Orthogonal) |  | What: Khóa góc 90° khi vẽ. | Why: Đo vẽ kỹ thuật. | Criteria: Enable → segments snap 0/90; disable free. |
| 26 | F326 Draw Length Constraint |  | What: Nhập chiều dài segment. | Why: Chính xác. | Criteria: Input length sets point; supports unit. |
| 27 | F327 Draw Area Constraint |  | What: Nhập diện tích mục tiêu (optional). | Why: Thiết kế nhanh. | Criteria: Input area adjusts polygon; error within tolerance |
| 28 | F328 Multi-Geometry Support |  | What: 1 markup gồm nhiều polygon/line. | Why: Phức hợp AOI. | Criteria: Add parts; delete part; export correct. |
| 29 | F329 Elevation Sampling Along Line |  | What: Lấy mẫu height theo bước. | Why: Profile chính xác. | Criteria: Step size config; chart updates. |
| 30 | F330 Buffer Tool |  | What: Tạo buffer quanh line/point. | Why: Phạm vi tác động. | Criteria: Buffer shown; radius input; export polygon. |
| 31 | F331 Intersect with Layers (Basic) |  | What: Tính giao cắt markup với layer (count/area). | Why: Phân tích nhanh. | Criteria: Run intersect → result table; handles empty. |
| 32 | F332 Measure Clearance |  | What: Đo khoảng hở giữa object và ground/other object. | Why: Hạ tầng/đường dây. | Criteria: Select objects → clearance shown; error if not sup |
| 33 | F333 Draw 3D Box Volume |  | What: Vẽ hộp 3D và tính thể tích. | Why: Khối lượng sơ bộ. | Criteria: Box adjustable; volume shown; unit m³. |
| 34 | F334 Draw Polyline Elevation Lock |  | What: Khóa độ cao đường vẽ. | Why: Vẽ tuyến trên cao. | Criteria: Enable lock; segments keep height ± tolerance. |
| 35 | F335 Measurement Snapshots |  | What: Lưu snapshot kết quả đo (time-stamped). | Why: Tài liệu hoá. | Criteria: Snapshot list; reopen shows same geometry. |
| 36 | F336 Markup Permission Modes |  | What: Private / Team / Public. | Why: Quản trị chia sẻ. | Criteria: Mode enforced; UI shows icon; audit recorded. |
| 37 | F337 Markup Versioning Basic |  | What: Auto-save versions khi sửa. | Why: Khôi phục. | Criteria: See versions; restore version; diff basic. |
| 38 | F338 Markup Comments |  | What: Comment thread trên markup. | Why: Review. | Criteria: Add comment; notify; resolve thread. |
| 39 | F339 Markup Attachment |  | What: Đính kèm ảnh/file/link (policy-based). | Why: Hồ sơ hiện trường. | Criteria: Upload allowed types; size limit; virus scan place |
| 40 | F340 Markup Export Screenshot Bundle |  | What: Xuất markup + screenshot gói zip. | Why: Báo cáo nhanh. | Criteria: Zip includes image+geojson+meta; reproducible. |

---

---

## Drawing & Editing


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

