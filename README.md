<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Reinforcement Learning Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@400;700;800&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet" />
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #0b0d10;
    --surface: #13161b;
    --surface2: #1c2028;
    --border: rgba(255,255,255,0.07);
    --border2: rgba(255,255,255,0.12);
    --text: #e8eaf0;
    --muted: #7a8097;
    --accent-green: #3bdc8c;
    --accent-purple: #9b7fff;
    --accent-amber: #f5a623;
    --accent-blue: #5ba4f5;
    --tag-bg: rgba(255,255,255,0.05);
  }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    min-height: 100vh;
  }

  /* ── GRID BACKGROUND ── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .wrapper { position: relative; z-index: 1; max-width: 860px; margin: 0 auto; padding: 0 2rem 6rem; }

  /* ── HERO ── */
  .hero {
    padding: 5rem 0 3.5rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 3rem;
  }

  .hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent-green);
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .hero-eyebrow::before {
    content: '';
    display: inline-block;
    width: 32px;
    height: 1px;
    background: var(--accent-green);
  }

  .hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 6vw, 3.8rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.02em;
    color: #fff;
    margin-bottom: 1.25rem;
  }

  .hero h1 span {
    color: transparent;
    -webkit-text-stroke: 1px rgba(255,255,255,0.3);
  }

  .hero-desc {
    max-width: 520px;
    color: var(--muted);
    font-size: 15px;
    line-height: 1.75;
    margin-bottom: 2rem;
  }

  .hero-stats {
    display: flex;
    gap: 2.5rem;
    flex-wrap: wrap;
  }

  .stat {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }
  .stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #fff;
  }
  .stat-label {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
  }

  /* ── SECTION TITLE ── */
  .section-title {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 1.5rem;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }

  /* ── PROJECT CARD ── */
  .project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    transition: border-color 0.2s;
  }
  .project-card:hover { border-color: var(--border2); }

  .card-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1rem;
    flex-wrap: wrap;
  }

  .card-title-group { flex: 1; min-width: 220px; }

  .card-number {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 0.1em;
    margin-bottom: 6px;
  }

  .card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: #fff;
    line-height: 1.2;
    margin-bottom: 4px;
  }

  .card-subtitle {
    font-size: 13px;
    color: var(--muted);
  }

  .card-badge {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.08em;
    padding: 5px 12px;
    border-radius: 99px;
    border: 1px solid;
    white-space: nowrap;
    align-self: flex-start;
  }
  .badge-green { color: var(--accent-green); border-color: rgba(59,220,140,0.25); background: rgba(59,220,140,0.07); }
  .badge-purple { color: var(--accent-purple); border-color: rgba(155,127,255,0.25); background: rgba(155,127,255,0.07); }

  .card-desc {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.75;
    margin-bottom: 1.5rem;
  }

  /* ── ALGO PILLS ── */
  .algo-grid {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 1.5rem;
  }

  .algo-pill {
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 8px 14px;
    font-size: 13px;
  }
  .algo-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    flex-shrink: 0;
  }
  .dot-green { background: var(--accent-green); }
  .dot-purple { background: var(--accent-purple); }
  .dot-blue { background: var(--accent-blue); }
  .dot-amber { background: var(--accent-amber); }

  /* ── RESULTS ROW ── */
  .results-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 10px;
    padding-top: 1.25rem;
    border-top: 1px solid var(--border);
  }

  .result-item {
    background: var(--surface2);
    border-radius: 10px;
    padding: 14px 16px;
  }

  .result-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 6px;
  }

  .result-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.25rem;
    font-weight: 700;
    color: #fff;
  }
  .result-value.green { color: var(--accent-green); }
  .result-value.purple { color: var(--accent-purple); }
  .result-value.blue { color: var(--accent-blue); }
  .result-value.amber { color: var(--accent-amber); }

  .result-sub {
    font-size: 11px;
    color: var(--muted);
    margin-top: 2px;
  }

  /* ── ALGO COMPARISON TABLE ── */
  .compare-section { margin-top: 2.5rem; margin-bottom: 2.5rem; }

  .compare-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
  }
  .compare-table th {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    text-align: left;
    padding: 10px 16px;
    border-bottom: 1px solid var(--border);
  }
  .compare-table td {
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    color: var(--text);
  }
  .compare-table tr:last-child td { border-bottom: none; }
  .compare-table tr:hover td { background: var(--surface2); }

  .algo-name {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #fff;
    font-weight: 500;
  }

  /* ── TECH STACK ── */
  .tech-stack {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 2.5rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
  }

  .tech-tag {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--muted);
    background: var(--tag-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 4px 12px;
    letter-spacing: 0.04em;
  }

  /* ── FOOTER ── */
  .footer {
    margin-top: 5rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }

  .footer-left {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 0.08em;
  }

  .footer-right {
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--muted);
  }

  .pulse {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--accent-green);
    animation: pulse 2s ease infinite;
  }
  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
  }

  /* ── ENV BANNER ── */
  .env-banner {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 2rem;
    font-size: 13px;
    color: var(--muted);
  }

  .env-name {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--accent-blue);
  }

  .divider { width: 1px; height: 14px; background: var(--border2); }

  /* ── KEY FINDINGS ── */
  .findings {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent-amber);
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    margin-top: 1.25rem;
  }

  .findings-title {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent-amber);
    margin-bottom: 10px;
  }

  .findings ul {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .findings li {
    font-size: 13.5px;
    color: var(--muted);
    display: flex;
    gap: 10px;
    align-items: baseline;
  }
  .findings li::before {
    content: '→';
    color: var(--accent-amber);
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    flex-shrink: 0;
  }
</style>
</head>
<body>
<div class="wrapper">

  <!-- HERO -->
  <header class="hero">
    <div class="hero-eyebrow">Reinforcement Learning Portfolio</div>
    <h1>Learning to Play,<br /><span>Learning to Balance</span></h1>
    <p class="hero-desc">
      Two independent RL experiments exploring tabular methods — from Q-Learning and SARSA on a card game, to Monte Carlo control on a classic control benchmark.
    </p>
    <div class="hero-stats">
      <div class="stat">
        <span class="stat-value">2</span>
        <span class="stat-label">Projects</span>
      </div>
      <div class="stat">
        <span class="stat-value">5</span>
        <span class="stat-label">Algorithms</span>
      </div>
      <div class="stat">
        <span class="stat-value">55K+</span>
        <span class="stat-label">Training episodes</span>
      </div>
      <div class="stat">
        <span class="stat-value">~43%</span>
        <span class="stat-label">Best win rate</span>
      </div>
    </div>
  </header>

  <!-- PROJECT 01 -->
  <div class="section-title">Projects</div>

  <div class="project-card">
    <div class="card-header">
      <div class="card-title-group">
        <div class="card-number">01 / 02</div>
        <div class="card-title">Twenty-One RL Agent 🃏</div>
        <div class="card-subtitle">Gymnasium Blackjack-v1 · Tabular TD Control</div>
      </div>
      <div class="card-badge badge-green">TD Learning</div>
    </div>

    <p class="card-desc">
      Trains two temporal-difference agents — Q-Learning and SARSA — to play Blackjack across 50,000 episodes.
      The environment provides a 3-tuple observation <code style="font-family:'DM Mono',monospace;font-size:12px;color:var(--accent-green)">(player_sum, dealer_card, usable_ace)</code> over
      360 discrete states and two actions: hit or stick.
    </p>

    <!-- Environments -->
    <div class="env-banner">
      <span class="env-name">Blackjack-v1</span>
      <span class="divider"></span>
      <span>States: 360 &nbsp;·&nbsp; Actions: 2 &nbsp;·&nbsp; Rewards: {−1, 0, +1}</span>
    </div>

    <!-- Algorithms -->
    <div class="algo-grid">
      <div class="algo-pill">
        <span class="algo-dot dot-green"></span>
        Q-Learning (off-policy)
      </div>
      <div class="algo-pill">
        <span class="algo-dot dot-purple"></span>
        SARSA (on-policy)
      </div>
      <div class="algo-pill">
        <span class="algo-dot dot-amber"></span>
        ε-greedy exploration
      </div>
      <div class="algo-pill">
        <span class="algo-dot" style="background:var(--muted)"></span>
        Random & Conservative baselines
      </div>
    </div>

    <!-- Results -->
    <div class="results-row">
      <div class="result-item">
        <div class="result-label">Q-Learning win rate</div>
        <div class="result-value green">42.9%</div>
        <div class="result-sub">avg reward ≈ +0.43</div>
      </div>
      <div class="result-item">
        <div class="result-label">SARSA win rate</div>
        <div class="result-value purple">42.3%</div>
        <div class="result-sub">avg reward ≈ +0.42</div>
      </div>
      <div class="result-item">
        <div class="result-label">Training episodes</div>
        <div class="result-value">50K</div>
        <div class="result-sub">eval over 10K greedy eps</div>
      </div>
      <div class="result-item">
        <div class="result-label">Learning rate α</div>
        <div class="result-value">0.1</div>
        <div class="result-sub">γ = 0.95, ε → 0.01</div>
      </div>
    </div>

    <div class="findings">
      <div class="findings-title">Key findings</div>
      <ul>
        <li>Both agents always stick on sums 18–21 and hit on 4–11 — consistent with basic strategy.</li>
        <li>Q-Learning takes riskier hits on borderline hands (e.g. sum 19, usable ace vs dealer 9/10) because it bootstraps from the greedy next action.</li>
        <li>SARSA is more conservative on borderline decisions, accounting for exploratory actions it actually takes during training.</li>
        <li>Both exceed the 40% win-rate benchmark for solid Blackjack play.</li>
      </ul>
    </div>
  </div>

  <!-- PROJECT 02 -->
  <div class="project-card">
    <div class="card-header">
      <div class="card-title-group">
        <div class="card-number">02 / 02</div>
        <div class="card-title">CartPole Balance — Monte Carlo RL ⚖️</div>
        <div class="card-subtitle">Gymnasium CartPole-v1 · Tabular Monte Carlo Control</div>
      </div>
      <div class="card-badge badge-purple">Monte Carlo</div>
    </div>

    <p class="card-desc">
      Compares First-Visit and Every-Visit Monte Carlo control on the CartPole balancing task. The continuous 4D observation space is discretized into a 6⁴ = 1,296-state grid before applying tabular Q-updates from complete episode trajectories.
    </p>

    <div class="env-banner">
      <span class="env-name">CartPole-v1</span>
      <span class="divider"></span>
      <span>States: 1,296 (6⁴) &nbsp;·&nbsp; Actions: 2 &nbsp;·&nbsp; Solved threshold: 195</span>
    </div>

    <div class="algo-grid">
      <div class="algo-pill">
        <span class="algo-dot dot-blue"></span>
        First-Visit Monte Carlo
      </div>
      <div class="algo-pill">
        <span class="algo-dot dot-green"></span>
        Every-Visit Monte Carlo
      </div>
      <div class="algo-pill">
        <span class="algo-dot dot-amber"></span>
        ε-greedy with exp. decay
      </div>
      <div class="algo-pill">
        <span class="algo-dot" style="background:var(--muted)"></span>
        Random policy baseline
      </div>
    </div>

    <div class="results-row">
      <div class="result-item">
        <div class="result-label">Every-Visit avg reward</div>
        <div class="result-value green">191.4</div>
        <div class="result-sub">≈ meets 195 threshold</div>
      </div>
      <div class="result-item">
        <div class="result-label">Best success rate</div>
        <div class="result-value blue">~58%</div>
        <div class="result-sub">Every-Visit at ep 4,000</div>
      </div>
      <div class="result-item">
        <div class="result-label">First-Visit avg reward</div>
        <div class="result-value purple">130.8</div>
        <div class="result-sub">success rate ~30%</div>
      </div>
      <div class="result-item">
        <div class="result-label">Random baseline</div>
        <div class="result-value" style="color:var(--muted)">~22</div>
        <div class="result-sub">never solves the task</div>
      </div>
    </div>

    <div class="findings">
      <div class="findings-title">Key findings</div>
      <ul>
        <li>Every-Visit MC converges faster — more Q-updates per episode due to revisited state-action pairs.</li>
        <li>First-Visit MC stabilises below the 195 threshold; Every-Visit nearly meets it with a mean reward of 191.4.</li>
        <li>High standard deviation (~114–157) reflects episodic instability typical of tabular methods on coarse discretization.</li>
        <li>A trained Every-Visit agent runs a verified 195-step perfect episode in the animation demo.</li>
      </ul>
    </div>
  </div>

  <!-- ALGORITHM COMPARISON -->
  <div class="compare-section">
    <div class="section-title">Algorithm comparison</div>
    <div class="project-card" style="padding:0; overflow:hidden;">
      <table class="compare-table">
        <thead>
          <tr>
            <th>Algorithm</th>
            <th>Type</th>
            <th>Update rule</th>
            <th>Behaviour</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="algo-name">Q-Learning</span></td>
            <td>Off-policy TD</td>
            <td><code style="font-family:'DM Mono',monospace;font-size:12px;color:var(--accent-green)">max Q(s',a')</code></td>
            <td>Aggressive — hits on risky borderline hands</td>
          </tr>
          <tr>
            <td><span class="algo-name">SARSA</span></td>
            <td>On-policy TD</td>
            <td><code style="font-family:'DM Mono',monospace;font-size:12px;color:var(--accent-purple)">Q(s', actual a')</code></td>
            <td>Conservative — accounts for exploratory actions</td>
          </tr>
          <tr>
            <td><span class="algo-name">First-Visit MC</span></td>
            <td>On-policy MC</td>
            <td>Update on first visit per episode</td>
            <td>Slower convergence, lower variance per episode</td>
          </tr>
          <tr>
            <td><span class="algo-name">Every-Visit MC</span></td>
            <td>On-policy MC</td>
            <td>Update on every visit per episode</td>
            <td>Faster convergence, more updates per trajectory</td>
          </tr>
          <tr>
            <td><span class="algo-name">Random Policy</span></td>
            <td>Baseline</td>
            <td>None</td>
            <td>No learning; lower-bound reference</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- TECH STACK -->
  <div class="section-title">Stack & tools</div>
  <div class="tech-stack">
    <span class="tech-tag">Python 3.8+</span>
    <span class="tech-tag">Gymnasium</span>
    <span class="tech-tag">NumPy</span>
    <span class="tech-tag">Matplotlib</span>
    <span class="tech-tag">Seaborn</span>
    <span class="tech-tag">Pandas</span>
    <span class="tech-tag">Jupyter Notebook</span>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <span class="footer-left">Reinforcement Learning Portfolio · 2 Projects</span>
    <span class="footer-right">
      <span class="pulse"></span>
      Tabular RL · Gymnasium environments
    </span>
  </div>

</div>
</body>
</html>