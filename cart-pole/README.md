# CartPole Balance — Monte Carlo Reinforcement Learning

A comparison of **Random Policy**, **First-Visit Monte Carlo**, and **Every-Visit Monte Carlo** control methods applied to the classic [CartPole-v1](https://gymnasium.farama.org/environments/classic_control/cart_pole/) reinforcement learning benchmark.

---

## Environment

| Property | Value |
|---|---|
| Environment | [`CartPole-v1`](https://gymnasium.farama.org/environments/classic_control/cart_pole/) |
| Library | [`Gymnasium`](https://gymnasium.farama.org/) (OpenAI Gym successor) |
| Action Space | Discrete(2) — push cart **left** or **right** |
| Observation Space | Box(4,) — cart position, cart velocity, pole angle, pole angular velocity |
| Solved Threshold | Average reward ≥ **195** over 100 consecutive episodes |
| Max Episode Length | 500 steps |

The agent observes a 4-dimensional continuous state vector and must keep a pole balanced upright on a moving cart by applying left/right forces.

---

## Approach

Because the observation space is continuous, the state is first **discretized** into a finite grid before applying tabular Q-learning via Monte Carlo methods.

### State Discretization

Each of the 4 state dimensions is binned into 6 intervals using `np.linspace`:

| Dimension | Range | Bins |
|---|---|---|
| Cart position | [-4.8, 4.8] | 6 |
| Cart velocity | [-3.0, 3.0] | 6 |
| Pole angle | [-0.42, 0.42] | 6 |
| Pole angular velocity | [-3.0, 3.0] | 6 |

This yields **1,296 total discrete states** (6⁴), each mapped to a flat integer index. The Q-table is therefore a `(1296, 2)` array.

### Exploration Strategy

Epsilon-greedy exploration with exponential decay:

```
ε ← max(ε_min, ε × decay_rate)
```

Training hyperparameters used:

| Parameter | Value |
|---|---|
| Initial ε | 0.95 |
| Min ε | 0.05 |
| Decay rate | 0.999 |
| Discount factor γ | 0.99 |
| Learning rate α | 0.05 |
| Episodes | 5,000 |

---

## Algorithms

### 1. Random Policy (Baseline)
Actions are chosen uniformly at random. No learning occurs. Serves as the lower-bound baseline.

### 2. First-Visit Monte Carlo
After each episode, returns are computed backwards. The Q-value for a `(state, action)` pair is updated **only on its first visit** within the episode:

```
G ← r_t + γ·G
Q(s,a) ← Q(s,a) + α·(G − Q(s,a))   [first visit only]
```

### 3. Every-Visit Monte Carlo
Same as above, but Q-values are updated **every time** a `(state, action)` pair is encountered in the episode — including revisits. This produces more updates per episode and generally converges faster in practice.

```
G ← r_t + γ·G
Q(s,a) ← Q(s,a) + α·(G − Q(s,a))   [every visit]
```

---

## Results

### Per-Method Summary (5,000 episodes, seed=42)

| Method | Mean Reward | Std Dev | Overall Success Rate |
|---|---|---|---|
| Random Policy | ~22 | — | 0.0% |
| First-Visit MC | 130.77 | ±114.20 | 21.4% |
| Every-Visit MC | **191.38** | ±157.37 | **39.9%** |

### Training Progression

**First-Visit Monte Carlo**

| Episode | Avg Reward | Success Rate |
|---|---|---|
| 1,000 | 55.92 | 2.1% |
| 2,000 | 120.65 | 18.0% |
| 3,000 | 159.26 | 28.1% |
| 4,000 | 160.41 | 28.5% |
| 5,000 | 157.61 | 30.3% |

**Every-Visit Monte Carlo**

| Episode | Avg Reward | Success Rate |
|---|---|---|
| 1,000 | 61.38 | 3.9% |
| 2,000 | 142.29 | 26.6% |
| 3,000 | 248.14 | 53.8% |
| 4,000 | 260.40 | 58.3% |
| 5,000 | 244.67 | 56.7% |

### Key Takeaways

- **Random policy** plateaus at ~22 reward and never solves the task.
- **First-Visit MC** learns meaningfully but stabilises below the 195 threshold, reaching ~30% success by episode 5,000.
- **Every-Visit MC** is the clear winner: it breaks the 195 threshold in terms of rolling average reward around episode 3,000 and peaks near 58–60% success rate. Its mean reward of 191.38 almost exactly meets the official "solved" criterion.
- The **high standard deviation** in both MC methods (~114–157) reflects the episodic instability typical of tabular methods on a coarsely discretized state space — some episodes the pole is balanced for the full 195 steps, others it falls quickly.
- A trained Every-Visit MC agent was verified to run a **perfect 195-step episode** in the animation demo.

---

## Project Structure

```
.
├── notebook.ipynb          # Main experiment notebook
├── create_animation.py     # visualize_episode() helper for rendering trained policy
└── README.md
```

---

## Setup & Usage

```bash
pip install gymnasium numpy pandas matplotlib
```

Run the notebook top-to-bottom. The key function calls are:

```python
# Baseline
random_policy_stats = test_random_policy_cartpole(n_episode=5000, seed=42)

# First-Visit Monte Carlo
fv_mc_stats = train_monte_carlo_cartpole(bins, q_table, first_visit=True, ...)

# Every-Visit Monte Carlo
ev_mc_stats = train_monte_carlo_cartpole(bins, q_table, first_visit=False, ...)

# Visualise the trained agent
animation = visualize_episode(ev_mc_stats['q_table'], bins, seed=42, max_frames=195)
```

---

## Real-World Applications

The Monte Carlo RL framework demonstrated here — discrete state representation, episodic learning, and Q-table updates from complete trajectories — maps directly onto several real-world problem domains:

### 🤖 Robotics & Control
CartPole is a simplified inverted pendulum. The same discretize-and-learn approach applies to **drone stabilisation**, **robotic arm joint control**, and **bipedal walking gaits**, where the goal is to keep a system within stable bounds using corrective actions.

### 🏭 Industrial Process Control
Manufacturing processes (e.g. temperature regulation in chemical reactors, CNC machine calibration) involve continuous sensor readings and discrete corrective actions — an almost direct analogue. Monte Carlo methods are particularly suited here because full production cycles (episodes) can be simulated before deployment.

### 💹 Algorithmic Trading
A trading agent observes market features (price momentum, volatility, volume) — continuous state — and takes discrete actions (buy, hold, sell). Episodic Monte Carlo updates fit naturally with daily/weekly trading windows, updating value estimates from complete trade trajectories.

### 🏥 Clinical Treatment Planning
Personalized medicine research uses RL to find optimal treatment sequences (drug dosing, radiation scheduling). Each patient's treatment course is a natural episode, and Monte Carlo updates allow learning from retrospective patient outcome data before clinical deployment.

### 🎮 Game Playing & Simulation
Beyond CartPole, this exact pipeline — discretise → Q-table → ε-greedy MC — is the foundation for early game-playing agents (e.g. Blackjack solvers, board game AI). Scaling up with neural networks in place of the Q-table leads to Deep Q-Networks (DQN), the approach behind AlphaGo and Atari agents.

### 🚦 Traffic Signal Control
Intersections can be framed as sequential decision problems: the state is traffic queue lengths (discretized), and actions are signal phase choices. Episodes correspond to traffic simulation runs, making Monte Carlo a natural fit for offline policy learning before live deployment.

---

## Limitations & Next Steps

- The coarse 6-bin discretization loses information; finer bins or **tile coding** would improve performance.
- Monte Carlo requires **complete episodes** before any learning — TD methods (Q-learning, SARSA) learn online and are more sample-efficient.
- Tabular methods don't scale beyond ~few thousand states; **Deep Q-Networks (DQN)** or **PPO** would handle higher-dimensional problems.
- High variance in results suggests that **n-step returns** or **eligibility traces** (TD(λ)) could stabilise learning.

---

## References

- [Gymnasium CartPole-v1 Documentation](https://gymnasium.farama.org/environments/classic_control/cart_pole/)
- [Gymnasium Official Docs](https://gymnasium.farama.org/)
- Sutton & Barto, *Reinforcement Learning: An Introduction* (2nd ed.) — [free PDF](http://incompleteideas.net/book/the-book-2nd.html)
- [OpenAI Spinning Up — Key Concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html)