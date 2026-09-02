#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data" / "economic-allocation.json").read_text(encoding="utf-8"))

assert data["document_version"] == "1.0"
assert data["finite_maximum_supply"] is False

maximum = data["genesis_allocation_rab"]
allocations = data["allocations"]
total = sum(item["amount_rab"] for item in allocations)
assert total == maximum, f"allocation total {total} != genesis allocation {maximum}"

protocol_reserve = next(
    item for item in allocations if item["id"] == "participation_protocol"
)
assert protocol_reserve["amount_rab"] == 10000000
assert protocol_reserve["is_source_of_block_rewards"] is False
assert protocol_reserve["enforcement"] == (
    "genesis_reserve_separate_from_consensus_issuance"
)
assert len(protocol_reserve["required_before_mainnet"]) == 6

ids = [item["id"] for item in allocations]
assert len(ids) == len(set(ids)), "duplicate allocation id"

testnet = next(item for item in allocations if item["id"] == "testnet_rewards")
category_total = sum(testnet["categories"].values())
assert category_total == testnet["amount_rab"], (
    f"testnet category total {category_total} != reserve {testnet['amount_rab']}"
)

operations = next(item for item in allocations if item["id"] == "operations")
assert operations["amount_rab"] + testnet["amount_rab"] == 500000

creator = next(item for item in allocations if item["id"] == "creator_developers")
vesting = creator["vesting"]
vesting_total = vesting["initial_release_rab"] + (
    vesting["remaining_installments"] * vesting["amount_per_installment_rab"]
)
assert vesting_total == creator["amount_rab"], (
    f"vesting total {vesting_total} != creator allocation {creator['amount_rab']}"
)

print("RAB_ALLOCATION_VERIFICATION=PASS")
print(f"GENESIS_ALLOCATION_RAB={maximum}")
print(f"FINITE_MAXIMUM_SUPPLY={str(data['finite_maximum_supply']).upper()}")
print(f"TAIL_REWARD_RAB={data['reward_schedule']['tail_reward_rab']}")
print(f"PROTOCOL_RESERVE_RAB={protocol_reserve['amount_rab']}")
print("PROTOCOL_RESERVE_IS_BLOCK_REWARD_SOURCE=FALSE")
print(f"ALLOCATION_TOTAL_RAB={total}")
print(f"TESTNET_REWARD_RESERVE_RAB={testnet['amount_rab']}")
print(f"OPERATIONS_PLUS_TESTNET_RAB={operations['amount_rab'] + testnet['amount_rab']}")
print(f"CREATOR_VESTING_TOTAL_RAB={vesting_total}")
