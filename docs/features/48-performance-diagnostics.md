# Performance & Diagnostics

> Advanced features and implementation details for performance & diagnostics.

## 📋 Overview

**Total Features**: ~28

**Categories**: 2

---

## Advanced - Observability & Diagnostics


**10 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F446 Client Log Levels |  | What: Level debug/info/warn/error. | Why: Kiểm soát log. | Criteria: Level applies; debug off by default in prod. |
| 2 | F447 Trace Correlation IDs |  | What: Gắn correlation id vào request. | Why: Triaging backend. | Criteria: Every request has id; displayed on error modal. |
| 3 | F448 Metrics Export Endpoint |  | What: Export metrics JSON từ viewer. | Why: Thu thập tại chỗ. | Criteria: Endpoint returns metrics; gated by debug flag. |
| 4 | F449 Real-time Console Panel |  | What: Console nội bộ hiển thị logs/events. | Why: Debug现场. | Criteria: Toggle panel; filter by type; copy lines. |
| 5 | F450 Tile/Render Profiler Mode |  | What: Mode profile tiles/render. | Why: Perf tuning. | Criteria: Start/stop profiler; summary table appears. |
| 6 | F451 User Journey Replay Tokens |  | What: Token hóa sự kiện để replay (privacy-safe). | Why: Debug bug khó. | Criteria: Replay reproduces UI path; no raw PII stored. |
| 7 | F452 Health Status Widget |  | What: Widget trạng thái dịch vụ (tiles/routing/search). | Why: Minh bạch. | Criteria: Shows green/yellow/red; updates every N sec. |
| 8 | F453 Outage Banner Remote Config |  | What: Banner sự cố bật/tắt từ remote config. | Why: Thông báo nhanh. | Criteria: Remote on → banner shows; off → hides. |
| 9 | F454 Anomaly Detection Alerts |  | What: Client phát hiện spike lỗi và cảnh báo (optional). | Why: Chủ động. | Criteria: Error rate > threshold → alert; includes context. |
| 10 | F455 Support Session Code |  | What: Mã phiên để hỗ trợ (share to support). | Why: Triaging nhanh. | Criteria: Code encodes config hash; expires; no secrets. |

---

---

## Advanced - Performance & Reliability


**20 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F426 Adaptive Quality Scaling |  | What: Tự giảm quality khi FPS thấp. | Why: Ổn định. | Criteria: FPS<target → reduce AA/shadow; restore when stable |
| 2 | F427 GPU Tier Detection |  | What: Tự chọn preset theo GPU tier. | Why: Tối ưu UX. | Criteria: Tier detected; preset applied; user can override. |
| 3 | F428 Texture Streaming Budget |  | What: Giới hạn texture residency. | Why: Tránh VRAM overflow. | Criteria: Budget enforced; mip fallback; warning shown. |
| 4 | F429 Worker Pool Manager |  | What: Quản lý worker decode/compute. | Why: Ổn định hiệu năng. | Criteria: Max workers configurable; no leak on destroy. |
| 5 | F430 Main Thread Jank Monitor |  | What: Phát hiện jank > X ms. | Why: Tối ưu UX. | Criteria: Jank events logged; includes stack sampling (optio |
| 6 | F431 Graceful Degradation Steps |  | What: Thứ tự tắt hiệu ứng khi quá tải. | Why: Không crash. | Criteria: Degrade ladder documented; triggers correctly. |
| 7 | F432 Low Memory Mode |  | What: Mode giảm cache/LOD cho thiết bị RAM thấp. | Why: Mobile. | Criteria: Enable → memory usage giảm; still usable. |
| 8 | F433 Thermal Throttling Detector |  | What: Detect nhiệt/power saving (best-effort). | Why: Bền vững mobile. | Criteria: Detect → suggest low preset; user can ignore. |
| 9 | F434 Network Adaptive Streaming |  | What: Chọn concurrency/LOD theo băng thông. | Why: Mượt mạng yếu. | Criteria: Slow net → fewer requests; still progressive. |
| 10 | F435 CDN Failover |  | What: Failover qua CDN thứ 2 khi lỗi. | Why: Độ sẵn sàng. | Criteria: Primary down → switch; user sees small banner. |
| 11 | F436 Service Worker Cache (Advanced) |  | What: Cache assets/metadata offline. | Why: Tốc độ + resilience. | Criteria: SW installs; cache versioned; can purge. |
| 12 | F437 Deterministic Rendering Mode |  | What: Mode render deterministic cho QA/regression. | Why: Test ổn định. | Criteria: Same input → same snapshot; debug flag. |
| 13 | F438 Memory Leak Detector Hook |  | What: Hook cảnh báo leak (dev). | Why: Giảm bug. | Criteria: Route open/close N lần → no steady memory growth. |
| 14 | F439 Frame Capture Export |  | What: Export frame capture for offline analysis. | Why: Debug. | Criteria: Capture produces file; can replay. |
| 15 | F440 Multi-Thread Picking Optimization |  | What: Picking chạy worker + spatial index. | Why: Picking nhanh trên dense data. | Criteria: Click response < target; accuracy maintained. |
| 16 | F441 Tile Warm Cache Seed |  | What: Seed cache theo AOI trước khi demo. | Why: Kiosk nhanh. | Criteria: Preseed completes; open scene fast offline-ish. |
| 17 | F442 Batch API Calls |  | What: Batch metadata calls để giảm RTT. | Why: Nhanh. | Criteria: Batch reduces total requests; fallback if unsuppor |
| 18 | F443 Idle-Time Precompute |  | What: Precompute indexes khi idle. | Why: Trải nghiệm mượt. | Criteria: Idle tasks pause on interaction; no blocking. |
| 19 | F444 Error Budget Dashboard Link |  | What: Link tới dashboard error budget. | Why: SRE. | Criteria: Click opens; respects access; shows current status |
| 20 | F445 Auto Bug Report Package |  | What: Gói log + config + stats tự động. | Why: Support nhanh. | Criteria: Export excludes secrets; includes reproduction ste |

---

---

