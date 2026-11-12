# ELDORIA-005 – Ship's log (site's certified translation)

Image: `../documents/005-spanish-ship-log.jpeg` (Spanish original). Each entry ends with three blank lines: *Latitude by reckoning / Longitude of arrival / Corrected longitude*.

> After twenty days at sea, we cast anchor and awaited the mercy of the waters. This voyage was but one stage toward the true treasure.

| Day | Text (summary of the key facts) |
|---|---|
| 21 | Course East since the previous evening. 4 knots, nearly 100 miles since yesterday. First waypoint in 2.5 days, **200 miles from departure**. |
| 23 | Course **North**, easterly wind. Two more days north, **175 miles**. Warm current under the keel. Red moon, three stars to the North, "the Crown of the Old King" (Corona Borealis?), "said to guide toward forbidden waters". |
| 26 | Came about to the **north-east**. **150 miles** on this heading. Needle restless. Seven sharks. "Tomorrow we shall reach the point marked with a black cross on the chart." |
| 28 | Course **East**, **250 miles** yet to overcome. Currents favour us. Green light pulsing beneath the waters. |
| 30 | Course **North**, **114 miles** to the appointed place, between two contrary currents. Compass motionless, pointing North. Dull glow on the water. "Tomorrow will be the final leg." |
| 32 | Prow to the **West**, **230 miles** toward the sunset. Sharks gone. **Compass fixed toward the East.** "We flee toward the sunset." |

## Notes
- Distances are presumably nautical miles (1 nm = 1′ of latitude).
- Starting point unknown. Candidate: the red X on ELDORIA-004.
- "Corrected longitude" may mean correcting for the faulty compass (Day 32) or for magnetic variation.
- Use `../tools/dead_reckoning.py` to run the legs from any start point.

## Test run from Tulum (2026-11-12) — SUSPECT, not confirmed
Start 20.2155 N, 87.4285 W (Temple of the Wind God):
- Day 21 E200 → 20.22 N, 83.88 W (sea, SW of Cuba)
- Day 23 N175 → 23.13 N, 83.88 W (just off NW Cuba)
- Day 26 NE150 → 24.90 N, 81.94 W (off Key West / Marquesas Keys; "tomorrow the black cross")
- Day 28 E250 → 24.90 N, 77.35 W (Exuma Sound / Eleuthera area)
- Day 30 N114 → 26.80 N, 77.35 W (near Abaco)
- Day 32 W230 → 26.80 N, 81.64 W (on land in SW Florida); if the reversed compass means the true heading was East → 26.80 N, 73.05 W (open Atlantic)
Every waypoint lands on a recognisable place, which is suggestive, but the log should start from the 004 X, which we have not located.

## Run from the 004 triangle point (2026-11-12) — SUSPECT
004 triangle (Garath: Bimini–Tulum ≈ 1040 km = base "10" → unit ≈ 100 km; Bimini–X 1000 km, Tulum–X 600 km) → start **17.2742 N, 82.6746 W** (sea, Swan Islands to the west).
- Day 21 E200 → 17.27 N, 79.18 W (sea, SW of Jamaica)
- Day 23 N175 → 20.19 N, 79.18 W (sea, south of central Cuba)
- Day 26 NE150 → 21.96 N, 77.29 W (sea, just off Cuba's north coast near Nuevitas)
- Day 28 E250 → 21.96 N, 72.80 W (sea, ~48 km from Mayaguana = 006!)
- Day 30 N114 → 23.86 N, 72.80 W (open Atlantic)
- Day 32 W230 → 23.86 N, 76.99 W (Great Bahama Bank, near Exuma); if really East → 23.86 N, 68.6 W (open Atlantic)
All waypoints are at sea.
- Reading of the full English log (Garath, 2026-11-12): day 30 ends "at the appointed place" ("114 miles to the appointed place … tomorrow our last leg"); day 32 is the flight away. → **005 precise point = end of day 30 ≈ 23.86 N, 72.80 W** (SUSPECT, strong).
- Day 26 "black cross on the chart" ≈ 21.96 N, 77.29 W — may line up with a cross on the 007 chart.

## Re-plot with "miles remaining" reading (2026-11-12) — SUSPECT
- Day 28 "250 miles remained to be crossed" and Day 30 "114 miles to the appointed place" read as distance still to go → east leg = 250 − 114 = **136 nm** (not 250).
- Day 26 note: 150 nm "covered on this new course" though they turned "at first light" → turn was probably earlier; black cross is reached "tomorrow" (day 27), beyond this leg.
- From the Swan Islands X (17.27 N, 82.67 W) the Day 26 NE leg crosses Cuba under either reading, even with compass offsets of ±60° → that start is WRONG.
- Sea-only start search (0.1° grid, legs E200 N175 NE150 E136 N114): in the western Caribbean only **15.3–16.7 N, 78.0–79.2 W** works (south of Jamaica, Pedro Bank area). Route then goes through the Windward Passage; appointed place lands at **21.9–23.3 N, 70.2–71.5 W** (north/north-east of Turks & Caicos, inside the Bermuda Triangle).
- Example: start 15.9 N 78.4 W → 15.9 N 74.93 W → 18.82 N 74.93 W → 20.58 N 73.06 W → 20.58 N 70.64 W → **22.48 N 70.64 W**.
- Map of sea-only starts: shared folder `005-possible-starts.png` (dots are faint).
