# Contributing to the Rabbit Chain whitepaper

Corrections and reproducible evidence are welcome.

## Reporting a documentation issue

Open an issue containing:

1. the exact section, table, field, diagram, or file;
2. the current statement;
3. the proposed correction;
4. a primary source, source-code line, genesis/configuration field, transaction, block, or reproducible test that supports the correction;
5. whether the issue affects safety, economics, compatibility, or only presentation.

Do not post private keys, seed phrases, passwords, personal data, or an unpatched exploitable vulnerability in a public issue. Security-sensitive reports should follow `SECURITY.md`.

## Pull requests

- Keep factual claims tied to a versioned source, network, or release.
- Do not replace unresolved fields with guessed values.
- Update `CHANGELOG.md` for material changes.
- Run `python3 scripts/verify_allocation.py`.
- Run `python3 scripts/check_release_readiness.py --phase pretestnet` for ordinary pre-testnet edits.
- Before a mainnet `1.0` proposal, run `python3 scripts/check_release_readiness.py --phase mainnet` and resolve every reported field.
- Preserve prior versions and hashes; do not silently rewrite published evidence.
