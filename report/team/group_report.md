# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: CR7
- Lớp: L3B
- Thành viên: xem `TEAM.md` (2 người: Phan Đào Minh Quân, Hà Văn Khánh Đạt; mỗi người kiêm 2 vai)

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu hỏi cho Gate 2a của trợ lý hoàn phí LogiX-VN: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định. Mọi con số tính bằng `src/lab13.py` trên 1.200 yêu cầu / 1.624 lần chạy (dữ liệu giả lập), đối chiếu với hướng dẫn chi tiết (lệch dưới 2%). Nhiệm vụ sau dùng lại số của nhiệm vụ trước: A3 chọn phạm vi, B cho rủi ro kinh tế, D lấy tỉ lệ mở lại hiện tại để đặt luật an toàn.

## 3. Giải pháp

- **A · Chi phí mỗi việc thành công** ([bang_chi_phi.md](bang_chi_phi.md)): tử số cộng token, tool của mọi lần chạy kể cả lần lỗi, cộng phút xem lại và làm lại × 2.000 đ; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Tách theo `loai` (A3) và cộng chi phí cố định 40 triệu đ/tháng (A4).
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): 9 kịch bản đổi từng yếu tố, một cặp, giới hạn 1/2/3 lần chạy tính cả chi phí hệ thống, xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo 5 loại PAIR, so nhãn, viết lại định nghĩa, chọn 5 ca mỗi loại một ca để gán cách phát hiện đo được và vai trò phụ trách.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính đủ 5 câu D1 trước, chọn chia theo nhân viên 20 + 20, chấp nhận MDE 6 điểm; 3 luật dừng an toàn, chi phí, mức sử dụng theo mẫu NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): 3 chỉ số tính thử + 2 chỉ số tự đề xuất, 10 event có `trace_id`, 3 dòng rủi ro kinh tế, hồ sơ một trang bảy mục.

## 4. Kết quả

- Chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8%, xem lại 40,7% tổng chi phí [simulated].
- Theo loại: noi_dia 0,22×, hang_nang 0,69×, doi_tac 0,85×, quoc_te 1,88× so với 12.000 đ [simulated]. Phạm vi noi_dia + hang_nang cộng cố định: 4.599 đ = 0,38× [simulated].
- Ba yếu tố nhạy nhất: làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ) [simulated]. Xem lại 100% đẩy chi phí lên 0,98–1,03× [simulated].
- Chỉ số chính trong đợt chạy thử là 82,83%; bỏ qua gợi ý 27,12%; mở lại 7 ngày 4,25% (phạm vi 3,97%).
- Pilot: 20 + 20 nhân viên, 859 yêu cầu/nhóm, DE 6,96, m ≥ 299; power chỉ 0,64 nếu tác động thật là 5 điểm.
- **Đề xuất cuối:** Go có điều kiện cho phạm vi noi_dia + hang_nang (4 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra).
- Kết quả duyệt chéo nhận được từ hội đồng: (điền sau buổi duyệt chéo)

## 5. Khó khăn và cách xử lý

- Nhóm chỉ có 2 người thay vì 4: mỗi người kiêm 2 vai, đổi người viết code sau giờ giải lao (Quân code A, B; Đạt code D1) để cả hai tự tính được chi phí.
- Hai người cùng sửa `bang_loi.md` trên hai máy: Quân push cột nhãn 1 trước, Đạt có cột nhãn 2 chưa commit. Xử lý bằng cách cất tạm bản của Đạt, pull về rồi ghép hai cột, không mất cột nào.
- Với 40 nhân viên, không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm (tối đa 1.000 < 1.251): nhóm ghi rõ đánh đổi MDE 6 điểm và power 0,64 trong `pilot_plan.yaml` và hồ sơ.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Toàn bộ chi phí xem lại và làm lại dựa trên cột `_simulated`; cần thay bằng phút đo thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng, nên chưa kết luận được trợ lý nâng chỉ số chính từ 0,70.
- MDE 6 điểm làm pilot dễ bỏ sót tác động thật 5 điểm (power 0,64); nếu có thêm nhân viên hoặc kéo dài pilot thì nên quay về MDE 5 điểm.
- Các ca lỗi "Ngầm" (ví dụ ca 12) chỉ lộ ra khi theo dõi chủ động; cần dashboard chi phí theo depot trước ngày bắt đầu.

## 8. Tài liệu tham khảo

- `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` (đề bài lab).
- Google PAIR, People + AI Guidebook, chương Errors + Graceful Failure (5 loại lỗi).
- statsmodels: `proportion_effectsize`, `NormalIndPower` (power khi n = 859).
