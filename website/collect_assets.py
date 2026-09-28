# レーベル棚の素材収集（2026-09-28）
# 各リリースの採用版ジャケット（配信の現物と照合済み）を website/public/img へ集める。
import shutil, hashlib
from pathlib import Path
from PIL import Image

M = Path(r"C:\Users\Admin\OneDrive\Desktop\Master")
WP = Path(r"C:\Users\Admin\OneDrive\Desktop\wordpress\opt\bitnami\wordpress\wp-content\uploads\2024\01")
IMG = Path(r"C:\Users\Admin\vicugna\website\public\img")
IMG.mkdir(parents=True, exist_ok=True)

COVERS = [
    ("cover_highway_mv_edit.png", M / "(not yet)/Highway_MV_Edit_ジャケット_20260928/Highway_MV_Edit_ジャケット.png"),
    ("cover_wakeru.png",          M / "wakeru/ジャケット候補_2026-09-16/wakeru_I_七日_3000.png"),
    ("cover_sora.png",            M / "Sora/ジャケット_20260925_AB/Sora_A_title_3000.png"),
    ("cover_both.png",            M / "both/both_cover_3000.png"),
    ("cover_omega.png",           M / "ω/omega_cover_sakura_face14_3000.png"),
    ("cover_collatz.png",         M / "Collatz/collatz_cover_3000_1.png"),
    ("cover_life.png",            M / "配信用LIFE/LIFE_3000.png"),
    ("cover_notyet.png",          M / "配信用(not yet)/cover.png"),
]

for name, src in COVERS:
    assert src.exists(), f"なし: {src}"
    shutil.copy2(src, IMG / name)
    im = Image.open(IMG / name)
    print(f"{name:28s} {im.size[0]}x{im.size[1]} {im.mode} {(IMG/name).stat().st_size//1024}KB")

# ロゴ・ファビコン（旧サイトの原画像から）
logos = sorted(WP.glob("brandmark-design.png")) + sorted(WP.glob("*favicon*"))
for p in WP.iterdir():
    pass
print("--- wordpress logo files ---")
for p in sorted(WP.glob("*.png")) + sorted(WP.glob("*.jpg")):
    if "brandmark" in p.name or "favicon" in p.name:
        im = Image.open(p)
        print(f"{p.name:45s} {im.size[0]}x{im.size[1]}")

# QCモンタージュ
tiles = [Image.open(IMG / n).convert("RGB").resize((300, 300)) for n, _ in COVERS]
sheet = Image.new("RGB", (300 * 4, 300 * 2), "#faf7f2")
for i, t in enumerate(tiles):
    sheet.paste(t, ((i % 4) * 300, (i // 4) * 300))
sheet.save(IMG.parent / "qc_covers.png")
print("QC:", IMG.parent / "qc_covers.png")
