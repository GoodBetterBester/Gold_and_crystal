# Eldoria hunt notes

Working notes for the Gold & Crystal "Eldoria" hunt.

## Puzzle 01: key phrase (solved)

- **Key:** `SANPEDRODELAROCA` (Castillo San Pedro de la Roca del Morro, Santiago de Cuba)
- **Cipher:** Vigenère (Blaise de Vigenère, *Traicté des Chiffres*)
- **Sentence (ELDORIA-TRIAL-001):** `Ey yxjh nov fpalhkfml nch ilzo sq aujgnluetw.`
- **Plaintext:** *My life was beautiful and full of adventures.*

| Trial | Place | How |
|---|---|---|
| Courage (002) | Havana | The 8 places form two arrows. Shafts: St. Augustine → Mound Key and Dominica → Tortuga; feathers: Tampa Bay + Lake Okeechobee, Isla Beata + Grand Turk. Extended, the shafts meet at Havana. Hint: "harrowing" hides "arrow". |
| Knowledge (003) | Jamaica north shore, Ocho Rios / St. Ann's Bay | Circled objects (bread, dog, celestial globe, rose) → forts; great-circle X crossing; Cistercian numeral 3839 × 185.2 m west; Shakespeare: "Go towards the sunset at the northern shore". |
| Cunning (004) | Town Hill, Bermuda | Polyominoes tile the board; black pieces from map clues; Qg8# → square g8 = Bermuda. |
| Sagacity (005) | St. George's, Grenada | Acrostic EAST OF CUMANA; reversed NORTH OF TOBAGO; anagram WEST OF BARBADOS; Caesar-3 SOUTH OF CARRIACOU; keep the capital. |

Crossroads: Havana–Grenada × Ocho Rios–Bermuda (great circles) = 20.02°N 75.84°W, Santiago de Cuba.

## Hunt status (12 Nov 2026)
The official hunt has started. Answers can no longer be entered on the site to unlock the next stage (Garath). Players on Discord think the solutions are kept for later, to reveal the chest locations. So there is no feedback from the site any more: rely on self-checks (cipher output, unique words, routes that close) and keep every answer recorded here.

## Puzzle 02: the shipwreck (name solved, position open)

- **Wreck name:** `MARAVILLAS` (self-checking, from the 007 grid).
- **Position:** candidate about 21.47 N, 79.03 W, not confirmed. Not submitted.

| Wind | Doc | Place | Point |
|---|---|---|---|
| North | 002 | Bimini | Shark Mound, 25.7491 N, 79.2475 W |
| East | 006 | Mayaguana | centre, 22.3743 N, 72.9626 W (suspect) |
| South | 004 | Bajo Nuevo Bank | SW reef tip, about 15.80 N, 78.75 W |
| West | 003 | Tulum (Zamá) | Temple of the Wind God, about 20.216 N, 87.428 W |

005 is the voyage from 004 to 006. Full write-up: `puzzle-02-shipwreck/README.md`.

## Layout

Each puzzle has its own folder; shared things live at the top.

| Folder | What |
|---|---|
| `puzzle-01-key-phrase/` | Stage 1 (solved): `walkthrough.md`, `documents/`, `images/`, `map/`, `tools/` |
| `puzzle-02-shipwreck/` | Stage 2: name solved, position still a candidate. See its `README.md` |
| `shared/tools/` | Reusable tools: Vigenère decoder, `satview.py` (satellite shapes and photos), `seabed.py` (reefs and banks) |
| `LEARNINGS.md` | What worked, mistakes to avoid, checklist for each new puzzle |

For a new puzzle, make `puzzle-NN-name/` with `README.md`, `documents/`, `transcripts/`, `tools/`, `map/`.
