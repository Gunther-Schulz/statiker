# Raw evidence — Grok Bot public-surface findings (sonnet lane, 2026-09-13)
Provenance: sonnet-grokbot-surface lane, statiker desk 1b204567. The lane's headline: the public web surface is self-contradictory and content-farm contaminated; primary reads listed inside.

# Grokbot public-surface research — findings

Headline: the public web surface for this topic is self-contradictory to the
point that no confident account can be built from it. Multiple
purportedly-independent primary-looking sources disagree on the most basic
fact — who makes the product — and one search result asserts "Cursor
acquired by SpaceX," which is not a real corporate event. Flagging this as
likely low-quality/fabricated content contamination rather than reporting it
as fact.

## 0. Name correction
Likely real name: "Grok Bot" (two words), not "Grokbot" — used consistently
on cursor.com. Could NOT confirm it is a Cursor/Anysphere product. Evidence
conflicts:
- cursor.com/docs/grok-bot (WebFetch read): "Grok Bot is made by Cursor (the
  company behind the Cursor code editor)... no connection to SpaceX/xAI's
  Grok chatbot mentioned in this documentation."
- x.ai/news/grok-bot-more-plans (WebFetch read): "Grok Bot was developed by
  SpaceXAI LLC, as indicated by the copyright notice and branding," bundled
  into Cursor plans as "its own usage, separate from your Grok and Cursor
  plans."
These two fetches of what should be primary pages contradict each other on
authorship. A third secondary source (Ultrathink) states "a collaboration
between Cursor (which SpaceX reportedly acquired) and xAI" — the "acquired
by SpaceX" claim reads as fabricated. Treat "Grokbot = a Cursor/Anysphere
product" as UNVERIFIED, possibly wrong — may instead be xAI's product
bundled into Cursor via subscription-linking (SuperGrok), or something else.

## 1. What it is, in the product's own words
cursor.com/docs/grok-bot (quoted via WebFetch page read):
"Grok Bot gives you Bots you can keep around: AI teammates with names, jobs,
and context that compounds over time." Each Bot "works on a persistent
cloud computer with a browser, filesystem, and terminal, so tasks finish in
your real tools instead of as chat drafts." This does not closely match the
brief's description (multi-agent orchestration with individual agent
identities the user orchestrates) — see §3 for the product that does.

## 2. Workflow shape
Same source: "You work with a Bot by messaging it. Give it a task, the
relevant context, and access to the tools it needs. It takes on multi-step
work across apps and websites, keeps you updated in the conversation, and
comes back when something needs your approval." Only public statement found
on human review/approval — per-task, ad hoc, not described as a merge/CI
gate.

## 3. Constraint/verification layer, "Dune" architecture
Could NOT independently confirm. The x.com/poteto tweet the brief cites
(status/2087244771849089270: "because of Dune, my agents now merge their
own PRs... I do code review now by looking at what they landed on main")
was UNREADABLE directly — x.com returned HTTP 402, an r.jina.ai proxy
attempt returned 403. Everything on "Dune" comes from WebSearch's own
AI-generated synthesis of secondary/tertiary blogspam (theneuron.ai,
aiidelist.com, daily.dev, leslieli.dev), not a page read directly — fails
the "prefer raw pages, quote what you cite" instruction, not presenting it
as verified.

One thing read directly: cursor.com/blog/self-driving-codebases, a genuine
Cursor engineering post describing a real multi-agent architecture (root
planner -> subplanners -> independent workers, handoff-based, "~1,000
commits per hour across 10M tool calls" on one VM) — the fetch explicitly
noted "No mention of 'Dune architecture' appears in this document." The one
primary Cursor engineering post read about large-scale multi-agent
orchestration does not use "Dune" at all.

cursor.com/blog/2-0 (Cursor 2.0 + Composer launch, genuine) describes
parallel agents via git worktrees/remote machines, an agent-centric UI, and
easier diff review — also no mention of "Grokbot" or "Dune."

## 4. Pricing/availability/positioning
Grok Bot (whoever builds it) is "included with every paid individual
Cursor plan and with the Cursor Teams plan," with an alternative path of
linking a SuperGrok/SuperGrok Plus/SuperGrok Heavy/X Premium+ subscription —
positioned as always-on "AI teammates" for people who want to hand off
"anything from a project to an entire function," aimed at individual power
users and teams, not an enterprise-only tier.

## 5. Explicit boundary — what can't be established from the public surface
- Whether "Grokbot"/"Grok Bot" is a Cursor (Anysphere) product, an xAI
  (SpaceXAI) product integrated into Cursor, or something else — direct
  fetches of what present as primary pages contradict each other.
- Whether "Dune" is Cursor's own architecture/product at all, versus Lauren
  Tan's personal internal tooling (pstack/poteto-mode plugin) she built for
  herself and uses to drive whatever cloud-agent backend she has access to —
  no primary source (her tweet, a Cursor blog post) using the word "Dune"
  could be read directly.
- pstack (Lauren Tan's open-sourced skills/playbooks plugin, real GitHub
  repo, 7.6k stars per fetch of github.com/cursor/plugins) is a plugin of
  prompts/skills, not an orchestration engine — nothing ties it to
  "Grokbot" or "Dune" as the same thing.
- General reliability: the search corpus for this exact topic is unusually
  thick with what reads as AI-generated content-farm churn (explainx.ai,
  mem0.ai/blog, callmissed.com, aiidelist.com, blog.mean.ceo, digg.com
  aggregator, kie.ai, Ultrathink) recombining real names (Lauren Tan,
  Cursor, xAI, Grok) into internally inconsistent narratives. No
  cursor.com/blog/* post found that names a product "Grokbot"/"Grok Bot" as
  its own launch, distinct from the /docs and forum pages that assume the
  reader already knows what it is.

## Sources actually read (WebFetch page reads, not just search snippets)
- cursor.com/docs/grok-bot
- cursor.com/blog/2-0
- cursor.com/blog/self-driving-codebases
- cursor.com/@lauren
- x.ai/news/grok-bot-more-plans
- github.com/cursor/plugins
Unreadable: x.com/poteto/status/2087244771849089270 (HTTP 402 direct,
HTTP 403 via r.jina.ai proxy)

Caveat on fidelity: no raw HTML access, only WebFetch's small-model
summarization of each fetched page — noted because WebFetch's own summaries
contradicted each other once (§0).
