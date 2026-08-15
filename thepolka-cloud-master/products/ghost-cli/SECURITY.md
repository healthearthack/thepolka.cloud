# Security

- Arithmetic is parsed through an allowlisted syntax tree; Python `eval` is never used.
- Prompts are not sent across a network.
- Ghost Agent cannot execute shell commands.
- The ledger is plain text stored locally at `~/.ghost/stream.log`.
- Review the ledger before sharing it because it contains the prompts entered at the helm.
