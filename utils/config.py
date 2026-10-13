# utils/config.py

"""
システム全体で利用する定数・設定・IDを管理するファイルです。
ここに集約することで、校舎が増えたりシートが変わった際のメンテナンスが一箇所で済みます。
"""

# ==========================================
# 📊 スプレッドシートIDの管理
# ==========================================
# 💡 ここにすべてのスプレッドシートIDを集約します

# メインのシステム管理用スプレッドシート（元々 g_sheets.py にあったものなどを想定）
# SPREADSHEET_ID = "ここにメインのシートIDがあれば記述"

# 🏫 校舎ごとの振替・欠席連絡用スプレッドシートID
TRANSFER_SHEET_IDS = {
    "池上校": "1V7o5FJiwRLIAOh8AuxpaX5ohdQZQdc1dNxvRiCHoMxc",
}

# ==========================================
# 📊 学習時間ダッシュボード用
# ==========================================

# ① 画像を生成するためのGAS (Google Apps Script) のURL
SELF_STUDY_GAS_URLS = {
    "池上校": {
        "小学生": "https://script.google.com/macros/s/AKfycbxTrynj_X3KcAX4n4dDA8HSRHItt3RPU349XoRgm_Ss0nolm8ZQANw0JefYOqoHPFZV/exec",
        "中学生": "https://script.google.com/macros/s/AKfycbw0c9AiBpQMIO-Cu2jSicYmghJbUVXKOFtLH9IWHo0wA9gyT_G_pv1-3elEmAEXCaaA/exec",
        "高校生": "https://script.google.com/macros/s/AKfycbx4s0gBmZfDyUXWGTMQ-JexTstSVcQ-DIAsNFB-yjrGXG2m0Q2kqzelwN4FtLN6jECC/exec"
    }
}

# ② セル(C1, D1)に直接年月を書き込むためのスプレッドシートID
SELF_STUDY_SHEET_IDS = {
    "池上校": {
        "小学生": "1fvxlDAZssHgDcwq9p-CG1pCeT8EdaYZv3_amfFpENdw",
        "中学生": "1pr2lIWGWqyB-k2YFmIhM4zcBpkfbdgAD-fG5e2j96x0",
        "高校生": "1OgZlzOOEZGxKlcyVLxWEYVDvWEmYf31X8tcQOfE83No"
    }
}

# 認証用シークレットキー
SELF_STUDY_SECRET_KEY = "juku-graph-2026"