# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (hàm `chi_so_e1`, `bang_b`). Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200); phạm vi noi_dia + hang_nang 3,97% |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý được nhân viên mở bằng trợ lý | Số `request_id` có `agent_suggestion_shown` chia số `refund_request_created` có arm = tro_ly | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | Số đơn trong `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Không kết luận trợ lý đã nâng chỉ số từ mức 0,70 vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, depot, arm, trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | quyet_dinh (giu/sua/bo), phut_xem_lai đo thật, trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai đo thật, ly_do, trace_id | Khi làm lại xong |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu, ngoai_pham_vi, het_so_lan_chay), tom_tat, trace_id | Khi chuyển nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| `ticket_closed` | Hệ thống ticket | closed_at, created_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu 100 đơn |

**Kiểm tra chéo:**

- Chỉ số chính: `refund_request_created` (mẫu số) + `ticket_closed` (closed_at − created_at ≤ 24 giờ) + `ticket_reopened` (không có trong 7 ngày).
- Bỏ qua gợi ý: `staff_review_decision` (sua + bo chia tổng số quyết định).
- Lỗi lọt đến khách: `ticket_reopened` chia `refund_request_created`.
- % yêu cầu mở bằng trợ lý: `agent_suggestion_shown` chia `refund_request_created` có arm = tro_ly.
- % đơn hoàn sai tiền: `audit_sample_checked`.
- Chi phí mỗi việc thành công (luật dừng chi phí): `agent_run_completed` (token, tool) + `staff_review_decision` và `staff_rework_completed` (phút đo thật, thay cho cột simulated) chia số việc thành công từ `ticket_closed`, `ticket_reopened`.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`, B1, B4, A4).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần trên 7% (đợt chạy thử 4,89% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu [simulated] | Hơn 50% yêu cầu còn được xem lại ở cuối bước rollout 0,25; phút xem lại đo thật trên 5 phút | Giảm xem lại theo bậc khi tỉ lệ sua + bo dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
