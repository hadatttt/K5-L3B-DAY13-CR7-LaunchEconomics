"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p                      # phân phối hình học: E = 1/p
    return (1 - (1 - p) ** k) / p         # = tổng (1-p)^(i-1), i = 1..k


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # = E[số lần chạy] / P(thành công) = 1/p, không phụ thuộc k (k triệt tiêu)
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    # Tử số: MỌI lần chạy, kể cả lần lỗi (lần lỗi vẫn tốn token và tool)
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ A3, A4 · Theo loại yêu cầu và chi phí cố định ----------
PHAM_VI = ['noi_dia', 'hang_nang']
CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
YEU_CAU_THANG = 45_000


def bang_a3(runs, reqs):
    so_lan = runs.groupby('request_id').size()
    print('\n== A3 · Theo loại yêu cầu (cps: simulated) ==')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"x12000":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        lan = so_lan.reindex(r['request_id']).fillna(0).mean()
        print(f'{loai:10s} {len(r):6d} {kq["thanh_cong"] / len(r):9.1%} {lan:7.2f} '
              f'{kq["cps"]:9,.0f} {kq["cps"] / BASELINE:6.2f}x')
    # Tỉ lệ ok theo từng lần thử: chạy lại có giúp không?
    ok = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ok['ok'] = (ok['status'] == 'ok').astype(float)
    print('\nTỉ lệ ok theo lần thử (attempt):')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3))


def bang_a4(runs, reqs):
    r = reqs[reqs['loai'].isin(PHAM_VI)]
    kq = mo_hinh(runs, r)
    print(f'\n== A4 · Chi phí cố định, phạm vi {"+".join(PHAM_VI)} (simulated) ==')
    print(f'cps phạm vi chưa cố định: {kq["tong"]:,.0f} / {kq["thanh_cong"]} = {kq["cps"]:,.0f} đ')
    for ten, he_so in [('45.000 yc/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YEU_CAU_THANG * he_so * kq['thanh_cong'] / len(reqs)
        co_dinh = CHI_PHI_CO_DINH / tc_thang
        tong = kq['cps'] + co_dinh
        print(f'{ten:20s} việc TC/tháng {tc_thang:9,.0f}  cố định/việc {co_dinh:6,.0f}  '
              f'cps+cố định {tong:6,.0f}  = {tong / BASELINE:.2f}x')


# ---------- Nhiệm vụ B · Độ nhạy ----------
KICH_BAN = {
    'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
    'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
    'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
    'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
    'Lương tăng 25%':           dict(luong_phut=2500),
    'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
    'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
}
PHUT_XEM_LAI_B4 = 5    # phút mỗi lần xem lại (đề bài B4)
PHUT_LAM_LAI_B4 = 9    # phút mỗi ca làm lại (đề bài B4)


def bang_b(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']
    print('\n== B1 · Đổi từng yếu tố (simulated) ==')
    print(f'{"Gốc (A2)":25s} {goc:8,.0f}')
    for ten, kw in KICH_BAN.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\n== B2 · Token x2 + xem lại x2: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%)')

    print('\n== B3 · Giới hạn số lần chạy, chi phí cả hệ thống (simulated) ==')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + BASELINE * khong_tc
        print(f'{k} lần: trợ lý {kq["tong"]:11,.0f}  không TC {khong_tc:4d}  '
              f'cả hệ thống {he_thong:11,.0f}  cps {kq["cps"]:7,.0f}')

    r = reqs[reqs['loai'].isin(PHAM_VI)]
    rr = runs[runs['request_id'].isin(r['request_id'])]
    co_ok = rr.loc[rr['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((r['ket_qua'] == 'lam_lai').sum())
    may = (rr['tokens_in'] / 1000 * GIA_VAO + rr['tokens_out'] / 1000 * GIA_RA
           + rr['tool_calls'] * GIA_TOOL).sum()
    tc = int((r['ket_qua'] == 'thanh_cong').sum())
    phut_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'\n== B4 · Xem lại 100%, phạm vi {"+".join(PHAM_VI)} ({len(r)} yc, simulated) ==')
    print(f'yc có ≥1 lần ok: {co_ok}; ca làm lại: {so_lam_lai}; token+tool: {may:,.0f}; thành công: {tc}')
    for nhan, phut_ll in [(f'làm lại {PHUT_LAM_LAI_B4} phút (đề)', PHUT_LAM_LAI_B4),
                          (f'làm lại {phut_tb:.1f} phút (TB dữ liệu)', phut_tb)]:
        tong = co_ok * PHUT_XEM_LAI_B4 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT + may
        hoa_von = (BASELINE * tc - may - so_lam_lai * phut_ll * LUONG_PHUT) / (co_ok * LUONG_PHUT)
        print(f'{nhan:30s} tổng {tong:12,.0f}  cps {tong / tc:7,.0f} = {tong / tc / BASELINE:.2f}x  '
              f'hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')


# ---------- Nhiệm vụ E1 · Tính thử ba chỉ số ----------
def chi_so_e1(reqs):
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan = reqs['mo_lai_trong_7_ngay'] == 1
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    print('\n== E1 · Ba chỉ số trên 1.200 yêu cầu ==')
    print(f'Chính   : {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)})')
    print(f'Dùng    : {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)}) bỏ qua gợi ý')
    print(f'An toàn : {an_toan.mean():.2%} ({an_toan.sum()}/{len(reqs)}) mở lại 7 ngày; '
          f'phạm vi {"+".join(PHAM_VI)}: {pv["mo_lai_trong_7_ngay"].mean():.2%}')
    print(f'Tỉ lệ làm lại trong phạm vi: {(pv["ket_qua"] == "lam_lai").mean():.2%}; '
          f'tỉ lệ được xem lại: {reqs["duoc_xem_lai"].mean():.2%}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\n== A2 · Mô hình chi phí (xem_lai, lam_lai, tong, cps: simulated) ==')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:14s} {gia_tri:>14,.1f}')
    print(f'cps / hoá đơn mỗi yc = {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f} lần')
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua["tong"]:6.1%}')
    he_thong = ket_qua['tong'] + BASELINE * (len(reqs) - ket_qua['thanh_cong'])
    print(f'Chi phí cả hệ thống / yêu cầu = {he_thong / len(reqs):,.0f} đ '
          f'= {he_thong / len(reqs) / BASELINE:.2f}x')
    bang_a3(runs, reqs)   # CP1 · A3
    bang_a4(runs, reqs)   # CP1 · A4
    bang_b(runs, reqs)    # CP2 · B1–B4
    chi_so_e1(reqs)       # CP5 · E1
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
