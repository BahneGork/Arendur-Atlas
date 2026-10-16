# Arendur atlas – assessment

- **Written**: 2026-10-16, Phase 0 of the `campaign-atlas` skill
- **Campaign**: The Arendur Rising (GM: the owner). Group: The Shadow Company
- **Decided with the owner**: two atlases kept apart, a **player atlas** first and a **GM layer** later. Notes are in the GMnostes repo. Three maps. Language as in the notes (Danish/English).

## 1. What exists

| Source | Where | Player-safe? | Published in GMnostes? |
|---|---|---|---|
| Player Vault (109 files: locations list, 43 people, 6 missions, handouts, chronicle) | `The Shadow Company/Bible/Player Vault/` | Yes (written for players) | **14 of 109** |
| Cutscenes (13) | `Handouts/Cutscenes/` | Yes, if they were shown | Yes, all 13 |
| Company Chronicle, book 1 (numbered story list, ~sessions 1–25?) | Player Vault | Yes | Yes |
| Session sheets "Logged – Session 26–47" (22) | `The Bible/03 Old sessions notes/Session sheet/` | **Unknown – GM sheets** | No |
| Summaries, sessions 30–47 (16; 44 and 46 missing) | `The Bible/03 Old sessions notes/Summaries/` | Mostly (table talk, outcomes) – needs a check | No |
| Fact sheets: people, factions, locations, setting, secrets & clues | `The Bible/04 Fact sheets/` | **No** – GM bible | No |
| Prep, seedbox, Claude-generated content | various | No | No |

GMnostes is a **public** repo. Anything published there is readable by anyone, including players.

## 2. Maps (three levels)

| Level | Image | Size | Notes |
|---|---|---|---|
| Region | `The Bible/04 Fact sheets/14 Locations/Ursia/ursia-baronies-map.png` | 7092×5686 | Barony areas as coloured hex zones; only Arendur and Kvalec labelled. Coloured lines (red, green, purple, blue) – **check that none of them is GM-only** |
| Area | `The Shadow Company/Bible/EastBlackwood-PC.png` | 1131×1080 | Player version. Many labels (Delios, Teslions, Blackspear, Sunken Citadel, Skull Gorge, Red Hand Warcamp …) and dotted routes – good for pins. Small image. A GM version exists (6812×6505); not used for the player atlas |
| Town | `10 Attachments/Delios no pins.png` (base) + `Player Vault/Handouts/Delios-poi.png` (labels) | 7680×4320 / 1449×1083 | The handout has ~22 named points (Town Hall, Black Portrait Inn, Gaed's sanctuary, Operation Mongoose …); positions can be transferred to the clean base map |

Links: Ursia → East Blackwood → Delios through map tabs and a button in the place panel (no signposts in pin clusters – skill lesson).

## 3. Grading per atlas feature (player atlas)

| Feature | Verdict | Why |
|---|---|---|
| Map + pins | **Build** | Three player-safe maps; the Blackwood and Delios maps carry their own labels; the locations list names ~25 places |
| Place panels | **Build partially** | Players have a list of place *names*, but the place notes those names link to are GM fact sheets. Panel text must come from player sources (chronicle, missions, cutscenes, summaries) or be short and written for players |
| Rejsen (journey) | **Build partially** | Sessions 1–25 exist only as the chronicle's numbered story list (no session numbers). 26–47 have GM sheets and summaries. The journey needs a session→places list that is checked for spoilers |
| People register | **Build** | 43 player-vault people notes; need checking for frontmatter (`location`, `status`) |
| Factions | **Skip for now** | No player-side faction notes; faction knowledge sits in the GM bible |
| Tråde (threads) | **Skip for now** | Possible later from "3.Secrets Revealed" and "Shadow Company Revelations list", but needs the owner |
| Party | **Build** | Four PCs known (Cedric, Brumor, Anton, Frekka) with class and role in the Company – the source is the GM summary, so the owner confirms |

Arendur extras worth considering later: The Shadow Company HQ (Fallen Star Inn), the Mission Board, domain/warfare – not features of the Erukana atlas.

## 4. Spoiler safety (the main difference from Erukana)

Erukana was built from a player's own notes, so everything in them was player knowledge. Here the owner is the GM, and most notes are secrets. Rules for the player atlas:
- **Read only player sources**: the Player Vault, cutscenes, the chronicle – plus GM summaries/session sheets *only* to get session numbers and places, never to copy text, and only after the owner confirms they're player-safe.
- **Never follow links into the bible.** A player-vault link to `[[Delios]]` resolves to a GM fact sheet; the atlas must not use its text or link to it.
- **Labels on maps count as content.** Use the PC map, not the GM map.
- The GM layer is never built from or deployed to anything public (GMnostes and GitHub Pages are public). It runs locally, or in a private place the owner chooses.

## 5. Answers from the owner (2026-10-16)

- **Sessions**: the "Logged – Session N" sheets are mostly prep notes; summaries exist for some sessions only. Which session did what is hard to pin down, so the journey is left out for now. Option: journey stages from the chronicle's numbered points instead of sessions.
- **Maps**: more maps will be added later (see README, "Adding a map").
- **Reading**: Claude may read everything, GM notes included. The public atlas still only states player knowledge.
- **Ursia map**: the coloured areas are the baronies, coloured by the major noble house the baron serves.
- **Repo**: `BahneGork/Arendur-Atlas`, site at https://bahnegork.github.io/Arendur-Atlas/

## 6. Still open

1. **Publishing**: only 13 of the Player Vault's notes are published in GMnostes (plus 13 cutscenes). Publishing the rest (people, handouts) would let the people register and "read the note" links work.
2. **Barony names**: which baronies and noble houses do the players know? Then the coloured areas can become regions.
3. **Approximate pins** around Delios (Click Claw Watch, Ravnekongens grav, Fallen Star, mausoleet, Blackbriar, rangerhytten, Blackspear-sumpen, Camp Oxbar, East Blackwood on Ursia): placed from the chronicle's directions; drag them into place on the site.
4. **Unplaced**: Dødebjerget, Akalane, Stålridderborgen – where are they?
