# Security and sensitive disclosures

This repository is public documentation. Do not disclose private keys, seed phrases, passwords, access tokens, unpublished personal information, or an immediately exploitable vulnerability in a public issue.

Until a dedicated responsible-disclosure address is published and verified on `https://rabbitchain.org/`, use the official Discord only to request a private reporting channel. Do not send exploit details in a public Discord channel.

The final mainnet release must replace this interim process with a dedicated security contact, encrypted reporting option, response targets, scope, safe-harbor language where legally appropriate, and disclosure policy.

## Testnet V2.3.0 known P2P compatibility limitation

**Status: disclosed on 11 September 2026. Mainnet remediation required.**

Rabbit-specific consensus activation heights are currently stored under the nested `LQCConfig`. The current EIP-2124 fork-ID gathering logic reflects the top-level `ChainConfig` fork fields and therefore does not encode the Rabbit-specific block-50000, block-50500, block-73000 and block-77000 activations into the advertised fork ID.

Operational consequence: a pre-V2.3.0 client may remain connected to an upgraded node at the P2P transport layer after block 77000. This does **not** make its incompatible blocks canonical: upgraded V2.3.0 consensus validation rejects incompatible history. Post-activation canonical convergence must be recorded from direct live-network observation rather than assumed in advance.

Required remediation before Mainnet:

- encode Rabbit consensus activations into peer compatibility/fork identification;
- add explicit regression tests proving pre-fork clients are rejected after activation;
- test mixed-version networks before release;
- publish compatibility behavior with each consensus upgrade.

This limitation is tracked as a compatibility and network-hygiene issue rather than concealed as an implementation detail.
