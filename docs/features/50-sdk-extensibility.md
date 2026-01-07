# SDK & Extensibility

> Advanced features and implementation details for sdk & extensibility.

## 📋 Overview

**Total Features**: ~27

**Categories**: 3

---

## Expert - Enterprise Integrations


**8 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F486 BIM Overlay Viewer |  | What: Overlay IFC/BIM converted tiles (read-only). | Why: AECO use-case. | Criteria: BIM layer loads; pick shows BIM properties; units  |
| 2 | F487 Asset Management Linkout |  | What: Link object → CMMS/ERP URL template. | Why: Kết nối nghiệp vụ. | Criteria: Click opens correct URL; uses feature id mapping. |
| 3 | F488 Real-time IoT Telemetry Overlay |  | What: Overlay sensor data realtime (websocket). | Why: Digital twin. | Criteria: Stream updates markers; reconnect; backpressure ha |
| 4 | F489 Alert Rules Visualization |  | What: Hiển thị rule/alert trên map (geofence breach). | Why: Vận hành. | Criteria: Alert appears; ack action; audit logged. |
| 5 | F490 Incident Timeline Panel |  | What: Timeline sự cố liên quan vị trí. | Why: Điều hành. | Criteria: Filter by time; click item zooms; data source conf |
| 6 | F491 Single Pane of Glass Dashboard Embed |  | What: Embed viewer vào dashboard BI. | Why: Doanh nghiệp. | Criteria: Embeddable responsive; SSO; rate-limit safe. |
| 7 | F492 Geospatial Report Generator |  | What: Tạo report tự động theo AOI/template. | Why: Báo cáo. | Criteria: Generate completes; includes maps+tables; template |
| 8 | F493 Data Loss Prevention Hooks |  | What: Hooks DLP chặn copy/export theo policy. | Why: Bảo vệ dữ liệu. | Criteria: Blocked action shows reason; attempts logged. |

---

---

## Expert - Immersive & AI


**7 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F494 AR Mode (Basic) |  | What: Chế độ AR overlay (WebXR nếu hỗ trợ). | Why: Trình diễn/field. | Criteria: Supported devices only; fallback message; stable. |
| 2 | F495 VR Walkthrough Mode |  | What: Chế độ VR walkthrough trong scene. | Why: Trình diễn nâng cao. | Criteria: Enter/exit VR works; controls mapped; motion comfo |
| 3 | F496 AI Search Assistant (Optional) |  | What: Gợi ý query/layer dựa trên ngữ cảnh. | Why: Tăng tốc tìm kiếm. | Criteria: Suggestions appear; user opt-in; no sensitive data |
| 4 | F497 AI Auto-Labeling (View) |  | What: Gợi ý nhãn POI nổi bật theo zoom. | Why: Đọc dễ. | Criteria: Labels selected sensibly; can disable; determinist |
| 5 | F498 AI Anomaly Highlight |  | What: Highlight vùng bất thường (heat/outliers) từ dữ li | Why: Phân tích nhanh. | Criteria: Outliers marked; thresholds configurable; explanat |
| 6 | F499 Simulation Playback Overlay |  | What: Phát mô phỏng theo thời gian (vehicles/people). | Why: Digital twin. | Criteria: Timeline play; speed control; smooth interpolation |
| 7 | F500 Scenario Compare (What-if) |  | What: So sánh 2 kịch bản style/data (what-if). | Why: Quyết định. | Criteria: Switch scenario shows diff; can export comparison  |

---

---

## Expert - SDK & Extensibility


**15 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F471 Embed SDK Core |  | What: SDK nhúng viewer, init/destroy, options. | Why: Tích hợp sản phẩm. | Criteria: Sample works; lifecycle no leaks; typings. |
| 2 | F472 Event Bus API |  | What: API subscribe/unsubscribe events chuẩn hoá. | Why: Tích hợp sâu. | Criteria: Events documented; no breaking changes without ver |
| 3 | F473 Command API |  | What: Host app gọi lệnh: setLayer, setFilter, route. | Why: Điều khiển từ ngoài. | Criteria: Commands validate input; return promises; errors t |
| 4 | F474 Plugin Framework Core |  | What: Đăng ký plugin (tool/panel) runtime. | Why: Mở rộng không fork. | Criteria: Plugin loads/unloads; sandboxed scope; versioned. |
| 5 | F475 Custom Tool Builder |  | What: Khai báo tool bằng schema (icon, action, UI). | Why: Dev nhanh. | Criteria: Schema -> tool appears; permissions respected. |
| 6 | F476 UI Extension Slots |  | What: Slot để gắn UI (topbar/sidebar/popup). | Why: White-label. | Criteria: Slot render stable; responsive; can remove. |
| 7 | F477 Custom Layer Type Adapter |  | What: Adapter thêm layer type mới. | Why: Hỗ trợ data mới. | Criteria: Register adapter; layer loads; error isolation. |
| 8 | F478 Scripting Sandbox |  | What: Chạy script nhỏ (limited) để automate. | Why: Tác vụ nâng cao. | Criteria: Sandbox denies network by default; timeouts enforc |
| 9 | F479 Plugin Marketplace Stub |  | What: Danh sách plugin từ registry (optional). | Why: Ecosystem. | Criteria: Install/uninstall works; signature verified (optio |
| 10 | F480 Versioned Plugin API |  | What: API plugin có versioning + deprecation. | Why: Ổn định lâu dài. | Criteria: Old plugin runs; warnings shown; docs provided. |
| 11 | F481 Headless Snapshot Renderer |  | What: Chạy render snapshot tự động (test/kiosk). | Why: QA/regression. | Criteria: Produces deterministic images; CI-friendly. |
| 12 | F482 Custom Data Inspector Panel |  | What: Panel inspect theo schema do host cung cấp. | Why: Tùy biến nghiệp vụ. | Criteria: Schema loads; renders fields; actions callbacks wo |
| 13 | F483 External Auth Provider Hook |  | What: Hook nhận token từ host (OIDC/SAML). | Why: Enterprise SSO. | Criteria: Token injection works; refresh callback; logout sy |
| 14 | F484 Webhook Trigger from Viewer |  | What: Trigger webhook events (export completed, feedback | Why: Tích hợp quy trình. | Criteria: Webhook sent; retries; signed payload. |
| 15 | F485 Multi-Instance SDK Support |  | What: Nhiều viewer trên 1 trang. | Why: Ứng dụng phức tạp. | Criteria: Instances isolated; no global collisions; performa |

---

---

