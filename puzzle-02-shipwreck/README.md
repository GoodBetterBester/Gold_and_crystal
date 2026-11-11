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

## Which documents are the four maps?
| # | Map | Place (guess) | Precise point (guess) | Confidence |
|---|---|---|---|---|
| 1 | 002 back | island group NW of the Bahamas (Bimini? Florida?) | from the Templar cipher + 16 boxes | low |
| 2 | 003 back | **Tulum**, Mexico (20.2148 N, 87.4290 W) | Temple of the Wind God or El Castillo | medium |
| 3 | 004 | ? (two islands) | SW tip ("where South meets West"), red X | low |
| 4 | 006 | ? long island (Eleuthera? Long Island?) | "where the four hold their balance" (centre point?) | low |

005 is a route, probably starting from the 004 X, not a map of its own.

## Clues and progress
| Clue | Our reading | Confidence |
|---|---|---|
| 002 front (Templar cipher) | **SOLVED:** "RECORDAD A JPDL EL HOMBRE QUE BUSCO LA VIDA ETERNA" = remember Juan Ponce de León. See `transcripts/002-templar-cipher.md` | high |
| 002 back: 15 boxes | JUANPONCEDELEON fits exactly; marked boxes give E _ C U A L O = **ESCUALO** (shark) → the shark legs in 005 | medium |
| 003 header `e2 b3 d1 d3 a4 d1` | grid references into the stela numerals | low |
| 004 triangle numerals | about 10 (left), 6 (right), 5 or 10 (bottom); maybe distances or bearings | low |
| 005 legs | net to Day 30 point: 556 nm E, 395 nm N; Day 32 compass fixed to East | medium |
| 007 "four winds keep the order" | the four maps go in a fixed order (cold, light, fire, shadow) | low |
| 007 numbers `27, 17, 20+4, 8, 23, 6, 19-3, 11+5, 15, 25-7` | index into the 28 boxes, possibly with letter shifts | low |
| 007 "overlay the charts, let the crosses meet" | line up the X/cross on each map; the wreck is where they meet | medium |

## Answer
_Not yet. Garath submits; Claude never submits._
