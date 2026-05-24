"""
create_animation.py - CartPole Animation Python Script

This script provides functions to create animations of trained CartPole agents.
"""

import gc
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

def discretize_state(state, bins):
    """Discretize continuous state into discrete state"""
    discrete_indices = []
    for i, value in enumerate(state):
        # Clamp value to bin range
        clamped_value = np.clip(value, bins[i][0], bins[i][-1])
        bin_index = np.digitize(clamped_value, bins[i]) - 1
        bin_index = max(0, min(bin_index, len(bins[i]) - 2))
        discrete_indices.append(bin_index)

    discrete_state = 0
    multiplier = 1
    for i, idx in enumerate(discrete_indices):
        discrete_state += idx * multiplier
        multiplier *= (len(bins[i]) - 1) 
    
    return discrete_state


def run_episode_with_visualization(q_table, bins, render_mode='rgb_array', seed=None, max_frames=200):
    """Run a single episode and collect data for visualization with memory optimization"""
    env = gym.make("CartPole-v1", render_mode=render_mode)
    state, info = env.reset(seed=seed)
    
    # Data collection with memory limits
    frames = []
    
    done = False
    total_reward = 0
    step = 0
    
    while not done and step < min(500, max_frames):  # Limit frames to prevent memory issues
        discrete_state = discretize_state(state, bins)
        
        # Use trained policy (greedy action selection)
        if discrete_state < len(q_table):  
            action = np.argmax(q_table[discrete_state])
        else:
            action = env.action_space.sample()  # Random if state out of bounds
        
        # Take action
        next_state, reward, terminated, truncated, info = env.step(action)
        
        # Capture frame for animation
        if render_mode == 'rgb_array':
            frame = env.render()
            frame = frame.astype(np.uint8)
            frames.append(frame)
        
        total_reward += reward
        
        done = terminated or truncated
        state = next_state
        step += 1
    
    env.close()
    
    return {
        'frames': frames,
        'total_reward': total_reward,
        'episode_length': step
    }


def create_lightweight_animation(episode_data, interval=100, figsize=(6, 4)):
    """Create a memory-efficient animated visualization"""
    frames = episode_data['frames']
    
    if not frames:
        print("No frames available for animation. Make sure render_mode='rgb_array'")
        return None
    
    # Use smaller figure size to reduce memory
    fig, ax = plt.subplots(figsize=figsize)
    ax.axis('off')
    
    # Display first frame
    im = ax.imshow(frames[0])
    
    def animate(frame_idx):
        im.set_array(frames[frame_idx])
        ax.set_title(f'Step {frame_idx + 1}/{len(frames)} | Reward: {episode_data["total_reward"]}')
        return [im]
    
    # Use longer interval to reduce rendering load
    anim = FuncAnimation(fig, animate, frames=len(frames), 
                        interval=interval, blit=True, repeat=True)
    
    plt.tight_layout()
    return anim


def visualize_episode(q_table, bins, seed=None, max_frames=150, save_path=None):
    """Create animation of trained policy
    
    Args:
        q_table: The trained Q-table
        bins: List of bin arrays for discretizing state space
        seed: Random seed for episode
        max_frames: Maximum number of frames to capture
        save_path: Optional path to save animation as HTML
    """
    n_states = len(q_table)
    print(f"Running episode with trained policy (seed: {seed}, max_frames: {max_frames})...")
    print(f"Using {n_states:,} total discrete states")
    
    # Force garbage collection before starting
    gc.collect()
    
    episode_data = run_episode_with_visualization(q_table, bins, seed=seed, max_frames=max_frames)
    
    print(f"Episode length: {episode_data['episode_length']}")
    print(f"Total reward: {episode_data['total_reward']}")
    
    # Create animation
    anim = create_lightweight_animation(episode_data)
    
    if anim:
        # Save animation as HTML if path provided
        if save_path:
            print(f"Saving animation to {save_path}...")
            if not save_path.endswith('.html'):
                save_path = save_path + '.html'
            
            # Save as HTML with controls
            html_content = anim.to_jshtml()
            with open(save_path, 'w') as f:
                f.write(html_content)
            print(f"Animation saved as {save_path} with pause/play controls!")
        
        # Display animation in Jupyter
        html_anim = HTML(anim.to_jshtml())
        plt.close()  # Close the figure to avoid duplicate display
        
        # Clean up episode data from memory
        del episode_data
        gc.collect()
        
        return html_anim
    
    return None


def visualize_key_frames(q_table, bins, seed=None, num_frames=5):
    """
    Args:
        q_table: The trained Q-table
        bins: List of bin arrays for discretizing state space
        seed: Random seed for episode
        num_frames: Number of key frames to show
    """
    episode_data = run_episode_with_visualization(q_table, bins, seed=seed, max_frames=100)
    frames = episode_data['frames']
    
    if not frames:
        print("No frames available")
        return
    
    # Select evenly spaced frames
    indices = np.linspace(0, len(frames)-1, num_frames).astype(int)
    
    fig, axes = plt.subplots(1, num_frames, figsize=(15, 3))
    if num_frames == 1:
        axes = [axes]
    
    for i, idx in enumerate(indices):
        axes[i].imshow(frames[idx])
        axes[i].set_title(f'Step {idx+1}\nReward: {episode_data["total_reward"]}')
        axes[i].axis('off')
    
    plt.suptitle(f'Episode Performance: {episode_data["episode_length"]} steps, {episode_data["total_reward"]} total reward')
    plt.tight_layout()
    plt.show()
    
    # Clean up
    del episode_data
    gc.collect()