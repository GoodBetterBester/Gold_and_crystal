# Puzzle 02 – The shipwreck (ELDORIA-001 to 007)

**Status (12 Nov 2026):** wreck **name solved: MARAVILLAS**. Wreck **position: candidate only** (about 21.47 N, 79.03 W), not confirmed. Nothing has been submitted; Garath submits.

The working log with every dead end is in [`notes-log.md`](notes-log.md). This page is the clean version.

## The task
From the Supplementary Analysis Note (`documents/000-supplementary-analysis-note.jpg`):
1. **Phase I:** documents 001–006 hold four plans or maps. Find the **4 locations** and a **precise point** in each.
2. **Phase II:** ELDORIA-007 is the key. Use it on the four points to get the **name and position of a shipwreck**.

## The solution in one picture

| Wind (007 poem) | Doc | Place | Word for the grid | Precise point | Confidence |
|---|---|---|---|---|---|
| Cold = north | 002 | Bimini, Bahamas | BIMINI | Shark Mound, 25.7491 N, 79.2475 W | KNOW |
| Light = east | 006 | Mayaguana, Bahamas | MAYAGUANA | island centre, 22.3743 N, 72.9626 W | place KNOW, point SUSPECT |
| Fire = south | 004 | Bajo Nuevo Bank | BAJONUEVO | SW end of the big reef, about 15.80 N, 78.75 W | place KNOW, point rough |
| Shadow = west | 003 | Tulum (old name Zamá) | ZAMA | Temple of the Wind God, about 20.216 N, 87.428 W | place KNOW, point SUSPECT |

005 (the ship's log) is not a fifth place: it is the voyage from 004 to 006.

## How each document was solved

### 002 – Bimini (KNOW)
- **Front:** Templar (Maltese cross) cipher → `RECORDAD A JPDL EL HOMBRE QUE BUSCO LA VIDA ETERNA` (Juan Ponce de León). All 41 symbols fit. See `transcripts/002-templar-cipher.md`.
- **Back:** the island sketch matches North and South Bimini line for line (`images/002-bimini-satellite.png`). The 15 boxes take `JUANPONCEDELEON`; the numbered boxes spell **ESCUALO** (shark).
- **Point:** Shark Mound on Bimini (Garath). It sits on the sketch's vertical line, about 79°15′ W.

### 003 – Tulum / Zamá (KNOW)
- **Back:** Yucatec Maya text about sunrise over the sea and wind among old stones, plus a walled site plan by the shore = Tulum. Text and translation in `transcripts/003-maya-text.md`.
- **Front:** the header `e2 b3 d1 d3 a4 d1` are grid references. Slide the stela's numeral tiles up into a 6 × 4 grid at the top (helper's hint: treat them like loose Scrabble tiles). Reading the six cells gives 2 6 1 1 3 1 → 26 · 1 · 13 · 1 → **ZAMA**, the old Maya name of Tulum ("dawn").
- **Point:** Temple of the Wind God, from the riddle (wind on the shore, breath, sunrise). Agreed with Garath; coordinates approximate.

### 004 – Bajo Nuevo Bank (KNOW, confirmed by 005 and 007)
- The map is a **triangulation** (also confirmed by a Discord spoiler). The corner glyphs are 002 (Bimini) and 003 (Tulum).
- The side marks are **Maya base-20 numbers** in two places (bar 5, dot 1, shell 0): base bar·shell = **100**, left bar·bar = **105**, right bar·dot = **101**. Garath spotted the 100 and 101. The triangle is drawn almost equilateral, which fits.
- Base = Shark Mound → Tulum = 1,038 km = 100 units. So X is 1,090 km from Shark Mound and 1,049 km from Tulum: **15.9215 N, 78.5948 W** (`tools/004_triangle.py`).
- That is Bajo Nuevo Bank: two reefs almost touching. Turned 180° (the map is drawn **south up**) it matches the sketch (`images/004-bajo-nuevo-compare.png`). South up also puts Bimini bottom-left and Tulum bottom-right, as drawn.
- **Point:** "The farthest point where South meets West" = SW end of the big reef, about 15.80 N, 78.75 W. Read off a Sentinel-2 photo; could be a kilometre or two out.
- The later marks "892 / 55" are unused. The note says they are not relevant yet.

### 005 – the voyage from 004 to 006 (KNOW)
Run the six legs exactly as written, in nautical miles, from Bajo Nuevo (`tools/dead_reckoning.py`):

| Day | Leg | Ends at |
|---|---|---|
| 21 | East 200 | 15.80 N, 75.29 W |
| 23 | North 175 | 18.72 N, 75.29 W |
| 26 | North-east 150 | 20.48 N, 73.41 W (Windward Passage) |
| 28 | East 250 | 20.48 N, 68.96 W |
| 30 | North 114 | 22.38 N, 68.96 W |
| 32 | West 230 | 22.38 N, 73.11 W = **Mayaguana** |

Every leg stays at sea, and the last one runs along Mayaguana's own latitude and lands on it. Map: `images/005-voyage-from-bajo-nuevo.png`. The compass trouble, green lights and "forbidden waters" are Bermuda Triangle colour; the route enters the triangle on Day 28.

### 006 – Mayaguana (KNOW)
- Long thin island with a hooked end, drawn rotated 90° clockwise (north to the right). Best shape match of 880 islands, confirmed by Garath (`images/006-mayaguana-rotated.png`).
- **Point (SUSPECT):** "Where the four hold their balance" read as the island's centre of area, 22.3743 N, 72.9626 W. Not confirmed.

### 007 – the key
**Name (KNOW, self-checking).** The poem gives the order of the four winds: cold (north), light (east), fire (south), shadow (west). The four names fill the 28 boxes exactly:

```
B I M I N I M
A Y A G U A N
A B A J O N U
E V O Z A M A
```

The numbers pick boxes and the small numbers shift the letter: 27 M, 17 A, 20 N+4 = R, 8 A, 23 V, 6 I, 19 O−3 = L, 11 G+5 = L, 15 A, 25 Z−7 = S → **MARAVILLAS**. Of the 24 possible orders only this one gives a word (`tools/007_grid.py`). Nuestra Señora de las Maravillas was a Spanish galleon lost in 1656.

**Position (SUSPECT).** Back of 007: "Overlay the charts / Let the crosses meet / The wreck shall be revealed", with a chart of Cuba and its surroundings rotated 90° clockwise.
- Our reading: join the four X points north–south and west–east; the wreck is where the lines cross. Overlay: `images/007-overlay-cross.png`.
- Straight lines on a flat map cross at **21.47 N, 79.03 W**: in the sea, about 12 km off Cuba's south coast (Gulf of Ana María). This fits the Discord hint that the answer is a point in the sea.
- Great-circle lines cross at 21.63 N, 79.03 W, about 4 km inland, so that version does not fit.

## Still open
1. The exact 006 point ("where the four hold their balance"). It moves the crossing the most.
2. The exact 004 point (SW tip of the reef). Using the triangle X instead moves the crossing about 7 km east.
3. Whether "let the crosses meet" really means the two joining lines, and whether lines should be flat or great-circle.
4. The "892 / 55" marks on 004.

## Rejected (don't retry)
- 004 as Swan Islands, Providencia / Santa Catalina, Corn Islands, Inagua, Isla Margarita, Pedro Bank, or the Belize / Chinchorro atolls (Garath: shapes wrong).
- 004 triangle sides as 10 / 6 / 10 or as 1000 / 1010 / 100 km.
- 005 starting from Tulum or from a point near the Swan Islands (the route crosses Cuba). 005 starting or ending at Grenada.
- 005 Day 28 as "136 miles" (250 minus 114). The legs work as written.
- 006 as San Andrés, Eleuthera, Cat Island or Long Island.
- 003 header as a Polybius square, paragraph index, or direct table of the border.
- 007 chart as a Havana close-up.

## Folder layout
| Folder | What |
|---|---|
| `documents/` | Every page, front and back |
| `transcripts/` | Text, translations and detailed working per document |
| `tools/` | `004_triangle.py`, `007_grid.py`, `dead_reckoning.py`, 003 brute-force scripts |
| `images/` | Comparison images and overlays |
| `notes-log.md` | The full working log, in order, including dead ends |

Shared tools used: `../shared/tools/satview.py` (10 m land map and Sentinel-2 photos) and `../shared/tools/seabed.py` (shallow reefs and banks).
