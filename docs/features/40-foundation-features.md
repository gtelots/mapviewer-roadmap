# Foundation Features

> Advanced features and implementation details for foundation features.

## 📋 Overview

**Total Features**: ~397

**Categories**: 26

---

## 📋 Nguồn


- **File**: 20. GTEL Maps Platform - Maps Viewer - Feature List - 2026.xlsx
- **Sheets analyzed**: 13 sheets
- **Total features extracted**: 1119

---

---

## 3D Scene & 3D Tiles


**4 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | 3D Mode Toggle | Chuyển 2D↔3D mượt | Chuyển 2D↔3D mượt |
| 2 | 3D Tileset Loader | Tải tileset 3D Tiles theo ID/URL | Tải tileset 3D Tiles theo ID/URL |
| 3 | 3D Feature Picking | Click đối tượng 3D để nhận diện/thông tin | Click đối tượng 3D để nhận diện/thông tin |
| 4 | 3D Tiles Cache Control | Quản lý cache tile (kích thước, eviction). | Quản lý cache tile (kích thước, eviction). |

---

---

## Core


**5 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Deep link boostrap | Khởi tạo trạng thái Viewer từ URL (camera, layers, tools,...) | Khởi tạo trạng thái Viewer từ URL (camera, layers, tools,...) |
| 2 | Config remote fetch | Lấy cấu hình viewer từ dịch vụ cấu hình (remote config) | Lấy cấu hình viewer từ dịch vụ cấu hình (remote config) |
| 3 | Startup State Presets | Áp dụng trạng thái khởi động mặc định: camera, layer, UI | Áp dụng trạng thái khởi động mặc định: camera, layer, UI |
| 4 | State Persistence | Lưu trạng thái gần nhất (chế độ xem vệ tinh, light mode,...) hoặc đang thao tác -> URL Hash | Lưu trạng thái gần nhất (chế độ xem vệ tinh, light mode,...) hoặc đang thao tác -> URL Hash |
| 5 | Feature flags | Bật/tắt tính năng bằng cờ cấu hình  | Bật/tắt tính năng bằng cờ cấu hình  |

---

---

## Foundation - 3D Tiles Streaming


**50 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F191 3D Tileset Loader |  | What: Load 3D Tiles (tileset.json + content). | Why: Nền tảng xem 3D. | Criteria: Tileset load; lỗi → message; retry. |
| 2 | F192 LOD Selection |  | What: Chọn LOD theo screen-space error. | Why: Hiệu năng & chất lượng. | Criteria: Zoom in → chi tiết tăng; zoom out → giảm. |
| 3 | F193 Frustum Culling |  | What: Chỉ tải/render tile trong frustum. | Why: Tiết kiệm tài nguyên. | Criteria: Quay camera → tiles ngoài frustum ngừng tải. |
| 4 | F194 Occlusion Culling Basic |  | What: Ẩn tile bị che (basic). | Why: Tăng FPS. | Criteria: Culling bật → draw calls giảm; không pop quá mức. |
| 5 | F195 Tile Cache (Memory) |  | What: Cache tile content trong RAM theo LRU. | Why: Giảm tải lại khi pan nhẹ. | Criteria: Pan quay lại → tile hit cache; LRU evict đúng. |
| 6 | F196 Tile Cache (Disk) |  | What: Cache tile content trong IndexedDB (optional). | Why: Tăng tốc lần sau. | Criteria: Reload → load nhanh; clear cache có tác dụng. |
| 7 | F197 Request Concurrency Limit |  | What: Giới hạn số request tile đồng thời. | Why: Tránh nghẽn mạng. | Criteria: Max N áp dụng; không gây starvation. |
| 8 | F198 Request Priority Queue |  | What: Ưu tiên tile gần camera/center. | Why: Trải nghiệm tốt hơn. | Criteria: Tile center load trước; far tiles load sau. |
| 9 | F199 Progressive Refinement |  | What: Hiển thị LOD thô trước, refine dần. | Why: Tránh màn trống. | Criteria: Mở scene → có geometry sớm; refine không giật. |
| 10 | F200 Tile Loading Indicator |  | What: Hiển thị progress tải tileset. | Why: User biết đang tải. | Criteria: Có % hoặc spinner; tắt khi ổn định. |
| 11 | F201 Tileset Bounds Visualization |  | What: Overlay bounds/tiles debug. | Why: Debug coverage. | Criteria: Toggle debug; click zoom to bounds. |
| 12 | F202 Tile Error Handling |  | What: Handle missing content/404 gracefully. | Why: Ổn định khi data thiếu. | Criteria: 404 tile → skip + log; không crash. |
| 13 | F203 Tile Retry with Backoff |  | What: Retry tile theo backoff. | Why: Chống mạng yếu. | Criteria: Timeout → retry <=N; success continues. |
| 14 | F204 Gzip/Brotli Support |  | What: Hỗ trợ content compression. | Why: Giảm băng thông. | Criteria: Response compressed → decode ok; size giảm. |
| 15 | F205 Draco/meshopt Decode |  | What: Hỗ trợ decode Draco/meshopt (nếu dùng). | Why: Giảm dung lượng 3D. | Criteria: Tileset compressed → render đúng; decode time with |
| 16 | F206 KTX2/Basis Texture |  | What: Hỗ trợ texture nén GPU. | Why: Giảm VRAM + tải nhanh. | Criteria: Texture render đúng; fallback to PNG/JPG ok. |
| 17 | F207 Tile Content Type Support |  | What: b3dm/i3dm/pnts/cmpt (cơ bản). | Why: Phủ nhiều loại nội dung. | Criteria: Load ít nhất b3dm; others theo config; error rõ. |
| 18 | F208 Point Cloud Rendering Basic |  | What: Render pnts point cloud. | Why: Scan/LiDAR use-case. | Criteria: Point size adjustable; FPS đạt ngưỡng. |
| 19 | F209 Instanced Models Basic |  | What: Render i3dm instances. | Why: Cây/cột/POI 3D. | Criteria: Instances hiển thị đúng; picking optional. |
| 20 | F210 Tile Material Pipeline |  | What: Chuẩn hoá material (PBR basic). | Why: Hiển thị nhất quán. | Criteria: Material parameters apply; gamma correct. |
| 21 | F211 Lighting per Tileset |  | What: Enable/disable lighting ảnh hưởng tileset. | Why: Chất lượng & performance. | Criteria: Toggle lighting works; visual changes expected. |
| 22 | F212 Tileset Clipping Planes |  | What: Áp clipping planes lên tileset. | Why: Cắt lát toà nhà. | Criteria: Clipping works; no major artifacts. |
| 23 | F213 Tileset Transforms |  | What: Apply transform matrix / georeference offset. | Why: Sửa lệch vị trí. | Criteria: Transform apply; persists; reset available. |
| 24 | F214 Tileset Height Correction |  | What: Correction theo geoid/ellipsoid. | Why: Đúng cao độ. | Criteria: Height adjust shifts model; documented. |
| 25 | F215 Tileset Shadow Receiver/ കാസter |  | What: Cấu hình nhận/đổ bóng. | Why: Chân thực. | Criteria: Receiver on → shadow visible; off → none. |
| 26 | F216 Tileset Picking Enable |  | What: Cho phép pick tile content. | Why: Identify 3D. | Criteria: Pick on → click returns feature; off → ignore. |
| 27 | F217 Tileset Feature Metadata Support |  | What: Đọc batch table/metadata. | Why: Hiển thị thuộc tính. | Criteria: Click → properties panel đầy đủ; missing safe. |
| 28 | F218 Tileset Style by Metadata |  | What: Style theo thuộc tính (color by height/type). | Why: Trực quan hoá. | Criteria: Rule applies; legend updates; performance ok. |
| 29 | F219 Tileset Temporal Loading Guard |  | What: Chặn unload/reload liên tục khi camera rung. | Why: Ổn định. | Criteria: Pan nhẹ → không thrash; requests giảm. |
| 30 | F220 Tile Unload Policy |  | What: Tùy policy unload theo distance/memory. | Why: Kiểm soát RAM. | Criteria: RAM cap → unload; no crash. |
| 31 | F221 Memory Budget Manager |  | What: Manager VRAM/RAM budget theo preset. | Why: Tránh OOM. | Criteria: Vượt budget → auto degrade; warn user. |
| 32 | F222 Tile Request Cancellation |  | What: Cancel request khi tile không còn cần. | Why: Tiết kiệm băng thông. | Criteria: Rotate camera nhanh → canceled requests tăng; net  |
| 33 | F223 HTTP/2 Friendly Batching |  | What: Tối ưu nhiều request nhỏ. | Why: Hiệu năng mạng. | Criteria: Request pattern ổn; không block main thread. |
| 34 | F224 CDN Cache Key Strategy |  | What: Chuẩn cache key (version, tokenless path). | Why: Tăng cache hit. | Criteria: Cache hit observable; no wrong-user leak. |
| 35 | F225 Signed URL Support |  | What: Hỗ trợ signed URLs cho tiles. | Why: Bảo mật nội dung. | Criteria: URL hết hạn → refresh flow; no infinite loop. |
| 36 | F226 Tileset Multi-Origin Support |  | What: Cho phép tileset từ nhiều domain. | Why: Linh hoạt hạ tầng. | Criteria: CORS ok; CSP ok; errors clear. |
| 37 | F227 Tileset Prewarming |  | What: Preload tiles quanh home view. | Why: Vào nhanh. | Criteria: Open scene → home area clear within target time. |
| 38 | F228 Tileset Streaming Metrics |  | What: Thu thập metrics: requests, bytes, decode time. | Why: Tối ưu hiệu năng. | Criteria: Metrics available in debug; export snapshot. |
| 39 | F229 Tileset Fallback LOD |  | What: Thiếu tile chi tiết → dùng LOD thấp. | Why: Tránh lỗ hổng. | Criteria: Missing child → parent stays; no holes. |
| 40 | F230 Tileset Versioned Manifest |  | What: Support manifest versioning. | Why: Rollback an toàn. | Criteria: Switch version → loads correct; cache invalidated. |
| 41 | F231 Multi-Tileset Orchestrator |  | What: Quản lý nhiều tileset đồng thời. | Why: Scene phức tạp. | Criteria: Enable 3 tilesets → stable; budgets shared. |
| 42 | F232 Tileset Dependency Graph |  | What: Tileset phụ thuộc (terrain mask etc.). | Why: Load đúng thứ tự. | Criteria: Dependency satisfied before render; error if missi |
| 43 | F233 Tileset Region-of-Interest |  | What: Ưu tiên ROI polygon. | Why: Focus khu vực quan trọng. | Criteria: ROI on → tiles inside load first. |
| 44 | F234 Tileset Throttling on Tab Hidden |  | What: Giảm tải khi tab hidden. | Why: Tiết kiệm tài nguyên. | Criteria: Hidden → request pause; visible → resume. |
| 45 | F235 Background Decode Worker |  | What: Decode mesh/texture trong WebWorker. | Why: Giảm lag UI. | Criteria: Main thread frame drops giảm; feature stable. |
| 46 | F236 GPU Instancing Optimization |  | What: Batch instances trên GPU. | Why: Tăng FPS. | Criteria: Draw calls giảm; visual identical. |
| 47 | F237 Tile Hotspot Detection |  | What: Detect tile “nặng” gây lag. | Why: Tối ưu dữ liệu. | Criteria: Debug shows top tiles; export list. |
| 48 | F238 Tile Integrity Check |  | What: Hash/size check (optional). | Why: Phát hiện corruption. | Criteria: Mismatch → re-fetch; log event. |
| 49 | F239 Tile Progressive Texture |  | What: Tải texture low-res trước, high-res sau. | Why: Nhanh có hình. | Criteria: Low-res appears fast; upgrade seamless. |
| 50 | F240 Multi-Resolution Terrain Tiles |  | What: Terrain tiles theo LOD. | Why: Địa hình mượt. | Criteria: Zoom in → terrain detail increases. |

---

---

## Foundation - App Shell


**40 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F001 App Init Config |  | What: Nạp cấu hình viewer theo project/scene từ JSON/URL | Why: Mở đúng ngữ cảnh; giảm công tích hợp. | Criteria: Load OK; config lỗi → fallback + banner. |
| 2 | F002 Environment Profiles |  | What: Profile dev/stg/prod cho endpoint tiles/api. | Why: Tránh nhầm môi trường; vận hành an toàn. | Criteria: Chọn profile → đổi endpoint; không cần rebuild. |
| 3 | F003 Responsive Layout Engine |  | What: Khung layout tự co giãn theo màn hình. | Why: Dùng tốt desktop/tablet/mobile. | Criteria: Không tràn UI ở 360px; panel vẫn dùng được. |
| 4 | F004 App State Store |  | What: Store trạng thái (camera, layers, tools) tập trung | Why: Đồng bộ UI; dễ debug. | Criteria: State change → UI cập nhật tức thì; không race. |
| 5 | F005 Deep Link Router |  | What: Router đọc params để mở scene, layer, view. | Why: Chia sẻ link; hỗ trợ support. | Criteria: URL hợp lệ → mở đúng; URL sai → trang lỗi thân thi |
| 6 | F006 Session Persistence |  | What: Lưu state theo sessionStorage/localStorage. | Why: Người dùng refresh không mất trạng thái. | Criteria: Refresh → giữ camera+layer; có nút “Reset”. |
| 7 | F007 Feature Flags |  | What: Toggle tính năng theo config/tenant. | Why: Rollout an toàn; A/B test. | Criteria: Flag off → UI ẩn + API không gọi. |
| 8 | F008 Theme System |  | What: Theme màu/typography theo brand. | Why: Chuẩn hoá UI; dễ white-label. | Criteria: Đổi theme → toàn UI đổi; contrast đạt ngưỡng. |
| 9 | F009 Keyboard Shortcuts Core |  | What: Phím tắt cho công cụ chính (measure, search, reset | Why: Tăng tốc thao tác. | Criteria: Shortcut hoạt động; có màn “Help”. |
| 10 | F010 Help & Onboarding |  | What: Tour hướng dẫn lần đầu + tooltip. | Why: Giảm đào tạo; tăng adoption. | Criteria: User mới thấy tour; có “Skip/Don’t show”. |
| 11 | F011 Error Boundary UI |  | What: Bắt lỗi render JS và hiển thị màn lỗi. | Why: Tránh crash trắng màn hình. | Criteria: Lỗi UI → show fallback; log kèm stack. |
| 12 | F012 Loading Skeleton |  | What: Hiển thị skeleton khi tải scene/layers. | Why: Cảm giác nhanh hơn; rõ trạng thái. | Criteria: Tải >300ms → show; xong → tự ẩn. |
| 13 | F013 Network Retry Policy |  | What: Retry có backoff cho request tiles/api. | Why: Ổn định khi mạng chập chờn. | Criteria: 5xx/timeouts → retry tối đa N lần; có cancel. |
| 14 | F014 Offline Detection |  | What: Detect offline/online và thông báo. | Why: Tránh hiểu nhầm “hệ thống lỗi”. | Criteria: Offline → banner; online → tự phục hồi. |
| 15 | F015 Telemetry Consent |  | What: Popup xin consent analytics (nếu cần). | Why: Tuân thủ privacy. | Criteria: Không consent → không gửi analytics. |
| 16 | F016 Basic Audit Trail (Client) |  | What: Ghi log thao tác chính (open scene, export, route) | Why: Hỗ trợ điều tra/sự cố. | Criteria: Log có timestamp; gửi theo batch. |
| 17 | F017 Resource Preload |  | What: Preload shader/font/icon/critical tiles. | Why: Giảm TTFP; mượt vào scene. | Criteria: TTFP giảm; preload không block tương tác. |
| 18 | F018 CDN Asset Support |  | What: Static assets dùng CDN + cache headers. | Why: Tăng tốc tải toàn quốc. | Criteria: Cache hit tăng; có versioned URLs. |
| 19 | F019 Multi-Tab Safety |  | What: Khóa xung đột khi mở nhiều tab cùng project. | Why: Tránh ghi đè state. | Criteria: 2 tab → không corrupt; cảnh báo khi cần. |
| 20 | F020 Localization Bootstrap |  | What: Nạp ngôn ngữ và định dạng số/đơn vị. | Why: Đa ngôn ngữ; chuẩn hoá hiển thị. | Criteria: Đổi lang → UI đổi; format đúng locale. |
| 21 | F021 Date/Time Utilities |  | What: Chuẩn timezone & format (ISO/locale). | Why: Đúng dữ liệu time-series. | Criteria: Hiển thị đúng timezone cấu hình; không lệch ngày. |
| 22 | F022 Permission Gate UI |  | What: Ẩn/disable UI theo role/permission. | Why: Bảo mật và đúng phân quyền. | Criteria: Role Viewer không thấy “Edit/Publish”. |
| 23 | F023 Rate Limit Friendly UI |  | What: Hiển thị trạng thái khi bị 429. | Why: Tránh user spam; dễ hiểu. | Criteria: 429 → show “try later”; auto retry sau T. |
| 24 | F024 Client Cache Control |  | What: Cache metadata (styles, catalog) theo TTL. | Why: Giảm gọi API; nhanh hơn. | Criteria: Trong TTL không gọi lại; quá TTL → refresh. |
| 25 | F025 Config Validation |  | What: Schema validation cho config khi load. | Why: Giảm lỗi cấu hình. | Criteria: Config sai → liệt kê field sai; dùng default. |
| 26 | F026 Dependency Health Check |  | What: Kiểm tra WebGL2, memory, GPU tier. | Why: Chọn preset phù hợp; tránh crash. | Criteria: Không hỗ trợ → cảnh báo + fallback 2D/basic. |
| 27 | F027 Security Headers Readiness |  | What: Chuẩn CSP/COOP/COEP tương thích. | Why: Tăng an toàn; hỗ trợ isolate. | Criteria: Không vi phạm CSP; docs cấu hình rõ. |
| 28 | F028 CORS Preflight Optimizer |  | What: Giảm preflight không cần thiết. | Why: Hiệu năng mạng tốt hơn. | Criteria: Request lặp → không phát sinh preflight quá mức. |
| 29 | F029 Version Badge & Build Info |  | What: Hiển thị version, commit, env trong About. | Why: Triage bug nhanh. | Criteria: About có version; copy được. |
| 30 | F030 Changelog Notifier |  | What: Thông báo tính năng mới sau deploy. | Why: Giảm support; user cập nhật. | Criteria: Có “What’s new”; dismiss nhớ trạng thái. |
| 31 | F031 API Key Input Modes |  | What: Nhận key qua header, query, or token provider. | Why: Linh hoạt tích hợp. | Criteria: Key hợp lệ → call OK; sai → lỗi rõ ràng. |
| 32 | F032 Token Refresh Hook |  | What: Hook refresh token khi 401. | Why: Trải nghiệm liền mạch; bảo mật. | Criteria: 401 → refresh 1 lần; fail → logout. |
| 33 | F033 Secure Storage Wrapper |  | What: Lưu token an toàn (memory/secure cookie strategy). | Why: Giảm rủi ro lộ token. | Criteria: Không lưu token plaintext localStorage (nếu policy |
| 34 | F034 Content Sanitization |  | What: Sanitize text/HTML trong popup/annotation. | Why: Chống XSS. | Criteria: Input chứa script → bị loại; không execute. |
| 35 | F035 Crash Recovery Mode |  | What: Chế độ safe-mode tắt tính năng nặng khi crash. | Why: Giúp mở được scene để debug. | Criteria: Sau crash → hỏi safe-mode; load thành công. |
| 36 | F036 Config Override UI UI |  | What: Tùy chọn override config trong debug panel. | Why: Debug nhanh mà không rebuild. | Criteria: Override áp dụng ngay; có reset. |
| 37 | F037 Startup Performance Budget |  | What: Budget thời gian khởi động & cảnh báo khi vượt. | Why: Kiểm soát regression. | Criteria: Vượt ngưỡng → log + badge đỏ. |
| 38 | F038 Accessibility Baseline |  | What: ARIA labels & focus ring cơ bản. | Why: Đáp ứng tối thiểu A11y. | Criteria: Tab đến nút chính; screen reader đọc được. |
| 39 | F039 Cookie/Storage Policy Banner |  | What: Banner tuân thủ cookie/storage (nếu cần). | Why: Compliance. | Criteria: Có Accept/Reject; hành vi đúng lựa chọn. |
| 40 | F040 Multi-Project Switcher |  | What: UI chuyển nhanh giữa các project trong org. | Why: Tăng hiệu suất vận hành. | Criteria: Switch → reload scene đúng; quyền áp dụng đúng. |

---

---

## Foundation - Interaction & Identify


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F241 Click Select Basics |  | What: Click chọn feature, highlight. | Why: Tương tác cơ bản. | Criteria: Click → highlight; click empty → clear. |
| 2 | F242 Hover Highlight |  | What: Hover feature → outline nhẹ. | Why: Tra cứu nhanh. | Criteria: Hover 150ms → highlight; off → clear. |
| 3 | F243 Properties Panel |  | What: Panel hiển thị thuộc tính feature. | Why: Hiểu đối tượng. | Criteria: Select → panel mở; fields theo schema. |
| 4 | F244 Attribute Formatting |  | What: Format số/đơn vị/ngày giờ theo locale. | Why: Đọc dễ; tránh hiểu sai. | Criteria: Format consistent; null → “—”. |
| 5 | F245 Copy Attribute |  | What: Copy giá trị field/JSON. | Why: Tác nghiệp nhanh. | Criteria: Click copy → clipboard; toast confirm. |
| 6 | F246 Feature Locate Button |  | What: Nút “Zoom to feature”. | Why: Đi nhanh đến đối tượng. | Criteria: Click → flyTo + focus; works for all layers pickab |
| 7 | F247 Multi-Select Mode |  | What: Chọn nhiều feature và xem list. | Why: So sánh/đối chiếu. | Criteria: Shift/checkbox select; list updates; clear all. |
| 8 | F248 Selection Set Save |  | What: Lưu tập selection thành “set”. | Why: Review/QA. | Criteria: Save/load set; permission guarded. |
| 9 | F249 Identify Across Layers |  | What: Click 1 điểm → trả kết quả nhiều layer. | Why: Tra cứu chồng lớp. | Criteria: Hiển thị danh sách; chọn item → focus. |
| 10 | F250 Pixel/World Tolerance Control |  | What: Chỉnh tolerance picking. | Why: Đúng với touch và dense data. | Criteria: Tolerance changes hit-rate; default reasonable. |

---

---

## Foundation - Scene & Camera


**80 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F041 Camera Orbit |  | What: Phiên điều khiển orbit quanh target. | Why: Điều hướng 3D cơ bản. | Criteria: Orbit mượt; không giật; có giới hạn pitch. |
| 2 | F042 Camera Pan |  | What: Pan theo mặt phẳng màn hình/ground. | Why: Khám phá khu vực nhanh. | Criteria: Pan không “drift”; tốc độ theo zoom. |
| 3 | F043 Camera Zoom |  | What: In/out bằng wheel/pinch. | Why: Điều hướng cơ bản. | Criteria: Zoom mượt; clamp min/max. |
| 4 | F044 Fly-To Position |  | What: Fly camera đến tọa độ/bounds. | Why: Đi nhanh đến POI/kết quả search. | Criteria: FlyTo <2s; có easing; có cancel. |
| 5 | F045 Home View |  | What: 1 nút về góc nhìn mặc định. | Why: Giảm lạc hướng. | Criteria: Click Home → đúng view; giữ trong config. |
| 6 | F046 Compass Widget |  | What: La bàn + click để reset heading. | Why: Dễ định hướng. | Criteria: Click compass → heading=0; rotate theo camera. |
| 7 | F047 Pitch Controls |  | What: Điều chỉnh tilt/pitch slider. | Why: Quan sát 3D linh hoạt. | Criteria: Pitch slider hoạt động; clamp 0-89°. |
| 8 | F048 Camera Inertia |  | What: Quán tính camera khi kéo. | Why: Cảm giác mượt. | Criteria: Inertia bật/tắt; không gây chóng mặt. |
| 9 | F049 Camera Collision |  | What: Chống camera xuyên terrain/building (basic). | Why: Tránh “tụt” vào trong mô hình. | Criteria: Đi xuống → dừng ở ground; không clip nặng. |
| 10 | F050 Globe/Plane Mode |  | What: Chế độ globe (3D) hoặc flat (2.5D). | Why: Tương thích use-case khác nhau. | Criteria: Switch mode → không crash; layers giữ trạng thái. |
| 11 | F051 Coordinate Display |  | What: Hiển thị tọa độ con trỏ (lat/lon/height). | Why: Hỗ trợ tác nghiệp. | Criteria: Cursor move → tọa độ cập nhật; copy được. |
| 12 | F052 Scale Bar |  | What: Thước tỷ lệ theo zoom. | Why: Hiểu khoảng cách trực quan. | Criteria: Scale thay đổi đúng; đơn vị auto m/km. |
| 13 | F053 Minimap (Optional) |  | What: Minimap 2D góc màn hình. | Why: Định hướng khi camera nghiêng. | Criteria: Minimap sync; click minimap → flyTo. |
| 14 | F054 North Lock Option |  | What: Khóa hướng Bắc (no rotate). | Why: Cho user mới; dùng kiosk. | Criteria: Bật lock → rotate bị disable; UI phản hồi rõ. |
| 15 | F055 Camera Bookmarks |  | What: Lưu/đặt tên góc nhìn. | Why: Demo, chia sẻ view chuẩn. | Criteria: Lưu được; mở lại sai số nhỏ; CRUD hoạt động. |
| 16 | F056 Camera Transition Presets |  | What: Preset tốc độ flyTo (fast/normal/cinematic). | Why: Trải nghiệm nhất quán. | Criteria: Chọn preset → thời gian bay thay đổi rõ. |
| 17 | F057 Camera Path Recording |  | What: Ghi lại đường bay camera (keyframes). | Why: Tạo tour/đào tạo. | Criteria: Record/playback hoạt động; export JSON. |
| 18 | F058 Camera Path Playback |  | What: Phát tour camera tự động. | Why: Showcase, kiosk. | Criteria: Play/pause/stop; loop tùy chọn. |
| 19 | F059 Camera Sync Multi-Views |  | What: Đồng bộ camera giữa 2 khung view. | Why: So sánh before/after. | Criteria: Pan/zoom ở view A → view B sync. |
| 20 | F060 Split Screen Compare |  | What: Chia đôi màn hình so 2 scene/layer set. | Why: So sánh dữ liệu. | Criteria: Drag slider; hai bên render ổn định. |
| 21 | F061 Field of View Control |  | What: Điều chỉnh FOV. | Why: Phù hợp nhiều màn hình/GPU. | Criteria: FOV slider; default an toàn; không méo quá mức. |
| 22 | F062 Near/Far Plane Tuning |  | What: Tinh chỉnh clip planes để giảm z-fighting. | Why: Ổn định render 3D. | Criteria: Auto hoặc manual; giảm flicker thấy rõ. |
| 23 | F063 Auto-Exposure (Basic) |  | What: Tự chỉnh sáng theo scene. | Why: Nhìn rõ ban ngày/đêm. | Criteria: Đổi time-of-day → exposure điều chỉnh mượt. |
| 24 | F064 Frame Rate Cap |  | What: Giới hạn FPS (30/60/unlimited). | Why: Tiết kiệm pin; ổn định. | Criteria: Chọn 30fps → CPU/GPU giảm; vẫn mượt. |
| 25 | F065 Camera Constraints by Area |  | What: Giới hạn camera trong bounding polygon. | Why: Kiosk/giới hạn khu vực dự án. | Criteria: Ra ngoài vùng → camera bị clamp +提示. |
| 26 | F066 Terrain Exaggeration |  | What: Phóng đại địa hình. | Why: Trực quan địa mạo. | Criteria: Slider 1–N; cập nhật realtime. |
| 27 | F067 Terrain Toggle |  | What: Bật/tắt terrain. | Why: Fallback cho máy yếu. | Criteria: Toggle không crash; objects clamp theo mode. |
| 28 | F068 Height Reference Modes |  | What: Clamp to ground / relative / absolute. | Why: Đúng hiển thị đối tượng 3D. | Criteria: Đổi mode → vị trí đối tượng đúng theo spec. |
| 29 | F069 Sun & Time-of-Day Basic |  | What: Điều chỉnh giờ để đổi hướng sáng. | Why: Trực quan hóa bóng/ánh sáng. | Criteria: Time slider → sun direction đổi; stable. |
| 30 | F070 Shadow Toggle |  | What: Bật/tắt shadow. | Why: Cân bằng chất lượng/hiệu năng. | Criteria: Toggle shadow; FPS thay đổi; không artifact nặng. |
| 31 | F071 Fog Control |  | What: Fog distance/density. | Why: Tạo chiều sâu; che noise LOD xa. | Criteria: Fog slider → hiệu ứng rõ; có off. |
| 32 | F072 Atmosphere Toggle |  | What: Atmosphere/skybox bật/tắt. | Why: Thẩm mỹ + hiệu năng. | Criteria: Toggle không ảnh hưởng data; không crash. |
| 33 | F073 Ground Transparency |  | What: Độ trong suốt ground/terrain. | Why: Nhìn tầng hầm/indoor. | Criteria: Alpha slider; không mất picking. |
| 34 | F074 Camera Reset Orientation |  | What: Reset heading/pitch/roll giữ vị trí. | Why: Thoát tình trạng “xoay loạn”. | Criteria: Reset → orientation chuẩn; position giữ. |
| 35 | F075 Jump to Coordinates |  | What: Nhập tọa độ → flyTo. | Why: Tác nghiệp nhanh. | Criteria: Input valid → bay đến; invalid → validate. |
| 36 | F076 Camera Speed Control |  | What: Chỉnh tốc độ pan/zoom. | Why: Phù hợp trackpad/mouse. | Criteria: Speed slider; effect rõ; lưu theo user. |
| 37 | F077 Touch Gesture Support |  | What: Pinch/rotate/two-finger pan. | Why: Mobile/tablet. | Criteria: Gesture hoạt động; không xung đột scroll page. |
| 38 | F078 Double-Click FlyTo |  | What: Double click đối tượng → zoom/flyTo. | Why: Đi nhanh vào chi tiết. | Criteria: Double click → flyTo feature; có disable. |
| 39 | F079 Camera Focus on Selection |  | What: Chọn feature → camera focus + offset đẹp. | Why: Trao đổi/giải thích đối tượng. | Criteria: Select → focus <1s; không xuyên model. |
| 40 | F080 Auto-LOD Targeting |  | What: Ưu tiên load tile quanh target khi flyTo. | Why: Giảm “màn hình trống”. | Criteria: FlyTo → tile near target ưu tiên tải trước. |
| 41 | F081 Camera Shake Guard |  | What: Chống rung khi terrain noisy. | Why: Tăng ổn định. | Criteria: Rung giảm; không ảnh hưởng điều hướng. |
| 42 | F082 High Precision Mode |  | What: Mode dùng high-precision for large coords. | Why: Tránh jitter xa gốc. | Criteria: Jitter giảm ở zoom sâu; FPS không tụt quá mức. |
| 43 | F083 Device Pixel Ratio Control |  | What: Chỉnh DPR cho render. | Why: Cân bằng chất lượng/hiệu năng. | Criteria: DPR thấp → FPS tăng; vẫn readable. |
| 44 | F084 Screenshot Viewport Safe Area |  | What: Đánh dấu vùng không bị che bởi UI. | Why: Ảnh chụp sạch. | Criteria: Screenshot exclude UI hoạt động đúng. |
| 45 | F085 Camera Presets by Role |  | What: Preset camera khác nhau theo role (viewer/operator | Why: Phù hợp nghiệp vụ. | Criteria: Role change → preset áp; override user vẫn được. |
| 46 | F086 Kiosk Auto-Rotate |  | What: Tự quay quanh điểm khi idle. | Why: Demo sự kiện. | Criteria: Idle T giây → auto-rotate; tương tác → dừng. |
| 47 | F087 Multi-Monitor Support |  | What: Tối ưu UI cho màn hình lớn/ultrawide. | Why: Phòng điều hành. | Criteria: Panel docking hợp lý; không stretch méo. |
| 48 | F088 VRAM Budget Indicator |  | What: Ước lượng VRAM usage hiển thị. | Why: Tránh crash do out-of-memory. | Criteria: Vượt ngưỡng → cảnh báo + gợi ý preset low. |
| 49 | F089 Camera Roll Lock |  | What: Khóa roll để tránh nghiêng. | Why: Trải nghiệm dễ dùng. | Criteria: Roll luôn 0 khi lock; vẫn tilt được. |
| 50 | F090 Camera Smooth Stop |  | What: Dừng camera mượt không giật. | Why: Tăng cảm giác “pro”. | Criteria: Stop không overshoot; consistent across devices. |
| 51 | F091 Adaptive Input Sensitivity |  | What: Tự chỉnh sensitivity theo FPS/latency. | Why: Mượt trên máy yếu. | Criteria: FPS thấp → giảm sensitivity; vẫn điều khiển được. |
| 52 | F092 Camera Teleport Mode |  | What: Tắt animation, nhảy tức thì. | Why: Dùng cho tác nghiệp nhanh. | Criteria: Teleport on → flyTo = instant; không flicker. |
| 53 | F093 Camera Follow Object |  | What: Follow 1 đối tượng di động (track). | Why: Theo dõi tài sản. | Criteria: Object move → camera follow; có stop. |
| 54 | F094 Camera LookAt Lock |  | What: Khóa nhìn vào 1 điểm khi pan/orbit. | Why: Quan sát công trình. | Criteria: LookAt giữ; user vẫn zoom/pan quanh. |
| 55 | F095 Camera Safe Height Floor |  | What: Không cho camera thấp hơn height min. | Why: Tránh xuyên mặt đất. | Criteria: Clamp height; configurable per scene. |
| 56 | F096 Camera Navigation History |  | What: Back/forward các vị trí camera. | Why: Quay lại vị trí trước. | Criteria: Back/Forward hoạt động; stack giới hạn N. |
| 57 | F097 Camera Jump List |  | What: Tự lưu “recent views” 10 mục. | Why: Tiện quay lại. | Criteria: List có timestamp; click → restore. |
| 58 | F098 Camera Metrics Overlay |  | What: Hiển thị camera pos/heading/pitch. | Why: Debug & support. | Criteria: Toggle overlay; copy JSON. |
| 59 | F099 Camera API Surface |  | What: Expose API: getCamera/setCamera/flyTo. | Why: Tích hợp bên ngoài. | Criteria: API ổn định; có typings; error handling. |
| 60 | F100 Camera Events |  | What: Emit events: moveStart/moveEnd/changed. | Why: Đồng bộ app host. | Criteria: Event phát đúng; debounce hợp lý. |
| 61 | F101 View Frustum Debug |  | What: Draw frustum & culling boxes (debug). | Why: Debug streaming. | Criteria: Debug bật → thấy frustum; tắt → không render. |
| 62 | F102 Ground Clamp Sampling Mode |  | What: Chọn method lấy height (terrain/mesh). | Why: Độ chính xác đo/vẽ. | Criteria: Mode đổi → kết quả height khác rõ; doc rõ. |
| 63 | F103 Transition Interruptability |  | What: Cho phép user can interrupt flyTo. | Why: Không bị “kẹt” animation. | Criteria: User drag → flyTo dừng ngay; state consistent. |
| 64 | F104 Camera Auto-Focus on Search |  | What: Khi search ra feature → auto-focus. | Why: Trải nghiệm search tốt hơn. | Criteria: Search select → focus; có toggle off. |
| 65 | F105 Precision Cursor Height |  | What: Read height dưới con trỏ theo raycast. | Why: Đo vẽ chính xác. | Criteria: Raycast trả height; fallback khi không hit. |
| 66 | F106 Scene Screenshot Thumbnail |  | What: Tạo thumbnail scene khi lưu bookmark. | Why: Dễ chọn bookmark. | Criteria: Bookmark có thumbnail; update khi re-save. |
| 67 | F107 Cinematic DOF (Basic) |  | What: Depth-of-field đơn giản (optional). | Why: Trình diễn nâng cao. | Criteria: Bật DOF → hiệu ứng rõ; FPS không tụt quá ngưỡng. |
| 68 | F108 Anti-Aliasing Toggle |  | What: MSAA/FXAA toggle. | Why: Cân bằng quality/perf. | Criteria: AA on → răng cưa giảm; off → FPS tăng. |
| 69 | F109 Anisotropic Filtering Level |  | What: Chỉnh mức anisotropic. | Why: Rõ texture góc xiên. | Criteria: Level tăng → texture rõ; VRAM tăng có cảnh báo. |
| 70 | F110 Screenshot at Resolution |  | What: Render screenshot 2x/4x. | Why: Báo cáo chất lượng cao. | Criteria: Chọn 4x → ảnh đúng size; không crash. |
| 71 | F111 Camera Tutorial Mode |  | What: Gợi ý thao tác (drag to rotate…) khi user lúng tún | Why: Giảm friction. | Criteria: Không thao tác 10s → hint; thao tác → ẩn. |
| 72 | F112 Center-on-Map Click |  | What: Click map (no feature) → set orbit center. | Why: Điều hướng nhanh. | Criteria: Click ground → orbit center đổi; có toggle. |
| 73 | F113 Auto-Leveling |  | What: Auto level pitch về 0 khi zoom out. | Why: Tránh bị nghiêng xa. | Criteria: Zoom out → pitch giảm; zoom in giữ. |
| 74 | F114 Safe Mode Rendering |  | What: Tắt shadow/AA khi FPS < threshold. | Why: Tự bảo vệ hiệu năng. | Criteria: FPS thấp → auto degrade; phục hồi khi FPS ổn. |
| 75 | F115 Camera Boundary Snap |  | What: Snap camera to boundaries (district/campus). | Why: Kiosk/giới hạn vùng. | Criteria: Gần biên → snap; user cảm nhận rõ. |
| 76 | F116 Telemetry for Navigation |  | What: Ghi metrics: time-to-move, move distance. | Why: Tối ưu UX. | Criteria: Metrics gửi theo batch; tôn trọng consent. |
| 77 | F117 Viewport Ruler |  | What: Grid overlay theo tọa độ. | Why: Định vị nhanh. | Criteria: Toggle grid; spacing theo zoom. |
| 78 | F118 Night Mode Preset |  | What: Preset tối (reduce glare). | Why: Dùng phòng điều hành ban đêm. | Criteria: Enable night mode → UI + scene phù hợp. |
| 79 | F119 High Contrast Scene Mode |  | What: Tăng tương phản cho người nhìn kém. | Why: A11y. | Criteria: Toggle → contrast tăng; text readable. |
| 80 | F120 Camera Snapshot API |  | What: API chụp camera state JSON. | Why: Lưu/chia sẻ view qua host app. | Criteria: getCameraState trả đủ fields; restore hoạt động. |

---

---

## Layer Catalog & Management


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

## Measurement & Geometry Tools


**8 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

## Observability & Integrations


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 9 | Webhook Triggers (Optional) | Kích hoạt webhook cho hành động quan trọng (optional). | Kích hoạt webhook cho hành động quan trọng (optional). |

---

---

## Performance & Reliability


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Adaptive Quality | Tự điều chỉnh chất lượng theo FPS/năng lực thiết bị. | Tự điều chỉnh chất lượng theo FPS/năng lực thiết bị. |
| 2 | Tile Request Concurrency Control | Giới hạn số request song song tránh nghẽn. | Giới hạn số request song song tránh nghẽn. |
| 3 | Progressive Loading | Tải thô trước, tinh dần để người dùng thấy nhanh. | Tải thô trước, tinh dần để người dùng thấy nhanh. |
| 4 | Cache Management UI | Xem/xóa cache để xử lý lỗi hiển thị. | Xem/xóa cache để xử lý lỗi hiển thị. |
| 5 | Network Resilience Mode | Chế độ tiết kiệm băng thông khi mạng yếu. | Chế độ tiết kiệm băng thông khi mạng yếu. |
| 6 | Error Boundary U | Màn hình lỗi thân thiện, có nút khôi phục. | Màn hình lỗi thân thiện, có nút khôi phục. |
| 7 | Offline Detection | Phát hiện offline và tạm dừng request hợp lý. | Phát hiện offline và tạm dừng request hợp lý. |
| 8 | Resource Budgeting | Giới hạn RAM, tự evict tile ít dùng. | Giới hạn RAM, tự evict tile ít dùng. |
| 9 | Warm Start | Preload tile quanh điểm xuất phát để mở nhanh. | Preload tile quanh điểm xuất phát để mở nhanh. |

---

---

## Routing & Navigation


**7 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Outdoor Routing | Tìm đường ngoài trời giữa A→B | Tìm đường ngoài trời giữa A→B |
| 4 | Route Profiles | Hồ sơ tuyến: car/bike/walk/accessibility. | Hồ sơ tuyến: car/bike/walk/accessibility. |
| 5 | Avoid Options | Tùy chọn tránh: thu phí/cao tốc/cầu thang/khu hạn chế. | Tùy chọn tránh: thu phí/cao tốc/cầu thang/khu hạn chế. |
| 6 | Multi-Stop Routing | Thêm điểm dừng (via points), tối ưu thứ tự (optional). | Thêm điểm dừng (via points), tối ưu thứ tự (optional). |
| 7 | Turn-by-Turn Steps | Danh sách hướng dẫn từng bước. | Danh sách hướng dẫn từng bước. |

---

---

## Security & Privacy (OAuth2 Opaque Tokens)


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | OAuth2 Login (Auth Code + PKCE) | Đăng nhập an toàn theo OAuth2 với PKCE. | Đăng nhập an toàn theo OAuth2 với PKCE. |
| 2 | Opaque Access Token Storage | Lưu access token dạng opaque an toàn, không “parse token”. | Lưu access token dạng opaque an toàn, không “parse token”. |
| 4 | Token Revocation on Logout | Logout thì revoke token theo RFC 7009 (nếu bật). | Logout thì revoke token theo RFC 7009 (nếu bật). |
| 7 | Cross-Tenant Isolation Guards | Ngăn request trộn tenant (đảm bảo isolation). | Ngăn request trộn tenant (đảm bảo isolation). |
| 8 | PII Redaction in Logs | Loại PII khỏi log/telemetry phía client. | Loại PII khỏi log/telemetry phía client. |

---

---

## Sharing & Export


**11 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

## Terrain & Elevation


**3 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 2 | Elevation Query | Truy vấn độ cao tại điểm người dùng click | Truy vấn độ cao tại điểm người dùng click |
| 3 | Height Profile Tool | Biểu đồ cao độ theo tuyến (profile) | Biểu đồ cao độ theo tuyến (profile) |

---

---

## Uncategory


**38 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Hiển thị bản đồ hình cầu |  |  |
| 2 | Bật, tắt lớp dữ liệu | Bật/ tắt lớp tình trạng kẹt xe, địa điểm (POI) | Bật/ tắt lớp tình trạng kẹt xe, địa điểm (POI) |
| 3 | Custom map button | Nút phóng to, thu nhỏ | Nút phóng to, thu nhỏ |
| 4 | Xoay trục Bắc bản đồ |  |  |
| 5 | Vị trí của tôi |  |  |
| 6 | Sao chép vị trí |  |  |
| 7 | None | Chia sẻ địa điểm | Chia sẻ địa điểm |

---

---

## Use Cases - tmp


**49 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Pan / Zoom / Rotate / Tilt | Điều khiển camera 3D | Điều khiển camera 3D |
| 2 | Reset / Home view | Về góc nhìn mặc định | Về góc nhìn mặc định |
| 3 | Fly-to (animate) | Bay đến vị trí/đối tượng | Bay đến vị trí/đối tượng |
| 4 | Bookmark viewpoints | Lưu góc nhìn | Lưu góc nhìn |
| 5 | Camera settings | Tùy chỉnh camera | Tùy chỉnh camera |
| 6 | Lighting (Sun) | Ánh sáng theo thời gian | Ánh sáng theo thời gian |
| 7 | Shadows | Đổ bóng | Đổ bóng |
| 8 | Terrain/DEM (tuỳ) | Địa hình 3D | Địa hình 3D |
| 9 | Globe/Flat mode (tuỳ) | Địa cầu/phẳng | Địa cầu/phẳng |
| 10 | Layer list & visibility | Bật/tắt lớp dữ liệu | Bật/tắt lớp dữ liệu |
| 11 | Opacity | Độ trong suốt | Độ trong suốt |
| 12 | Layer ordering / priority | Ưu tiên hiển thị | Ưu tiên hiển thị |
| 13 | 3D Tiles / Model layer | Lớp mô hình 3D | Lớp mô hình 3D |
| 14 | Vector / POI layers | Lớp 2D/POI trên 3D | Lớp 2D/POI trên 3D |
| 15 | Filter by attribute | Lọc theo thuộc tính | Lọc theo thuộc tính |
| 16 | Time filter (tuỳ) | Lọc theo thời gian | Lọc theo thời gian |
| 17 | Pick / Select object | Chọn đối tượng | Chọn đối tượng |
| 18 | Hover highlight | Tô sáng khi hover | Tô sáng khi hover |
| 19 | Tooltip / Popup | Thông tin nhanh | Thông tin nhanh |
| 20 | Details panel | Bảng chi tiết | Bảng chi tiết |
| 21 | Multi-select (tuỳ) | Chọn nhiều đối tượng | Chọn nhiều đối tượng |
| 22 | Search (place/POI/address) | Tìm kiếm | Tìm kiếm |
| 23 | Autocomplete | Gợi ý khi gõ | Gợi ý khi gõ |
| 24 | Locate me / GPS (tuỳ) | Định vị người dùng | Định vị người dùng |
| 25 | Route | Vẽ tuyến đường | Vẽ tuyến đường |
| 26 | Route preview | Xem trước tuyến | Xem trước tuyến |
| 27 | Turn-by-turn steps (tuỳ) | Hướng dẫn từng bước | Hướng dẫn từng bước |
| 28 | Measure distance | Đo khoảng cách | Đo khoảng cách |
| 29 | Measure area | Đo diện tích | Đo diện tích |
| 30 | Measure height | Đo chiều cao | Đo chiều cao |
| 31 | Draw/Annotate (tuỳ) | Vẽ & ghi chú | Vẽ & ghi chú |
| 32 | Clipping plane/box | Cắt để nhìn bên trong | Cắt để nhìn bên trong |
| 34 | Indoor/Outdoor switch | Chuyển cảnh indoor/outdoor | Chuyển cảnh indoor/outdoor |
| 35 | Style / Theme switch | Đổi style | Đổi style |
| 36 | Label control | Điều khiển nhãn | Điều khiển nhãn |
| 37 | Color by attribute | Tô màu theo thuộc tính | Tô màu theo thuộc tính |
| 38 | Heatmap/Choropleth (tuỳ) | Bản đồ nhiệt/choropleth | Bản đồ nhiệt/choropleth |
| 39 | Share link | Chia sẻ trạng thái | Chia sẻ trạng thái |
| 40 | Screenshot | Chụp ảnh | Chụp ảnh |
| 41 | Export data (tuỳ) | Xuất dữ liệu | Xuất dữ liệu |
| 42 | LOD/Streaming | Tải theo mức chi tiết | Tải theo mức chi tiết |
| 43 | Cache | Cache tiles/models | Cache tiles/models |
| 44 | FPS/Debug panel | Bảng debug | Bảng debug |
| 45 | API key / token | Xác thực truy cập | Xác thực truy cập |
| 46 | RBAC / Access control | Phân quyền dữ liệu | Phân quyền dữ liệu |
| 47 | Event API | Sự kiện tương tác | Sự kiện tương tác |
| 48 | Custom layers | Nhúng lớp tuỳ chỉnh | Nhúng lớp tuỳ chỉnh |
| 49 | Plugin system (tuỳ) | Hệ plugin | Hệ plugin |

---

---

## Use Cases - tmp2


**18 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Trải nghiệm bản đồ & Camera | Pan / Zoom / Rotate / Tilt | Pan / Zoom / Rotate / Tilt |
| 2 | Trực quan hóa & Style |  |  |
| 3 | Tìm kiếm & Định vị | Search address | Search address |
| 4 | Dẫn đường | Route | Route |
| 5 | Đo đạc & vẽ | Measure distance | Measure distance |
| 7 | Nền/khung cảnh 3D | Lighting (Sun) | Lighting (Sun) |
| 8 | Dữ liệu & Layer | Layer list & visibility | Layer list & visibility |
| 9 | Tương tác & Thông tin | Pick / Select object | Pick / Select object |
| 13 | Cắt lớp & Indoor | Clipping plane/box | Clipping plane/box |
| 15 | Chia sẻ & Xuất bản | Share link | Share link |
| 16 | Hiệu năng & Debug | LOD/Streaming | LOD/Streaming |
| 17 | Bảo mật & Phân quyền | API key / token | API key / token |
| 18 | Tích hợp & Mở rộng | Event API | Event API |

---

---

## Use Cases - tmp3


**296 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | CORE MAP & VISUALIZATION | NỀN TẢNG BẢN ĐỒ | NỀN TẢNG BẢN ĐỒ |
| 2 | Hiển thị bản đồ cơ bản |  |  |
| 3 | Xem chi tiết | Người dùng có thể xem chi tiết một địa điểm | Người dùng có thể xem chi tiết một địa điểm |
| 5 | Quay bản đồ | Người dùng có thể quay bản đồ sang trái | Người dùng có thể quay bản đồ sang trái |
| 6 | Nghiêng bản đồ | Người dùng có thể nghiêng bản đồ lên trên | Người dùng có thể nghiêng bản đồ lên trên |
| 7 | Phóng to thu nhỏ bản đồ | Người dùng có thể phóng to bản đồ | Người dùng có thể phóng to bản đồ |
| 8 | Đổi layout hiển thị | Cho phép đổi bản đồ sang tối | Cho phép đổi bản đồ sang tối |
| 9 | Xem vị trí | Người dùng có thể click chuột trái vào bản đồ để xem thông tin một vị trí bất kỳ trên bản đồ | Người dùng có thể click chuột trái vào bản đồ để xem thông tin một vị trí bất kỳ trên bản đồ |
| 10 | Sao chép kinh độ vĩ độ | Người dùng có thể click chuột phải trên bản đồ và sao chép kinh độ, vĩ độ của vị trí đó | Người dùng có thể click chuột phải trên bản đồ và sao chép kinh độ, vĩ độ của vị trí đó |
| 11 | Người dùng có thể xem tọa độ vn2000/WGS84 | Người dùng có thể xem tọa độ VN2000, WGS 84 | Người dùng có thể xem tọa độ VN2000, WGS 84 |
| 12 | Basemap & đa nguồn, Thao tác vị trí & tọa độ |  |  |
| 13 | Hiển thị bản đồ đa nguồn | hỗ trợ basemaps (OSM, satelit, bản đồ chính phủ), tiles raster/ vector (XYZ, TileJSON), WMS/WMTS, TM | hỗ trợ basemaps (OSM, satelit, bản đồ chính phủ), tiles raster/ vector (XYZ, TileJSON), WMS/WMTS, TM |
| 15 | Định vị GPS “Vị trí của tôi” | Cho phép định vị gps của tôi | Cho phép định vị gps của tôi |
| 16 | Measurement tools | đo khoảng cách, diện tích, tọa độ. | đo khoảng cách, diện tích, tọa độ. |
| 17 | Drawing & annotation | vẽ vùng, đường, điểm; lưu annotation vào hệ thống (kèm meta: user, time). | vẽ vùng, đường, điểm; lưu annotation vào hệ thống (kèm meta: user, time). |
| 18 | Hiển thị Lớp địa giới | tỉnh / huyện / xã / phường | tỉnh / huyện / xã / phường |
| 19 | Lưu địa điểm | Người dùng có thể lưu địa điểm để dễ dàng xem lại sau đó | Người dùng có thể lưu địa điểm để dễ dàng xem lại sau đó |
| 20 | Chia sẻ địa điểm | Người dùng có thể chia sẻ địa điểm bằng sao chép link | Người dùng có thể chia sẻ địa điểm bằng sao chép link |
| 21 | Đề xuất chỉnh sửa | Người dùng có thể đề xuất chỉnh sửa một địa điểm | Người dùng có thể đề xuất chỉnh sửa một địa điểm |
| 22 | Cài đặt hiển thị bản đồ | Người dùng có thể cái đặt hiển thị bản đồ theo thời tiết: tự động, nắng, mưa, tuyết | Người dùng có thể cái đặt hiển thị bản đồ theo thời tiết: tự động, nắng, mưa, tuyết |
| 23 | Lựa chọn ngôn ngữ | Người dùng có thể lựa chọn ngôn ngữ sử dụng là tiếng Việt hoặc tiếng Anh | Người dùng có thể lựa chọn ngôn ngữ sử dụng là tiếng Việt hoặc tiếng Anh |
| 24 | Phân quyền dữ liệu theo lớp bản đồ | Camera, GPS, lực lượng → chỉ user được phép mới thấy | Camera, GPS, lực lượng → chỉ user được phép mới thấy |
| 25 | Bản đồ ẩn danh | Thao tác bản đồ ẩn danh | Thao tác bản đồ ẩn danh |
| 26 | Watermark & chống chụp màn hình | Ghi dấu user, thời gian trên bản đồ, Phát hiện export trái phép | Ghi dấu user, thời gian trên bản đồ, Phát hiện export trái phép |
| 27 | Bảng điều khiển | Tổng hợp: số vụ việc, lực lượng đang hoạt động, điểm nóng… | Tổng hợp: số vụ việc, lực lượng đang hoạt động, điểm nóng… |
| 28 | Playbook xử lý sự cố trên bản đồ | Mẫu kịch bản: Cháy lớn, Tai nạn liên hoàn. Map tự động bật: lực lượng gần nhất | Mẫu kịch bản: Cháy lớn, Tai nạn liên hoàn. Map tự động bật: lực lượng gần nhất |
| 29 | Người dùng có thể nhúng link vào web | Cho phép nhúng link embed | Cho phép nhúng link embed |
| 30 | Hiển thị bản đồ các điểm cháy | Cho phép bật lớp dữ liệu đám cháy | Cho phép bật lớp dữ liệu đám cháy |
| 31 | Hiển thị các vị trí cứu nạn cứu hộ | Cho phép thêm địa điểm khi offline và đồng bộ khi online | Cho phép thêm địa điểm khi offline và đồng bộ khi online |
| 32 | Tính năng đăng nhập, đăng xuất | Cho phép đăng nhập bằng tài khoản | Cho phép đăng nhập bằng tài khoản |
| 33 | Cho phép thao tác model 3D | Cho phép xem thông tin, đo chiều cao, chỉ đường trên nền 3D | Cho phép xem thông tin, đo chiều cao, chỉ đường trên nền 3D |
| 34 | DATA & LAYER MANAGEMENT | QUẢN LÝ DỮ LIỆU & LỚP | QUẢN LÝ DỮ LIỆU & LỚP |
| 35 | Cấu hình hiển thị đối tượng 3D theo thời gian | Người dùng có thể chọn mốc thời gian | Người dùng có thể chọn mốc thời gian |
| 36 | Báo cáo lỗi | Người dùng có thể gửi báo cáo lỗi đến hệ thống | Người dùng có thể gửi báo cáo lỗi đến hệ thống |
| 37 | Layer time slider / temporal playback | em dữ liệu theo thời gian (ví dụ: tracks xe, trafic theo thời gian). | em dữ liệu theo thời gian (ví dụ: tracks xe, trafic theo thời gian). |
| 38 | Feature info & pop-ups | hiển thị thông tin chi tiết, liên kết tới hồ sơ (case ID). | hiển thị thông tin chi tiết, liên kết tới hồ sơ (case ID). |
| 39 | Tìm kiếm theo bán kính, theo thuộc tính | tìm kiếm, lọc theo thuộc tính, spatial query (within, intersect), saved queries. | tìm kiếm, lọc theo thuộc tính, spatial query (within, intersect), saved queries. |
| 40 | Heatmaps | Mật độ kẹt xe, an ninh giao thông | Mật độ kẹt xe, an ninh giao thông |
| 41 | Hiển thị tuyến đường cấm | Đường cấm khi có dự kiện, đường cấm xe xăng dầu | Đường cấm khi có dự kiện, đường cấm xe xăng dầu |
| 42 | Hiển thị vùng cấm bay của drone | Hiển thị vùng cấm bay | Hiển thị vùng cấm bay |
| 43 | Hiển thị các tuyến đường ngập | Hiển thị tuyến đường ngập do mưa hoặc triểu cường, bảo lũ | Hiển thị tuyến đường ngập do mưa hoặc triểu cường, bảo lũ |
| 44 | Thêm mới địa điểm | Người dùng có thể thêm mới một địa điểm trên map | Người dùng có thể thêm mới một địa điểm trên map |
| 45 | Thêm đối tượng 3D | Người dùng có thể thêm mới một đối tượng 3D | Người dùng có thể thêm mới một đối tượng 3D |
| 46 | Chỉnh sửa tuyến đường | Người dùng có thể chính sửa tuyến đường trực tiếp trên map | Người dùng có thể chính sửa tuyến đường trực tiếp trên map |
| 47 | Xem dữ liệu theo mốc thời gian | Cho phép xem dữ liệu theo chiều thời gian | Cho phép xem dữ liệu theo chiều thời gian |
| 48 | Hiển thị đèn giao thông toàn quốc |  |  |
| 49 | Hiển thị tuyến đường ngập |  |  |
| 50 | SEARCH & SPATIAL QUERY | (TÌM KIẾM & PHÂN TÍCH KHÔNG GIAN) | (TÌM KIẾM & PHÂN TÍCH KHÔNG GIAN) |
| 51 | Cấu hình địa điểm của tôi | Người dùng có thể thiết lập địa điểm là nhà riêng | Người dùng có thể thiết lập địa điểm là nhà riêng |
| 52 | Tìm kiếm theo địa chỉ | Cho phép tìm kiếm theo địa chỉ | Cho phép tìm kiếm theo địa chỉ |
| 53 | Tìm kiếm theo tọa độ | vn2000/WGS 84 | vn2000/WGS 84 |
| 54 | Tìm kiếm theo đơn vị hành chính | Theo đơn vị hành chính | Theo đơn vị hành chính |
| 55 | Search around |  |  |
| 56 | Tìm kiếm trên bản đồ | Người dùng có thể tìm kiếm thông tin bất kỳ trên bản đồ: địa điểm, địa chỉ, khu vực, số nhà, thửa đấ | Người dùng có thể tìm kiếm thông tin bất kỳ trên bản đồ: địa điểm, địa chỉ, khu vực, số nhà, thửa đấ |
| 57 | Chức năng cho phép người dùng gửi thông tin về sự cố giao thông lớn | Cho phép đưa thông tin về sự cố giao thông trên bản đồ | Cho phép đưa thông tin về sự cố giao thông trên bản đồ |
| 58 | Chức năng cho phép người dùng chia sẽ thông tin sự cố giao thông | cho phép chia sẽ thông tin giao thông tại nơi xảy ra sự cố | cho phép chia sẽ thông tin giao thông tại nơi xảy ra sự cố |
| 59 | Tìm kiếm nâng cao QR Code scanner | QR Code scanner | QR Code scanner |
| 60 | Tìm kiếm nâng cao Photo location | Photo location | Photo location |
| 61 | Tìm kiếm nâng cao Voice search | Voice search | Voice search |
| 62 | Tìm kiếm nâng cao Autocomplete | Autocomplete | Autocomplete |
| 63 | Search history | Search history | Search history |
| 64 | Spatial query theo điều kiện | Cho phép tìm kiếm danh sách con đường có camera | Cho phép tìm kiếm danh sách con đường có camera |
| 65 | NAVIGATION & ROUTING | DẪN ĐƯỜNG – LỘ TRÌNH | DẪN ĐƯỜNG – LỘ TRÌNH |
| 66 | Chỉ đường | Người dùng có thể chỉ đường từ một điểm xuất phát đến một điểm đến trên bản đồ: dành cho xe cứu thươ | Người dùng có thể chỉ đường từ một điểm xuất phát đến một điểm đến trên bản đồ: dành cho xe cứu thươ |
| 67 | Chức năng AI chỉ đường né kẹt xe | tự động tối ưu lộ trình giờ cao điểm | tự động tối ưu lộ trình giờ cao điểm |
| 68 | Hiển thị tuyến đường dành riêng cho bộ công an | xe cứu thương, xe chữ cháy, xe tuần tra | xe cứu thương, xe chữ cháy, xe tuần tra |
| 69 | AI chỉ đường dựa trên kẹt xe và đèn giao thông | tính toàn lưu lượng xe và đèn giao thông để chỉ đường với thời gian ngắn nhất | tính toàn lưu lượng xe và đèn giao thông để chỉ đường với thời gian ngắn nhất |
| 70 | Dẫn đường trong nhà (indoor map) | cho phép chỉ đường nội khu, trong tòa nhà | cho phép chỉ đường nội khu, trong tòa nhà |
| 71 | Bản đồ offline mã hoá | Cho phép chỉ đường khi offline, phục vụ cứu nạn tỏng rừng sâu | Cho phép chỉ đường khi offline, phục vụ cứu nạn tỏng rừng sâu |
| 72 | Dẫn đường nghiệp vụ Xe cứu thương, Xe chữa cháy |  |  |
| 73 | AI Routing | Né kẹt xe theo thời gian thực | Né kẹt xe theo thời gian thực |
| 77 | REAL-TIME MONITORING | GIÁM SÁT THỜI GIAN THỰC | GIÁM SÁT THỜI GIAN THỰC |
| 78 | Real-time feeds | ingest feed từ GPS/AVL, CCTV meta, cảm biến IoT, alert stream. | ingest feed từ GPS/AVL, CCTV meta, cảm biến IoT, alert stream. |
| 79 | Automatic Vehicle Location (AVL) | hiển thị vị trí xe, trạng thái (on-duty, off-duty), breadcrumb trails. | hiển thị vị trí xe, trạng thái (on-duty, off-duty), breadcrumb trails. |
| 80 | Thêm api/ link nhúng camera hiển thị | Hiển thị hình ảnh camera giao thông trực tuyến | Hiển thị hình ảnh camera giao thông trực tuyến |
| 81 | Hiển thị Bản đồ camera giao thông | Hiển thị trực tiếp camera giao thông | Hiển thị trực tiếp camera giao thông |
| 82 | Gắn camera vào bản đồ 2D / 3D | Gắn link camera vào gtel maps | Gắn link camera vào gtel maps |
| 83 | Hiển thị hệ thống đèn giao thông toàn quốc | Thông tin đèn giao thông toàn quốc | Thông tin đèn giao thông toàn quốc |
| 84 | IoT sensors | Mưa, bão, lũ | Mưa, bão, lũ |
| 85 | COMMAND & DISPATCH | CHỈ HUY – ĐIỀU PHỐI | CHỈ HUY – ĐIỀU PHỐI |
| 86 | Integrated CAD/113/114/115 systems | phối hợp gọi cứu hộ, dispatch trực tiếp từ bản đồ. | phối hợp gọi cứu hộ, dispatch trực tiếp từ bản đồ. |
| 87 | Giao nhiệm vụ trực tiếp trên bản đồ | Hiển thị các địa điểm cần cứu hộ cứu nạn và địa điểm cần cấp cứu | Hiển thị các địa điểm cần cứu hộ cứu nạn và địa điểm cần cấp cứu |
| 88 | Geofencing & Alerts: | tạo vùng cảnh báo kẹt xe, push alert khi có vi phạm/entry/exit. | tạo vùng cảnh báo kẹt xe, push alert khi có vi phạm/entry/exit. |
| 89 | AI gợi ý phân bổ lực lượng CSGT | Hiển thị khu vực cần CSGT giám sát và điều tiết giao thông | Hiển thị khu vực cần CSGT giám sát và điều tiết giao thông |
| 90 | Ước tính ETA tiếp cận |  |  |
| 91 | Dispatch trực tiếp từ bản đồ |  |  |
| 92 | Cảnh báo sự cố lớn | Hiển thị cảnh báo sự cố lớn | Hiển thị cảnh báo sự cố lớn |
| 93 | AI & ADVANCED ANALYTICS |  |  |
| 94 | AI dự báo kẹt xe theo thời gian | Dự báo kẹt xe theo tuần tháng năm, ngày , giờ. | Dự báo kẹt xe theo tuần tháng năm, ngày , giờ. |
| 95 | AI phân tích tuyển đường theo camera trên bản đồ | Theo dõi lộ trình xe theo camera, Phân tích mối liên hệ không gian | Theo dõi lộ trình xe theo camera, Phân tích mối liên hệ không gian |
| 96 | Hiển thị thành phố 3D | Hiển thị đối tương 3D trên bản đồ | Hiển thị đối tương 3D trên bản đồ |
| 97 | AR hiển thị thông tin lên camera | Hiển thị thông tin camera AR | Hiển thị thông tin camera AR |
| 98 | Mô phỏng tình huống an ninh/ Mô phỏng tình huống cháy | Hiển thị trực quan hình ảnh cháy, an ninh trên bản đồ | Hiển thị trực quan hình ảnh cháy, an ninh trên bản đồ |
| 99 | Digital twins / 3D city models | mô phỏng kịch bản cho giám sát và chỉ huy | mô phỏng kịch bản cho giám sát và chỉ huy |
| 100 | Theo dõi lực lượng thời gian thực (GPS) | Theo dõi GPS theo thời gian thực | Theo dõi GPS theo thời gian thực |

*... và 196 features khác*

---

---

## Use Cases - tmp4


**5 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Data loading & access APIs | Tiling Service | Tiling Service |
| 2 | Tiling & rendering APIs | Vector Tiles API | Vector Tiles API |
| 3 | Map design | Styles API | Styles API |
| 4 | Navigation APIs | Directions API | Directions API |
| 5 | Search APIs | Geocoding API | Geocoding API |

---

---

## Use Cases - tmp5


**19 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Nhóm tính năng lớp dữ liệu bản đồ - Layer Maps |  |  |
| 2 | Nhóm công cụ tương tác bản đồ - Map Tools |  |  |
| 3 | Nhóm tính năng tiện ích - Convenient Tools |  |  |
| 4 | Nhóm tính năng tìm kiếm - Search |  |  |
| 5 | Nhóm tính năng điều hướng - Direction |  |  |
| 6 | Nhóm tính năng phân tích không gian |  |  |
| 7 | Nhóm tính năng tạo vùng tiếp cận - Isochrone |  |  |
| 8 | Nhóm tính năng tạo vùng phát hiện - Geofence |  |  |
| 9 | DASHBOARD - ĐIỀU KHIỂN |  |  |
| 10 | Nhóm tính năng thống kê người dùng |  |  |
| 11 | Nhóm tính năng thống kê dữ liệu bản đồ |  |  |
| 12 | Nhóm tính năng thống kê lớp dữ liệu bản đồ |  |  |
| 13 | LANDING PAGE - TRANG ĐÍCH |  |  |
| 14 | NOTIFICATION - THÔNG BÁO |  |  |
| 15 | AUTHENTICATION - XÁC THỰC |  |  |
| 16 | USER MANAGEMENT - QUẢN LÝ NGƯỜI DÙNG |  |  |
| 17 | PERMISSION GROUP MANAGEMENT - QUẢN LÝ NHÓM QUYỀN |  |  |
| 18 | SETTING - THIẾT LẬP |  |  |
| 19 | APPEARANCE - TƯƠNG THÍCH |  |  |

---

---

## Use Cases - tmp6


**11 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Bản đồ nền | Thêm bản đồ nền mới bằng URL. | Thêm bản đồ nền mới bằng URL. |
| 2 | Tương tác bản đồ | Phóng to/thu nhỏ bản đồ. | Phóng to/thu nhỏ bản đồ. |
| 3 | Tiện ích | Chia sẻ vị trí hiện tại hoặc vị trí được chọn cho người khác. | Chia sẻ vị trí hiện tại hoặc vị trí được chọn cho người khác. |
| 4 | Tìm kiếm | Chuyển đổi địa chỉ dạng văn bản (địa chỉ, tên địa điểm) thành thông tin vị trí. | Chuyển đổi địa chỉ dạng văn bản (địa chỉ, tên địa điểm) thành thông tin vị trí. |
| 5 | Điều hướng | Tìm tuyến đường tránh: đường thu phí, phà, cao tốc, khu cấm, chiều cao/trọng tải xe.... | Tìm tuyến đường tránh: đường thu phí, phà, cao tốc, khu cấm, chiều cao/trọng tải xe.... |
| 6 | Các trang giới thiệu | Giới thiệu tổng quan về nền tảng bản đồ. | Giới thiệu tổng quan về nền tảng bản đồ. |
| 7 | Xác thực người dùng | Đăng nhập bằng tài khoản thông thường (username/email & mật khẩu). | Đăng nhập bằng tài khoản thông thường (username/email & mật khẩu). |
| 8 | Quản lý người dùng | Thay đổi mật khẩu đăng nhập. | Thay đổi mật khẩu đăng nhập. |
| 9 | Quản lý quyền | Quản lý danh sách nhóm quyền. | Quản lý danh sách nhóm quyền. |
| 10 | Thiết lập | Thay đổi logo hiển thị cho nền tảng. | Thay đổi logo hiển thị cho nền tảng. |
| 11 | Cấu hình giao diện | Hỗ trợ giao diện và trải nghiệm người dùng trên thiết bị di động. | Hỗ trợ giao diện và trải nghiệm người dùng trên thiết bị di động. |

---

---

## Use Cases - tmp7


**26 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | Maps Viewer |  |  |
| 16 | Maps Accounts | Đăng nhập thường | Đăng nhập thường |
| 18 | Maps MyAccount | Cập nhật thông tin cá nhân (avatar, tên người dùng, số điện thoại, địa chỉ,... ) | Cập nhật thông tin cá nhân (avatar, tên người dùng, số điện thoại, địa chỉ,... ) |
| 22 | Điều hướng & Camera | Chuyển chế độ 2D / 3D | Chuyển chế độ 2D / 3D |
| 23 | Tìm kiếm, tra cứu, identify | Thanh tìm kiếm tổng (Global Search) | Thanh tìm kiếm tổng (Global Search) |
| 24 | Đo vẽ & chú thích |  |  |
| 25 | Chỉ đường & Di chuyển |  |  |

---

---

## User Profile


**1 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

## Users


**7 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

## 📝 Ghi chú


- File này bổ sung chi tiết implementation cho các features đã có trong 01-39
- Tập trung vào acceptance criteria và technical requirements
- Không duplicate với features tổng quan trong các file khác

---

