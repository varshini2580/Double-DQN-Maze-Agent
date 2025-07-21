# Double-DQN-Maze-Agent
A reinforcement learning project where an agent learns to navigate a maze using a Deep Q-Network (DQN).
The agent is trained using a neural network with 2 hidden layers (128 neurons each) to estimate Q-values for each action, allowing it to efficiently explore and reach the goal.

Features
Custom Gym Maze Environment (envs/maze_env.py)

DQN Agent with 2 Hidden Layers (128 neurons each) (agents/dqn_agent.py)

Training Pipeline with experience replay and target network (connected_maze_training.py)

Pre-trained Model included (dqn_model.pth)

Configurable Maze Layouts (maze_grid.npy, source_destination.npy)

Visualization of Learning Metrics (rewards, returns, epsilon decay, TD error)
Project Structure
simulations/
│── agents/
│   └── dqn_agent.py        # DQN Agent with 2-layer NN (128 neurons each)
│   └── models/             # Pre-trained models (.pth)
│── envs/
│   └── maze_env.py         # Custom Gym environment for maze navigation
│── Utils/
│   └── utils.py            # Helper functions
│── connected_maze_training.py  # Training script for DQN agent
│── maze_simulation.py          # Run trained agent in maze
│── maze_grid.npy               # Maze grid configuration
│── source_destination.npy      # Start and goal positions
│── plots/                      # Training plots (rewards, TD error, etc.)
│── config.json                 # Training and environment configs

Neural Network Architecture
The DQN Agent’s Q-network:

Input Layer: Encodes maze state (grid-based features).

Hidden Layer 1: 128 neurons, ReLU activation.

Hidden Layer 2: 128 neurons, ReLU activation.

Output Layer: Q-values for each possible action.

Optimizer: Adam with learning rate from config.json.
