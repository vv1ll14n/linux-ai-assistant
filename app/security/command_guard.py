class CommandGuard:
    BLOCKED_PATTERNS = [
        "rm -rf /",
        "mkfs",
        ":(){",
        "dd if="
    ]

    def is_safe(self, command: str) -> bool:
        return not any(pattern in command for pattern in self.BLOCKED_PATTERNS)
