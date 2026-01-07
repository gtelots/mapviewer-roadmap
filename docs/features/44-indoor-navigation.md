# Indoor Navigation & Mapping

> Advanced features and implementation details for indoor navigation & mapping.

## 📋 Overview

**Total Features**: ~29

**Categories**: 2

---

## Core - Indoor - Core


**30 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F361 Floor Selector |  | What: UI chọn tầng/level. | Why: Indoor bắt buộc. | Criteria: Select level → indoor layers filter đúng. |
| 2 | F362 Indoor Level Auto-Detect |  | What: Tự chọn tầng theo selection/camera. | Why: Trải nghiệm tốt. | Criteria: Select room at L3 → selector jumps to L3. |
| 3 | F363 Indoor POI List |  | What: Danh sách POI theo tầng. | Why: Tìm nhanh trong nhà. | Criteria: Filter by level; click POI → focus. |
| 4 | F364 Indoor Room Highlight |  | What: Chọn phòng → highlight polygon/mesh. | Why: Định vị. | Criteria: Select room → highlight; clear works. |
| 5 | F365 Indoor Routing A->B |  | What: Tuyến trong nhà giữa 2 POI/rooms. | Why: Use-case chính. | Criteria: Route shown per level; steps include level changes |
| 6 | F366 Vertical Transitions Support |  | What: Thang máy/cầu thang connectors. | Why: Tuyến đúng. | Criteria: Route includes connectors; shows instructions. |
| 7 | F367 Indoor Accessibility Routing |  | What: Tuyến tránh cầu thang (elevator only). | Why: Phục vụ xe lăn. | Criteria: Mode on avoids stairs; if none -> message. |
| 8 | F368 Indoor Wayfinding Arrows |  | What: Mũi tên dẫn đường trong nhà. | Why: Dễ theo. | Criteria: Arrows align with corridor; visible on chosen leve |
| 9 | F369 Indoor Map Styling |  | What: Preset style (walls, rooms, labels). | Why: Đọc dễ. | Criteria: Style switch works; legend updates. |
| 10 | F370 Indoor Labeling Rules |  | What: Label theo room name/category. | Why: Điều hướng. | Criteria: No overlap basic; priority rule works. |
| 11 | F371 Indoor Search Scoped |  | What: Tìm kiếm giới hạn theo building/level. | Why: Kết quả chuẩn. | Criteria: Scoped search returns only within building when en |
| 12 | F372 Indoor Occupancy Layer (View) |  | What: Hiển thị mức độ đông (if data). | Why: Quản lý vận hành. | Criteria: Heat/indicator shows; refresh interval works. |
| 13 | F373 Indoor Access Control Zones |  | What: Hiển thị vùng restricted. | Why: An ninh. | Criteria: Restricted zone visible; tooltip; role-based visib |
| 14 | F374 Indoor Emergency Exits Layer |  | What: Layer lối thoát hiểm (if data). | Why: An toàn. | Criteria: Exits visible; click shows details; filter by leve |
| 15 | F375 Indoor Navigation Voice Prompts (Basic) |  | What: Voice prompt cho bước dẫn đường (optional). | Why: Hands-free. | Criteria: Toggle voice; speaks steps; respects language. |
| 16 | F376 Indoor Route Re-route |  | What: Đổi tuyến khi đổi điểm/level. | Why: Trải nghiệm. | Criteria: Change destination → reroute <1s; keeps UI stable. |
| 17 | F377 Indoor POI Categories Filter |  | What: Lọc POI theo category (WC, ATM…). | Why: Dễ tìm. | Criteria: Filter works; counts update; remembers selection. |
| 18 | F378 Indoor Building Selector |  | What: Chọn toà nhà trong campus. | Why: Campus rộng. | Criteria: Select building → layers & floor list update. |
| 19 | F379 Indoor-to-Outdoor Transition |  | What: Chuyển route indoor ra outdoor (hybrid). | Why: End-to-end navigation. | Criteria: Route shows indoor segment + outdoor segment; seam |
| 20 | F380 Indoor Blue Dot Positioning (Basic) |  | What: Hiển thị “blue dot” theo GPS/WiFi (if provided). | Why: Dẫn đường trong nhà. | Criteria: Receives position events; dot updates; smoothing a |
| 21 | F381 Indoor Calibration UI (Basic) |  | What: UI hiệu chỉnh vị trí (choose reference point). | Why: Giảm sai số positioning. | Criteria: User sets anchor → position offset applied; can re |
| 22 | F382 Indoor POI Details Panel |  | What: Chi tiết POI (giờ mở cửa, ảnh). | Why: Tăng giá trị. | Criteria: Panel shows fields; missing safe; links open. |
| 23 | F383 Indoor Crowd-safe Route (Optional) |  | What: Tránh khu đông (if occupancy). | Why: An toàn. | Criteria: Mode on uses occupancy costs; falls back if no dat |
| 24 | F384 Indoor Route Print View |  | What: In route → view in printable layout. | Why: Bảng chỉ dẫn. | Criteria: Print view hides UI; shows steps & map. |
| 25 | F385 Indoor Level Transition Animation |  | What: Animation chuyển tầng mượt. | Why: Trải nghiệm. | Criteria: Transition <500ms; no flicker; user can disable. |
| 26 | F386 Indoor Layer Isolation |  | What: Chỉ hiển thị 1 level hoặc multi-level transparency | Why: Trực quan. | Criteria: Isolation on → only selected level; multi-level sh |
| 27 | F387 Indoor Door/Entrance Graph |  | What: Hỗ trợ điểm vào phòng/door nodes. | Why: Route đúng. | Criteria: Route uses doors; if missing uses centroid with wa |
| 28 | F388 Indoor Network Debug Overlay |  | What: Overlay graph nodes/edges (debug). | Why: Debug routing. | Criteria: Toggle overlay; shows counts; export graph stats. |
| 29 | F389 Indoor Navigation Events |  | What: Emit events: levelChanged, routeStep. | Why: Tích hợp app host. | Criteria: Events fire correctly; payload documented. |
| 30 | F390 Indoor Route Accessibility Annotations |  | What: Show icons for stairs/elevator segments. | Why: Rõ ràng. | Criteria: Steps show icons; color coding consistent. |

---

---

## Indoor Mapping


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

