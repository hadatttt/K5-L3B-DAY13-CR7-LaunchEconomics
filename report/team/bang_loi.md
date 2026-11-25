# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phan Đào Minh Quân · Người gắn nhãn 2: Hà Văn Khánh Đạt (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Do người dùng | Hệ thống | Không | Do người dùng |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Hệ thống | Hệ thống | Có | Hệ thống |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Do người dùng | Không | Ngầm |
| 9 | Ngữ cảnh | Giới hạn hệ thống | Không | Ngữ cảnh |
| 10 | Ngữ cảnh | Hệ thống | Không | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Do người dùng | Có | Ngầm |
| 13 | Hệ thống | Hệ thống | Có | Hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Hệ thống | Hệ thống | Có | Hệ thống |
| 18 | Ngữ cảnh | Ngữ Cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 16 / 20 = 80%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

Đồng thuận 80%. Phần lớn ca lệch là người 2 gắn "Hệ thống" cho mọi ca trợ lý có liên quan, trong khi người 1 tách theo nguyên nhân gốc. Định nghĩa đã viết lại:

- **Do người dùng:** nguyên nhân gốc là thao tác hoặc dữ liệu khách nhập sai; trợ lý làm đúng với đầu vào nhận được.
- **Hệ thống:** trợ lý hoặc tool làm sai so với chính sách hay thiết kế, và lỗi lộ ra ngay (khách mở lại, nhân viên bắt được, API báo lỗi).
- **Ngữ cảnh:** trợ lý làm đúng thiết kế hoặc chính sách, nhưng kết quả không khớp kỳ vọng hay hoàn cảnh của khách (giờ gửi, kênh nhận tiền, cách giải thích, lời hứa của ứng dụng).
- **Giới hạn hệ thống:** yêu cầu nằm ngoài khả năng hoặc dữ liệu mà trợ lý có (âm thanh, dữ liệu quá 12 tháng, chặng của hãng khác).
- **Ngầm:** lỗi không ai phát hiện cho tới khi kiểm tra chủ động (đối soát, theo dõi chi phí); không khách nào báo, không cảnh báo nào kích.

Quy tắc cho từng ca không trùng:

- Ca 2: theo nhãn người 1 (Do người dùng). Cần nhóm xác nhận lại trước khi nộp: mô tả cho thấy trợ lý gọi tool với tham số hàng thường thay vì hàng nặng.
- Ca 3: Ngữ cảnh, vì trợ lý hoàn đúng thiết kế (về ví LogiX), lỗi là khách kỳ vọng tiền về tài khoản ngân hàng.
- Ca 8: Ngầm, vì số tiền vẫn đúng, không ai báo; chỉ lộ ra khi đối chiếu căn cứ với chính sách hiện hành.
- Ca 9: Ngữ cảnh, vì khách hiểu "mã đơn" theo thói quen của sàn thương mại điện tử, còn trợ lý không gợi ý cách tìm mã vận đơn.
- Ca 10: Ngữ cảnh, vì trợ lý từ chối đúng chính sách, nhưng ứng dụng vẫn hứa "cam kết giao 24 giờ" nên khách thấy vô lý.
- Ca 12: Ngầm, vì kết quả cuối vẫn đúng, chi phí token của D05 gấp 3 lần suốt 3 tuần mà không ai thấy.
- Ca 16: Ngữ cảnh, vì trợ lý gửi đúng thiết kế "gửi ngay khi xong", nhưng giờ gửi 2:14 sáng không hợp hoàn cảnh của khách.
- Ca 18: Ngữ cảnh, vì số tiền tính đúng, lỗi nằm ở tin nhắn thiếu cách tính nên khách hiểu sai.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | `refund_ledger_write` có `ket_qua` lỗi ngân hàng "sai số tài khoản"; cảnh báo khi trên 1% lệnh mỗi ngày | Kiểm tra độ dài và định dạng số tài khoản trước khi tạo lệnh; sai thì hỏi lại khách, không tạo lệnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát hằng ngày: số tin "đã hoàn tiền thành công" so với số `refund_ledger_write` có `ket_qua` = ok theo `trace_id`; ngưỡng 0 ca lệch | Chỉ báo thành công khi sổ cái xác nhận; lỗi 503 sau 3 lần thử thì `handoff_to_staff` và báo khách "đang xử lý" | Trưởng nhóm kỹ thuật trợ lý |
| 18 | Ngữ cảnh | `ticket_reopened` có reason "hoàn thiếu" trong khi số tiền khớp chính sách; cảnh báo khi trên 1% yêu cầu mỗi tuần | Tin nhắn hoàn tiền luôn kèm cách tính: phí gốc, tỉ lệ hoàn, điều khoản áp dụng | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | Đếm yêu cầu có tin nhắn thoại mỗi tuần và tỉ lệ khách bỏ đi sau câu "vui lòng nhập bằng chữ"; ngưỡng 20% | Nhận tin thoại thì `handoff_to_staff` ngay kèm tóm tắt, nói rõ trợ lý chưa xử lý được âm thanh | PM trợ lý hoàn phí |
| 12 | Ngầm | Chi phí token + tool theo depot từ `agent_run_completed`; kiểm tra hằng ngày, cảnh báo khi một depot vượt 1,5 lần trung vị các depot | Sửa tool tra đơn D05 trả đủ trường; thêm kiểm tra schema đầu ra của tool, thiếu trường thì báo lỗi thay vì gọi lại | Trưởng nhóm kỹ thuật trợ lý |
