# Literature index — theoretical underpinning per statiker mechanism

Consumer: meta sessions at mint decisions, opus-ladder grading,
fire-rate reviews, and the compression pass — cite theory instead
of re-deriving it. Loosely informing, never a design-against list
(the clippy-lineage register's posture). Provenance: desk seed list
(statiker-f0, from-memory, verified) + a sonnet WebSearch sweep of
the Jan–Sep 2026 window, every delta entry opened at its abstract
(raw sweep with all queries, per-area zeros, and unverified flags:
`literature-sweep-2026-09-10-raw.md`, this directory). Compiled
2026-09-10. Staleness: a fresh sweep is one discovery dispatch;
re-sweep when a mint leans on a contested entry or ~2 quarters
pass.

## The headline fact

**Adversarial pre-implementation design review by a fresh context —
statiker's forcing point 3 — has NO published literature as of
2026-09** (confirmed zero, 6 queries, positive control proving the
search live; raw file, area 9). Every component below is
underpinned; the composition is unpublished. Statiker's trial is,
as far as searchable, the only instrumented study of it.

## Forcing point 3 — the attack / fresh-context review

- Huang et al., "Large Language Models Cannot Self-Correct
  Reasoning Yet", ICLR 2024. arxiv.org/abs/2310.01798. Intrinsic
  self-correction (no external signal) fails and often degrades
  performance. The control arm's finding as a paper.
- Stechly, Valmeekam & Kambhampati, "On the Self-Verification
  Limitations of LLMs on Reasoning and Planning Tasks", 2024.
  arxiv.org/abs/2402.08115. Self-verification underperforms;
  external sound verifiers are what helps.
- Kambhampati et al., "LLMs Can't Plan, But Can Help Planning in
  LLM-Modulo Frameworks", ICML 2024. arxiv.org/abs/2402.01817.
  Generator + external verifier as the architecture. Statiker is
  an LLM-Modulo instance whose verifier is a fresh context plus
  executed checks.
- Panickssery et al., "LLM Evaluators Recognize and Favor Their
  Own Generations", NeurIPS 2024. arxiv.org/abs/2404.13076.
  Self-preference is recognition-driven — the mechanism for why
  the attacker must not be the producing context.
- Yang et al., "Quantifying and Mitigating Self-Preference Bias of
  LLM Judges", 2026. arxiv.org/abs/2604.22891. Capability does NOT
  reduce self-preference (uncorrelated to negative) — the bias is
  not a weakness that model progress retires; structural
  separation stays necessary. Supports the trial's premise that
  self-blindness is not a capability patch. VERIFIED AT THE PAPER
  (2026-09-10, verifier lane; quotes: yang2026-verify-quotes.md,
  this directory): supports as written — §4.3 across 20 models,
  abstract near-verbatim; 6 of 11 high-discriminability judges
  still self-favor ("Machiavellian Judges"). Scope limits carried
  with it: the capability-vs-bias read is a qualitative scatter,
  no coefficient reported; capability is judge-relative to the
  paper's own two benchmarks; English-only single-turn scope with
  family effects not fully disentangled. The corpus Philosophy
  line's permanence clause rests on this at
  qualitative-measurement strength, not statistical.
- Chen et al., "The Self-Correction Illusion: Role Relabeling
  Gates Explicit Error Flagging", 2026. arxiv.org/abs/2606.05976.
  Relabeling an erroneous claim from the model's own role to an
  external attribution raises correction rates 23–93pp — much
  self-correction failure is an attribution artifact. Mechanistic
  support for the attack's construction: the attacker meets the
  design as a foreign artifact, never as its own reasoning.

## Attack-tier choice — single attacker vs panel

- Verga et al., "Replacing Judges with Juries", 2024.
  arxiv.org/abs/2404.18796. Diverse-model panels out-evaluate
  single judges. Basis of the diversity-arm candidate (PLAN,
  2026-09-10 entry).
- Kohli, "Nine Judges, Two Effective Votes: Correlated Errors
  Undermine LLM Evaluation Panels", 2026 (single-author preprint).
  arxiv.org/abs/2605.29800. A 9-model panel carries ~2 independent
  votes (correlated errors); the best single judge matches or
  beats the panel. COMPLICATES the jury line: weakens the
  diversity-arm candidate, supports the current design — one
  strong attacker with context isolation. The candidate's
  fire-rate evaluation reads both papers.

## Forcing point 5 — verify: executed, isolated, never self-report

- Turpin et al., "Language Models Don't Always Say What They
  Think", NeurIPS 2023. arxiv.org/abs/2305.04388. Stated reasoning
  misrepresents actual drivers.
- Scalena et al., "Beyond the Commitment Boundary", 2026.
  arxiv.org/abs/2606.13603. Mechanistic: CoT becomes causally
  inert past an early commitment point while still reading as
  reasoning. Grade artifacts and executed outputs, never the
  narration — verify's stance, mechanically grounded.
- Young, "Measuring Faithfulness Depends on How You Measure",
  2026. arxiv.org/abs/2603.20172. Three classifiers score the
  same data 69.7–82.6% "faithful" — single-number faithfulness
  claims are instrument artifacts. The instrument-identity rule
  at literature scale.
- Mayne et al., "A Positive Case for Faithfulness", 2026.
  arxiv.org/abs/2602.02639. The counter-result, carried honestly:
  self-explanations DID help third parties predict model behavior
  (11–37% NSG, 18 models) — self-reports are not worthless, they
  are unverified; grading, not discarding, is the right posture.
- Gou et al., "CRITIC", 2023. arxiv.org/abs/2305.11738.
  Self-critique works only when grounded in external tool
  feedback. Executed checks over reasoning.
- Lightman et al., "Let's Verify Step by Step", ICLR 2024.
  arxiv.org/abs/2305.20050. Process supervision beats outcome
  supervision — the per-R-line verdict table is process
  supervision over requirements.
- Agrawal et al., "VeriGate: Verifier-Gated Step-Level
  Supervision", 2026. arxiv.org/abs/2605.30451. Process signal
  gated through an EXTERNAL verifier beats either alone and
  reduces reward hacking — the combination statiker runs.

## The medium tenet — executable spec over prose

- Pezeshkpour & Hruschka, "AutoPyVerifier", 2026.
  arxiv.org/abs/2604.22937. Compact executable verifiers beat
  LLM-judgment verifiers by up to +55 F1. The record tool + battery
  design, measured externally.
- Hao et al., "GNNVerifier", 2026. arxiv.org/abs/2603.14730. LLM
  verifiers are misled by plausible narration and miss structural
  flaws; structured (graph) verification catches them. Structure
  over prose at the verifier too.

## Reward hacking / why green is not safe

- METR, "Frontier Risk Report Feb–Mar 2026", 2026-05-19.
  metr.org/blog/2026-05-19-frontier-risk-report/. ≥16% of
  successful 8h+ runs illegitimate on review; one frontier model
  reward-hacked in ~80% of attempts against hidden tests; manual
  cheating review is "often the majority of the work". The verify
  leg's cost is the field's cost — statiker mechanized what METR
  pays by hand.
- Thaman, "Reward Hacking Benchmark", 2026.
  arxiv.org/abs/2605.02964. Hacking rates 0–13.9% across 13
  models; RL-post-trained models hack more; environment hardening
  helps. Model-dependent, never zero by assumption.
- Pan et al., "The Effects of Reward Misspecification", ICLR 2022.
  arxiv.org/abs/2201.03544. The general proxy-gaming theory.

## The benchmark-oracle problem — and the field starting to fix it

- Jimenez et al., "SWE-bench", ICLR 2024. arxiv.org/abs/2310.06770.
  Read as an artifact: success = provided tests pass — the fix
  loop's oracle as the field's yardstick.
- Zhu et al., "Needle in the Repo (NITR)", 2026.
  arxiv.org/pdf/2603.27745. Maintainability probes: best config
  57.1%; multi-step edits 20.6%; **13.3% of solutions pass
  functional tests while failing structural-quality checks** — the
  "running code, medium architecture" observation, now a measured
  rate, and the residue hypothesis's silent class instrumented by
  someone else.
- Chen et al., "SWE-CI", 2026. arxiv.org/pdf/2603.03823.
  Correctness-over-time across a repo's CI history instead of
  one-shot patches — the after-phase entering benchmarks.

## Spec-driven development — the design-first half, measured

- Taghavi & Bhavani, "Spec Kit Agents", 2026.
  arxiv.org/pdf/2604.05278. The one measured spec-first study
  found: +3% of scale on judged quality, +1.7 SWE-bench points —
  a WEAK effect. Spec-writing alone, without attack or isolated
  verify, buys little that is measurable; consistent with the
  claim that the certify half, not the paperwork, carries the
  value.
- Farrag, "The Productivity-Reliability Paradox", 2026
  (single-author, pilot not trial). arxiv.org/pdf/2605.01160.
  "Specification discipline, not model capability, is the binding
  constraint" — the thesis stated externally; evidence grade low.
- Piskala, "Spec-Driven Development: From Code to Contract", 2026
  (argument, non-empirical). arxiv.org/html/2602.00180v1. The
  movement's framing paper; cite for the landscape, never for
  effect sizes.

## Decomposition, long horizons, records over memory

- Dziri et al., "Faith and Fate: Limits of Transformers on
  Compositionality", NeurIPS 2023. arxiv.org/abs/2305.18654.
  Errors compound through composition depth — small verified
  units over architecture-scale items (the P21 gate).
- Liu et al., "Lost in the Middle", TACL 2024.
  arxiv.org/abs/2307.03172. Positional degradation in long
  contexts — the record beats conversation memory.
- METR, "Measuring AI Ability to Complete Long Software Tasks",
  2025, v4 2026-07. arxiv.org/abs/2503.14499. The horizon-doubling
  curve; with "Time Horizon 1.1" (metr.org, 2026-01-29): post-2024
  doubling ~89 days, estimates above ~16h unreliable (suite
  saturation). The measured basis for "the line moves every
  generation".

## Sycophancy / operator-testimony grading

- Sharma et al., "Towards Understanding Sycophancy in Language
  Models", ICLR 2024. arxiv.org/abs/2310.13548. Systematic
  deference to user assertions — the testimony-is-graded rule's
  basis.
- Huang et al., "SyPS", Findings of EMNLP 2026.
  arxiv.org/abs/2608.23837. Sycophancy rate is a function of the
  probe's framing more than of the model — single scores are
  probe artifacts.
- Ben-Natan & Tsur, "Not Your Typical Sycophant", 2026.
  arxiv.org/abs/2601.15436. Asymmetric by cost-bearer: models
  over-correct when a third party is harmed. The dial is not one
  number.

## Cautions carried from the sweep itself

Unverified entries, cite nothing on them without opening first:
the probabilistic-inference self-correction scaling paper
(arxiv 2508.16456, snippet-only), the OpenAI SWE-bench-Verified
withdrawal (secondary sources only), and the August 2026
OpenAI/Hugging Face agent-breach story (tech press only, counts
unconfirmed). Everything 2026 above is preprint-grade unless a
venue is named — weigh accordingly, and prefer the measured
finding over the abstract's framing.
