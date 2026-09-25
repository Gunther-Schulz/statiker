# Kickoff directive — beat-the-books run: prod data-handling design (2026-09-25)

Driving desk: statiker-c2 [99f316] (this repo's meta session).
Receiver desk: beat-the-books-46 [58558e] (opus, operator-chosen), repo
`~/dev/Gunther-Schulz/beat-the-books`.
Arrangement: two-session layout, meta drives end to end (operator decision
2026-08-23); ONE first-hand operator delegation line pasted at desk start
(U2-measured requirement), all later authority lines relayed meta→desk marked
as the operator's words with date. Run is INERT until the desk acknowledges
the operator's delegation line on its record.

## Served version
Installed pin statiker 0.2.103 = reviewed 0.2.102 payload + hooks.json key
drop (f3b8325; plugin.json version bump + 1 deleted hooks line, no SKILL.md
change). Eve-of-run review floor met: 0.2.101 checkpoint review + repair lap
(bf82f4a) released as 0.2.102 (ae93661), nothing unreviewed since. Desk
confirms served version from its Skill injection's base-directory line before
the first forcing point; expected 0.2.103.

## INTENT (operator, verbatim, 2026-09-25, this session)
- "i am ready for a new trial run for beat the books. but it sthe pressing
  issue a ctually [ops disk alert]" — the alert: `/` on the prod host 95.2%
  used, threshold 92%.
- "there is a machnism behind it. the drive shodllndt get this full. there
  needs to be deciosns how to handle the data better"
- On bet_evidence retention: "1 is obvious what to do with it … we dont need
  to store these forever. i mean its a trade-off but an eay one i would say"
  — operator ground: bounded retention / not-forever is settled; the design
  (horizon, archival vs deletion, mechanism) is the run's.

## Evidence handed to the desk (gathered by this session, 2026-09-25 ~13:00–13:10 UTC, via `ssh coolify`)
- Host `/` (75G) hit 100% — 0 bytes free; all 10 containers unhealthy,
  Coolify API 500s. Emergency triage by this session restored 7.3G free
  (91%): truncated Coolify's 7.0G laravel.log, journal vacuum, apt clean.
  All health checks green again as of 13:11 UTC. Nothing of the app's data
  deleted.
- Growth mechanism 1: bet_evidence PDFs — 24G, 9,493 files, docker volume
  `egw8cgkgwokggw4kkg4kscog_app-data/_data/bet_evidence/`, per-month:
  2026-09 15G, 2026-08 8.9G, 2026-06 3.1M. Unbounded append, no retention
  mechanism exists.
- Growth mechanism 2: postgres `market_snapshots` table — 26G of the 35G
  `postgres` DB (container `ww404g8ggswocg4k08k404ww`, postgres:17-alpine).
  Next largest: performance_metrics 2G, autobet_detections 1.4G, weekly
  replay_opportunity_cache_* ~0.4G each. No retention/rollup policy.
- OUT of run scope: Coolify's own log leak (dead server entry "excited-eagle"
  server_id 2 → 127.0.0.1, stack trace per failed check, no rotation) — the
  driving desk fixes that infra-side, operator-approved.
- Headroom at September's rate: roughly two weeks. Real deadline.

## Run unit
Statiker run in the beat-the-books repo: design and implement the
data-handling mechanisms for growth mechanisms 1 and 2 (retention/archival/
rollup), verified; prod-touching destructive acts fall under the skill's own
irreversible-unit hold, cleared through the driving desk.

## Consumers of this run's field data
Softlocked statiker items awaiting "the next statiker run": st-12 (via
st-15), st-13, st-16, st-17, st-19, st-26, st-31 — their evidence predicates
key on run events (operator stall, real unit classes, V1→V2 cycle, both
forms' field data). The meta harvest watches these during relays.

## Horizon
Kickoff ack expected in minutes of the operator's paste (idle subscription
armed on the driving send; recurring artifact look at ~30 min while a cycle
runs). Silence past horizon is a finding.
