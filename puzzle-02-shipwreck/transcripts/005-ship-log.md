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
