# Advanced Security & Governance

> Advanced features and implementation details for advanced security & governance.

## 📋 Overview

**Total Features**: ~14

**Categories**: 1

---

## Advanced - Security & Governance


**15 features**

| # | Feature Name | Description | Details |
|---|--------------|-------------|----------|
| 1 | F456 CORS/Referrer Restrictions |  | What: Hỗ trợ giới hạn domain referrer cho key. | Why: Chống lộ key. | Criteria: Wrong domain → denied; correct domain → ok. |
| 2 | F457 Token Scope Enforcement |  | What: UI chỉ gọi API đúng scope. | Why: Least privilege. | Criteria: No scope → request blocked client-side + server-si |
| 3 | F458 Sensitive Field Masking |  | What: Mask field nhạy cảm trong properties. | Why: Privacy. | Criteria: Masked by default; role-based reveal. |
| 4 | F459 PII Redaction in Logs |  | What: Xoá PII khỏi log/telemetry. | Why: Compliance. | Criteria: Logs contain no email/phone; validated by tests. |
| 5 | F460 Download/Export Policy Controls |  | What: Chính sách bật/tắt export theo tenant. | Why: Ngăn rò rỉ dữ liệu. | Criteria: Policy off → export buttons hidden + API blocked. |
| 6 | F461 Watermark with User ID |  | What: Watermark có user/session id (optional). | Why: Răn đe leak. | Criteria: Export includes watermark; cannot disable if enfor |
| 7 | F462 View-Only Hardening |  | What: Chặn devtools hooks (best-effort) + disable edit e | Why: Bảo vệ basic. | Criteria: View-only mode prevents write calls; audit shows a |
| 8 | F463 Content Security Policy Compatibility |  | What: Không dùng inline script; nonce ready. | Why: Hardening. | Criteria: App runs under strict CSP; documented headers. |
| 9 | F464 Secure File Attachment Handling |  | What: Sanitize/scan attachments (stub). | Why: An toàn. | Criteria: Blocked types rejected; size limits; logs recorded |
| 10 | F465 Session MFA Prompt Integration |  | What: Flow yêu cầu MFA cho action nhạy cảm. | Why: Bảo mật. | Criteria: Export restricted → MFA required; success continue |
| 11 | F466 Audit Event Signing (Optional) |  | What: Ký event client-side (optional). | Why: Chống giả mạo log. | Criteria: Event has signature; server verifies or ignores. |
| 12 | F467 Data Residency Mode |  | What: Chọn region endpoint theo policy. | Why: Compliance. | Criteria: Region locked; cannot call other regions; tested. |
| 13 | F468 Security Diagnostics Report |  | What: Báo cáo cấu hình security hiện tại. | Why: Kiểm tra nhanh. | Criteria: Report includes CSP/CORS/masking status; exportabl |
| 14 | F469 RBAC-Aware UI Testing Hooks |  | What: Hooks test xác nhận UI theo role. | Why: Đảm bảo phân quyền. | Criteria: Test role matrix passes; no forbidden button visib |
| 15 | F470 Tamper-Evident Share Links |  | What: Link share có chữ ký + expiry. | Why: Chống sửa param. | Criteria: Modified params → invalid; expiry enforced. |

---

---

