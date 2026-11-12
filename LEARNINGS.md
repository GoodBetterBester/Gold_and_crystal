# Learnings and mistakes to avoid

## What worked
- **Treat every drawing as data.** Frames, circles, arrows, connecting lines and stray glyphs all carried information (the Cistercian numeral, the arrow shapes, the circles on the paintings).
- **Overlay, don't recall.** Superimposing the sketch circle onto the real painting settled Venus = rose in a minute after a lot of guessing from memory.
- **Use great circles for any "draw a line" step.** Google My Maps' lines are geodesic. Flat (Mercator) straight lines moved crossings by ~90 km and sent us to the wrong side of Jamaica.
- **Verify with the cipher.** The fort name is checkable: the right key turns the sentence into clean English instantly. Test candidate keys cheaply and often.
- **Brute-force small search spaces.** Tiling the polyominoes and the mate search were solved by tiny scripts; same for testing every painting/fort combination.
- **Word-count checks.** The `??` letter counts confirmed each Shakespeare step.
- **Community hints are terse.** "The problem is harrowing" = "arrow". Look for hidden words inside hints.

## Mistakes to avoid next time
- **Assuming sketch lines show compass directions.** We guessed X islands from line angles (Bimini, Dry Tortugas, Inagua). Wrong: the links only show grouping; identify places by **shape**.
- **Assuming an "island" is an island.** X3 was Lake Okeechobee and X4 was a bay (Tampa). Consider lakes, bays and parts of coastlines.
- **Trusting labels with question marks literally, or dismissing them.** "South of Hispaniola?" turned out to be right (Isla Beata).
- **Answering from memory about images.** I called the Venus circle "roses" then "waves" then "wings" before overlaying. Look at the actual image first.
- **Not asking for every page early.** The back of 003 (with the monk numeral and arrows) was missing for a long time. Collect front and back of every document before solving.
- **Combining steps too early.** "Bard's direction" and "Bard's last instructions" were treated as one; it worked, but write each instruction down separately before merging.
- **Coarse coastline data.** The 1:10m data lacks tiny islands and misplaces coasts by ~1 km. Use satellite view for final checks.

## Checklist for the next stage
1. Save every document (front and back) and every download into the repo `images/` before starting.
2. Transcribe text exactly, including stray marks, letter counts and symbols.
3. For each trial, list: inputs, operations implied by wording, expected output type.
4. Put every candidate place on the shared map with a confidence label.
5. Use geodesic lines and record coordinates to 4 decimals.
6. Keep a "guesses vs confirmed" table and promote only with evidence.
7. Look for a self-check (cipher, letter counts, unique solution) before committing.
8. Never submit until the result is verified; the user submits, not the assistant.

## Better map images (added during puzzle 02)
- Natural Earth / old OSM-derived coastline files are too coarse for small islands. Don't shape-match with them.
- Use `shared/tools/satview.py`:
  - `shape` = ESA WorldCover 2021, 10 m land/water map (crisp coastlines, lakes, lagoons, mangroves in green).
  - `photo` = Sentinel-2 true colour, 10 m, least-cloudy recent scene.
  - Both read straight from public AWS buckets, which the sandbox can reach. Needs `pip install rasterio mgrs`.
- First test: the ELDORIA-002 sketch matches Bimini almost line for line, including the two islets in the lagoon.
