# UI/UX Components & Sharing

> Advanced features and implementation details for ui/ux components & sharing.

## 📋 Overview

**Total Features**: ~39

**Categories**: 3

---

## Annotations & Collaboration


**9 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 6 | Share to Tenant | Chia sẻ ghi chú trong cùng tenant/workspace. | Chia sẻ ghi chú trong cùng tenant/workspace. |
| 9 | Notification Hooks | Gửi thông báo khi có thay đổi/mention (optional). | Gửi thông báo khi có thay đổi/mention (optional). |

---

---

## Core - Sharing & Export


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F391 Share Stateful URL |  | What: Link chứa state camera/layers/selection (optional) | Why: Chia sẻ nhanh. | Criteria: Open link restores state; can redact selection. |
| 2 | F392 Share Short Link |  | What: Short link qua backend (optional). | Why: Dễ gửi. | Criteria: Short link resolves; expires policy supported. |
| 3 | F393 Screenshot Export PNG/JPG |  | What: Chụp ảnh màn hình. | Why: Báo cáo nhanh. | Criteria: Image correct; include/exclude UI option. |
| 4 | F394 Export Map Snapshot JSON |  | What: Export state JSON (camera, layers, filters). | Why: Tái hiện bug. | Criteria: Export file created; import restores. |
| 5 | F395 Print Map Layout Basic |  | What: In layout A4/A3 (simple). | Why: In báo cáo. | Criteria: Print preview; scale bar; north arrow optional. |
| 6 | F396 Export Selection Data |  | What: Export selected features attributes. | Why: Báo cáo. | Criteria: CSV/JSON export; respects permission. |
| 7 | F397 Export Visible Extent |  | What: Export bbox/extent polygon. | Why: Tích hợp GIS. | Criteria: Export returns extent; CRS indicated. |
| 8 | F398 Share Bookmark Link |  | What: Bookmark có link riêng. | Why: Truy cập nhanh. | Criteria: Bookmark link opens view; handles permission. |
| 9 | F399 Public View Mode |  | What: Read-only mode cho link công khai. | Why: Chia sẻ ngoài. | Criteria: Public mode hides sensitive panels; rate-limit app |
| 10 | F400 Watermark & Branding |  | What: Watermark logo/text trên screenshot/print. | Why: Bản quyền/brand. | Criteria: Config watermark; cannot be removed in public mode |

---

---

## Core - UI/UX & Accessibility


**30 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F251 Dockable Panels |  | What: Panel docking (left/right/bottom) + resize. | Why: Tối ưu workspace. | Criteria: Drag dock works; state persists; no overlap. |
| 2 | F252 Collapsible Toolbar |  | What: Toolbar thu gọn mở rộng. | Why: Tối ưu màn nhỏ. | Criteria: Collapse works; icons still accessible. |
| 3 | F253 Command Palette |  | What: Gõ để chạy lệnh (Open layer, Measure…). | Why: Tốc độ thao tác pro. | Criteria: Ctrl+K opens; search commands; executes. |
| 4 | F254 Toast Notifications |  | What: Thông báo ngắn cho actions. | Why: Feedback tức thời. | Criteria: Toast appears; auto-dismiss; accessible. |
| 5 | F255 Confirm Dialog for Destructive |  | What: Confirm khi xóa markup/preset. | Why: Tránh thao tác nhầm. | Criteria: Delete shows confirm; cancel safe. |
| 6 | F256 Undo/Redo Core |  | What: Undo/redo cho drawing/filters/panel actions. | Why: Tăng an toàn thao tác. | Criteria: Ctrl+Z/Y works; history limit N. |
| 7 | F257 Empty States |  | What: Empty state có hướng dẫn (no layers, no search). | Why: Giảm bối rối. | Criteria: Empty shows CTA; disappears when data exists. |
| 8 | F258 Loading Progress Bar |  | What: Thanh tiến trình tổng khi load scene. | Why: Rõ trạng thái. | Criteria: Progress updates; completes; timeout message. |
| 9 | F259 Keyboard Navigation Panels |  | What: Điều hướng panel bằng phím. | Why: A11y & power users. | Criteria: Tab order hợp lý; focus visible. |
| 10 | F260 Screen Reader Labels |  | What: Nhãn ARIA cho nút/tool. | Why: A11y. | Criteria: Screen reader đọc đúng; no unlabeled controls. |
| 11 | F261 High Contrast UI Mode |  | What: Chế độ tương phản cao cho UI. | Why: A11y. | Criteria: Toggle changes colors; meets contrast ratio. |
| 12 | F262 Font Size Scaling |  | What: Tăng/giảm cỡ chữ UI. | Why: A11y + kiosk. | Criteria: Scale applies; layout not broken. |
| 13 | F263 Reduced Motion Mode |  | What: Giảm animation khi user prefers-reduced-motion. | Why: A11y. | Criteria: Respect OS setting; animations disabled. |
| 14 | F264 Touch Target Enlargement |  | What: Tăng kích thước nút trên mobile. | Why: Tránh bấm nhầm. | Criteria: Min 44px targets; usability improves. |
| 15 | F265 Tooltip Delay Settings |  | What: Chỉnh delay tooltip. | Why: Không gây rối. | Criteria: Delay applies; persist. |
| 16 | F266 Context Menu on Map |  | What: Menu chuột phải: copy coords, add marker. | Why: Tác nghiệp nhanh. | Criteria: Right-click opens; actions work; closes on outside |
| 17 | F267 Status Bar |  | What: Thanh trạng thái: coords, zoom, EPSG, FPS (opt). | Why: Nhìn nhanh thông tin. | Criteria: Status updates; toggle per field. |
| 18 | F268 Multi-Language UI Strings |  | What: Quản trị chuỗi ngôn ngữ. | Why: Quốc tế hoá. | Criteria: No hardcoded strings; fallback language exists. |
| 19 | F269 Unit Preferences |  | What: Chọn đơn vị m/ft, km/mi. | Why: Phù hợp khách hàng. | Criteria: Unit switch updates measure outputs instantly. |
| 20 | F270 Error Message Catalog |  | What: Chuẩn hoá mã lỗi + hướng dẫn. | Why: Support nhanh. | Criteria: Error shows code + suggestion; localized. |
| 21 | F271 Session Timeout Banner |  | What: Banner khi sắp hết session. | Why: Tránh mất việc. | Criteria: Warn at T-2min; extend works; logout on expire. |
| 22 | F272 Accessibility Audit Checklist Mode |  | What: Trang checklist A11y tích hợp. | Why: Chuẩn hoá QA. | Criteria: Checklist exportable; indicates pass/fail. |
| 23 | F273 In-App Feedback Button |  | What: Gửi feedback kèm screenshot/log snapshot. | Why: Thu thập lỗi nhanh. | Criteria: Submit works; attaches version + context (no secre |
| 24 | F274 Shortcut Cheat Sheet |  | What: Popup liệt kê phím tắt. | Why: Giảm learning curve. | Criteria: Opens; searchable; closes by Esc. |
| 25 | F275 Panel Search |  | What: Search trong panel list (layers, bookmarks). | Why: Tăng tốc. | Criteria: Type search → filter; highlight matches. |
| 26 | F276 Customizable Toolbar |  | What: Chọn tool hiển thị trên toolbar. | Why: Cá nhân hoá. | Criteria: User can pin/unpin; persists. |
| 27 | F277 Workspace Presets |  | What: Preset bố cục panel cho use-case. | Why: Vào việc nhanh. | Criteria: Select preset → layout changes; can reset. |
| 28 | F278 Accessibility Focus Trap in Modals |  | What: Modal có focus trap + Esc close. | Why: A11y chuẩn. | Criteria: Tab không thoát modal; Esc đóng. |
| 29 | F279 Long-Running Task Queue UI |  | What: Hàng đợi tác vụ: export, analysis. | Why: Rõ tiến trình. | Criteria: Task shows progress; cancel supported. |
| 30 | F280 Notification Center |  | What: Lưu lịch sử thông báo trong 1 panel. | Why: Xem lại sự kiện. | Criteria: Items logged; mark read; clear all. |

---

---

