# Team

## Thông tin nhóm

- Tên nhóm: CR7
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-CR7-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/hadatttt/K5-L3B-DAY13-CR7-LaunchEconomics · `main` ·

## Thành viên

Nhóm 2 người, mỗi người kiêm 2 vai.

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phan Đào Minh Quân | 2A202603971 | emiyashirou191@gmail.com | Shirou191 | Người viết code (trước giải lao) · Người gắn nhãn 1 · Người kiểm số (sau giải lao) |
|   2 | Hà Văn Khánh Đạt | 2A202604074 | hagamer2004@gmail.com | hadatttt | Người kiểm số (trước giải lao) · Người gắn nhãn 2, kiêm giữ hồ sơ · Người viết code (sau giải lao) |

### Bảng chia việc theo checkpoint

| Checkpoint | Phan Đào Minh Quân | Hà Văn Khánh Đạt |
| --- | --- | --- |
| CP1 · A (14:10–14:53) | Viết A1 (3 hàm), `mo_hinh` (A2), A3 theo `loai`, A4 | Tính tay 1–2 con số để đối chiếu; điền `bang_chi_phi.md` (A2, A3, A4, nhãn `simulated`); mở `ho_so_launch_v0.md` |
| CP2 · B (14:53–15:20) | Viết code B1 (9 kịch bản), B2, B3, B4 | Kiểm "giảm nửa = nửa mức tăng gấp đôi"; điền bảng B1, xếp hạng 3 yếu tố, trả lời B3, B4 |
| CP3 · C (15:35–16:08) | Gắn nhãn 1: 20 ca độc lập (8 phút) | Gắn nhãn 2: 20 ca độc lập (8 phút) |
| | Cùng so nhãn, tính đồng thuận, viết quy tắc ca lệch; Quân điền bảng khắc phục 5 ca | Đạt ghi hai bộ nhãn + tỉ lệ đồng thuận vào `bang_loi.md` |
| CP4 · D (16:08–16:36) | Kiểm số D1 bằng công thức tay; trả lời D2; viết luật dừng | Viết code D1 (cỡ mẫu, hệ số thiết kế), tính tỉ lệ `mo_lai_trong_7_ngay`; điền `pilot_plan.yaml` |
| CP5 · E (16:36–17:00) | `chi_so.md`: 3 chỉ số, ≥6 event, ≥2 rủi ro kinh tế | Hoàn thiện `ho_so_launch_v0.md` (7 mục, dòng cuối là đề xuất) |
| Duyệt chéo (17:00–17:45) | Bảo vệ hồ sơ trước hội đồng | Chấm nhóm khác vào `phieu_cham.md` |
| Đóng gói (17:45–18:00) | Báo cáo cá nhân của mình | `group_report.md`, báo cáo cá nhân, commit, push |

Cả hai người đều nộp link repo trên LMS.

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## PhanDaoMinhQuan-2A202603971

### Phần việc phụ trách

- CP1, CP2: viết code A1–A4 và B1–B4 trong `src/lab13.py`.
- CP3: người gắn nhãn 1 (20 ca, độc lập).
- CP4: kiểm tay D1, trả lời năm câu D2, viết ba luật dừng trong `pilot_plan.yaml`.
- CP5: `chi_so.md`; bảo vệ hồ sơ trước hội đồng; chuẩn bị 5 câu hỏi hội đồng hỏi NhomT2.

### Đóng góp cụ thể

- `lab13.py`: ba hàm A1, `mo_hinh`, `bang_a3`, `bang_a4`, `bang_b`, `chi_so_e1`; chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu.
- D1 kiểm tay khớp code của Đạt: 1.251 · 3.103 · 1.000 · 300 · m ≥ 299; power 0,64.
- `chi_so.md`: 3 chỉ số (82,83% · 27,12% · 4,25%), 10 event có `trace_id`, 3 dòng rủi ro kinh tế.

### Bằng chứng

- `python lab13.py` in ba phép thử ĐẠT và các bảng A2, A3, A4, B1–B4, E1.
- Báo cáo cá nhân: `report/team/2A202603971_PhanDaoMinhQuan.md`.

## HaVanKhanhDat-2A202604074

### Phần việc phụ trách

- CP1, CP2: kiểm số, điền `bang_chi_phi.md`.
- CP3: người gắn nhãn 2 (20 ca, độc lập); ghi hai bộ nhãn và đồng thuận vào `bang_loi.md`.
- CP4: viết code D1 trong `lab13.py`; điền `pilot_plan.yaml`.
- CP5: giữ hồ sơ `ho_so_launch_v0.md`; `phieu_cham.md`; `group_report.md`; commit, push.

### Đóng góp cụ thể

- `lab13.py`: `co_mau`, `he_so_thiet_ke`, `cau_d1`.
- `bang_chi_phi.md` đủ A1–A4, B1–B4; `pilot_plan.yaml` chia theo nhân viên 20 + 20, MDE 0,06, n = 859, DE 6,96.
- `ho_so_launch_v0.md`: bảy mục, đề xuất Go có điều kiện cho phạm vi noi_dia + hang_nang.

### Bằng chứng

- Báo cáo cá nhân: `report/team/2A202604074_HaVanKhanhDat.md`.
