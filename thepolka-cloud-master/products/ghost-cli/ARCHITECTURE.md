# Architecture

The foreground loop returns a safe arithmetic result or acknowledges the prompt. A single queue-backed daemon worker records three bounded planning steps. On exit, the process waits for accepted jobs and closes the worker cleanly.
