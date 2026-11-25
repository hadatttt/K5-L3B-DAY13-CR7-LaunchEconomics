# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): CR7 (L3B)
- Nhóm được chấm: NhomT2

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | "Go có điều kiện" khớp số của nhóm: phạm vi noi_dia + hang_nang 0,38× (0,48× nếu khối lượng còn một nửa). Nêu đủ ba con số bất lợi kèm cách xử lý: power 0,64 nếu tác động thật 5 điểm → Giám đốc vận hành ký chấp nhận trước 2026-12-04; xem lại 100% thì 0,98–1,03× → giảm xem lại theo bậc khi sua + bo < 15% và ≤ 4,8 phút/lần; ca 20, 5, 13 → vá trước ngày bắt đầu. Mỗi điều kiện có một vai trò phụ trách và ngày kiểm tra |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mục 1, 2, 3, 7 ghi trạng thái Giả lập và nhãn simulated ở từng số (4.472 đ, 6.787 đ, 0,49×, 11.743–12.415 đ); `pilot_plan.yaml` liệt kê 6 đầu vào giả lập trong `simulated_inputs`, kể cả ngưỡng 8.000 đ. Phạm vi thu hẹp có lý do bằng số: loại quoc_te (1,88×, thành công 27,3%) và doi_tac (0,85×, điều khoản riêng) |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20, bốc thăm có seed, phân tầng theo 12 depot, đối chứng chạy cùng tuần; đủ 20 cụm mỗi nhóm. Đủ mẫu cho MDE 6 điểm (n = 859, DE = 6,96, m ≥ 299) và ghi rõ đánh đổi so với 5 điểm (tối đa 1.000 < 1.251). Ba luật dừng đủ bốn vế, có ngưỡng (+2 điểm / trần 6%, 8.000 đ, 40%), thời hạn (3 ngày, 2 tuần, 1 tuần) và người dừng (Giám đốc vận hành, Trưởng sản phẩm, Trưởng nhóm CSKH); ngưỡng an toàn đặt theo tỉ lệ hiện tại 3,97%; rollback 30 phút |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ khớp bằng chứng và không giấu con số bất lợi: power 0,64, xem lại 100% lên 1,03× (simulated), quoc_te 1,88× (simulated). Pilot tách được tác động (20 + 20 nhân viên, ngẫu nhiên, đối chứng cùng lúc), luật dừng đo được. Góp ý nhỏ: điều kiện 1 yêu cầu giới hạn tối đa 2 lần chạy, nhưng `pilot_plan.yaml` chỉ đưa giới hạn này vào luật dừng thứ hai (khi chi phí vượt 8.000 đ), chưa đặt từ đầu. Nên thống nhất hai file trước ngày 2026-12-04.

**Một câu hỏi cho đội trình:** Hội đồng hỏi 5 câu:

1. doi_tac có 0,85×, vẫn rẻ hơn nhân viên tự làm. Sao lại loại?
2. Con số 0,38× là chi phí của cả công ty, hay chỉ tính phần việc trợ lý làm xong?
3. Pilot chỉ có 20 nhân viên, khối lượng nhỏ. Chi phí cố định 40 triệu mỗi tháng có làm mất tiết kiệm không?
4. Nếu giá token tăng gấp đôi thì sao?
5. Nhân viên dùng trợ lý và nhân viên đối chứng ngồi cùng depot. Nếu nhóm đối chứng chép câu trả lời của trợ lý thì kết quả có còn đúng không?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đội trình trả lời đúng cả 5 câu. Hội đồng đối chiếu với các ý cần có sau:

1. 0,85× sát ngưỡng; thành công 54,4%, chạy lại không giúp (ok lần 1 là 51,5%, lần 2 là 18,2%); làm lại gấp đôi thì +51,8%, vượt 1× (simulated).
2. 0,38× chỉ tính việc trợ lý làm xong; cộng 222 ca chuyển nhân viên thì cả hệ thống là 5.865 đ/yêu cầu = 0,49× (simulated).
3. Khối lượng còn một nửa thì 5.784 đ = 0,48×, vẫn tiết kiệm; hoà vốn ở khoảng 14% khối lượng đầy đủ (simulated).
4. Chỉ +5,6% (4.723 đ), vì token chiếm 5,6% chi phí; giờ nhân viên chiếm 92,5% (simulated).
5. Có rủi ro ảnh hưởng gián tiếp; giảm bằng quyền truy cập theo tài khoản và log theo staff_id; chia theo depot chỉ có 6 cụm, tối đa 300 < 859.
