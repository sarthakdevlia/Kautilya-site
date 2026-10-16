# Kautilya School — 3D website demo

A 3D scroll tour of Kautilya Sr. Sec. School, Kota: step through the school photo, walk the lobby gallery, come out onto the cricket ground. Static: no build step, no server, no database.

- `index.html` — the whole site (Three.js scene, Lenis scroll, styles).
- `photos/` — the school's photographs, taken from kautilyaschool.com. The 3D slots are listed in `PHOTOS` in `index.html`.
- `photos/photos.js` — the same photos packed as text, loaded only when the page is opened straight from disk. Rebuild it with `python pack-photos.py` after changing a photo.

Share it as a **link**. An HTML file sent on WhatsApp does not run the 3D on iPhone.

## Hosting (Render static site)

New → Static Site → this repo → Build Command empty → Publish Directory `.`

Site by SD Ventures.
