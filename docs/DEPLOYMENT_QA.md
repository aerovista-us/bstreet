# B Street Production / QA Notes

## Production

- Site: https://aerovista-us.github.io/bstreet/
- Source branch: `main`
- Canonical knowledge base: `AV_1011_N_B_ST_HOMEOWNER_EXIT_POWERHOUSE_MASTER_COMPLETE_2026-09-15.html`
- Production entry point: `index.html`
- Base builder: `scripts/build_index.py`
- Production enhancement layer: `scripts/enhance_index.py`

The production site is built from the MASTER COMPLETE Powerhouse, then enhanced with the owner dashboard, paid-frontage lane, negotiation assistant, print-document controls, global search, focus mode, mobile controls, and navigation helpers. No iframe/app-within-app architecture is used.

## Required build QA

The GitHub Action must fail if any of these are false:

- 23 owner-facing sections render.
- No iframe exists.
- Paid Frontage Packet exists as a first-class section.
- Global search exists.
- Section/document printing exists.
- No `sandbox:/` links are present.
- No broken `documents/` links are generated.
- Production includes `noindex` metadata.

## Public-site caution

The repository and Pages site are public. `robots.txt` plus `noindex,nofollow,noarchive,nosnippet` reduce search-engine discovery, but they are not authentication or access control. Anyone with the direct URL can view owner-side strategy material.

## Transaction-document rule

The site can print the complete gift, same-day active-sale, paid-frontage, and negotiation sections directly. The surveyor/title/Idaho counsel still control the final survey legal description, lender release, recording sequence, and final deed form.
