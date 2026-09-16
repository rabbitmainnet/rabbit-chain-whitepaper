# Rabbit Chain Testnet V2.3.0 Liveness V3 Upgrade Record

**Network:** Rabbit Testnet
**Chain ID:** `9280`
**Release:** `rabbit-core-testnet-v2.3.0`
**Source commit:** `7128cb6db44dbecff608a54b4890a03f5e426647`
**Liveness V3 activation:** canonical block `77000`
**Genesis block hash:** `0x9b71d7f2922fdf8383a4a12be5594e25938625195e0d84c05c3bd71b7bcf93f7`

## Purpose

This document records the Rabbit Core V2.3.0 software release and the LQC
Liveness V3 rules scheduled for activation at canonical block 77000.

It complements and preserves the historical V2.2.3 stabilization and V2.2.5
Fairness/Liveness upgrade records. The Testnet is not reset and no new chain
is created.

## Verified release artifacts

| Platform | Archive | SHA-256 |
|---|---|---|
| Windows AMD64 | `rabbit-core-testnet-v2.3.0-windows-amd64.zip` | `a23662ee6def886b62336ce0dedd5b0d6bf8daeb0cb12cc96eadae435c12ab0e` |
| Linux AMD64 | `rabbit-core-testnet-v2.3.0-linux-amd64.tar.gz` | `e5d75d1b3c71b31420a1999043a369f661bea794afc4aaefdff5e157262ec2ad` |

Official release:

<https://github.com/rabbitmainnet/rabbit-geth/releases/tag/rabbit-core-testnet-v2.3.0>

Official download page:

<https://rabbitchain.org/mining/>

## Consensus activation

Beginning at canonical block 77000, Rabbit Testnet activates LQC Liveness V3.

The activation introduces:

- deterministic producer rotation derived from canonical persistent-seat state;
- bounded fallback and recovery when the scheduled producer is unavailable;
- canonical committee-participation claims;
- committee reward accounting tied to verified participation;
- one eligible wallet, one canonical selection chance;
- deterministic header and runtime validation for the V3/V4 protocol path;
- preserved permissionless RandomX Work V2 admission.

The block-50000 hardening, block-50500 stabilization and block-73000
Fairness/Liveness transitions remain part of canonical history.

## Reward behavior

When a committee exists, the configured block reward is divided into a 70%
producer share and a 30% committee pool.

Verified committee participants receive deterministic fixed shares from that
pool. A missing participant's share is not reassigned or issued.

When the canonical selection contains no committee, the producer receives the
full configured block reward.

Reward calculations do not mutate the original total-reward value.

## Non-destructive upgrade

Rabbit Core V2.3.0 reuses the existing:

- Rabbit Testnet datadir;
- canonical blockchain;
- encrypted mining wallet;
- keystore and wallet password;
- persistent LCQ participation state.

Operators must not delete their blockchain, datadir, keystore or participation
state as part of this upgrade.

Rabbit Core applies the official Testnet configuration to the existing
database, waits for canonical synchronization and resumes Work V2/LCQ
participation automatically.

## Compatibility and validation

Before publication, the release passed:

- tagged Liveness V3 and RandomX test suites;
- default untagged test suites;
- committee and V4 race tests;
- identical old/new genesis-block hash verification;
- in-place chain-configuration upgrade verification;
- Windows AMD64 native package verification;
- Linux AMD64 package verification;
- live Explorer and public RPC synchronization;
- canonical block-height and block-hash comparison;
- live pre-activation producer and committee participation on upgraded miners.

Consensus behavior after block 77000 must still be confirmed through direct
live-network observation.

## Operational requirement

Miners and node operators must upgrade to Rabbit Core V2.3.0 before canonical
block 77000.

Older software may remain connected at the P2P transport layer because the
Rabbit-specific nested LQC activation blocks are not currently encoded in the
standard EIP-2124 fork ID. Transport connectivity does not make incompatible
blocks canonical; upgraded nodes enforce the active consensus rules.
