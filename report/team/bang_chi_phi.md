# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (ĐẠT) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (ĐẠT) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (ĐẠT) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.805 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? 4.472 ÷ 274,7 = 16,3 lần [simulated]; phần lớn là giờ của nhân viên, không phải token.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Làm lại 51,8%, kế đến xem lại 40,7%; token chỉ 5,6%, tool 1,9% [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 [simulated] | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? quoc_te: 22.515 đ = 1,88× nhân viên tự làm [simulated]. Chạy lại không giúp: tỉ lệ ok lần 1/2/3 là 30,0% / 11,4% / 2,2%, mỗi lần chạy lại càng ít khả năng đúng, chỉ tốn thêm token và tool. doi_tac (0,85×) cũng sát ngưỡng, nên để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Chi phí mỗi việc thành công trong phạm vi khi chưa cộng cố định: 3.072.513 ÷ 900 = 3.414 đ [simulated]. Chi phí cố định 40 triệu đ/tháng; tỉ lệ thành công trong phạm vi 900/1.200 = 75% của tổng khối lượng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 | 5.784 [simulated] | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi ở cả hai mức: 4.599 đ (0,38×) và 5.784 đ (0,48×) [simulated]. Hoà vốn khi việc thành công mỗi tháng còn khoảng 40.000.000 ÷ (12.000 − 3.414) ≈ 4.659, tức khoảng 14% khối lượng đầy đủ.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated].

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 [simulated] | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 [simulated] | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 [simulated] | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 [simulated] | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 [simulated] | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 [simulated] | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 [simulated] | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 [simulated] | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 [simulated] | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" giảm đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ, +46,3% [simulated] = 5,6% + 40,7%, vì mô hình cộng tuyến tính nên tác động của cặp bằng tổng hai tác động riêng.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1% khi tăng 25%) [simulated]. Giá token chỉ +5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm lại từ đầu).

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 [simulated] | 319 | 7.449.781 [simulated] | 4.111 [simulated] |
| 2 lần | 4.093.220 [simulated] | 234 | 6.901.220 [simulated] | 4.237 [simulated] |
| 3 lần | 4.373.585 [simulated] | 222 | 7.037.585 [simulated] | 4.472 [simulated] |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Rẻ nhất cho công ty là 2 lần (6.901.220 đ) [simulated]. Không trùng: chi phí mỗi việc thành công thấp nhất ở 1 lần (4.111 đ), nhưng khi đó 319 yêu cầu phải chuyển nhân viên, cả hệ thống tốn thêm 548.561 đ so với 2 lần.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: 11.743 đ = 0,98× (làm lại 9 phút theo đề); 12.415 đ = 1,03× nếu làm lại 15,3 phút như trung bình dữ liệu [simulated]. Gần như mất hết khoản tiết kiệm.
- Kết quả này nói gì về thứ pilot cần học được? Pilot phải đo phút xem lại thật và chứng minh được có thể giảm xem lại theo bậc: chỉ hoà vốn khi xem lại trung bình ≤ 4,8–5,1 phút mỗi yêu cầu [simulated].
