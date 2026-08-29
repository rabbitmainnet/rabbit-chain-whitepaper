#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

parser = argparse.ArgumentParser()
parser.add_argument("--phase", choices=("pretestnet", "mainnet"), required=True)
args = parser.parse_args()

allocation = json.loads((ROOT / "data" / "economic-allocation.json").read_text(encoding="utf-8"))
endpoints = json.loads((ROOT / "data" / "official-endpoints.json").read_text(encoding="utf-8"))
registry = json.loads((ROOT / "data" / "contract-registry.template.json").read_text(encoding="utf-8"))

problems = []

if args.phase == "mainnet":
    if endpoints["mainnet"]["genesis_hash"] is None:
        problems.append("mainnet genesis_hash is unresolved")
    if not endpoints["mainnet"]["bootnodes"]:
        problems.append("mainnet bootnodes are unresolved")
    for key in ("rpc_http", "rpc_websocket", "explorer"):
        if endpoints["mainnet"][key]["status"] != "active":
            problems.append(f"mainnet {key} is not active")
    if registry["registry_version"] is None:
        problems.append("contract registry is still a template")
    if any(item["address"] is None for item in allocation["allocations"]):
        problems.append("one or more allocation addresses are unresolved")
    contract_allocations = [item for item in allocation["allocations"] if item["id"] != "participation_protocol"]
    if any(item.get("deployment_status") != "verified" for item in contract_allocations):
        problems.append("one or more allocation contracts are not deployed and verified")
    required_contract_ids = {item["id"] for item in contract_allocations}
    registry_by_id = {item["allocation_id"]: item for item in registry["contracts"]}
    if set(registry_by_id) != required_contract_ids:
        problems.append("contract registry does not cover every contract-controlled allocation exactly once")
    for allocation_id, item in registry_by_id.items():
        for key in ("deployment_method", "predicted_address", "genesis_balance_proof",
                    "deployment_block", "deployed_address", "deployment_transaction",
                    "creation_bytecode_hash", "runtime_bytecode_hash"):
            if item.get(key) is None:
                problems.append(f"{allocation_id} {key} is unresolved")
        if item.get("predicted_address") != item.get("deployed_address"):
            problems.append(f"{allocation_id} deployed address differs from predicted address")
        if item.get("verification_status") != "verified":
            problems.append(f"{allocation_id} contract verification is incomplete")
    creator = next(item for item in allocation["allocations"] if item["id"] == "creator_developers")
    if creator["vesting"]["installment_interval"] is None:
        problems.append("creator installment interval is unresolved")
    if creator["vesting"]["liquidity_start_reference"] is None:
        problems.append("creator liquidity start reference is unresolved")

if problems:
    print(f"RELEASE_READINESS_{args.phase.upper()}=FAIL")
    for problem in problems:
        print(f"- {problem}")
    raise SystemExit(1)

print(f"RELEASE_READINESS_{args.phase.upper()}=PASS")
