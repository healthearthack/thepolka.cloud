# Ghost Agent 1.0.0

Ghost Agent is a zero-dependency Python command-line interface with a responsive foreground “helm” and one bounded background planning worker. It writes a transparent, local ledger to `~/.ghost/stream.log`.

## Run on Windows

1. Install Python 3.10 or newer.
2. Extract this ZIP file.
3. Open PowerShell in the extracted folder.
4. Run `Set-ExecutionPolicy -Scope Process Bypass`, then `.\run.ps1`.
5. Enter `2+2`, then `:wait`, then `:tail 10`.

macOS or Linux: run `chmod +x run.sh && ./run.sh`.

## Commands

| Command | Result |
|---|---|
| `:status` | Show unfinished background jobs |
| `:wait` | Wait for the local queue |
| `:tail 10` | Read the last ten ledger lines |
| `:paths` | Show the ledger path |
| `:quit` | Finish queued work and exit |

Ghost Agent does not use a network service, application programming interface, shell execution, telemetry, or hidden automation. The visual planner creates a plan; it does not claim to render images.
