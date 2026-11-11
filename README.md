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

## Layout

Each puzzle has its own folder; shared things live at the top.

| Folder | What |
|---|---|
| `puzzle-01-key-phrase/` | Stage 1 (solved): `walkthrough.md`, `documents/`, `images/`, `map/`, `tools/` |
| `puzzle-02/` | Next puzzle: starts from the template in its `README.md` |
| `shared/tools/` | Reusable tools (Vigenère decoder) |
| `LEARNINGS.md` | What worked, mistakes to avoid, checklist for each new puzzle |

For a new puzzle, copy `puzzle-02/` and rename it.
