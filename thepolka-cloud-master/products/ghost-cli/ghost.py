#!/usr/bin/env python3
"""Ghost Agent: a safe, local background planning CLI."""

from __future__ import annotations

import ast
import operator
import queue
import threading
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

LOG_FILE = Path.home() / ".ghost" / "stream.log"


class SafeMath:
    """Evaluate small arithmetic expressions without eval or shell access."""

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    @classmethod
    def evaluate(cls, expression: str) -> int | float:
        tree = ast.parse(expression, mode="eval")
        return cls._visit(tree.body, 0)

    @classmethod
    def _visit(cls, node: ast.AST, depth: int) -> int | float:
        if depth > 12:
            raise ValueError("Expression is too deep")
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            if abs(node.value) > 1_000_000_000:
                raise ValueError("Number is too large")
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in cls.OPERATORS:
            left = cls._visit(node.left, depth + 1)
            right = cls._visit(node.right, depth + 1)
            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent is too large")
            return cls.OPERATORS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in cls.OPERATORS:
            return cls.OPERATORS[type(node.op)](cls._visit(node.operand, depth + 1))
        raise ValueError("Only bounded arithmetic is supported")


class Planner:
    @staticmethod
    def branches(query: str, result: str) -> list[str]:
        lowered = query.lower()
        if any(word in lowered for word in ("image", "duck", "render")):
            return [
                "Draft a five-frame visual iteration plan",
                "Identify lighting, composition, and texture variables",
                "Record the plan only; no image was rendered",
            ]
        if any(word in lowered for word in ("code", "script", "function")):
            return [
                "List the smallest testable implementation step",
                "Identify one failure mode and a verification check",
                "Record a bounded follow-up plan",
            ]
        return [
            f"Inspect the immediate result: {result}",
            "Identify the next logical question",
            "Record a bounded follow-up plan",
        ]


@dataclass
class Job:
    query: str
    result: str


class GhostAgent:
    def __init__(self, log_file: Path = LOG_FILE, delay: float = 0.15):
        self.log_file = log_file
        self.delay = delay
        self.jobs: queue.Queue[Job | None] = queue.Queue()
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        self.worker = threading.Thread(target=self._work, daemon=True)
        self.worker.start()

    def log(self, message: str) -> None:
        stamp = datetime.now().astimezone().isoformat(timespec="seconds")
        with self.log_file.open("a", encoding="utf-8") as stream:
            stream.write(f"[{stamp}] [GHOST] {message}\n")

    def execute(self, query: str) -> str:
        try:
            return str(SafeMath.evaluate(query))
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError):
            return f"Received: {query}"

    def submit(self, query: str) -> str:
        result = self.execute(query)
        self.jobs.put(Job(query, result))
        return result

    def _work(self) -> None:
        while True:
            job = self.jobs.get()
            if job is None:
                self.jobs.task_done()
                return
            self.log(f"Anchor: {job.query!r} -> {job.result!r}")
            for step in Planner.branches(job.query, job.result):
                time.sleep(self.delay)
                self.log(step)
            self.log("Background branch complete")
            self.jobs.task_done()

    def tail(self, lines: int = 10) -> str:
        if not self.log_file.exists():
            return "Ledger is empty."
        return "".join(self.log_file.read_text(encoding="utf-8").splitlines(keepends=True)[-lines:]).rstrip()

    def close(self) -> None:
        self.jobs.join()
        self.jobs.put(None)
        self.worker.join(timeout=2)


def run_cli() -> None:
    agent = GhostAgent()
    print("Ghost Agent 1.0.0 — Helm ready")
    print(f"Local ledger: {agent.log_file}")
    print("Commands: :help  :status  :wait  :tail  :paths  :quit")
    try:
        while True:
            query = input("helm> ").strip()
            if not query:
                continue
            if query in {":quit", ":exit"}:
                break
            if query == ":help":
                print("Enter bounded arithmetic or a planning prompt. No network or shell commands run.")
            elif query == ":status":
                print(f"Queued background jobs: {agent.jobs.unfinished_tasks}")
            elif query == ":wait":
                agent.jobs.join()
                print("Background queue complete.")
            elif query.startswith(":tail"):
                parts = query.split(maxsplit=1)
                count = int(parts[1]) if len(parts) == 2 and parts[1].isdigit() else 10
                print(agent.tail(min(count, 100)))
            elif query == ":paths":
                print(agent.log_file)
            else:
                print(f"> {agent.submit(query)}")
                print("  Background branch queued.")
    except (KeyboardInterrupt, EOFError):
        print()
    finally:
        agent.close()
        print("Ghost Agent stopped cleanly.")


if __name__ == "__main__":
    run_cli()
