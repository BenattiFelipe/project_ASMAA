Authors:
Fábio Bassoi Sayeg 101753
Felipe Benatti 101751



The project was done in python (version 3.8.6). The libraries used that might need installation were:
Pygame
numpy
math
random
mateplotlib
datetime

To run the project, just run the command "python main_game.py". It will ask the number of cars in the simulation (500, for example). It will also ask about the flow. For this project, we used:
45: High flow
75: Average Flow
125: Low flow

At the end of the simulation, type 1 to plot the graphs. They will be saved on the directory "Results".

Reinforcement Learning Library:

To use the environment of the reinforcement learning agents, you need to run:

pip install highway-env
pip install gym pyvirtualdisplay
git clone https://github.com/eleurent/rl-agents
pip install rl-agents
cd rl-agents/scripts
python experiments.py evaluate <env> \
                               <agent \
                               --train --episodes=<n_episodes>

For example:
python experiments.py evaluate configs/IntersectionEnv/env_multi_agent.json \
                               configs/IntersectionEnv/agents/DQNAgent/ego_attention_2h.json \
                               --train --episodes=3000
python experiments.py evaluate configs/HighwayEnv/env_multi_agent.json \
                               configs/HighwayEnv/agents/DQNAgent/dqn.json \
                               --train --episodes=3000

To run the code the same way we did, you have to change the file "env_multi_agent.json" with the following changes:

"controlled_vehicles": 4, 
"observation_config": {"vehicles_count": 0,}
"observation_config": {
            "type": "OccupancyGrid",}

or

"observation_config": {
            "type": "Kinematics",}



