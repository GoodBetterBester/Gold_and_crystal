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
