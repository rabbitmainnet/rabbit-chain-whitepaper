# Changelog

## v1.0 - Public Testnet V2

- Published the verified Testnet V2 network identity, endpoints, bootnodes, genesis and release commit.
- Replaced Work V1 and epoch-scoped seats with Work V2 one-time admission and persistent equal seats.
- Documented blocks 128/256, miner states, 70/30 rewards and two-minute permissionless recovery.
- Aligned participation, validation evidence, security limitations, FAQ and glossary with the released implementation.

## v0.9-r4 - Repository-wide consistency correction

- Regenerated the allocation PNG so it no longer claims a fixed or maximum 15,000,000 RAB supply.
- Synchronized the machine-readable economic document version with the whitepaper version.
- Defined the 10,000,000 RAB staking/participation amount as a genesis reserve separate from consensus block-reward issuance.
- Required public custody, balance, release, authorization, and spending evidence for that reserve before mainnet.
- Clarified the activation formula and the release requirement to publish registration block, activation delay, and earliest activation block.
- Regenerated and visually verified the complete PDF.

## v0.9-r3 - Monetary-policy reconciliation

- Replaced the incorrect 15,000,000 RAB maximum-supply claim with the accurate 15,000,000 RAB genesis-allocation statement.
- Published the active 8,409,600-block era calculation and the 1.20, 0.60, 0.30, and permanent 0.15 RAB reward levels.
- Disclosed that the 0.15 RAB tail reward continues without further halving, so active consensus has no finite maximum supply.
- Removed the inactive legacy first-100,000-block mining-lock claim and documented immediate canonical reward credit.
- Clarified 70% producer / 30% committee distribution and the producer's 100% result when no valid committee recipient exists.
- Regenerated the PDF with independent list numbering and updated economic tables and diagrams.

All material changes to the Rabbit Chain whitepaper and its machine-readable disclosures are recorded here.

## [0.9-r2] - 2026-08-29

- Replaces fixed-width README diagram images with native responsive Mermaid diagrams.
- Removes numbered labels and crossing annotation arrows from the PDF mining diagram.
- Keeps PNG diagrams only as PDF and downloadable source assets.

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
- Fixes the genesis allocation at 15,000,000 RAB.
- Separates the former 500,000 RAB operations allocation into 400,000 RAB operations and 100,000 RAB public-testnet participation rewards.
- Adds contract, vesting, treasury, reward-vault, reporting, and reconciliation transparency requirements.
- Adds stable planned official endpoint names, each explicitly inactive until deployed and verified.
- Adds diagrams for mining, LCQ liveness, and allocation transparency.

## Versioning policy

- `0.x`: pre-mainnet editions. Undeployed addresses and launch evidence may remain unresolved when clearly identified.
- `1.0`: mainnet edition. All required contract addresses, genesis hashes, release hashes, endpoints, multisigs, timelocks, and registry entries must be final and verifiable.
- Patch releases correct wording, links, formatting, or evidence without changing protocol claims.
- Minor releases add or materially revise documented behavior before mainnet.
