# Changelog

## Post-v1.5 - Rabbit Core Testnet V2.3.4 software release

- Published Rabbit Core Testnet V2.3.4 from source commit `b6fda8e6118d6ac7a6af81119120345e80081249`.
- Preserved Whitepaper v1.5 as the Liveness V3 protocol edition and preserved V2.3.0 as the historical block-77000 activation release.
- Recorded that V2.3.4 introduces no new scheduled consensus activation block.
- Documented P2P peer-retention/discovery hardening and clearer Rabbit Miner reward activity reporting.
- Preserved the existing Testnet blockchain, datadir, encrypted wallet and persistent LCQ participation state.
- Published verified Windows AMD64, Linux AMD64, macOS Intel/AMD64 and macOS Apple Silicon/ARM64 archive hashes.
- Added `docs/Testnet-V2.3.4-Software-Release.md`.

## v1.5 - Rabbit Core Testnet V2.3.0 Liveness V3

- Published Rabbit Core Testnet V2.3.0 from source commit `7128cb6db44dbecff608a54b4890a03f5e426647`.
- Scheduled LQC Liveness V3 activation at canonical block 77000.
- Added deterministic producer rotation, fallback recovery, committee participation claims and reward accounting.
- Preserved the block-73000 Fairness/Liveness transition as canonical history.
- Preserved the Testnet blockchain, datadir, encrypted wallet and persistent LCQ state.
- Recorded verified Windows and Linux artifacts and live pre-activation validation.
- Added `docs/Testnet-V2.3.0-Liveness-V3-Upgrade.md`.

## v1.4 - Rabbit Core Testnet V2.2.5 Fairness/Liveness

- Published Rabbit Core Testnet V2.2.5 from source commit `ed6fb1692392ce93886d112d84142b8aa487fceb`.
- Scheduled the Fairness/Liveness consensus activation at canonical block 73000 while preserving the block-50000 hardening and block-50500 stabilization history.
- Documented deterministic producer ordering after activation without legacy stale-jail reordering, while preserving separate committee eligibility filtering.
- Documented the deterministic transition clearing legacy `MissedTurns` / `JailedUntil` state at the activation boundary.
- Preserved persistent WorkSeats, permissionless fallback/recovery and the 70% producer / 30% committee reward model.
- Published Windows AMD64 SHA-256 `08a7cf8d79b8183cdde641fa06157b60c92329105e31965492ccc1b32031c945`.
- Published Linux AMD64 SHA-256 `f376de87e944624834ea9128018ed4ee42df7ab6e55779dfded5085aacf7ca35`.
- Updated the official Testnet genesis-file SHA-256 to `ef115b86fe0225b8fddd41d61ff9576c08960b97bd4e1e374fcfa0cee4ec7ad9`.
- Documented Rabbit Core V2.2.5 non-destructive local-state reuse and supervised node restart behavior.
- Added a dedicated V2.2.5 Fairness/Liveness upgrade record.

## v1.3 - Rabbit Core Testnet V2.2.3 stabilization

- Published Rabbit Core Testnet V2.2.3 from source commit `42ed7d943bad9143d23ae821d6d23c332b46e1b7`.
- Documented the consensus-stabilization activation at canonical block 50500 while preserving the historical block-50000 hardening record.
- Published Windows AMD64 SHA-256 `6cb9335cb412f86bfe7ff02fb01488ee231e5e9bde9788edf27f49a117719fbb`.
- Published Linux AMD64 SHA-256 `3152fca57f91d7128f01f5e143d6c0accadfead86b173129c4f20c9e378cf4e4`.
- Recorded successful in-place Windows upgrade using the existing encrypted wallet, datadir, chain history and active WorkSeat.
- Recorded canonical RPC/Explorer convergence at block 50698 with hash `0xc128c9aa7c35d631c090514e60f9db48fce7411b02ac6d66f824945363ab4606`.
- Recorded post-stabilization cadence evidence: 40-block sample, 10.22-second mean, 10-second median, 13-second maximum and no interval above 20 seconds.
- Recorded deterministic same-height fork choice and one-block reorganization observed during post-fork convergence.
- Disclosed that Rabbit-specific LQC fork activations are not currently encoded into the EIP-2124 fork ID because they are nested in `LQCConfig`; older clients can remain P2P-connected even though incompatible blocks are rejected by canonical consensus.
- Added a dedicated public stabilization report and made ForkID compatibility hardening a pre-mainnet requirement.


## v1.2 - Rabbit Core Testnet V2.2.2 hard-fork upgrade

- Published the required consensus-hardening activation at Testnet block 50000.
- Documented deterministic WorkSeat liveness and the one-second future timestamp tolerance after activation.
- Documented the in-place upgrade path preserving chain history, datadir, wallet, keystore, balances, contracts and persistent WorkSeat.
- Published the V2.2.2 source commit, Windows/Linux archive hashes and updated genesis-file checksum.
- Recorded successful existing-wallet upgrade testing and matching RPC/Explorer canonical-chain validation.
- Confirmed that the canonical block-0 hash remains unchanged and that no network reset occurs.

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
