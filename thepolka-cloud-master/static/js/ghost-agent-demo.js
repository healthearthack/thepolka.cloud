(() => {
  const run = document.getElementById("run-demo");
  const reset = document.getElementById("reset-demo");
  const helm = document.getElementById("helm-output");
  const ghost = document.getElementById("ghost-output");
  const status = document.getElementById("demo-status");
  if (!run || !reset || !helm || !ghost || !status) return;
  const pause = (ms) => new Promise((resolve) => window.setTimeout(resolve, ms));
  let generation = 0;
  function resetDemo() {
    generation += 1; run.disabled = false; status.textContent = "Ready";
    helm.innerHTML = '<p>Ghost Agent 1.0.0 — Helm ready</p><p>helm&gt; <span class="terminal-cursor">_</span></p>';
    ghost.innerHTML = "<p>Waiting for a bounded local job...</p>";
  }
  async function runDemo() {
    const current = ++generation; run.disabled = true; status.textContent = "Running";
    helm.innerHTML = "<p>Ghost Agent 1.0.0 — Helm ready</p><p>helm&gt; 2+2</p>";
    await pause(300); if (current !== generation) return;
    helm.insertAdjacentHTML("beforeend", "<p class='terminal-success'>&gt; 4</p><p>queued ghost job 4f24a1c0</p><p>helm&gt; <span class='terminal-cursor'>_</span></p>");
    ghost.innerHTML = "<p>[QUEUED] '2+2' -&gt; '4'</p>";
    for (const line of ["[STARTED] Background planning started.","[BRANCH 1] Verified arithmetic result: 4.","[BRANCH 2] 4 squared is 16.","[BRANCH 3] 4! is 24.","[COMPLETED] Background planning completed."]) {
      await pause(400); if (current !== generation) return;
      ghost.insertAdjacentHTML("beforeend", `<p>${line}</p>`);
    }
    status.textContent = "Complete"; run.disabled = false;
  }
  run.addEventListener("click", runDemo); reset.addEventListener("click", resetDemo);
})();
