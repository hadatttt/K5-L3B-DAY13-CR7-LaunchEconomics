# Báo cáo cá nhân — PhanDaoMinhQuan-2A202603971

## 1. Thông tin thành viên

- Họ tên: Phan Đào Minh Quân
- MSSV: 2A202603971
- Email:
- Vai trong nhóm: người viết code (trước giải lao) · người gắn nhãn 1 · người kiểm số (sau giải lao)

## 2. Phần việc phụ trách

- CP1, CP2: viết code nhiệm vụ A (A1, A2, A3, A4) và B (B1–B4) trong `src/lab13.py`.
- CP3: gắn nhãn 1 cho 20 ca lỗi (độc lập); điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- CP4: kiểm số D1 bằng công thức tay; trả lời năm câu D2; viết ba luật dừng trong `report/team/pilot_plan.yaml`.
- CP5: `report/team/chi_so.md` (3 chỉ số, 10 event, 3 dòng rủi ro kinh tế); bảo vệ hồ sơ trước hội đồng Gate 2a.

## 3. Đóng góp cụ thể

- `src/lab13.py`: ba hàm A1, `mo_hinh` (tử số tính mọi lần chạy kể cả lỗi, mẫu số chỉ đếm `thanh_cong`, có tham số cho B), `bang_a3` (kèm tỉ lệ ok theo lần thử), `bang_a4`, `bang_b`, `chi_so_e1`.
- Kết quả chính: chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8% tổng chi phí [simulated].
- A3: quoc_te 22.515 đ = 1,88× [simulated], tỉ lệ ok lần 1/2/3 là 30,0% / 11,4% / 2,2%, nên chạy lại không giúp.
- B: xếp hạng nhạy nhất là làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%) [simulated]; giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ).
- D1 kiểm tay (công thức so hai tỉ lệ, z = 1,95996 và 0,84162): a) 1.251 · b) DE 2,48 → 3.103/nhóm, 42 người/nhóm > 20 · c) tối đa 1.000 · d) tối đa 300 · e) m ≥ 299 (DE 6,96). Power khi tác động thật chỉ 5 điểm với n = 859: 0,64.
- Luật dừng an toàn dựa trên tỉ lệ mở lại hiện tại 3,97% trong phạm vi (không đặt ngưỡng 3% vì sẽ dừng ngay tuần đầu).

## 4. Bằng chứng

- `src/lab13.py`: `python lab13.py` in "Ba phép thử đáp án biết trước: ĐẠT" và các bảng A2, A3, A4, B1–B4, E1.
- `report/team/chi_so.md`, phần D2 + `identifiability` + `stop_rules` trong `report/team/pilot_plan.yaml`.
- Commit: (điền hash sau khi commit)

## 5. Công cụ AI đã dùng

- Claude Code: gợi ý code cho `lab13.py`, soạn nháp `chi_so.md`, D2 và luật dừng.
- Cách tự kiểm tra: chạy `python lab13.py` và đối chiếu từng số với bảng trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (đều khớp, lệch dưới 2%); kiểm tra "giảm nửa = nửa mức tăng gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9); tính lại D1 bằng công thức độc lập với code của Đạt; kiểm tra `pilot_plan.yaml` đọc được bằng `yaml.safe_load`.
- Không dùng AI để gắn nhãn 20 ca lỗi ở CP3.

## 6. Tự đánh giá

...
