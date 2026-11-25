# Báo cáo cá nhân — HaVanKhanhDat-2A202604074

## 1. Thông tin thành viên

- Họ tên: Hà Văn Khánh Đạt
- MSSV: 2A202604074
- Email:
- Vai trong nhóm: người kiểm số (trước giải lao) · người gắn nhãn 2, kiêm giữ hồ sơ · người viết code (sau giải lao)

## 2. Phần việc phụ trách

- CP1, CP2: kiểm số và điền `report/team/bang_chi_phi.md` (A1–A4, B1–B4, nhãn `simulated`).
- CP3: gắn nhãn 2 cho 20 ca lỗi (độc lập); ghi hai bộ nhãn và tỉ lệ đồng thuận vào `report/team/bang_loi.md`.
- CP4: viết code D1 (cỡ mẫu, hệ số thiết kế, power) trong `src/lab13.py`; điền các trường còn `?` trong `report/team/pilot_plan.yaml`.
- CP5: giữ hồ sơ `report/team/ho_so_launch_v0.md`; chấm nhóm khác vào `report/team/phieu_cham.md`; `group_report.md`, commit, push.

## 3. Đóng góp cụ thể

- `src/lab13.py`: hàm `co_mau`, `he_so_thiet_ke`, `cau_d1`. Kết quả D1: a) 1.251 · b) DE 2,48 → 3.103/nhóm, 42 người/nhóm, tổng 84 > 40 · c) tối đa 1.000 · d) tối đa 300 · e) m ≥ 299 (DE 6,96) · power 0,64 nếu tác động thật 5 điểm với n = 859.
- `pilot_plan.yaml`: owner, scope (noi_dia + hang_nang), unit `staff`, MDE 0,06, n_per_arm 859, design_effect 6,96, clusters_per_arm 20, rollback, decision_date 2027-01-05, simulated_inputs; ghi D1 và đánh đổi vào chú thích đầu file.
- `bang_chi_phi.md`: điền đủ A1, A2 (9 dòng), A3 (4 dòng), A4, B1 (9 dòng), B2, B3, B4. Chi phí mỗi việc thành công 4.472 đ [simulated]; giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ) dù giới hạn 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ).
- `bang_loi.md`: gắn nhãn 2 cho 20 ca; ghép hai bộ nhãn, điền cột Trùng? và nhãn thống nhất, định nghĩa viết lại cho 5 loại, quy tắc cho từng ca lệch, bảng khắc phục 5 ca (ca 1, 7, 18, 11, 12) có event, ngưỡng và vai trò phụ trách.
- `group_report.md`: tóm tắt cách làm A–E, kết quả chính, khó khăn, hạn chế.
- `ho_so_launch_v0.md`: bảy mục, đề xuất Go có điều kiện cho phạm vi noi_dia + hang_nang, bốn điều kiện có người phụ trách và ngày kiểm tra.

## 4. Bằng chứng

- `python lab13.py` in mục `== D1 · Cỡ mẫu ==` khớp bảng D1 trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))"` chạy không lỗi; ngoài chú thích không còn dấu `?`.
- Commit: `c12b889` (D1, pilot_plan, bảng chi phí, hồ sơ launch), `0d3d0f8` (bảng lỗi), commit báo cáo nhóm cuối buổi.

## 5. Công cụ AI đã dùng

- Claude Code: gợi ý code D1, điền nháp `bang_chi_phi.md`, `pilot_plan.yaml`, `ho_so_launch_v0.md` từ output của `lab13.py`; soạn nháp định nghĩa viết lại, quy tắc ca lệch và bảng khắc phục 5 ca trong `bang_loi.md`; soạn nháp `group_report.md`.
- Cách tự kiểm tra: mọi số trong bảng lấy từ output `lab13.py`; đối chiếu D1 với hướng dẫn chi tiết (1.251 · 3.103 · 1.000 · 300 · 299 · 0,64); kiểm tra B3 bằng tay (7.449.781 − 6.901.220 = 548.561 đ); kiểm tra hoà vốn A4: 40.000.000 ÷ (12.000 − 3.414) ≈ 4.659 việc/tháng.
- Không dùng AI để gắn nhãn 20 ca lỗi ở CP3 (bộ nhãn người 2 tự gắn) và không dùng AI để chấm nhóm khác.

## 6. Tự đánh giá

- Làm tốt: phần D1 và pilot_plan khớp đáp án, nắm được vì sao số cụm quyết định cỡ mẫu hiệu dụng (c / ICC) chứ không phải tổng số yêu cầu.
- Chưa tốt: ở CP3 gắn nhãn "Hệ thống" cho nhiều ca chỉ vì có trợ lý liên quan, chưa tách theo nguyên nhân gốc (Ngữ cảnh, Ngầm).
- Lần sau: đọc kỹ định nghĩa 5 loại PAIR trước khi gắn nhãn; tự chạy lại `lab13.py` sau mỗi lần sửa thay vì chỉ đọc output.
