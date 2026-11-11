# Stage 1 walkthrough

Goal (ELDORIA-TRIAL-001): four trials each point to a place. Where their paths cross is a fort whose name is a 16-letter key. Decrypt the sentence at the bottom of 001 with the *Traicté des Chiffres* (Vigenère).

## Sagacity (005) → St. George's, Grenada
Four hidden messages, "keep the capital":
1. Acrostic of the poem's line initials: **EAST OF CUMANA**
2. `ogabot fo htron` read backwards: **NORTH OF TOBAGO**
3. `Stew fo dabonabs`, each word unscrambled: **WEST OF BARBADOS**
4. `vrxwk ri fduuldfrx`, Caesar −3 ("ancient Imperator"): **SOUTH OF CARRIACOU**

The box contains Grenada; its capital is St. George's.

## Cunning (004) → Town Hill, Bermuda
- Back page: Caribbean map with an 8×8 grid = chessboard, plus 8 polyominoes of 8 squares each.
- The polyominoes tile the 8×8 board in exactly one way (no rotation). White: Kc1, Nb1, Qg2, Rh7, pawns d4, e3, f2, f5 (`tools/chess_tiling.py`).
- Black from the text: King on the Caymans (b3) with a pawn north (b4); Queen on La Evangelista = Isla de la Juventud (a4); pawn on Green Turtle Cay (c6); Knight NE (d7); Bishop N (c7); Rook far NW watching bishop and queen (a7).
- White to move: **Qg8#** (only mate, `tools/chess_mate.py`). Square g8 on the map = Bermuda; highest point = Town Hill.

## Knowledge (003) → north shore of Jamaica (Ocho Rios / St. Ann's Bay)
1. **Cross the paintings.** Overlay each sketch frame on the real painting; the circle marks one object, which maps to a fort in the table:
   - Last Supper → bread → Castillo de los Tres Reyes del Morro (Havana)
   - Las Meninas → dog → San Felipe del Morro (San Juan)
   - The Ambassadors → celestial globe → Fort Charles (Port Royal, Jamaica)
   - Birth of Venus → rose → St. Ann's Fort (Barbados)
   Draw the X between diagonal frames (bread–rose, dog–globe) as **great circles** → 18.33°N 70.38°W.
2. **Shakespeare direction.** Fill the blanks (waves, Hamlet, glorious, dangerous, and, question, Denmark, holy); each arrow moves one word along the quote, ↑ goes to the same word position on the line above → "Go towards the sunset at the northern shore."
3. **Number of the monks** = Cistercian numeral on the back page = **3839**. × 1 international cable (185.2 m) = 711 km west → 18.33°N 77.11°W.
4. **Northern shore** → Jamaica's north coast at Ocho Rios / St. Ann's Bay.

## Courage (002) → Havana
- Text places: Mound Key (shell), Castillo de San Marcos (star fort), Tortuga (turtle), Morne Diablotins (volcano).
- Sketch X places (by shape): Tampa Bay (Y-shaped bay), Lake Okeechobee (round), Isla Beata (south of Hispaniola), Grand Turk (north of Hispaniola).
- The sketch links form two arrows (Discord hint: "harrowing" → arrow). Extend the shafts St. Augustine → Mound Key and Dominica → Tortuga ("take some distance") → they meet at **Havana** (23.13°N 82.36°W).

## Crossroads → key
Great circles Havana → St. George's and Ocho Rios → Town Hill cross at **20.02°N 75.84°W**, Santiago de Cuba, guarded by **Castillo San Pedro de la Roca del Morro**.

Key `SANPEDRODELAROCA` (16) + Vigenère on `Ey yxjh nov fpalhkfml nch ilzo sq aujgnluetw.` → **My life was beautiful and full of adventures.**
