# Changelog

All material changes to the Rabbit Chain whitepaper and its machine-readable disclosures are recorded here.

## [0.9-r1] - 2026-08-29

- Clarifies that allocation contracts are not deployed in genesis.
- Defines genesis funding of precomputed contract addresses and deterministic deployment in the first mainnet blocks.
- Adds address-derivation, bytecode, balance, authority, deployment-window, and verification requirements.
- Extends the machine-readable registry and mainnet readiness gate.
- Reworks and resizes diagrams for clear GitHub and PDF rendering.

## [0.9] - 2026-08-29

Pre-testnet technical edition.

- Documents LCQ, Work V1, RandomX admission, WorkSeats, deterministic production, fallback, and recovery.
- Records the validated same-wallet multi-process gate and evidence hashes.
- Fixes the maximum allocation at 15,000,000 RAB.
- Separates the former 500,000 RAB operations allocation into 400,000 RAB operations and 100,000 RAB public-testnet participation rewards.
- Adds contract, vesting, treasury, reward-vault, reporting, and reconciliation transparency requirements.
- Adds stable planned official endpoint names, each explicitly inactive until deployed and verified.
- Adds diagrams for mining, LCQ liveness, and allocation transparency.

## Versioning policy

- `0.x`: pre-mainnet editions. Undeployed addresses and launch evidence may remain unresolved when clearly identified.
- `1.0`: mainnet edition. All required contract addresses, genesis hashes, release hashes, endpoints, multisigs, timelocks, and registry entries must be final and verifiable.
- Patch releases correct wording, links, formatting, or evidence without changing protocol claims.
- Minor releases add or materially revise documented behavior before mainnet.
