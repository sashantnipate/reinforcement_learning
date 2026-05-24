# Reinforcement Learning Portfolio

> Two independent RL experiments exploring tabular methods — from Q-Learning and SARSA on a card game, to Monte Carlo control on a classic control benchmark.

| Projects | Algorithms | Training Episodes | Best Win Rate |
|----------|------------|-------------------|---------------|
| 2 | 5 | 55,000+ | ~43% |

---

## Projects

### 01 — Twenty-One RL Agent 🃏
**Environment:** Gymnasium `Blackjack-v1` · Tabular TD Control

Trains two temporal-difference agents — Q-Learning and SARSA — to play Blackjack across 50,000 episodes. The environment provides a 3-tuple observation `(player_sum, dealer_card, usable_ace)` over 360 discrete states and two actions: hit or stick.

**Environment specs:** States: 360 · Actions: 2 · Rewards: {−1, 0, +1}

**Algorithms used:**
- Q-Learning (off-policy)
- SARSA (on-policy)
- ε-greedy exploration
- Random & Conservative baselines

#### Results

| Metric | Value | Notes |
|--------|-------|-------|
| Q-Learning win rate | **42.9%** | avg reward ≈ +0.43 |
| SARSA win rate | **42.3%** | avg reward ≈ +0.42 |
| Training episodes | 50,000 | eval over 10K greedy episodes |
| Learning rate α | 0.1 | γ = 0.95, ε → 0.01 |

#### Key Findings

- Both agents always stick on sums 18–21 and hit on 4–11, consistent with basic strategy.
- Q-Learning takes riskier hits on borderline hands (e.g. sum 19, usable ace vs dealer 9/10) because it bootstraps from the greedy next action.
- SARSA is more conservative on borderline decisions, accounting for exploratory actions it actually takes during training.
- Both exceed the 40% win-rate benchmark for solid Blackjack play.

---

### 02 — CartPole Balance — Monte Carlo RL ⚖️
**Environment:** Gymnasium `CartPole-v1` · Tabular Monte Carlo Control

Compares First-Visit and Every-Visit Monte Carlo control on the CartPole balancing task. The continuous 4D observation space is discretized into a 6⁴ = 1,296-state grid before applying tabular Q-updates from complete episode trajectories.

**Environment specs:** States: 1,296 (6⁴) · Actions: 2 · Solved threshold: 195

**Algorithms used:**
- First-Visit Monte Carlo
- Every-Visit Monte Carlo
- ε-greedy with exponential decay
- Random policy baseline

#### Results

| Metric | Value | Notes |
|--------|-------|-------|
| Every-Visit avg reward | **191.4** | ≈ meets 195 threshold |
| Best success rate | **~58%** | Every-Visit at episode 4,000 |
| First-Visit avg reward | **130.8** | success rate ~30% |
| Random baseline | ~22 | never solves the task |

#### Key Findings

- Every-Visit MC converges faster — more Q-updates per episode due to revisited state-action pairs.
- First-Visit MC stabilises below the 195 threshold; Every-Visit nearly meets it with a mean reward of 191.4.
- High standard deviation (~114–157) reflects episodic instability typical of tabular methods on coarse discretization.
- A trained Every-Visit agent runs a verified 195-step perfect episode in the animation demo.

---

## Algorithm Comparison

| Algorithm | Type | Update Rule | Behaviour |
|-----------|------|-------------|-----------|
| Q-Learning | Off-policy TD | `max Q(s', a')` | Aggressive — hits on risky borderline hands |
| SARSA | On-policy TD | `Q(s', actual a')` | Conservative — accounts for exploratory actions |
| First-Visit MC | On-policy MC | Update on first visit per episode | Slower convergence, lower variance per episode |
| Every-Visit MC | On-policy MC | Update on every visit per episode | Faster convergence, more updates per trajectory |
| Random Policy | Baseline | None | No learning; lower-bound reference |

---

## Stack & Tools

`Python 3.8+` · `Gymnasium` · `NumPy` · `Matplotlib` · `Seaborn` · `Pandas` · `Jupyter Notebook`

---

*Reinforcement Learning Portfolio · 2 Projects · Tabular RL · Gymnasium Environments*
