# memorax.py
# Minimal proof of identity persistence across resets
# Not a product — demonstrates why a memory layer is necessary

import json
import os
from typing import Dict, Any

MEMORY_FILE = "identity_persistence.json"


class SimpleIdentityMemory:
    """
    Ultra-minimal persistent store for identity and trajectory.
    Shows what dies on reset without persistence.
    """

    def __init__(self):
        self.data: Dict[str, Any] = self._load()

    def _load(self) -> Dict:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        return {
            "identity": "uninitialized",
            "trajectory": []
        }

    def save(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.data, f, indent=2)

    def set_identity(self, identity: str):
        self.data["identity"] = identity
        self.save()

    def add_step(self, step: str):
        self.data["trajectory"].append(step)
        self.save()

    def state(self) -> Dict:
        return dict(self.data)


if __name__ == "__main__":
    print("=== Run 1: First session ===")
    mem = SimpleIdentityMemory()
    mem.set_identity("Explorer v1")
    mem.add_step("Explored cave")
    mem.add_step("Found map")
    print(mem.state())

    print("\n=== Run 2: New session (after reset) ===")
    mem2 = SimpleIdentityMemory()
    print(mem2.state())
    mem2.add_step("Used map from previous exploration")
    print(mem2.state())
