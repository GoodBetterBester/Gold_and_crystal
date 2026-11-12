# Puzzle 02 – The shipwreck (ELDORIA-001 to 007)

**Status:** all documents received, solving in progress.

## Objective
From the Supplementary Analysis Note (`documents/000-supplementary-analysis-note.jpg`):
1. **Phase I:** documents 001–006 hold **four plans or maps**. Find the **4 locations** and a **precise point** in each.
2. **Phase II:** ELDORIA-007 is the **operational key**. It says how to combine or project the 4 points to find the **location and name of a shipwreck**.

The "892 / 55" marks on ELDORIA-004 were added later and are "not immediately relevant". Full archive decryption date: 9 November 2026.

## Folder layout
| Folder | What |
|---|---|
| `documents/` | Every page, named `<doc>-<side>-<what>.jpeg` |
| `transcripts/` | Text from the site, our translations and notes, one file per document |
| `tools/` | Scripts (`dead_reckoning.py` runs the 005 log legs) |
| `images/` | Our comparison images and overlays |
| `map/` | Map files and KML for this puzzle |

## Documents
| Doc | What it is | Files | Notes |
|---|---|---|---|
| Note | Instructions | `000-supplementary-analysis-note.jpg` | |
| 001 | Spanish letter, March 1513, signed (likely Ponce de León) | `001-letter-1513.jpeg` | `transcripts/001-prologue.md` |
| 002 | Front: Maltese cross + 3 lines of triangle/chevron symbols. Back: island map, "Bahama" arrow to the SE, Maya glyph, 16 letter boxes numbered 4 5 · 7 · 3 · 6 1 | `002a-…`, `002b-…` | below |
| 003 | Front: Maya stela, header `e2 b3 d1 d3 a4 d1`. Back: Yucatec Maya text + walled site plan by the sea | `003a-…`, `003b-…` | `transcripts/003-maya-text.md` |
| 004 | Logbook map: two islands, dashed route from the NE to a red X, triangle under the X with Maya numerals on its sides, two Maya glyphs at the corners, "The farthest point where South meets West", later marks 892 / 55 | `004-logbook-map.jpeg` | below |
| 005 | Spanish ship's log, days 21–32, six legs | `005-spanish-ship-log.jpeg` | `transcripts/005-ship-log.md` |
| 006 | Long, thin, curved island with a hooked north end. "Where the four hold their balance" | `006-island-four-balance.jpeg` | below |
| 007 | Key. Front: Spanish poem, 4 × 7 box grid, number list. Back: "Overlay the charts / Let the crosses meet / The wreck shall be revealed" + island chart | `007a-…`, `007b-…` | `transcripts/007-key.md` |

## What we KNOW (confirmed)
| Item | Fact | How we know |
|---|---|---|
| 002 front | Templar cipher → "RECORDAD A JPDL EL HOMBRE QUE BUSCO LA VIDA ETERNA" (Juan Ponce de León) | every one of 41 symbols fits |
| 002 back boxes | 15 boxes = JUANPONCEDELEON; numbered boxes spell ESCUALO (shark) | Garath: "=" is a wave |
| 002 back map | **Bimini** (North + South Bimini, lagoon islets) | satellite outline matches line for line |
| 002 back line | vertical line ≈ 79°15′W meridian | affine fit of sketch to satellite |
| 007 back chart | **Cuba region rotated 90° clockwise** (north to the right): Cuba, Isla de la Juventud, S Florida, Andros/Bahamas, Hispaniola | Garath spotted it; satellite overlay confirms |
| 007 "four winds" | cold, light, fire, shadow = four ordered slots | text |
| Discord | 007: names go in the 4 × 7 boxes left→right, top→bottom, in order; answer is a point in the sea | other players |
| Discord | 003 header = tiles on the stela; 003's place feeds into 004 | other players |

## What we SUSPECT (not confirmed)
| Item | Suspicion | Confidence |
|---|---|---|
| 003 back | site plan is Tulum (walls on 3 sides, sea to the east; text about sunrise over the sea) | medium |
| 002 point | where the 79°15′W line meets something (box row ≈ 25.718N 79.246W?) | low |
| 005 | log starts from the 004 X; "black cross" on Day 26; sharks link to ESCUALO | low |
| 007 order | cold = north, light = east, fire = south, shadow = west | low |

## Rejected (don't retry)
- 006 = San Andrés, 004 = Providencia/Santa Catalina (Garath: shapes are off).
- 007 chart = Havana bay close-up (it's the whole Cuba region, rotated).
- 003 header as 5×5 Polybius square, as paragraph/word index, or as a 6×4 table of the border (see transcripts/003).

## Answer
_Not yet. Garath submits; Claude never submits._

## 006 update (2026-11-12)

**KNOW (confirmed by Garath 2026-11-12):** 006 is **Mayaguana** (Bahamas), drawn rotated 90° clockwise (north points right), the same rotation as the 007 chart. The hook at the top right is the NW lobe, the bump halfway down the right side matches, and the SW tail with a small islet is the east end. Best shape score of all 880 islands (IoU 0.77). See `images/006-mayaguana-rotated.png`.

**SUSPECT — point:** "where the four hold their balance" = the island's balance point (centroid). From 10 m WorldCover: **22.3743 N, 72.9626 W** (bounding-box centre 22.3698 N, 72.9497 W). Not confirmed.

Eleuthera, Cat Island and Long Island were checked and do not fit (`images/006-other-candidates.png`).

## 004 work (2026-11-12)

- Searched every pair of nearby islands in the atlas (any rotation) against the two 004 shapes: no convincing land match (best scores are noise or mirrored).
- The drawing style (hatched rim, blotchy interior) looks like a **reef atoll**, which the land data cannot see. Compared Sentinel-2 photos of Banco Chinchorro, Turneffe, Lighthouse Reef, Glover's Reef, Alacranes, Hogsty: `images/004-atoll-candidates.png`.
- **SUSPECT (weak):** Banco Chinchorro (two lobes with a waist, ~250 km south of Tulum, fits "003 feeds 004"). Not confirmed.
- Inagua, Providencia (rejected earlier) do not fit.

## 007 grid insight (Garath, 2026-11-12) — SUSPECT (strong)
The 007 grid is 4 rows × 7 boxes, so each of the four locations gives a **7-letter word**, one per row. 002 fits: **ESCUALO** (7 letters). So row answers are hidden words, not the place names (Bimini, Tulum, Mayaguana).
- 003: the code `e2 b3 d1 d3 a4 d1` has only 6 pairs, and d1 repeats → the 7-letter word repeats a letter; the 7th letter must come from somewhere else (or our grid reading is wrong).

## 004 triangle (2026-11-12) — SUSPECT
- Bottom-left glyph = the glyph on 002 (Bimini). Bottom-right glyph = presumably 003 (Tulum/Zamá) (Garath).
- Side marks: Bimini–X "II" (Maya 10), Tulum–X "bar+dot" (Maya 6), base "1 + shell" (10?). Bimini–Tulum = 1036 km (560 nm).
- With 10 : 6 : 10 and X on the side shown in the drawing → X ≈ 16.9 N, 82.7 W (open Caribbean, east of the Swan Islands).
- ~~Candidate islands: Swan Islands~~ REJECTED by Garath. Swan Islands (Islas del Cisne, Honduras)** — two islands almost touching, matches the sketch turned 180°. `images/004-swan-islands.png`.
- "The farthest point where South meets West" → SW tip of Great Swan: **17.4004 N, 83.9430 W**.
- 892 / 55 not yet used.

## KEEP FOR LATER
- **003 answer word: ZAMA** (Tulum's old name). Helper: "note ZAMA down, you will need it later" (probably the 007 grid).
- 002 word: ESCUALO.

## Precise points (2026-11-12)
- **002 Bimini: "Shark Mound" 25.7491 N, 79.24753 W** (Garath; ESCUALO = shark). Sits exactly on the 002 meridian line (~79°15′W). KNOW (strong).
- **003 Tulum: Temple of the Wind God** (≈ 20.216 N, 87.428 W; approximate — refine on a map). Agreed with Garath 2026-11-12 (wind on the shore, sound/breath, sunrise).
- 004: triangle X ≈ 17.0–17.3 N, 82.66 W (Shark Mound–Tulum base 1038 km). Whether 005 starts here is doubtful (route would cross Cuba).
- 006 Mayaguana: centroid 22.3743 N, 72.9626 W (suspect).

## 004 islands: Isla Margarita (2026-11-12) — REJECTED by Garath ("shape is way wrong")
- Garath: the triangle distances and all earlier candidates (Corn Is., Providencia, Swan, atolls) do not match.
- New candidate: **Isla Margarita (Venezuela)**. Small west lobe (Macanao) + bigger, pointed east lobe, joined at the bottom by a thin strip (La Restinga) — same layout as the sketch, north-up, no rotation. Mangrove lagoon matches the sketch's blotchy interior. `images/004-margarita-compare.png`.
- "The farthest point where South meets West" = SW extreme, which is also the westernmost point: **Punta Arenas, 10.9722 N, 64.4081 W** (WorldCover 10 m).
- Triangle not yet explained: from this point, Shark Mound 2269 km, Tulum 2670 km, Mayaguana 1565 km. Side marks re-read: left "II" = 10, right bar+dot = 6, base bar+shell = 5 (shell above) or 100.

## 004 status (2026-11-12, later)
- Discord spoiler: 004 is a **triangulation** (KNOW). Corners and units unknown.
- Garath's side reading: 1000 km, 1010 km, 100 km. With Bimini as a corner this always puts X at ~16.7–17.7 N (Swan / Pedro / Jamaica belt) — all shapes there rejected. Pedro Bank REJECTED. So probably the corners are not Bimini/Tulum, or the units differ.

## 004 = Bajo Nuevo Bank (2026-11-12) — SUSPECT (strong; three clues agree, waiting on Garath)
- Triangle side marks read as **Maya base-20 numbers** (bar 5, dot 1, shell 0; two-place): base bar·shell = 5×20+0 = **100**, left bar·bar = 5×20+5 = **105**, right bar·dot = 5×20+1 = **101**. (Garath read 100 / 101 / 10; the drawn triangle is nearly equilateral, which fits 100/105/101.)
- Base = Shark Mound (Bimini) to Tulum Temple of the Wind God = 1038 km = 100 units → Bimini–X 1090 km, Tulum–X 1049 km → **X = 15.9215 N, 78.5948 W** (southern solution).
- That is **Bajo Nuevo Bank** (Petrel Islands, ~15.88 N 78.63 W): two reef complexes almost touching, small NE one and big SW one. Turned 180° (south up) it matches the sketch: small left, big right, reef rim on top. South-up also explains the triangle: Bimini bottom-left, Tulum bottom-right, X above. `images/004-bajo-nuevo-compare.png`.
- The point also lies inside the only western-Caribbean zone where the 005 legs stay at sea (15.3–16.7 N, 78.0–79.2 W).
- "The farthest point where South meets West" → SW end of the big reef ≈ **15.80 N, 78.75 W** (from Sentinel-2 shallow-water outline; rough, refine on satellite view). On the south-up sketch this is the top-right tip, where there is a dark red blot.
