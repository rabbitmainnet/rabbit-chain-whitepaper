---
title: "Rabbit Chain Testnet"
subtitle: "Technical addendum v1.0 for Rabbit Core V2.4.25"
lang: en
geometry: margin=24mm
---

# Scope and network

This addendum accompanies the historical Technical Whitepaper v1.7. It describes the public Testnet software built from Rabbit Core commit `4f502f971c3b3166be14da6e25fbc7c531404d42`. The original whitepaper and earlier activation records are preserved.

Rabbit Chain is a permissionless EVM Layer 1 using Live Consensus Queue (LCQ). The public network is Rabbit Chain Testnet, chain ID and network ID **9280**, with **tRAB** as its native test asset. Mainnet has yet to launch.

> One wallet. One fair chance.\
> Use the computer you already have.\
> No farms. No privileged miners.

The technical fairness boundary is one persistent seat per eligible wallet. A faster CPU can affect the time to discover an admission proof, while additional hash power gives an activated seat no extra rotation weight. Wallet identities do not establish unique human identities.

# Admission, production and rewards

1. Rabbit Core prepares or reuses an encrypted wallet and starts its local full node. The node must synchronize to participate against canonical state.
2. For a wallet without a seat, Rabbit Miner searches for valid RandomX Work V2 admission work in the current protocol context. The official builds use the Rabbit 1 GiB RandomX dataset profile.
3. `ADMISSION_PENDING` indicates an admission awaiting canonical activation. `ACTIVE_SEAT` indicates an activated persistent seat. Normal admission work stops after activation, and the full node remains online for LCQ.
4. LCQ derives the eligible set, scheduled producer, fallbacks and committee from canonical state. The node attempts production automatically when selected and synchronized. The configured block target is 10 seconds. Observed intervals depend on network and producer conditions.

The WorkSeat subsidy path uses a configured 70/30 producer-to-committee allocation when an eligible committee exists. When an eligible producer has no eligible committee, the producer path can receive the full subsidy. Emergency registry fallback with zero eligible WorkSeats can advance the chain without minting the normal WorkSeat subsidy. These are mining rules. VRF request and fulfillment fees follow a separate policy.

Missed assigned production turns can result in a canonical penalty. `PENALIZED` reports the expiry height and remaining blocks, while the cause of the missed turn requires operational evidence. After expiry the wallet still needs a synchronized node and an eligible assignment. A restart with the same wallet and state retains the canonical seat.

# Installation and recovery

Extract the package into a program directory and verify the archive against its SHA-256. Use `Start-Rabbit-Core.cmd` on Windows, `Start-Rabbit-Core.sh` on Linux, or `Start-Rabbit-Core.command` on macOS. Keep the encrypted keystore and its password separately. On an upgrade, stop the old launcher cleanly and preserve the full data directory, wallet, node identity and participation state.

Fresh installations use the official multipart bootstrap at block **385,509**. The launcher checks the parts and assembled data, supports interrupted-download resumption and synchronizes subsequent blocks through peers. Existing databases bypass fresh bootstrap. The archive is approximately 7.49 GiB compressed. The distributed genesis file SHA-256 is `4970159f077b62b7aa9bde1f81cb61ae837b42ef64861d7b23241e1af4d75c9f`.

The V2.4.25 build includes earlier restart reconstruction and checkpoint handling, plus changes to synchronization recovery and miner cancellation relative to V2.4.23. After failed synchronization, production recovery checks canonical progress before resuming. RPC nodes serve blockchain data, and the Explorer indexes it separately. Their public availability and the synchronization of individual miners require separate observation.

# Activation and verification

| Public Testnet rule | Historical block |
|---|---:|
| LCQ stabilization | 50,500 |
| Fairness and liveness | 73,000 |
| Liveness V3, V4, V5 and V6 | 77,000 / 97,991 / 115,000 / 115,022 |
| VRF DKG preparation | 136,065 |
| VRF protocol and VRF liveness | 136,193 |
| Mining reward V5 | 153,601 |
| VRF Availability V2 | 173,057 |
| VRF economics V2 and WorkSeat admission V2 | 320,000 |
| WorkSeat liveness V2 | 323,800 |

The V2.4.25 changes introduce no new scheduled activation height. The build includes authenticated VRF transport, DKG artifact replay changes and changes to finalization gossip. DKG prepares distributed signing material. A successful VRF request requires canonical fulfillment and a verifiable proof. Build and laboratory results establish neither public request completion rates nor Mainnet readiness.

# References

- [Rabbit Core source at the V2.4.25 build commit](https://github.com/rabbitmainnet/rabbit-geth/tree/4f502f971c3b3166be14da6e25fbc7c531404d42)
- [GitHub Actions build and test run](https://github.com/rabbitmainnet/rabbit-geth/actions/runs/43128197592)
- [Rabbit Chain website and operator guides](https://rabbitchain.org)
- [Public RPC](https://rpc-testnet.rabbitchain.org)
- [Public Explorer](https://explorer-testnet.rabbitchain.org)
