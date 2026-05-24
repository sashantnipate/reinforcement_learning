# Twenty-One RL Agent 🃏

A reinforcement learning project that trains agents to play **Twenty-One** (Blackjack) using **Q-Learning** and **SARSA** on the [Gymnasium Blackjack-v1](https://gymnasium.farama.org/environments/toy_text/blackjack/) environment.

---

## Table of Contents

- [Game Overview](#game-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [Results](#results)
- [Visualizations](#visualizations)

---

## Game Overview

Twenty-One is a simplified, turn-based card-drawing game. The goal is to get your hand as close to **21 points** as possible without going over.

### Card Values

| Card Type       | Value             |
|-----------------|-------------------|
| Number cards    | Face value (2–10) |
| Face cards (J, Q, K) | 10 points    |
| Aces            | 1 or 11 (whichever helps) |

### Observation Space

The agent receives a 3-tuple at each step:

```
(player_sum, dealer_card, usable_ace)
```

| Field          | Description                                      |
|----------------|--------------------------------------------------|
| `player_sum`   | Total value of the agent's hand (e.g., 18)       |
| `dealer_card`  | The dealer's visible card (1–10)                 |
| `usable_ace`   | Whether the agent has an ace counting as 11      |

### Actions

| Action | Meaning                      |
|--------|------------------------------|
| `0`    | **Stick** – stop drawing     |
| `1`    | **Hit** – take another card  |

### Rewards

| Outcome | Reward |
|---------|--------|
| Win     | `+1`   |
| Tie     | `0`    |
| Loss    | `-1`   |

---

## Project Structure

```
twenty-one-game.ipynb   # Main notebook: environment, agents, evaluation, plots
README.md               # This file
```

---

## Installation

```bash
pip install gymnasium numpy matplotlib seaborn
```

Requires Python 3.8+.

---

## Usage

Open and run `twenty-one-game.ipynb` top-to-bottom. The notebook is organized into these sections:

1. **Environment Setup** – wraps `Blackjack-v1` as `TwentyOneEnv` and sets seeds for reproducibility.
2. **Baseline Policies** – tests a random policy and a conservative policy (stick at 17+) as baselines.
3. **State Distribution Analysis** – runs 1,000 episodes to visualize the distribution of player sums, dealer cards, usable aces, and rewards.
4. **State Mapping** – creates a discrete index mapping for the 360 possible states `(player_sum 4–21) × (dealer_card 1–10) × (usable_ace T/F)`.
5. **Agent Training** – trains both Q-Learning and SARSA agents for 50,000 episodes each.
6. **Evaluation** – evaluates both agents over 10,000 episodes and compares win rates.
7. **Visualization** – plots policy heatmaps and training metrics.

---

## Algorithms

### Q-Learning (Off-policy TD)

Updates Q-values using the **best possible** next action:

```
Q(s, a) ← Q(s, a) + α [ r + γ · max_a' Q(s', a') − Q(s, a) ]
```

Because it bootstraps from the optimal next action, Q-Learning is more aggressive — it is willing to hit on borderline hands where SARSA would stick.

### SARSA (On-policy TD)

Updates Q-values using the **actual next action** taken by the current policy:

```
Q(s, a) ← Q(s, a) + α [ r + γ · Q(s', a') − Q(s, a) ]
```

SARSA is more conservative and realistic about policy performance because it accounts for the exploratory actions the agent actually takes.

### Shared Hyperparameters

| Parameter         | Value   |
|-------------------|---------|
| Episodes          | 50,000  |
| Learning rate (α) | 0.1     |
| Discount (γ)      | 0.95    |
| Initial ε         | 0.1     |
| ε decay           | 0.9995  |
| Min ε             | 0.01    |

---

## Results

After 50,000 training episodes, both agents were evaluated over 10,000 greedy episodes:

| Agent       | Win Rate | Avg Reward |
|-------------|----------|------------|
| Q-Learning  | 42.9%    | ~+0.43     |
| SARSA       | 42.3%    | ~+0.42     |

Both exceeded the **40% win rate** benchmark for solid Twenty-One play.

**Key policy differences:**
- Both agents always **STICK** on sums 18–21 and **HIT** on sums 4–11.
- Q-Learning takes riskier hits on borderline hands (e.g., sum of 19 with a usable ace vs. dealer 9/10).
- SARSA is more conservative on borderline decisions, reflecting on-policy caution.

---

## Visualizations

The notebook generates:

- **Player sum distribution** – histogram of states visited during training.
- **Dealer card distribution** – histogram of dealer face-up cards encountered.
- **Usable ace frequency** – pie chart of ace availability.
- **Reward distribution** – histogram of episode outcomes.
- **Policy heatmaps** – Hit/Stick decisions across all states, split by usable ace.
- **Training metrics** – rolling average reward, Q-value delta (log scale), epsilon decay, and rolling win rate.
