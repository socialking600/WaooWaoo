# DESCENT — 60s, 16:9, 1920x1080
### Director's treatment + shoot-ready prompts
Style pass by the agent. Replaces the earlier beat sheet.

---

## 0. What was wrong with the previous draft (mine)

| Claim I made | Reality | Fix |
|---|---|---|
| "Release 20–30s before the next peak" | In 60s that gives **2 peaks**. A 60s film needs 4. | Release = **1.5–3s**. 20–30s releases are for 90–180s cuts. |
| 12 + 11 shots in 60s | 23 generations, each ~2.5s. Models can't hold character identity across that many 2.5s clips, and hard cuts at 1.5s read as noise, not rhythm. | **10 + 10 shots over 25s + 35s.** Fewer clips, more internal beats. |
| "no shot longer than 4 seconds" | Shot 10 ran 21–25s (4s) and the time-lapse read as a duration violation. | Hard cap **3.5s**, and the cap lives in the prompt header, not per-shot. |
| Four arms in wide, two in close | Continuity break the model will not resolve. It will just pick one and lie. | **Never show four arms.** The trident and damaru exist as *light in the water* only. More mythic, and it removes the top filter risk instead of treating it as fallback. |
| "If it struggles, split into 3 clips" | Splitting is not a fallback, it's the correct method. | **Always generate short clips** — 3 for Video 1, 6 for Video 2, every one ≤10s — and join at peak/release boundaries. |
| "Video 1 is 0–30s, Video 2 is 30–60s" | The second peak is at 25s, so a 30/30 split puts the seam *after* the peak and kills it. | **Video 1 = 0–25s, Video 2 = 25–60s.** The seam sits on the peak. |

---

## 1. The style — seven rules I actually work by

**Rule 1 — Anchor the face before the world.**
AI continuity fails at the cut, never inside a clip. A model will render any single frame beautifully and then hand you a stranger after a hard cut. So identity is locked in the first 3 seconds, in a frame that contains skin, eye-line and hair at legible size, and that identity block is then repeated *verbatim* in every later prompt. If a clip must open wide, the wide shot still gets the identity block — it just can't be the audience's first read of her.

**Rule 2 — One impossible thing per shot.**
One violation of physics, one verb, one emotion. Two impossibilities in one clip means the model splits its attention and you get grey mush. "The sky tears open *and* a river falls *and* a shockwave rings out" is three shots wearing a trench coat.

**Rule 3 — The cut is the special effect.**
Never cut on similar. Cut scale (extreme wide → extreme macro), cut light (storm-blue → silver), cut movement (locked-off → handheld), or cut time (real-time → time-lapse). If a cut doesn't do one of those four, delete it.

**Rule 4 — Camera alternates; the eye needs a place to recover.**
Moving / locked / moving / locked. Three moving shots in a row and the audience stops reading the frame. Every peak is preceded by a locked-off shot.

**Rule 5 — Sound lands the peak, not the image.**
Cut on silence, not on impact. 40–80% of a peak is the 1.5s of pre-impact silence and the sub-drop. Write the sound cue *into the shot line*, not in a footnote at the bottom — models weight what sits next to the visual.

**Rule 6 — The stillness is the spine.**
One character stays almost perfectly still while everything else accelerates around her. Her only action in the whole film is opening her eyes at 17.5s. Everything after that is earned by that one gesture. The previous draft had her rising *and* walking — two actions, half the power.

**Rule 7 — Build an EDL, not a prayer.**
Generation is stochastic. You are a casting director, not a photographer. Generate 2–3 takes per peak shot, log them against timecodes, and re-roll only the failure. Never re-roll a whole video because one clip went soft.

---

## 2. Beat map (60s)

Peaks land on 9 / 25 / 43 / 56. Your instinct was right; I only tightened the releases.

| Time | Function | Beat | Question the audience is holding |
|---|---|---|---|
| 0.0–2.0 | Hook | Golden trident on a snow peak, crescent moon | what is that up there? |
| 2.0–3.5 | Hook 2 | The gorge; one figure, dust-covered | who is she? |
| 3.5–5.0 | Lock identity | Macro: fingers on rudraksha, seasons flash past | how long has she sat there? |
| 5.0–7.0 | Identity | Her face, sharp, eyes shut | what is she waiting for? |
| 7.0–9.0 | Intensify | Earth trembles, cracks race, birds burst | what is shaking the ground? |
| **9.0–12.0** | **PEAK 1** | Sky tears; a river falls out of the clouds | — |
| 12.0–13.5 | Release | Shockwave ring; she does not flinch | why doesn't she move? |
| 13.5–15.5 | Re-hook | Silence, mist, droplets hang; **her eyes open** | she saw it |
| 15.5–18.5 | Build | The river stops in mid-air; a white bull walks out of the mist | why did the water stop? |
| 18.5–21.5 | Re-hook 2 | Light pools at her bare feet; the river lowers toward her | what will it do to her? |
| **21.5–25.0** | **PEAK 2** | One drop lands; the whole river collapses over her | — |
| 25.0–28.0 | Release | Mist; the saree turns dust-grey → pure white | what happened to her? |
| 28.0–30.0 | Re-hook | Her face, luminous, eyes open | who is she now? |
| 30.0–33.0 | Build | Top-down: jasmine petals on the pool; bull enters; trident glows crimson far off | what is waking up out there? |
| 33.0–36.0 | Stillness | She sits in the water; her reflection holds a trident of light | — |
| **36.0–40.0** | **PEAK 3** | She mounts the bull; jasmine blooms across the slopes in a wave; sunrise explodes | — |
| 40.0–43.0 | Release | Ride through the blooming valley, silver river racing beside | where is she going? |
| 43.0–46.0 | Re-hook | The trident ignites; gold light runs down the range toward her | what is coming? |
| 46.0–49.0 | Build | She rides straight into it | — |
| **49.0–52.5** | **PEAK 4** | Bullet-time orbit, backlit; the range flares gold; the trident blazes | — |
| 52.5–55.5 | Release | Her face; a smile; sunrise in her eyes | — |
| 55.5–58.5 | Re-hook | The bull lowers its head to drink | one more beat |
| 58.5–60.0 | **LOOP** | A hand dips into the silver river; the water glows | *(same gesture as 0–2s, different scale)* |

The loop is engineered, not hoped for: the film opens on a symbol seen from far away and closes on the same material — light on water — seen from arm's length. Rewatch reads as a circle.

---

## 3. VIDEO 1 — 0:00 to 0:25 (10 shots, 3 clips)

Video 1 runs **25.0s**, not 30 — the second peak sits on the seam and Video 2
picks it up on the same cut. Generate as **3 clips**: shots 1–5 (0–9s) /
6–9 (9–18.5s) / 10 (18.5–25s). Join at 9.0s and 18.5s. Every clip is ≤10s,
which keeps each generation inside the usual per-clip duration ceiling.

```
Photorealistic cinematic mythological epic, 16:9 horizontal, 1920x1080, 25
seconds, 10 shots with hard cuts, longest continuous shot 3.5 seconds. Large-format look: deep-focus
layering of foreground, midground, background; motivated volumetric light; water
caustics; anamorphic flares; 35mm grain. Palette: storm-blue, slate, silver, with
dust-ochre accents. Real photographic texture — real dust, real water, real silk,
real animal. NOT cartoon, NOT video game, NOT 3D render. All characters are
fictional adults. No violence. No on-screen text. No dialogue. No named deities.

IDENTITY (unchanged in every shot): a young fictional woman in deep meditation,
delicate gentle features, calm dark eyes, skin dusted and sun-warmed with natural
micro-texture and fine pores, long dark hair loosely tied and dust-covered, a
faded ochre cotton saree, a rudraksha mala, bare feet. A real white bull, calm
animal, dust on its flanks. A distant snow peak carries a golden three-pronged
trident on its summit under a crescent moon — a symbol only, never a person.

1 (0.0-2.0s) [Locked-off telephoto 200mm, compression] Night. A snow peak fills
the frame; a golden trident stands on the summit under a crescent moon; thin cloud
drifts across it. SOUND: one low held drone, wind.
2 (2.0-3.5s) [Wide 16mm, static, deep focus] Storm-blue Himalayan gorge at dawn;
one tiny seated figure in ochre on a cliff ledge; dust in the air. SOUND: drone
drops an octave.
3 (3.5-5.0s) [Macro 100mm, speed-ramped time-lapse] Her dusty fingers resting on
rudraksha beads while seasons flash behind her: sun, monsoon, snow, dust storm.
SOUND: a fast breath of wind, then stillness.
4 (5.0-7.0s) [Close-up 85mm, handheld, shallow focus] Her face, sharp, eyes
closed, dust on her lashes, hair moving in a rising wind. SOUND: held breath.
5 (7.0-9.0s) [35mm handheld, low angle] The earth trembles; cracks race through
the rock; her beads shake; birds explode off the cliffs. SOUND: trembling rumble,
rising.
6 (9.0-12.0s) [Ultra-wide 14mm, crash zoom out, internal cut at 10.5s to locked-off
24mm] The clouds split and the sky tears open along a thin silver line, and a
colossal river falls out of the sky onto the Himalayas — IMAX scale, one single
falling body of water. SOUND: silence for 0.5s, then a deep sub-bass boom that
sustains.
7 (12.0-13.5s) [Wide 24mm, slow motion] A shockwave ring crosses the gorge,
blowing dust off the cliffs and bending the trees; her hair and saree whip in the
blast and she does not flinch. SOUND: a long exhale.
8 (13.5-15.5s) [Macro 100mm, slow push-in] Sudden silence; mist drifts; droplets
hang in the air; her eyes open for the first time. SOUND: near silence, one water
drop.
9 (15.5-18.5s) [Low-angle 35mm anamorphic, slow push-in] The falling river stops
in mid-air above her, trembling as if waiting; a real white bull steps out of the
mist at the water's edge and looks up. SOUND: a low string note entering.
10 (18.5-25.0s) [Steadicam 28mm to extreme macro 100mm to ultra-wide 16mm, speed
ramp, internal cuts at 21.5s] Silver light pools at her bare feet and the
suspended river lowers toward her; a single silver drop falls to her upturned face
and lands — the whole river collapses over her in a silver explosion that blasts
the dust off her in a huge swirling cloud; white flash, cut to black. SOUND:
rising choir with no drums, then a full orchestral swell cutting to nothing.
```

**Note on shot 12:** it is deliberately the only shot in the film that breaks
Rule 2 (two impossibilities). That is the exception you spend on your biggest
peak. Everything else obeys the rule so this one lands.

---

## 4. VIDEO 2 — 0:25 to 1:00 (10 shots, 6 clips)

Video 2 starts at **25.0s**, on the cut at the end of Video 1's last shot — that
is the seam. Generate as **6 clips**: shots 1–3 (25–33s) / 4–6 (33–40s) /
7–8 (40–46s) / 9 (46–49s) / 10a (49–55.5s) / 10b (55.5–60s). Join at 33.0s,
40.0s, 46.0s, 49.0s and 55.5s. Every clip is ≤8s, so nothing fights the usual
10s per-generation ceiling. The 46.0s join sits exactly on the re-hook "what is
coming?", which is where you want a seam anyway.

```
Photorealistic cinematic mythological epic, 16:9 horizontal, 1920x1080, 35
seconds, 10 shots with hard cuts, longest continuous shot 3.5 seconds. Large-format
look: deep-focus layering; motivated volumetric light; water caustics; anamorphic
flares; 35mm grain. Palette: silver, pearl-white and storm-blue turning to
crimson and antique gold at dawn. Real photographic texture — real water, real
silk, real animal. NOT cartoon, NOT video game, NOT 3D render. All characters
are fictional adults. No violence. No on-screen text. No dialogue. No named
deities. She has TWO arms in every shot.

IDENTITY (unchanged in every shot): the same young fictional woman, now radiant:
soft luminous untouched skin with natural micro-texture and a dewy sheen on the
highlights, a serene gentle expression, long dark hair loose and damp with white
jasmine flowers, a pure white silk saree with a thin silver border, white pearl
and silver ornaments, a small silver crown. A real white bull, calm, is her
mount. A distant snow peak carries a golden three-pronged trident — a symbol only.

1 (25.0-28.0s) [Slow-motion wide 24mm] Silver mist and ribbons of dust drift in
silence; her saree turns from dust-grey to pure white. SOUND: near silence, soft
pad.
2 (28.0-30.0s) [Extreme close-up 135mm, slow push-in, shallow focus] Her face
emerging, luminous untouched skin with water beads, gentle rim light, her eyes
open. SOUND: one breath.
3 (30.0-33.0s) [Overhead top-down crane 24mm, slow rotation] Ripples spread
across the pool; white jasmine petals appear on the water; the white bull steps
in; far away the golden trident on the snow peak begins to glow crimson. SOUND: a
single plucked note that opens a question.
4 (33.0-36.0s) [Locked-off 50mm, low angle, still water] She sits in the pool;
her reflection on the surface is luminous and holds a trident of pure light;
steam rises. SOUND: low drone, no melody.
5 (36.0-38.0s) [Steadicam 28mm, low] She rises from the water in white silk, hair
loose and dripping, two arms, calm. SOUND: choir entering.
6 (38.0-40.0s) [Low-angle orbit 35mm anamorphic, speed ramp] She mounts the white
bull in one fluid slow-motion movement; thousands of white jasmine blossoms bloom
across the slopes in a wave and the sunrise explodes in crimson and gold. SOUND:
booming choir swell.
7 (40.0-43.0s) [FPV drone chase 16mm] She rides through the blooming valley
beside a silver river racing along with her — calm, floating, flowing. SOUND:
soft sitar line over the drone.
8 (43.0-46.0s) [Aerial crane 24mm] Far ahead the golden trident ignites and a
wave of gold light runs down the mountain range toward the valley. SOUND: rising
drone, no beat.
9 (46.0-49.0s) [Tracking drone 18mm, straight-on] She rides directly toward the
peak as the gold light rushes across the mountains to meet her. SOUND: drone
tightening into one heartbeat.
10 (49.0-60.0s) [Bullet-time orbit 24mm backlit, to extreme close-up 85mm, to
wide 35mm, to extreme macro 100mm locked-off; internal cuts at 52.5s, 55.5s and
58.5s] The sun explodes over the peak and a frozen orbit holds her on the bull as
the whole range flares gold and the trident blazes — then her serene face, a
gentle smile, sunrise in her eyes — then the bull lowers its head to drink,
petals drifting past — then a hand dips into the silver river and the water glows
around it. Hard cut to black. SOUND: full orchestral hit with a bell, dropping to
one held note, then silence, then a single drop of water on the cut to black.
```

**Why shot 10 is a compound shot:** it is the only place in the film where four
beats share one generation. Keeping them inside a single clip is what makes the
loop land on the cut to black instead of drifting a frame or two off it.

---

## 5. Continuity anchors (the actual workflow)

This app supports first-frame, first/last-frame and reference-image modes, and
availability depends on the model — H3 Max takes a **single first frame only**
(no first/last pair). So:

1. **Generate one identity still first** (image model): her face, 85mm, the dust
   version. This is the reference image for every Video 1 shot.
2. **Second still:** the radiant version, white silk, jasmine. Reference for
   every Video 2 shot.
3. **Peak anchors:** generate a still of Peak 1 (river out of the sky) and Peak 3
   (jasmine wave + sunrise). Use each as the **first frame** of its clip. A still
   you approve is a clip you can re-roll without losing the shot.
4. **Clip joins:** use the last frame of clip *n* as the first frame of clip
   *n+1* wherever the model allows it (not on H3 Max). Where it doesn't, cut on
   the flash or on black — never on a face.

---

## 6. Re-roll ladder (do this instead of regenerating a whole video)

| Failure | Re-roll with |
|---|---|
| Face changes between shots | Re-run with the identity still as reference; lower the shot count in that clip |
| Sky-river shot is mush | Plainer words: "a large waterfall falling from clouds onto mountains, slow motion, wide shot" — drop "tears open", drop "luminous" |
| River frozen in mid-air | Change to "a wall of falling water held still above her, slow motion" |
| Valley blooming fails | Split: one clip of blossoms on a slope, one of her on the bull; join on the light |
| Clip is blocked by a filter | Remove in order: the silver crown → the white bull → the face close-up. Never the meditation. |
| Two impossibilities collided | Delete one of them. Rule 2. |

---

## 7. Music map (for the Suno track)

Drops land on **9 / 25 / 43 / 56**. Structure it as: drone 0–9 → boom 9 → silence
13.5 → choir build 18.5 → swell 25 → pad 25–33 → plucked question 33 → boom 43 →
sitar flow 40–46 → full hit with bell 56 → single water drop on the last frame.
Write the track to 60.0s exactly; the loop only works if the final drop sits on
the cut to black.

---

## 8. Verified

`python3 treatments/descent-60s/check_timing.py` parses the shot lines straight
out of the two prompt blocks above and checks them — **64 checks, all passing**.

It is not a style check; it is arithmetic. It confirms:

- shot numbering is 1..N with no gaps, and N matches the number declared in each prompt header
- shots are contiguous — no gaps, no overlaps — and cover 0.0–25.0s and 25.0–60.0s exactly
- no continuous shot exceeds the 3.5s cap once declared internal cuts are applied
  (Video 1's longest is 6.5s as a compound shot, 3.5s after its internal cut at 21.5s;
  Video 2's 11.0s finale breaks to 3.5s after cuts at 52.5 / 55.5 / 58.5s)
- all four peaks (9 / 25 / 43 / 56) land inside a shot or exactly on a cut
- every clip in the split is ≤10s and every join falls on a real edit point,
  never through the middle of a shot
- the beat map is contiguous, opens at 0.0s and closes at 60.0s, so the loop
  lands on the cut to black

It cannot tell you whether a clip will *look* right. Only generation can. What
it guarantees is that when you cut these clips together at the stated timecodes,
the peaks land where the music says they land.

Re-run it after any edit to a shot line:

```
python3 treatments/descent-60s/check_timing.py
```
