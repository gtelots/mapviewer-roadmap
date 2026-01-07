# Advanced Search & Geocoding

> Advanced features and implementation details for advanced search & geocoding.

## 📋 Overview

**Total Features**: ~19

**Categories**: 3

---

## Core - Search & Geocoding


**20 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F281 Global Search Bar |  | What: Thanh search chính (địa điểm/feature). | Why: Entry point quan trọng. | Criteria: Enter query → results; empty → suggestions. |
| 2 | F282 Autocomplete Suggestions |  | What: Gợi ý khi gõ. | Why: Nhanh & ít lỗi. | Criteria: Suggestions <200ms (cached); keyboard select. |
| 3 | F283 Search Result List |  | What: List kết quả + phân loại. | Why: Dễ chọn. | Criteria: Result click → flyTo; highlight query term. |
| 4 | F284 Search History |  | What: Lưu lịch sử tìm kiếm. | Why: Tiện dùng lại. | Criteria: History shows last N; clear option. |
| 5 | F285 Search Filters |  | What: Lọc theo loại (POI, address, layer). | Why: Kết quả chính xác. | Criteria: Filter applies; count updates; persists per sessio |
| 6 | F286 Coordinate Search |  | What: Tìm theo “lat,lon” hoặc MGRS (optional). | Why: Tác nghiệp chuẩn. | Criteria: Input parse ok; invalid shows hint. |
| 7 | F287 Reverse Geocoding |  | What: Click map → lấy địa chỉ gần nhất. | Why: Tra cứu nhanh. | Criteria: Click → address within T sec; no result → message. |
| 8 | F288 Layer Feature Search |  | What: Tìm feature theo thuộc tính trong layer. | Why: Truy vấn dữ liệu nghiệp vụ. | Criteria: Query returns list; select → focus. |
| 9 | F289 Saved Places |  | What: Lưu địa điểm ưa thích. | Why: Tiện truy cập. | Criteria: Save/remove works; sync per user. |
| 10 | F290 Recent Places Chips |  | What: Hiển thị chip “recent” dưới search. | Why: Nhanh thao tác. | Criteria: Click chip → flyTo; auto updates. |
| 11 | F291 Search Result Ranking |  | What: Ưu tiên theo khoảng cách/độ liên quan. | Why: Kết quả tốt hơn. | Criteria: Ranking stable; can switch sorting. |
| 12 | F292 Search Highlight on Map |  | What: Hiển thị marker/highlight kết quả. | Why: Dễ thấy. | Criteria: Select result → marker + pulse; clears on close. |
| 13 | F293 Batch Search (List Input) |  | What: Nhập danh sách mã/ID để tìm nhiều. | Why: Use-case vận hành. | Criteria: Paste list → results grouped; missing shown. |
| 14 | F294 Fuzzy Matching |  | What: Tìm gần đúng tên. | Why: Tránh lỗi chính tả. | Criteria: Misspelling still returns; show “did you mean”. |
| 15 | F295 Vietnamese Diacritics Handling |  | What: Tìm không dấu vẫn ra có dấu. | Why: Phù hợp VN. | Criteria: “Ho Chi Minh” -> “Hồ Chí Minh”. |
| 16 | F296 Search Analytics Events |  | What: Emit event search_query/search_select. | Why: Đo hiệu quả. | Criteria: Event contains query length; no PII by default. |
| 17 | F297 Search Empty Suggestions |  | What: Gợi ý khi không có kết quả. | Why: Giảm thất bại. | Criteria: No result → show alternatives; clickable. |
| 18 | F298 Geofence Search Within Area |  | What: Tìm trong polygon/viewport. | Why: Kết quả đúng khu vực. | Criteria: Toggle “within view”; results update. |
| 19 | F299 Search by Category |  | What: Category browse (restaurants, hospitals…). | Why: Use-case phổ biến. | Criteria: Category select → results; icons show. |
| 20 | F300 Search Result Export |  | What: Export kết quả search ra CSV/GeoJSON. | Why: Báo cáo nhanh. | Criteria: Export includes fields; respects permission. |

---

---

## Identify & Query


**7 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

## Search & Discovery


**9 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|

---

---

