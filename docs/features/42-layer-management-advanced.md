# Advanced Layer Management

> Advanced features and implementation details for advanced layer management.

## 📋 Overview

**Total Features**: ~104

**Categories**: 5

---

## 2D Vector & Raster Rendering


**9 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 3 | Client-Side Caching | Cache tile phía client để kéo thả mượt | Cache tile phía client để kéo thả mượt |
| 4 | Tile Retry Policy | Retry có backoff khi tile lỗi tạm thời | Retry có backoff khi tile lỗi tạm thời |
| 5 | Overzoom Support | Phóng to vượt zoom gốc vẫn hiển thị hợp lý | Phóng to vượt zoom gốc vẫn hiển thị hợp lý |
| 6 | Anti-Aliasing Toggle | Bật/tắt AA cân bằng giữa chất lượng và hiệu năng | Bật/tắt AA cân bằng giữa chất lượng và hiệu năng |
| 7 | Feature Simplification | Tự đơn giản hóa hình học ở zoom nhỏ để tăng tốc | Tự đơn giản hóa hình học ở zoom nhỏ để tăng tốc |
| 8 | Symbol Collision Avoidance | Tránh chồng nhãn/icon gây rối | Tránh chồng nhãn/icon gây rối |
| 9 | High-DPI Rendering | Hiển thị sắc nét trên màn hình retina | Hiển thị sắc nét trên màn hình retina |

---

---

## Advanced - Visualization & Styling


**25 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F401 Style Rule Engine Advanced |  | What: Rule theo nhiều field, ranges, expressions. | Why: Trực quan hoá phức tạp. | Criteria: Rule evaluate đúng; fallback safe; perf within bud |
| 2 | F402 Thematic Mapping |  | What: Choropleth/gradient theo attribute. | Why: Phân tích. | Criteria: Color ramp applies; legend auto; missing values ha |
| 3 | F403 3D Extrusion by Attribute |  | What: Extrude height theo field. | Why: Thấy dữ liệu 3D. | Criteria: Extrusion accurate; clamp max; toggle off. |
| 4 | F404 3D Label Occlusion |  | What: Hide labels khi bị che. | Why: Đọc dễ. | Criteria: Occlusion reduces clutter; no flicker excessive. |
| 5 | F405 Ambient Occlusion |  | What: SSAO toggle. | Why: Tăng chiều sâu. | Criteria: AO visible; performance cost indicated; can disabl |
| 6 | F406 Bloom/Glow Effects |  | What: Hiệu ứng phát sáng cho layer/selection. | Why: Highlight. | Criteria: Glow visible; per-layer toggle; doesn’t hide text. |
| 7 | F407 Color Blind Friendly Palettes |  | What: Bộ màu thân thiện mù màu. | Why: A11y. | Criteria: Palette switch; legend updates; verified contrast. |
| 8 | F408 Dynamic Styling by Zoom |  | What: Style thay đổi theo zoom/height. | Why: Rõ ràng ở mọi mức. | Criteria: Zoom changes style smoothly; no popping. |
| 9 | F409 Material Library |  | What: Preset material (concrete, glass…). | Why: Trình diễn. | Criteria: Apply material; revert; no shader errors. |
| 10 | F410 Day/Night Scene Profiles |  | What: Profile scene theo thời điểm. | Why: Ngữ cảnh. | Criteria: Switch profile updates lights/UI; schedule optiona |
| 11 | F411 Section Box Tool |  | What: Section box 3D cắt khối. | Why: Xem bên trong. | Criteria: Box adjustable; culling correct; reset. |
| 12 | F412 Multi-Plane Clipping |  | What: Nhiều mặt phẳng cắt đồng thời. | Why: Phân tích nâng cao. | Criteria: Add/remove plane; performance acceptable. |
| 13 | F413 Ghost Mode for Context |  | What: Làm mờ layer phụ để nhìn layer chính. | Why: Focus. | Criteria: Ghost intensity slider; only affects non-target la |
| 14 | F414 Highlight by Query |  | What: Kết quả filter/query được highlight khác màu. | Why: Đọc nhanh. | Criteria: Apply query → highlight; legend indicates conditio |
| 15 | F415 Animated Layers |  | What: Animation theo time/attribute (optional). | Why: Dữ liệu động. | Criteria: Play/pause; timeline; FPS stable. |
| 16 | F416 Vector Tile Style Editor (View) |  | What: Chỉnh style vector tiles trong viewer (read-only p | Why: Custom nhanh. | Criteria: Select preset; render updates; cannot break scene. |
| 17 | F417 Terrain Contours |  | What: Hiển thị đường đồng mức. | Why: Đọc địa hình. | Criteria: Contours show; interval config; toggle. |
| 18 | F418 Hillshade Layer |  | What: Hillshade cho terrain. | Why: Tăng trực quan. | Criteria: Hillshade visible; blends with basemap. |
| 19 | F419 Skybox & Weather Presets |  | What: Skybox mưa/sương (optional). | Why: Trình diễn. | Criteria: Preset applies; can disable; no data impact. |
| 20 | F420 Reflections (Basic) |  | What: Phản chiếu đơn giản (optional). | Why: Chất lượng cao. | Criteria: Reflection visible; togglable; perf warning. |
| 21 | F421 Outline Styles |  | What: Chỉnh kiểu outline selection (dashed/glow). | Why: Nhấn mạnh. | Criteria: Style change visible; consistent across layers. |
| 22 | F422 Color Scale Calibration |  | What: Chỉnh min/max domain cho choropleth. | Why: Tránh outlier. | Criteria: Domain input clamps; legend updates; reset. |
| 23 | F423 Style Preset Sharing |  | What: Share preset style JSON. | Why: Đồng bộ team. | Criteria: Export/import works; validation prevents invalid s |
| 24 | F424 Multi-Layer Blending Graph |  | What: Trình tự blend giữa nhiều overlay. | Why: Cartography nâng cao. | Criteria: Blend order deterministic; UI shows stack. |
| 25 | F425 Render Pipeline Debug |  | What: View passes, draw calls, shader time. | Why: Debug perf. | Criteria: Debug shows metrics; export snapshot. |

---

---

## Basemaps & Reference Layers


**7 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Basemap Gallery | Thư viện basemap (street/satellite/terrain) để chọn nhanh | Thư viện basemap (street/satellite/terrain) để chọn nhanh |
| 2 | Attribution Display | Hiển thị attribution/nguồn dữ liệu theo yêu cầu license | Hiển thị attribution/nguồn dữ liệu theo yêu cầu license |
| 3 | Custom Basemap URL | Thêm basemap từ mẫu URL XYZ/WMTS | Thêm basemap từ mẫu URL XYZ/WMTS |
| 5 | Administrative Boundaries | Lớp ranh giới hành chính theo cấp | Lớp ranh giới hành chính theo cấp |
| 6 | Labels-Only Layer | Bật lớp nhãn độc lập với nền ảnh vệ tinh | Bật lớp nhãn độc lập với nền ảnh vệ tinh |
| 7 | Night Mode Basemap | Basemap tối phù hợp hiển thị ban đêm | Basemap tối phù hợp hiển thị ban đêm |

---

---

## Foundation - Layer Management


**70 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F121 Layer Catalog Panel |  | What: Danh mục layer theo nhóm, tìm kiếm, bật/tắt. | Why: Quản lý dữ liệu lớn. | Criteria: Toggle hiển thị đúng; search theo tên/tag. |
| 2 | F122 Layer Grouping (Folders) |  | What: Folder + nested groups cho layer. | Why: Gọn gàng; dễ vận hành. | Criteria: Expand/collapse; trạng thái nhớ theo session. |
| 3 | F123 Layer Ordering DragDrop |  | What: Kéo thả thứ tự render layer. | Why: So sánh & ưu tiên hiển thị. | Criteria: DragDrop hoạt động; z-order đúng. |
| 4 | F124 Opacity Slider |  | What: Chỉnh opacity cho raster/overlay 2D. | Why: So sánh nhiều lớp. | Criteria: Opacity đổi realtime; giá trị lưu. |
| 5 | F125 Visibility by Zoom |  | What: Rule ẩn/hiện theo zoom/height. | Why: Giảm rối; tăng perf. | Criteria: Zoom out → layer auto hide; có override. |
| 6 | F126 Layer Metadata View |  | What: Xem mô tả, source, update time, owner. | Why: Minh bạch dữ liệu. | Criteria: Metadata hiển thị đầy đủ; link source mở được. |
| 7 | F127 Legend Auto-Render |  | What: Hiển thị legend theo style rules. | Why: Hiểu ký hiệu nhanh. | Criteria: Legend khớp style; layer không legend → “N/A”. |
| 8 | F128 Layer Load Status |  | What: Icon trạng thái (loading/ok/error) theo layer. | Why: Triaging nhanh. | Criteria: Lỗi layer → icon đỏ + tooltip nguyên nhân. |
| 9 | F129 Layer Retry Button |  | What: Nút retry khi layer lỗi. | Why: Tự xử lý nhanh. | Criteria: Retry gọi lại request; thành công → xanh. |
| 10 | F130 Layer Solo Mode |  | What: Chế độ chỉ hiển thị 1 layer. | Why: Focus phân tích. | Criteria: Solo on → layer khác ẩn; off → restore. |
| 11 | F131 Layer Pin Favorites |  | What: Ghim layer ưa dùng. | Why: Tăng tốc thao tác. | Criteria: Favorite list lưu theo user; sync thiết bị. |
| 12 | F132 Layer Search Highlight |  | What: Highlight kết quả search trong catalog. | Why: Dễ tìm layer. | Criteria: Kết quả được highlight; clear search restore. |
| 13 | F133 Layer Tags Filter |  | What: Lọc catalog theo tags (transport, indoor…). | Why: Dễ điều hướng catalog lớn. | Criteria: Chọn tag → list lọc đúng; multi-tag AND/OR. |
| 14 | F134 Layer Permissions Display |  | What: Hiển thị quyền xem theo role. | Why: Tránh user tưởng “mất dữ liệu”. | Criteria: No access → disabled + reason; access → clickable. |
| 15 | F135 Layer Style Switcher |  | What: Chọn style preset cho layer (day/night). | Why: Trực quan theo ngữ cảnh. | Criteria: Switch style → render đổi; legend update. |
| 16 | F136 Layer Transparency for 3D |  | What: Chỉnh transparency/material intensity cho 3D tiles | Why: So sánh lớp 3D. | Criteria: Slider tác động rõ; không phá picking. |
| 17 | F137 Layer Clipping Integration |  | What: Áp dụng clipping/section riêng cho layer. | Why: Phân tích cục bộ. | Criteria: Enable clip → chỉ layer đó bị cắt; others giữ. |
| 18 | F138 Layer Time Filter (Basic) |  | What: Lọc layer theo thời gian (from-to). | Why: Dữ liệu time-series. | Criteria: Chọn range → data cập nhật; empty → thông báo. |
| 19 | F139 Layer Refresh Interval |  | What: Tự refresh layer mỗi N phút (optional). | Why: Giám sát realtime. | Criteria: Interval chạy; có pause; không spam API. |
| 20 | F140 Layer Source Switching |  | What: Chuyển endpoint/source cho layer (fallback). | Why: Độ sẵn sàng. | Criteria: Source down → switch; UI báo rõ. |
| 21 | F141 Layer Cache Control UI |  | What: Clear cache metadata/tiles per layer. | Why: Debug & troubleshooting. | Criteria: Clear cache → reload; không ảnh hưởng layer khác. |
| 22 | F142 Layer Query Builder Basic |  | What: UI tạo query theo thuộc tính (equals/range). | Why: Lọc dữ liệu nhanh. | Criteria: Query apply đúng; clear dễ; state hiển thị chip. |
| 23 | F143 Spatial Filter by Viewport |  | What: Chỉ hiển thị feature trong viewport. | Why: Tăng perf + giảm nhiễu. | Criteria: Pan camera → features cập nhật; có toggle. |
| 24 | F144 Layer Min/Max Height Range |  | What: Chỉ hiển thị layer trong dải height. | Why: Phân tích theo độ cao. | Criteria: Chọn range → render đúng; edge case = inclusive. |
| 25 | F145 Layer Hover Tooltip |  | What: Hover → tooltip tên/field chính. | Why: Tra cứu nhanh. | Criteria: Hover 200ms → tooltip; move out → ẩn. |
| 26 | F146 Layer Cluster Control |  | What: Chỉnh clustering cho point layer (2D/3D billboard) | Why: Dữ liệu điểm dày đặc. | Criteria: Zoom in → cluster tách; click cluster zoom. |
| 27 | F147 Layer Heatmap Mode |  | What: Chuyển point layer sang heatmap. | Why: Nhìn mật độ nhanh. | Criteria: Heatmap on → gradient rõ; legend đổi. |
| 28 | F148 Layer Label Toggle |  | What: Bật/tắt label text cho layer. | Why: Giảm rối. | Criteria: Toggle label; label không chồng quá mức (basic). |
| 29 | F149 Layer Label Priority |  | What: Ưu tiên label theo weight. | Why: Đọc dễ. | Criteria: Priority cao → label giữ; thấp → ẩn. |
| 30 | F150 Layer Data Stats Summary |  | What: Số lượng feature, bbox, update time. | Why: Nắm nhanh quy mô. | Criteria: Stats load <2s; lỗi → fallback “unknown”. |
| 31 | F151 Layer Thumbnail Preview |  | What: Preview thumbnail/mini-legend. | Why: Nhanh chọn layer. | Criteria: Thumbnail load; click mở layer. |
| 32 | F152 Layer Dependency Handling |  | What: Layer phụ thuộc (e.g., labels depends on base). | Why: Tránh hiển thị sai. | Criteria: Enable child → auto enable parent; disable parent  |
| 33 | F153 Layer Conflict Detection |  | What: Cảnh báo xung đột style/z-order. | Why: Giảm bug hiển thị. | Criteria: Conflict → banner + gợi ý fix. |
| 34 | F154 Layer Local Draft State |  | What: Lưu draft set layer bật/tắt chưa “Apply”. | Why: Tránh thao tác nhầm. | Criteria: Edit → chưa áp; Apply → commit; Cancel → revert. |
| 35 | F155 Layer Presets (Saved Sets) |  | What: Lưu “bộ layer” theo mục đích. | Why: Mở nhanh kịch bản. | Criteria: Save/load preset; rename; share (optional). |
| 36 | F156 Layer Import from URL |  | What: Add layer nhanh từ URL (WMS/XYZ/3DTiles). | Why: Demo/POC nhanh. | Criteria: URL hợp lệ → thêm; sai → validate & msg. |
| 37 | F157 Layer Attribution Panel |  | What: Panel hiển thị attribution theo layer. | Why: Compliance license. | Criteria: Attribution đúng; update khi layer toggle. |
| 38 | F158 Layer Tile Coverage Preview |  | What: Xem coverage/bounds của tileset. | Why: Chẩn đoán “thiếu data”. | Criteria: Show bounds overlay; click zoom to bounds. |
| 39 | F159 Layer Quality Indicator |  | What: Chỉ số quality (resolution, last update). | Why: Chọn đúng dữ liệu. | Criteria: Indicator hiển thị; tooltip giải thích. |
| 40 | F160 Layer Feature Flags per Layer |  | What: Tắt/bật capability theo layer (pickable, queryable | Why: Kiểm soát hành vi. | Criteria: Flag off → không pick/query; UI ẩn nút. |
| 41 | F161 Layer Sync with URL |  | What: State layer reflect vào URL (optional). | Why: Chia sẻ đúng trạng thái. | Criteria: Share link → restore toggles 1:1. |
| 42 | F162 Layer Bulk Actions |  | What: Bật/tắt hàng loạt theo group/tag. | Why: Tốc độ thao tác. | Criteria: Bulk on/off đúng; undo 1 bước. |
| 43 | F163 Layer Performance Hint |  | What: Gợi ý “layer nặng” khi bật nhiều. | Why: Tránh lag. | Criteria: Bật >N layers nặng → toast cảnh báo. |
| 44 | F164 Layer Error Details Modal |  | What: Modal chi tiết lỗi request/status. | Why: Debug nhanh. | Criteria: Show request id/status; copy được. |
| 45 | F165 Layer Access Request CTA |  | What: No permission → nút “Request access”. | Why: Cải thiện quy trình. | Criteria: Click → mở form/email/template; log event. |
| 46 | F166 Layer Style JSON Inspector |  | What: Xem JSON style (read-only). | Why: Debug & transparency. | Criteria: Inspector mở; search trong JSON; copy. |
| 47 | F167 Layer Bounding Box Filter |  | What: Filter feature theo bbox custom. | Why: Phân tích khu vực. | Criteria: Nhập bbox → data lọc; clear restore. |
| 48 | F168 Layer Elevation Offset |  | What: Offset height cho tileset. | Why: Sửa lệch cao. | Criteria: Offset apply; persist; reset available. |
| 49 | F169 Layer Level-of-Detail Bias |  | What: Chỉnh bias LOD per layer. | Why: Perf tuning. | Criteria: Bias +1 → ít chi tiết; -1 → nhiều chi tiết. |
| 50 | F170 Layer Multi-Style Rules |  | What: Rule-based style theo attribute. | Why: Trực quan hóa dữ liệu. | Criteria: Rule apply đúng; legend sync; fallback default. |
| 51 | F171 Layer Feature Count by Filter |  | What: Đếm số feature sau filter. | Why: Định lượng phân tích. | Criteria: Count update <1s (sampled ok); hiển thị rõ. |
| 52 | F172 Layer Download Sample Data |  | What: Tải sample (N features) theo filter. | Why: Kiểm tra nhanh. | Criteria: Download CSV/GeoJSON; respect permission. |
| 53 | F173 Layer Scenegraph Toggle (3D) |  | What: Bật/tắt tối ưu scenegraph/batching. | Why: Perf. | Criteria: Toggle changes FPS; no visual break. |
| 54 | F174 Layer Material Override |  | What: Override material màu/alpha nhanh. | Why: Review nhanh. | Criteria: Override apply; reset restores. |
| 55 | F175 Layer Per-Layer Screenshot |  | What: Chụp ảnh chỉ 1 layer (mask). | Why: Báo cáo. | Criteria: Export layer-only đúng; background optional. |
| 56 | F176 Layer Notes |  | What: Thêm ghi chú nội bộ cho layer. | Why: Vận hành/knowledge. | Criteria: Notes save; permission check; audit log. |
| 57 | F177 Layer Version Selector |  | What: Chọn version dataset/layer (v1/v2). | Why: So sánh & rollback. | Criteria: Switch version; reload; hiển thị version badge. |
| 58 | F178 Layer Change Diff Badge |  | What: Hiển thị badge “updated” khi layer đổi. | Why: Nhận biết cập nhật. | Criteria: Layer update → badge xuất hiện; click xem chi tiết |
| 59 | F179 Layer Preload Strategy |  | What: Preload layer quan trọng khi mở scene. | Why: Trải nghiệm tốt. | Criteria: Config priority; preload respects budget. |
| 60 | F180 Layer Lazy Mount |  | What: Mount UI layer panel khi mở. | Why: Tối ưu startup. | Criteria: Startup nhanh hơn; mở panel vẫn mượt. |
| 61 | F181 Layer Access Token per Layer |  | What: Token riêng cho layer nhạy cảm. | Why: Bảo mật data. | Criteria: Token missing → deny; refresh token works. |
| 62 | F182 Layer Masking |  | What: Mask layer theo polygon (AOI). | Why: Phân tích vùng. | Criteria: Mask apply đúng; invert supported. |
| 63 | F183 Layer Blend Modes |  | What: Blend mode (multiply/screen) cho raster overlay. | Why: So sánh ảnh nền. | Criteria: Blend đổi rõ; fallback nếu không hỗ trợ. |
| 64 | F184 Layer Elevation Profile Link |  | What: Liên kết layer với công cụ profile (độ cao). | Why: Phân tích địa hình. | Criteria: Select line → profile chart (basic). |
| 65 | F185 Layer Advanced Filter Operators |  | What: Contains, startsWith, regex (optional). | Why: Lọc linh hoạt. | Criteria: Operator chạy đúng; hạn chế regex theo policy. |
| 66 | F186 Layer Filter Save/Load |  | What: Lưu bộ filter theo user. | Why: Khôi phục nhanh. | Criteria: Save; load đúng; share optional. |
| 67 | F187 Layer Diagnostics Snapshot |  | What: Chụp snapshot trạng thái layer (requests/errors). | Why: Support nhanh. | Criteria: Export JSON snapshot; có request ids. |
| 68 | F188 Layer Data Lineage Link |  | What: Link tới portal lineage (nếu có). | Why: Minh bạch nguồn dữ liệu. | Criteria: Click opens portal; respects permission. |
| 69 | F189 Layer Annotation Binding |  | What: Gắn annotation vào layer/feature id. | Why: Review theo dữ liệu. | Criteria: Annotation theo feature; feature đổi → update. |
| 70 | F190 Layer Visibility Rules by Role |  | What: Rule hiển thị layer theo role/team. | Why: Phân quyền hiển thị. | Criteria: Role Viewer không thấy layer restricted; audit log |

---

---

## Styling & Theming


**6 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

