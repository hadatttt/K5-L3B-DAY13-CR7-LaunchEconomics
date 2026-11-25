# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: CR7 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ cả bộ, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 4.599 đ [simulated] (`bang_chi_phi.md` A2, A4) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi +51,8% · xem lại gấp đôi +40,7% · lương +25% → +23,1%; giá token gấp đôi chỉ +5,6% [simulated] (B1, B2) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Phạm vi: 0,38× của 12.000 đ (0,48× nếu khối lượng còn một nửa); quoc_te 1,88× nên loại; xem lại 100% thì 0,98–1,03× [simulated] (A3, A4, B4) | Giả lập | Trưởng nhóm CSKH |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số chính trong đợt chạy thử là 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại 7 ngày 4,25%, trong phạm vi 3,97%; 10 event có `trace_id` (`chi_so.md`) | Xong, có bằng chứng | Trưởng nhóm phân tích dữ liệu |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, đồng thuận 16/20 = 80%, đã viết lại định nghĩa; bảng khắc phục 5 ca đủ 5 loại, mỗi dòng có event và ngưỡng (`bang_loi.md`) | Xong, có bằng chứng | Trưởng nhóm kỹ thuật trợ lý |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, ngẫu nhiên phân tầng theo depot; MDE 6 điểm, 859 yêu cầu/nhóm, DE 6,96, m ≥ 299; power 0,64 nếu tác động thật chỉ 5 điểm; 3 luật dừng; quyết định 2027-01-05 (`pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ; xem lại 100% → 11.743 đ (0,98×); khối lượng còn một nửa → +2.370 đ/việc cố định [simulated] (`chi_so.md` E2) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện, cho pilot chỉ trong phạm vi noi_dia + hang_nang (quoc_te và doi_tac giữ cho nhân viên tự làm).

- Sửa lỗi báo hoàn thành công khi sổ cái lỗi (ca 7) và có khoá chống hoàn trùng (ca 20; `idempotency_key` ở `refund_ledger_write`) chạy được trước ngày bắt đầu · Trưởng nhóm kỹ thuật trợ lý · kiểm tra 2026-12-04.
- Giám đốc vận hành ký chấp nhận MDE 6 điểm thay vì 5 điểm (power chỉ 0,64 nếu tác động thật là 5 điểm) · Giám đốc vận hành · kiểm tra 2026-12-04.
- Bật đủ 10 event có `trace_id`; sau tuần 1 thay phút xem lại / làm lại simulated bằng phút đo thật và tính lại chi phí mỗi việc thành công · Trưởng nhóm phân tích dữ liệu · kiểm tra 2026-12-14.
- Có kế hoạch giảm xem lại theo bậc, vì xem lại 100% thì không còn tiết kiệm (0,98×; hoà vốn khi xem lại ≤ 4,8–5,1 phút) [simulated] · Trưởng nhóm CSKH · kiểm tra 2026-12-21.
