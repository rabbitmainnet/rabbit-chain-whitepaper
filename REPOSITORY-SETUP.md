# Create the official GitHub repository

Recommended repository:

`https://github.com/rabbitmainnet/rabbit-chain-whitepaper`

Create it as a **public empty repository** under the `rabbitmainnet` organization. Do not initialize it with a README, `.gitignore`, or license because those files already exist here.

From the extracted repository directory:

```bash
git init -b main
git add .
git diff --cached --check
python3 scripts/verify_allocation.py
python3 scripts/check_release_readiness.py --phase pretestnet
git commit -m "docs: publish Rabbit Chain pre-testnet whitepaper v0.9"
git remote add origin https://github.com/rabbitmainnet/rabbit-chain-whitepaper.git
git push -u origin main
```

Expected validation:

```text
RAB_ALLOCATION_VERIFICATION=PASS
MAXIMUM_SUPPLY_RAB=15000000
ALLOCATION_TOTAL_RAB=15000000
TESTNET_REWARD_RESERVE_RAB=100000
OPERATIONS_PLUS_TESTNET_RAB=500000
CREATOR_VESTING_TOTAL_RAB=1500000
RELEASE_READINESS_PRETESTNET=PASS
```

The mainnet readiness check must fail during the pre-testnet phase because mainnet addresses, genesis identity, bootnodes, active services, contract registry, and final vesting references do not exist yet. A false PASS would hide unresolved launch work.
