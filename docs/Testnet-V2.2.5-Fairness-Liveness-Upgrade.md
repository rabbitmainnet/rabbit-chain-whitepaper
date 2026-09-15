# Rabbit Chain Testnet V2.2.5 Fairness/Liveness Upgrade Record

**Date:** 14 September 2026  
**Network:** Rabbit Testnet  
**Chain ID / Network ID:** `9280` / `9280`  
**Release:** `rabbit-core-testnet-v2.2.5`  
**Source commit:** `ed6fb1692392ce93886d112d84142b8aa487fceb`  
**Fairness/Liveness activation:** canonical block `73000`

## Purpose

This document records the software release and protocol rules scheduled for the Rabbit Testnet Fairness/Liveness activation at block 73000. It complements, rather than replaces, the historical V2.2.3 stabilization report for block 50500.

## Verified release artifacts

| Artifact | SHA-256 |
|---|---|
| `rabbit-core-testnet-v2.2.5-windows-amd64.zip` | `08a7cf8d79b8183cdde641fa06157b60c92329105e31965492ccc1b32031c945` |
| `rabbit-core-testnet-v2.2.5-linux-amd64.tar.gz` | `f376de87e944624834ea9128018ed4ee42df7ab6e55779dfded5085aacf7ca35` |

Genesis file SHA-256:

`ef115b86fe0225b8fddd41d61ff9576c08960b97bd4e1e374fcfa0cee4ec7ad9`

Official release:

<https://github.com/rabbitmainnet/rabbit-geth/releases/tag/rabbit-core-testnet-v2.2.5>

## Consensus transition

At block 73000 the producer-selection path transitions to deterministic WorkSeat ordering without legacy stale-jail state reordering the producer queue.

The transition preserves:

- persistent equal WorkSeats;
- separate committee eligibility filtering;
- deterministic fallback timing;
- permissionless recovery;
- heartbeat participation tracking;
- the 70% producer / 30% committee reward model;
- the existing canonical Testnet history.

At the activation boundary, legacy `MissedTurns` / `JailedUntil` state that could affect producer ordering is deterministically cleared. After activation, a later valid candidate winning a block does not by itself jail an earlier deterministic seat.

## In-place upgrade

This is not a Testnet reset. Operators retain the existing Rabbit Testnet datadir, encrypted mining wallet, keystore, chain history and persistent consensus state.

Rabbit Core V2.2.5 also changes launcher recovery behavior so that recoverable startup conditions do not deliberately delete `chaindata` or `triedb`. If the node process stops unexpectedly, Rabbit Core attempts to restart it with the same data directory and does not restart mining until the node RPC is ready and canonical synchronization checks pass.

These operational safeguards reduce destructive recovery behavior; they are not a guarantee against arbitrary disk corruption, operating-system failure or hardware loss. Wallet and keystore backups remain mandatory.

## Historical continuity

The earlier consensus transitions remain part of canonical history:

- block `50000`: consensus hardening;
- block `50500`: consensus stabilization;
- block `73000`: Fairness/Liveness activation.

The historical V2.2.3 stabilization evidence remains available in:

`docs/Testnet-V2.2.3-Stabilization-Report.md`

## Validation status

The V2.2.5 Windows and Linux release jobs completed successfully from the published source commit and produced the verified artifacts above.

This document does not claim post-activation network observations that have not yet been recorded. Post-fork canonical convergence and live-network evidence should be appended only after direct observation.

Testnet remains experimental software.
