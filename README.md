# Eldoria hunt notes

Working notes for the Gold & Crystal "Eldoria" hunt.

## Stage 1: solved

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

## Notes

- `notes/walkthrough.md` – step-by-step solution of every trial.
- `notes/learnings.md` – what worked, mistakes, and a checklist for the next stage.

## Folders

- `map/eldoria-trial1.kml` – import into Google My Maps (Add layer → Import).
- `map/eldoria-map.html` – standalone interactive map.
- `tools/` – Vigenère, chess tiling and mate search scripts.
- `images/` – sketch crops and painting overlays.
