# Rabbit Chain Testnet V2.2.3 Stabilization Report

**Network:** Rabbit Chain Testnet
**Chain ID / Network ID:** 9280 / 9280
**Release:** `rabbit-core-testnet-v2.2.3`
**Source commit:** `42ed7d943bad9143d23ae821d6d23c332b46e1b7`
**Consensus stabilization activation:** block 50500
**Report date:** 11 September 2026

## Purpose

This report records the public operational evidence surrounding the Rabbit Testnet V2.2.3 stabilization activation. It is intended to preserve both successful results and observed limitations rather than present the upgrade as defect-free.

## Release artifacts

| Artifact | SHA-256 |
|---|---|
| Windows AMD64 ZIP | `6cb9335cb412f86bfe7ff02fb01488ee231e5e9bde9788edf27f49a117719fbb` |
| Linux AMD64 TAR.GZ | `3152fca57f91d7128f01f5e143d6c0accadfead86b173129c4f20c9e378cf4e4` |

Genesis file SHA-256:

`ab66857a5b28da355ff270ced29176ac151e70e8281dbad8fc8d24a2192fc71b`

Canonical block-0 hash remained:

`0x9b71d7f2922fdf8383a4a12be5594e25938625195e0d84c05c3bd71b7bcf93f7`

## Upgrade-path validation

An existing Windows Rabbit Core installation was upgraded in place.

Observed behavior:

- the existing encrypted mining wallet was detected and reused;
- the existing Testnet datadir and chain history were retained;
- Rabbit Core rebuilt canonical LCQ state;
- the existing active LCQ seat was recovered;
- peer discovery and synchronization resumed automatically;
- no manual RPC, WebSocket or peer configuration was required;
- canonical LCQ production resumed after synchronization.

## Stabilization activation

The public chain crossed block 50500 successfully.

Canonical hashes observed around activation:

| Block | Canonical hash |
|---:|---|
| 50499 | `0x2d77980f6be4ea5ca895f1b38838d332e99c0c76ee11b15b0006212197774f5a` |
| 50500 | `0xc2da9c398c55929ed5dca94c09a60b0975991bb139a5f53f66152c7fb0173f10` |
| 50501 | `0x7441de96fee62d76bac60840cdeab58971953c10df19a36939b2c085ffc74170` |
| 50502 | `0x14372df5142f480c56af96622a0c40f9da8ef0ddbe8f8264b4e2bf789dfe0e96` |
| 50503 | `0xd160f9e9a86944d5671d433306b7dfe407f1358715b360c5b07e1e3ada885af8` |

## RPC / Explorer convergence

The official RPC and Explorer node were independently queried at canonical block 50698.

Both reported:

`0xc128c9aa7c35d631c090514e60f9db48fce7411b02ac6d66f824945363ab4606`

At that checkpoint both nodes reported head 50698. No recent `BAD BLOCK`, registry-root mismatch, invalid-block, future-block, panic or fatal event was found in the Explorer node's final 15-minute audit window.

## Block cadence

Immediately after the activation sequence, two 120-second intervals were observed around blocks 50561 and 50562 while competing same-height blocks and fork recovery were being resolved.

The node subsequently stabilized.

A later 40-block post-fork sample reported:

- mean interval: **10.22 seconds**;
- median interval: **10 seconds**;
- maximum interval: **13 seconds**;
- intervals above 20 seconds: **0**;
- intervals above 30 seconds: **0**;
- intervals above 60 seconds: **0**.

The protocol target remains 10 seconds. Individual blocks are not guaranteed to arrive at exactly the target interval.

## Deterministic fork recovery observation

At block 50562, multiple same-height candidates were observed. V2.2.3 applied deterministic fork choice, performed a one-block reorganization and converged on the canonical block subsequently shared by the network.

This is operational evidence that the same-height recovery path executed in a live mixed-peer environment. It is not a formal proof that every possible fork scenario is safe.

## Canonical producers

The stabilized post-fork sample showed three recurring canonical producer addresses. Older clients remained visible as P2P peers but did not appear as canonical producers in the stabilized sample.

## Known compatibility limitation: EIP-2124 ForkID

A post-fork code audit found that Rabbit-specific consensus activation fields are nested under `LQCConfig`, while the current `core/forkid.gatherForks` logic discovers fork heights from top-level `ChainConfig` fields.

As a result, the Rabbit block-50000 and block-50500 consensus activations are not currently encoded into the EIP-2124 fork ID.

Practical effect:

- older clients may remain P2P-connected after the Rabbit-specific consensus fork;
- P2P connectivity does not imply canonical-consensus compatibility;
- V2.2.3 rejects incompatible blocks through consensus validation;
- this behavior can generate unnecessary fork-recovery traffic/timeouts.

Required before Mainnet:

1. include Rabbit consensus activations in peer compatibility/fork identification;
2. add mixed-version handshake regression tests;
3. verify that incompatible pre-fork clients are rejected automatically after activation;
4. publish compatibility behavior and activation evidence for every consensus upgrade.

## Scope and limitations

This report records observations from the public Testnet and official infrastructure. It does not claim that LCQ, Rabbit Core, the EVM execution layer, networking, recovery logic or economic rules are free of defects.

Executable source code, versioned releases, genesis configuration and canonical chain state remain authoritative where documentation and software differ.
