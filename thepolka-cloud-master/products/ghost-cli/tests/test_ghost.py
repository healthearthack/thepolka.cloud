import tempfile
import unittest
from pathlib import Path

from ghost import GhostAgent, Planner, SafeMath


class GhostTests(unittest.TestCase):
    def test_safe_arithmetic(self):
        self.assertEqual(SafeMath.evaluate("2 + 2 * 3"), 8)

    def test_rejects_code_execution(self):
        with self.assertRaises(ValueError):
            SafeMath.evaluate("__import__('os').system('echo nope')")

    def test_visual_planner_is_truthful(self):
        plan = " ".join(Planner.branches("render a duck image", "received"))
        self.assertIn("no image was rendered", plan)

    def test_background_job_writes_ledger(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stream.log"
            agent = GhostAgent(path, delay=0)
            self.assertEqual(agent.submit("3+3"), "6")
            agent.close()
            ledger = path.read_text(encoding="utf-8")
            self.assertIn("Background branch complete", ledger)


if __name__ == "__main__":
    unittest.main()
