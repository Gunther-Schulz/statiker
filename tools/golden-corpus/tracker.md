# Run: golden-corpus
Status: bogus-status
Phase: bogus-phase
Skill: statiker 0.2.87

INTENT — synthetic corpus fixture for st-28 (golden-corpus sweep test); no real run content.

## Cycle 1

## Block: entry-form
- F10 missing brackets entirely — basis: design
- F11 [VERIFIED] properly bracketed control — basis: design

## Block: entry-near-miss
F12 [VERIFIED] no leading dash near-miss — basis: design
- F13 [VERIFIED] with leading dash control — basis: design

## Block: tag-enum
- F14 [BOGUS] tag not in the class enum — basis: design
- F15 [VERIFIED] tag in the class enum control — basis: design

## Block: scope-near-miss
- F16 [VERIFIED] Unit U1 wrong-case scope opener — basis: design
- F17 [VERIFIED] unit U1 correct-case scope opener — basis: design

## Block: hold-form
- F18 [VERIFIED] unit U1 held: something bad — basis: design
- F19 [AUTO-ACCEPTED] unit U1 held: something bad — basis: design

## Block: write-set-near-miss + declarator-bookkeeping
- F30 [VERIFIED] unit U2 write-set a.txt — basis: design
- F30 [VERIFIED] unit U2 write-set: a.txt — basis: design
- F30 [VERIFIED] record: corrects line 31 — basis: y
- F31 [VERIFIED] unit U3 write-set: b.txt — basis: design
- F32 [VERIFIED] unit U4 write-set a.txt — basis: design
- F32 [VERIFIED] unit U4 write-set: a.txt — basis: design
- F32 [VERIFIED] unit U4 write-set: a.txt (corrects line 35) — basis: design

## Block: write-set-path-near-miss
- F40 [VERIFIED] unit U5 write-set: a.txt b.txt — basis: design
- F41 [VERIFIED] unit U6 write-set: a.txt — basis: design

## Block: basis-missing
- F50 [VERIFIED] no basis clause here at all
- F51 [VERIFIED] has a basis clause control — basis: design

## Block: corrects-token-out-of-body
- F60 [VERIFIED] some finding — basis: corrects line 5 additional
- F61 [VERIFIED] some finding — basis: design, see analysis

## Block: superseded-block-form
> stray quote line outside any Superseded block
> Superseded — F1 restated below
> the original superseded text, properly opened
>
(resumed prose after the block)

## Block: landing-indent + landing-blank
unit U20 landed: sha1111111111111111111111111111111111111a
some prose line right before an indented landing
  unit U21 landed: sha2222222222222222222222222222222222b

  unit U22 landed: sha3333333333333333333333333333333333c

## Block: landing-missing
- F90 [VERIFIED] unit U30 committed clean (UNIT_COMMITTED, sha deadbeef01) — basis: unit-commit
- F91 [VERIFIED] unit U31 committed clean (UNIT_COMMITTED, sha deadbeef02) — basis: unit-commit

  unit U31 landed: sha4444444444444444444444444444444444d

## Block: pending-latest
- F100 [PENDING] awaiting verification, stays latest — basis: design
- F101 [PENDING] first draft — basis: design
- F101 [VERIFIED] confirmed, no longer pending — basis: design

## Block: killerless-dead
- F110 [INVALIDATED] clause alpha dead — basis: design
- F111 [INVALIDATED] clause beta dead (F1) — basis: design

## Block: clause-unparsed
- F120 [INVALIDATED] clause gamma unresolved — basis: design
- F121 [INVALIDATED] clause delta dead (F1) — basis: design

## Block: tag-literal-in-body
- F130 [VERIFIED] mentions [VERIFIED] again in the body — basis: design
- F131 [VERIFIED] mentions verified (already defanged) in the body — basis: design

## Block: basis-cites-invalidated (B1/B2 incident rows)
- F20 [INVALIDATED] the initial claim was wrong — basis: F1
- F21 [VERIFIED] cites the invalidated claim, parenthesized — basis: (F20)
- F22 [VERIFIED] cites the invalidated claim, trailing paren — basis: prose F20)
- F23 [VERIFIED] cites the invalidated claim, trailing period — basis: prose F20.
- F24 [VERIFIED] cites the invalidated claim, code pointer form — basis: tools/x.py:40 F20
- F25 [VERIFIED] cites the invalidated claim, labeled prose form — basis: the probe: F20
- F26 [VERIFIED] cites a live id, no violation — basis: F21
- F27 [VERIFIED] cites a foreign high id under a record-name prefix — basis: docs/other-run.md F9999

## Block: foreign-id-suspect
- F140 [VERIFIED] cites a bare id past this run's own max — basis: F9999

## Block: multi-corrects-token + corrects-nothing
- F150 [VERIFIED] two bogus corrects tokens (corrects line 999999) (corrects line 999998) — basis: design
- F154 [VERIFIED] filler with no basis clause at all
- F154 [VERIFIED] record: corrects line 103 — basis: the basis-missing verdict at line 103

## Block: repair-scope-change
- D160 [COMMITED] record: bookkeeping v4 — basis: probe
- D160 [COMMITTED] unit U40 bookkeeping v4 (corrects line 107) — basis: probe
- D162 [COMMITED] record: bookkeeping v5 — basis: probe
- D162 [COMMITTED] record: bookkeeping v5 (corrects line 109) — basis: probe

## Block: repair-tag-change
- D170 [COMMITTED] Record: bookkeeping v6 — basis: probe
- D170 [INVALIDATED] record: bookkeeping v6 (corrects line 113) — basis: probe
- D172 [COMMITTED] Record: bookkeeping v7 — basis: probe
- D172 [COMMITTED] record: bookkeeping v7 (corrects line 115) — basis: probe

## Block: intent-near-miss
Intent - about to do stuff informally
INTENT: proper late-intent form

## Block: tripwire-arm-near-miss
- F160 [VERIFIED] record: tripwire armed at 2 (per operator) — basis: design
- F161 [VERIFIED] record: tripwire armed at 2 — basis: design

## Block: freeze-breach
- A1 [DISPATCHED] an earlier, resolved round — basis: brief
- A1 [ZERO-DELTA] clean return — basis: report
- F200 [VERIFIED] fine, appended after a RESOLVED round — basis: design
- A99 [DISPATCHED] the final, open round — basis: brief
- F201 [VERIFIED] appended after the open freeze — basis: design
