# Layer Management # Layer Management & Styling Features Styling Features

> Comprehensive layer management, styling, and visualization features from basic to advanced.

## Basic Layer Management

| Feature Group | Feature Name | Short Description | Detailed Description | Why This Feature is Needed | Implementation Phase |
|--------------| -------------- |------------|----------------|---------------------------|---------------------|
| Layer Catalog | Layer Catalog Panel | Danh mục layer | Danh mục layer theo nhóm để quản lý dễ dàng | Tổ chức nhiều layer theo chủ đề | Phase 1 |
| Layer Management | Layer Visibility Toggle | Bật/tắt layer | Bật/tắt hiển thị layer tức thời | Kiểm soát thông tin hiển thị | Phase 1 |
| Layer Management | Layer Reordering | Sắp xếp lại layer | Đổi thứ tự vẽ layer để kiểm soát ưu tiên hiển thị | Kiểm soát layer nào hiển thị trên cùng | Phase 1 |
| Layer Management | Layer Opacity Slider | Chỉnh độ trong suốt | Chỉnh độ trong suốt theo từng layer | So sánh nhiều layer chồng lên nhau | Phase 1 |
| Layer Management | Layer Grouping | Nhóm layer | Nhóm layer dạng cây, có thể thu gọn/mở rộng | Tổ chức layer phức tạp theo cấu trúc | Phase 1 |
| Layer Management | Layer Favorites | Layer yêu thích | Đánh dấu layer yêu thích để truy cập nhanh | Truy cập nhanh các layer thường dùng | Phase 1 |
| Layer Management | Layer Metadata Viewer | Xem metadata | Xem metadata: nguồn, cập nhật, license, mô tả | Hiểu nguồn gốc và chất lượng dữ liệu | Phase 1 |
| Layer Management | Scale-Dependent Visibility | Hiển thị theo tỷ lệ | Tự động ẩn/hiện layer theo mức zoom | Tối ưu hiển thị theo mức chi tiết | Phase 1 |
| Layer Management | Layer Loading Indicators | Chỉ báo tải | Hiển thị trạng thái tải/lỗi theo layer để dễ debug | Theo dõi trạng thái tải dữ liệu | Phase 1 |
| Layer Management | Basemap Opacity | Độ trong suốt basemap | Chỉnh độ trong suốt lớp overlay để so sánh basemap | So sánh nhiều basemap | Phase 1 |
| Layer Management | Custom Layer URLs | URL layer tùy chỉnh | Thêm layer từ URL XYZ/WMTS/WMS tùy chỉnh | Sử dụng dữ liệu từ nguồn bên ngoài | Phase 2 |
| Layer Management | Layer Blending Modes | Chế độ hòa trộn | Chế độ hòa trộn layer (multiply, screen, overlay) | Hiệu ứng trực quan đặc biệt | Phase 3 |
| Layer Management | Time-Aware Layers | Layer theo thời gian | Layer hỗ trợ dimension thời gian | Xem dữ liệu thay đổi theo thời gian | Phase 2 |
| Styling & Theming | Style Preset Switcher | Chuyển style | Chuyển nhanh giữa các preset style của cùng dataset | Thay đổi giao diện bản đồ nhanh | Phase 1 |
| Styling & Theming | Label Styling | Style nhãn | Chỉnh font, kích thước, halo, vị trí nhãn | Tùy chỉnh cách hiển thị nhãn | Phase 1 |
| Styling & Theming | Icon Library | Thư viện icon | Bộ icon chuẩn dùng cho POI/marker | Icon đồng nhất, chuyên nghiệp | Phase 1 |
| Styling & Theming | Dynamic Styling Rules | Luật style động | Luật style điều kiện (if/else) theo thuộc tính | Hiển thị theo dữ liệu realtime | Phase 2 |
| Styling & Theming | Style Preview | Xem trước style | Xem trước style trước khi áp dụng | Tránh áp dụng style không phù hợp | Phase 1 |
| Styling & Theming | Legend Auto-Generation | Tự tạo legend | Tự tạo legend từ style để người dùng hiểu ký hiệu | Giải thích ý nghĩa màu sắc, ký hiệu | Phase 1 |
| Styling & Theming | Custom Color Ramps | Dải màu tùy chỉnh | Tạo dải màu gradient tùy chỉnh cho dữ liệu | Trực quan hóa dữ liệu số | Phase 2 |
| Styling & Theming | Symbol Library | Thư viện ký hiệu | Thư viện ký hiệu chuẩn cho bản đồ chuyên đề | Bản đồ chuyên nghiệp, dễ hiểu | Phase 2 |
| Styling & Theming | Style JSON Editor | Editor style JSON | Chỉnh sửa Mapbox Style Specification trực tiếp | Tùy chỉnh sâu cho người dùng cao cấp | Phase 2 |
| Styling & Theming | Thematic Mapping | Bản đồ chuyên đề | Tạo bản đồ choropleth, graduated symbols, heat map | Trực quan hóa dữ liệu thống kê | Phase 2 |
| Styling & Theming | Dark Mode Basemap | Basemap tối | Basemap tối phù hợp hiển thị ban đêm | Giảm mỏi mắt, tiết kiệm pin | Phase 1 |
## Advanced Layer Management
> Advanced features and implementation details for advanced layer management.

| Feature Group | Feature Name | Short Description | Detailed Description | Why This Feature is Needed | Implementation Phase |
|--------------| -------------- |------------|----------------|---------------------------|---------------------|
| 2D Vector & Raster Rendering | Client-Side Caching | Cache tile phía client để kéo thả mượt | Cache tile phía client để kéo thả mượt | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 2D Vector & Raster Rendering | Tile Retry Policy | Retry có backoff khi tile lỗi tạm thời | Retry có backoff khi tile lỗi tạm thời | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 2D Vector & Raster Rendering | Overzoom Support | Phóng to vượt zoom gốc vẫn hiển thị hợp lý | Phóng to vượt zoom gốc vẫn hiển thị hợp lý | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 2D Vector & Raster Rendering | Anti-Aliasing Toggle | Bật/tắt AA cân bằng giữa chất lượng và hiệu năng | Bật/tắt AA cân bằng giữa chất lượng và hiệu năng | Cải thiện hiệu suất và trải nghiệm người dùng | Phase 2 |
| 2D Vector & Raster Rendering | Feature Simplification | Tự đơn giản hóa hình học ở zoom nhỏ để tăng tốc | Tự đơn giản hóa hình học ở zoom nhỏ để tăng tốc | Cải thiện hiệu suất và trải nghiệm người dùng | Phase 2 |
| 2D Vector & Raster Rendering | Symbol Collision Avoidance | Tránh chồng nhãn/icon gây rối | Tránh chồng nhãn/icon gây rối | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| 2D Vector & Raster Rendering | High-DPI Rendering | Hiển thị sắc nét trên màn hình retina | Hiển thị sắc nét trên màn hình retina | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Style Rule Engine Advanced | Tính năng style rule engine advanced | Tính năng style rule engine advanced | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Thematic Mapping | Tính năng thematic mapping | Tính năng thematic mapping | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | 3D Extrusion by Attribute | Tính năng 3d extrusion by attribute | Tính năng 3d extrusion by attribute | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | 3D Label Occlusion | Tính năng 3d label occlusion | Tính năng 3d label occlusion | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Ambient Occlusion | Tính năng ambient occlusion | Tính năng ambient occlusion | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Bloom/Glow Effects | Tính năng bloom/glow effects | Tính năng bloom/glow effects | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Color Blind Friendly Palettes | Tính năng color blind friendly palettes | Tính năng color blind friendly palettes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Dynamic Styling by Zoom | Tính năng dynamic styling by zoom | Tính năng dynamic styling by zoom | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Material Library | Tính năng material library | Tính năng material library | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Day/Night Scene Profiles | Tính năng day/night scene profiles | Tính năng day/night scene profiles | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Section Box Tool | Tính năng section box tool | Tính năng section box tool | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Multi-Plane Clipping | Tính năng multi-plane clipping | Tính năng multi-plane clipping | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Ghost Mode for Context | Tính năng ghost mode for context | Tính năng ghost mode for context | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Highlight by Query | Tính năng highlight by query | Tính năng highlight by query | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Animated Layers | Quản lý và điều khiển animated layers | Quản lý và điều khiển animated layers | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Vector Tile Style Editor (View) | Tính năng vector tile style editor (view) | Tính năng vector tile style editor (view) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Terrain Contours | Tính năng terrain contours | Tính năng terrain contours | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Hillshade Layer | Quản lý và điều khiển hillshade layer | Quản lý và điều khiển hillshade layer | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Skybox & Weather Presets | Tính năng skybox & weather presets | Tính năng skybox & weather presets | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Reflections (Basic) | Tính năng reflections (basic) | Tính năng reflections (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Outline Styles | Tính năng outline styles | Tính năng outline styles | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Color Scale Calibration | Tính năng color scale calibration | Tính năng color scale calibration | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Style Preset Sharing | Tính năng style preset sharing | Tính năng style preset sharing | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Multi-Layer Blending Graph | Quản lý và điều khiển multi-layer blending graph | Quản lý và điều khiển multi-layer blending graph | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Advanced - Visualization & Styling | Render Pipeline Debug | Tính năng render pipeline debug | Tính năng render pipeline debug | Hỗ trợ troubleshooting và phân tích vấn đề | Phase 2 |
| Basemaps & Reference Layers | Basemap Gallery | Thư viện basemap (street/satellite/terrain) để chọn nhanh | Thư viện basemap (street/satellite/terrain) để chọn nhanh | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Basemaps & Reference Layers | Attribution Display | Hiển thị attribution/nguồn dữ liệu theo yêu cầu license | Hiển thị attribution/nguồn dữ liệu theo yêu cầu license | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Basemaps & Reference Layers | Custom Basemap URL | Thêm basemap từ mẫu URL XYZ/WMTS | Thêm basemap từ mẫu URL XYZ/WMTS | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Basemaps & Reference Layers | Administrative Boundaries | Lớp ranh giới hành chính theo cấp | Lớp ranh giới hành chính theo cấp | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Basemaps & Reference Layers | Labels-Only Layer | Bật lớp nhãn độc lập với nền ảnh vệ tinh | Bật lớp nhãn độc lập với nền ảnh vệ tinh | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Basemaps & Reference Layers | Night Mode Basemap | Basemap tối phù hợp hiển thị ban đêm | Basemap tối phù hợp hiển thị ban đêm | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 2 |
| Foundation - Layer Management | Layer Catalog Panel | Quản lý và điều khiển layer catalog panel | Quản lý và điều khiển layer catalog panel | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Grouping (Folders) | Quản lý và điều khiển layer grouping (folders) | Quản lý và điều khiển layer grouping (folders) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Ordering DragDrop | Quản lý và điều khiển layer ordering dragdrop | Quản lý và điều khiển layer ordering dragdrop | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Opacity Slider | Tính năng opacity slider | Tính năng opacity slider | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Visibility by Zoom | Tính năng visibility by zoom | Tính năng visibility by zoom | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Metadata View | Quản lý và điều khiển layer metadata view | Quản lý và điều khiển layer metadata view | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Legend Auto-Render | Tính năng legend auto-render | Tính năng legend auto-render | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Load Status | Quản lý và điều khiển layer load status | Quản lý và điều khiển layer load status | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Retry Button | Quản lý và điều khiển layer retry button | Quản lý và điều khiển layer retry button | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Solo Mode | Quản lý và điều khiển layer solo mode | Quản lý và điều khiển layer solo mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Pin Favorites | Quản lý và điều khiển layer pin favorites | Quản lý và điều khiển layer pin favorites | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Search Highlight | Quản lý và điều khiển layer search highlight | Quản lý và điều khiển layer search highlight | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Tags Filter | Quản lý và điều khiển layer tags filter | Quản lý và điều khiển layer tags filter | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Permissions Display | Quản lý và điều khiển layer permissions display | Quản lý và điều khiển layer permissions display | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Style Switcher | Quản lý và điều khiển layer style switcher | Quản lý và điều khiển layer style switcher | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Transparency for 3D | Quản lý và điều khiển layer transparency for 3d | Quản lý và điều khiển layer transparency for 3d | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Clipping Integration | Quản lý và điều khiển layer clipping integration | Quản lý và điều khiển layer clipping integration | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Time Filter (Basic) | Quản lý và điều khiển layer time filter (basic) | Quản lý và điều khiển layer time filter (basic) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Refresh Interval | Quản lý và điều khiển layer refresh interval | Quản lý và điều khiển layer refresh interval | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Source Switching | Quản lý và điều khiển layer source switching | Quản lý và điều khiển layer source switching | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Cache Control UI | Quản lý và điều khiển layer cache control ui | Quản lý và điều khiển layer cache control ui | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Query Builder Basic | Quản lý và điều khiển layer query builder basic | Quản lý và điều khiển layer query builder basic | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Spatial Filter by Viewport | Tính năng spatial filter by viewport | Tính năng spatial filter by viewport | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Min/Max Height Range | Quản lý và điều khiển layer min/max height range | Quản lý và điều khiển layer min/max height range | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Hover Tooltip | Quản lý và điều khiển layer hover tooltip | Quản lý và điều khiển layer hover tooltip | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Cluster Control | Quản lý và điều khiển layer cluster control | Quản lý và điều khiển layer cluster control | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Heatmap Mode | Quản lý và điều khiển layer heatmap mode | Quản lý và điều khiển layer heatmap mode | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Label Toggle | Quản lý và điều khiển layer label toggle | Quản lý và điều khiển layer label toggle | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Label Priority | Quản lý và điều khiển layer label priority | Quản lý và điều khiển layer label priority | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Data Stats Summary | Quản lý và điều khiển layer data stats summary | Quản lý và điều khiển layer data stats summary | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Thumbnail Preview | Quản lý và điều khiển layer thumbnail preview | Quản lý và điều khiển layer thumbnail preview | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Dependency Handling | Quản lý và điều khiển layer dependency handling | Quản lý và điều khiển layer dependency handling | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Conflict Detection | Quản lý và điều khiển layer conflict detection | Quản lý và điều khiển layer conflict detection | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Local Draft State | Quản lý và điều khiển layer local draft state | Quản lý và điều khiển layer local draft state | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Presets (Saved Sets) | Quản lý và điều khiển layer presets (saved sets) | Quản lý và điều khiển layer presets (saved sets) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Import from URL | Quản lý và điều khiển layer import from url | Quản lý và điều khiển layer import from url | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Attribution Panel | Quản lý và điều khiển layer attribution panel | Quản lý và điều khiển layer attribution panel | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Tile Coverage Preview | Quản lý và điều khiển layer tile coverage preview | Quản lý và điều khiển layer tile coverage preview | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Quality Indicator | Quản lý và điều khiển layer quality indicator | Quản lý và điều khiển layer quality indicator | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Feature Flags per Layer | Quản lý và điều khiển layer feature flags per layer | Quản lý và điều khiển layer feature flags per layer | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Sync with URL | Quản lý và điều khiển layer sync with url | Quản lý và điều khiển layer sync with url | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Bulk Actions | Quản lý và điều khiển layer bulk actions | Quản lý và điều khiển layer bulk actions | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Performance Hint | Quản lý và điều khiển layer performance hint | Quản lý và điều khiển layer performance hint | Cải thiện hiệu suất và trải nghiệm người dùng | Phase 1 |
| Foundation - Layer Management | Layer Error Details Modal | Quản lý và điều khiển layer error details modal | Quản lý và điều khiển layer error details modal | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Access Request CTA | Quản lý và điều khiển layer access request cta | Quản lý và điều khiển layer access request cta | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Style JSON Inspector | Quản lý và điều khiển layer style json inspector | Quản lý và điều khiển layer style json inspector | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Bounding Box Filter | Quản lý và điều khiển layer bounding box filter | Quản lý và điều khiển layer bounding box filter | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Elevation Offset | Quản lý và điều khiển layer elevation offset | Quản lý và điều khiển layer elevation offset | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Level-of-Detail Bias | Quản lý và điều khiển layer level-of-detail bias | Quản lý và điều khiển layer level-of-detail bias | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Multi-Style Rules | Quản lý và điều khiển layer multi-style rules | Quản lý và điều khiển layer multi-style rules | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Feature Count by Filter | Quản lý và điều khiển layer feature count by filter | Quản lý và điều khiển layer feature count by filter | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Download Sample Data | Quản lý và điều khiển layer download sample data | Quản lý và điều khiển layer download sample data | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Scenegraph Toggle (3D) | Quản lý và điều khiển layer scenegraph toggle (3d) | Quản lý và điều khiển layer scenegraph toggle (3d) | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Material Override | Quản lý và điều khiển layer material override | Quản lý và điều khiển layer material override | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Per-Layer Screenshot | Quản lý và điều khiển layer per-layer screenshot | Quản lý và điều khiển layer per-layer screenshot | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Notes | Quản lý và điều khiển layer notes | Quản lý và điều khiển layer notes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Version Selector | Quản lý và điều khiển layer version selector | Quản lý và điều khiển layer version selector | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Change Diff Badge | Quản lý và điều khiển layer change diff badge | Quản lý và điều khiển layer change diff badge | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Preload Strategy | Quản lý và điều khiển layer preload strategy | Quản lý và điều khiển layer preload strategy | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Lazy Mount | Quản lý và điều khiển layer lazy mount | Quản lý và điều khiển layer lazy mount | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Access Token per Layer | Quản lý và điều khiển layer access token per layer | Quản lý và điều khiển layer access token per layer | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Masking | Quản lý và điều khiển layer masking | Quản lý và điều khiển layer masking | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Blend Modes | Quản lý và điều khiển layer blend modes | Quản lý và điều khiển layer blend modes | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Elevation Profile Link | Quản lý và điều khiển layer elevation profile link | Quản lý và điều khiển layer elevation profile link | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Advanced Filter Operators | Quản lý và điều khiển layer advanced filter operators | Quản lý và điều khiển layer advanced filter operators | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Filter Save/Load | Quản lý và điều khiển layer filter save/load | Quản lý và điều khiển layer filter save/load | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Diagnostics Snapshot | Quản lý và điều khiển layer diagnostics snapshot | Quản lý và điều khiển layer diagnostics snapshot | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Data Lineage Link | Quản lý và điều khiển layer data lineage link | Quản lý và điều khiển layer data lineage link | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Annotation Binding | Quản lý và điều khiển layer annotation binding | Quản lý và điều khiển layer annotation binding | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
| Foundation - Layer Management | Layer Visibility Rules by Role | Quản lý và điều khiển layer visibility rules by role | Quản lý và điều khiển layer visibility rules by role | Nâng cao khả năng và tính linh hoạt của hệ thống | Phase 1 |
