# B Street — 1011 N B St Owner Exit Powerhouse

AeroVista research workspace for the owner of **1011 N B St, Coeur d’Alene, Idaho (APN C3510003001A)**.

## Site model

This project is now **one owner-facing site built directly from the Powerhouse**.

- [`index.html`](index.html) is the canonical top-level site and the file intended to be served as the root page.
- The original image-rich [`AV_1011_N_B_ST_HOMEOWNER_EXIT_POWERHOUSE_MASTER_COMPLETE_2026-09-15.html`](AV_1011_N_B_ST_HOMEOWNER_EXIT_POWERHOUSE_MASTER_COMPLETE_2026-09-15.html) remains the source/archive Powerhouse.
- The root site does **not** embed one app inside another. Instead, the command-center material is folded into the existing Powerhouse sections wherever those topics already exist.
- New presentation-only material, such as the Bytecast player, is added inside the existing Owner Dashboard because there was no equivalent section to enhance.
- Supporting `/docs` files remain the source-controlled research and execution record.

## What was folded into the Powerhouse

The existing **Start Here** section is now the **Owner Dashboard** and carries the current mission, planning stage, property/frontage/debt metrics, four-step decision sequence, quick actions, and Bytecast briefing.

Overlapping command-center content was merged into the existing sections rather than duplicated:

- **1007 Said YES** — same-day capture / active-sale action path.
- **First-Time Owner Playbook** — first-week execution sequence.
- **House First vs Lot First** — money-strategy context.
- **Document Kit** — correct document order and deed timing.
- **12-Month Roadmap** — current stage and next gate.
- **My Chosen Path** — proof-project framing.
- **Who Does What** — homeowner / AeroVista / licensed-professional role boundaries.

## Bytecast briefing

The Owner Dashboard contains four browser-narrated chapters with transcripts:

1. **The 1011 big picture**
2. **If 1007 says yes**
3. **The money strategy**
4. **Your first week**

A produced MP3 can replace browser narration later without changing the information architecture.

## Purpose

The strategy is to prove the high-value frontage/subdivision opportunity with the least possible owner cash, then choose the exit that best eliminates the mortgage while preserving equity.

Current working path, if survey / City / title / lender work is green:

**prove the split → test selling the house-side parcel → pay off the mortgage → retain the buildable lot**.

## Important role distinction

AeroVista is a **research and strategy consultant** providing decision support, research organization, scripts, checklists and working-draft documents. AeroVista is not the homeowner's attorney, broker, lender, surveyor, title company, CPA, appraiser or City representative and does not bind either property owner.

The **1011 homeowner is the decision-maker and contracting party**.

## Build flow

`scripts/build_index.py` builds the root `index.html` from the archived MASTER COMPLETE Powerhouse. `.github/workflows/build-index.yml` runs the builder when the Powerhouse, builder, or workflow changes and commits the generated root page if needed.

This preserves a clean rule: **the Powerhouse is the source; `index.html` is the production presentation of that same Powerhouse.**

## Supporting documentation

- [`docs/MASTER_STRATEGY.md`](docs/MASTER_STRATEGY.md) — property strategy, one-foot reconstruction, R-12 logic, survey mission, City questions, value stages and stop/go gates.
- [`docs/1007_YES_PATH.md`](docs/1007_YES_PATH.md) — exactly what to do the day 1007 says yes.
- [`docs/ACTIVE_SALE_PROTECTION.md`](docs/ACTIVE_SALE_PROTECTION.md) — how to protect cooperation while 1007 remains listed and how buyer assumption fits.
- [`docs/FIRST_TIME_OWNER_STEPS.md`](docs/FIRST_TIME_OWNER_STEPS.md) — step-by-step execution guide for a homeowner doing this for the first time.
- [`docs/PAID_FALLBACK.md`](docs/PAID_FALLBACK.md) — negotiation path if the gift is declined, including authority limits and scripts.
- [`docs/SOURCE_REGISTER.md`](docs/SOURCE_REGISTER.md) — official-source map and unresolved diligence checklist.
- [`docs/BYTECAST_OWNER_BRIEFING.md`](docs/BYTECAST_OWNER_BRIEFING.md) — audio briefing source copy.

## Professional gates

Do not rely on a future two-lot sale until a licensed survey, title review and written City direction support the geometry. Use Idaho counsel/title to finalize binding neighbor documents and the deed; use the mortgage servicer for release/recast/payoff rules; use a CPA for tax sequencing.
