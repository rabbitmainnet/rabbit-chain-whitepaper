# Rabbit Chain Testnet V2.3.4 Software Release Record

**Date:** 18 September 2026
**Network:** Rabbit Testnet
**Chain ID / Network ID:** `9280` / `9280`
**Current Rabbit Core release:** `v2.3.4`
**Source commit:** `b6fda8e6118d6ac7a6af81119120345e80081249`
**Consensus baseline:** LQC Liveness V3, active since canonical block `77000`

## Purpose

This document records the Rabbit Core V2.3.4 public Testnet software release.

V2.3.4 is not a new Rabbit Testnet hard fork and does not schedule a new
consensus activation height. The existing canonical history is preserved:

- block `50000`: consensus hardening;
- block `50500`: consensus stabilization;
- block `73000`: Fairness/Liveness activation;
- block `77000`: Liveness V3 activation.

The historical Liveness V3 activation record remains:

`docs/Testnet-V2.3.0-Liveness-V3-Upgrade.md`

## Verified release artifacts

| Platform | Archive | SHA-256 |
|---|---|---|
| Windows AMD64 | `rabbit-core-testnet-v2.3.4-windows-amd64.zip` | `791970d2071191db54cbcc3a1fb5db22ccfc9a771640f30cf7624d6fc10e143f` |
| Linux AMD64 | `rabbit-core-testnet-v2.3.4-linux-amd64.tar.gz` | `9063b3d349172a79e61b89fb6c01c815874c82eaf63741d1034cba330125913c` |
| macOS Intel / AMD64 | `rabbit-core-testnet-v2.3.4-darwin-amd64.tar.gz` | `10bda73072fc8a9ddc68cc4e96e569ea76241e77553c17c4b5ca5b7a9c606271` |
| macOS Apple Silicon / ARM64 | `rabbit-core-testnet-v2.3.4-darwin-arm64.tar.gz` | `6ee3b40eacd8b94d2b7b95aaa4a0a9219173226f2bd3d239f132f49448d536ba` |

Official release:

<https://github.com/rabbitmainnet/rabbit-geth/releases/tag/v2.3.4>

Official download page:

<https://rabbitchain.org/mining/>

## Software changes

V2.3.4 improves live Rabbit Core operation without introducing a new scheduled
consensus activation.

The release includes:

- peer-retention hardening when Rabbit committee context is temporarily
  unavailable, allowing the peer to remain useful for normal Ethereum-chain
  synchronization instead of being disconnected solely for that transient
  Rabbit-specific condition;
- bounded bootnode/discovery iteration rather than continuously cycling the same
  configured node iterator;
- clearer Rabbit Miner reward activity messages distinguishing normal producer,
  committee and full-reward/no-eligible-committee cases;
- updated release metadata and verified Windows, Linux and macOS packages.

These changes do not create additional LCQ seats, alter the one-wallet /
one-persistent-seat invariant, reset canonical history or define a new fork
height.

## Reward display and consensus accounting

The underlying Liveness V3 reward rules remain unchanged.

When an eligible committee exists, the configured reward is divided 70% to the
producer and 30% to the committee pool. The producer is not paid again as a
committee member for its own block. When no eligible paid committee exists, the
producer receives the full configured block reward.

For the current 1.20 tRAB Testnet base reward this corresponds to:

- `0.84 tRAB` producer share when an eligible committee exists;
- `0.36 tRAB` total committee pool when an eligible committee exists;
- `1.20 tRAB` to the producer when no eligible paid committee exists.

The V2.3.4 miner interface makes these outcomes clearer to the operator; the
display change does not itself redefine consensus accounting.

## Non-destructive upgrade

Operators upgrading to V2.3.4 must preserve the existing:

- Rabbit Testnet datadir;
- canonical blockchain;
- encrypted mining wallet;
- keystore and wallet password;
- persistent LCQ participation state.

The release is intended to reuse the same persistent Rabbit Testnet state.
Deleting the blockchain, datadir, keystore or participation state is not part
of the normal upgrade procedure.

## Platform launchers

The verified packages provide the normal Rabbit Core launch path for each
supported operating system:

- Windows: `Start-Rabbit-Core.cmd`
- Linux: `Start-Rabbit-Core.sh`
- macOS Intel / AMD64: `Start-Rabbit-Core.command`
- macOS Apple Silicon / ARM64: `Start-Rabbit-Core.command`

Users should verify the outer archive SHA-256 before extraction and may also
verify the internal `SHA256SUMS.txt`.

## Protocol continuity

Whitepaper v1.5 remains the Liveness V3 protocol edition. V2.3.4 supersedes
V2.3.0 as the current public Rabbit Core software release, but V2.3.0 remains
the historical release associated with the block-77000 Liveness V3 activation.
