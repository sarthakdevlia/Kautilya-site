"""Pack the photos into photos/photos.js so index.html also works when opened
straight from disk (WebGL cannot read image files over file://).

Run after adding or replacing a photo:  python pack-photos.py
Keys must match PHOTOS in index.html (plus 'logo').
"""
import base64, json, pathlib

HERE = pathlib.Path(__file__).parent / 'photos'
FILES = {
    'hero': 'slider1.jpg', 'logo': 'logo.jpg',
    'independence': 'independence-day.jpg', 'republic': 'republic-day.jpg', 'janmashtami': 'janmashtami.jpg', 'annual': 'annual-day.jpg',
    'krishna': 'krishna.jpg', 'picnic': 'picnic.jpg', 'heritage': 'heritage-day.jpg', 'space': 'space-exhibition.jpg', 'fruits': 'fruits-day.jpg',
    'house': 'house.jpg', 'fair': 'childrens-fair.jpg', 'tournament': 'cricket-tournament.jpg',
}
MIME = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp'}

packed = {}
for key, name in FILES.items():
    f = HERE / name
    if not f.exists():
        print('missing', name); continue
    packed[key] = f'data:{MIME[f.suffix.lower()]};base64,' + base64.b64encode(f.read_bytes()).decode()
(HERE / 'photos.js').write_text('window.K_IMG = ' + json.dumps(packed) + ';\n', encoding='utf-8')
print(f'packed {len(packed)} photos into photos/photos.js')
