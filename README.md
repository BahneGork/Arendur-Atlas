# Arendur Atlas

An interactive atlas of the **Arendur Rising** campaign, as the Shadow Company knows it: Ursia, East Blackwood and the town of Delios. Pins open panels about each place, written from the players' own chronicle.

Built from the same code as the Erukana atlas ([Atlassian](https://github.com/BahneGork/Atlassian)); the experience behind it is in the Claude skill `campaign-atlas`.

## Run locally
```bash
python3 -m http.server 8000   # open http://localhost:8000
```

## Update the atlas
- `tools/curation.py`: campaign settings (`CAMPAIGN`), maps, places, sessions. Player knowledge only – the site is public.
- `tools/build.py`: fetches the published player notes from GitHub (`BahneGork/GMnostes`, only the folders in `CAMPAIGN["notes_dirs"]`) and writes `data/atlas.json` and `data/notes.json`.

```bash
python3 tools/build.py
```

### Adding a map
1. Save the image as WebP in `maps/` (max ~4096 px wide; keep positions in the original image's pixels).
2. Add it to `MAPS` with its original `size`, and `place` = the place whose panel should open it.
3. Add a signpost back in `PORTALS`, at an empty map edge.
4. Place pins on it (`map=`, `at=`), or drag them there in the site's edit mode.

### Moving and placing pins
On the site: **Signaturer → Redigér placeringer**, drag pins, then **Gem for alle** (commits a file to `moves/`; the "Rebuild atlas" workflow applies it).

## Layout
- `index.html`, `css/`, `js/`: the site (no build step)
- `data/`: generated
- `maps/`: map images (WebP)
- `vendor/`: Leaflet 1.9.4 (BSD-2-Clause), marked 12.0.2 (MIT)
- `docs/assessment.md`: what the notes support, and open questions
