#!/bin/bash

python -m swarm_rl.train \
--env=quadrotor_multi \
--train_for_env_steps=1000000000 \
--algo=APPO \
--use_rnn=False \
--num_workers=2 \
--num_envs_per_worker=8 \
--learning_rate=0.0001 \
--ppo_clip_value=5.0 \
--recurrence=1 \
--nonlinearity=tanh \
--actor_critic_share_weights=False \
--policy_initialization=xavier_uniform \
--adaptive_stddev=False \
--with_vtrace=False \
--max_policy_lag=100000000 \
--rnn_size=256 \
--with_pbt=False \
--gae_lambda=1.00 \
--max_grad_norm=5.0 \
--exploration_loss_coeff=0.0 \
--rollout=128 \
--batch_size=1024 \
--quads_use_numba=True \
--quads_num_agents=1 \
--quads_mode=static_same_goal \
--quads_episode_duration=15.0 \
--quads_neighbor_encoder_type=no_encoder \
--quads_neighbor_hidden_size=0 \
--quads_neighbor_obs_type=none \
--quads_neighbor_visible_num=0 \
--replay_buffer_sample_prob=0.75 \
--anneal_collision_steps=300000000 \
--normalize_input=False \
--normalize_returns=False \
--reward_clip=10.0 \
--save_milestones_sec=3600

#!/bin/bash

# Запуск с seed=0
python -m swarm_rl.train --env=quadrotor_multi --train_for_env_steps=1000000000 --algo=APPO --use_rnn=False --num_workers=2 --num_envs_per_worker=8 --learning_rate=0.0001 --ppo_clip_value=5.0 --recurrence=1 --nonlinearity=tanh --actor_critic_share_weights=False --policy_initialization=xavier_uniform --adaptive_stddev=False --with_vtrace=False --max_policy_lag=100000000 --rnn_size=256 --with_pbt=False --gae_lambda=1.00 --max_grad_norm=5.0 --exploration_loss_coeff=0.0 --rollout=128 --batch_size=1024 --quads_use_numba=True --quads_num_agents=1 --quads_mode=static_same_goal --quads_episode_duration=15.0 --quads_neighbor_encoder_type=no_encoder --quads_neighbor_hidden_size=0 --quads_neighbor_obs_type=none --quads_neighbor_visible_num=0 --replay_buffer_sample_prob=0.75 --anneal_collision_steps=300000000 --normalize_input=False --normalize_returns=False --reward_clip=10.0 --save_milestones_sec=3600 --with_wandb=False --wandb_project=Quad-Swarm-RL --wandb_group=single --wandb_user=multi-drones --seed=0 --experiment=test_seed0

# Запуск с seed=1111
python -m swarm_rl.train --env=quadrotor_multi --train_for_env_steps=1000000000 --algo=APPO --use_rnn=False --num_workers=2 --num_envs_per_worker=8 --learning_rate=0.0001 --ppo_clip_value=5.0 --recurrence=1 --nonlinearity=tanh --actor_critic_share_weights=False --policy_initialization=xavier_uniform --adaptive_stddev=False --with_vtrace=False --max_policy_lag=100000000 --rnn_size=256 --with_pbt=False --gae_lambda=1.00 --max_grad_norm=5.0 --exploration_loss_coeff=0.0 --rollout=128 --batch_size=1024 --quads_use_numba=True --quads_num_agents=1 --quads_mode=static_same_goal --quads_episode_duration=15.0 --quads_neighbor_encoder_type=no_encoder --quads_neighbor_hidden_size=0 --quads_neighbor_obs_type=none --quads_neighbor_visible_num=0 --replay_buffer_sample_prob=0.75 --anneal_collision_steps=300000000 --normalize_input=False --normalize_returns=False --reward_clip=10.0 --save_milestones_sec=3600 --with_wandb=False --wandb_project=Quad-Swarm-RL --wandb_group=single --wandb_user=multi-drones --seed=1111 --experiment=test_seed1111

# Запуск с seed=2222
python -m swarm_rl.train --env=quadrotor_multi --train_for_env_steps=1000000000 --algo=APPO --use_rnn=False --num_workers=2 --num_envs_per_worker=8 --learning_rate=0.0001 --ppo_clip_value=5.0 --recurrence=1 --nonlinearity=tanh --actor_critic_share_weights=False --policy_initialization=xavier_uniform --adaptive_stddev=False --with_vtrace=False --max_policy_lag=100000000 --rnn_size=256 --with_pbt=False --gae_lambda=1.00 --max_grad_norm=5.0 --exploration_loss_coeff=0.0 --rollout=128 --batch_size=1024 --quads_use_numba=True --quads_num_agents=1 --quads_mode=static_same_goal --quads_episode_duration=15.0 --quads_neighbor_encoder_type=no_encoder --quads_neighbor_hidden_size=0 --quads_neighbor_obs_type=none --quads_neighbor_visible_num=0 --replay_buffer_sample_prob=0.75 --anneal_collision_steps=300000000 --normalize_input=False --normalize_returns=False --reward_clip=10.0 --save_milestones_sec=3600 --with_wandb=False --wandb_project=Quad-Swarm-RL --wandb_group=single --wandb_user=multi-drones --seed=2222 --experiment=test_seed2222

# Запуск с seed=3333
python -m swarm_rl.train --env=quadrotor_multi --train_for_env_steps=1000000000 --algo=APPO --use_rnn=False --num_workers=2 --num_envs_per_worker=8 --learning_rate=0.0001 --ppo_clip_value=5.0 --recurrence=1 --nonlinearity=tanh --actor_critic_share_weights=False --policy_initialization=xavier_uniform --adaptive_stddev=False --with_vtrace=False --max_policy_lag=100000000 --rnn_size=256 --with_pbt=False --gae_lambda=1.00 --max_grad_norm=5.0 --exploration_loss_coeff=0.0 --rollout=128 --batch_size=1024 --quads_use_numba=True --quads_num_agents=1 --quads_mode=static_same_goal --quads_episode_duration=15.0 --quads_neighbor_encoder_type=no_encoder --quads_neighbor_hidden_size=0 --quads_neighbor_obs_type=none --quads_neighbor_visible_num=0 --replay_buffer_sample_prob=0.75 --anneal_collision_steps=300000000 --normalize_input=False --normalize_returns=False --reward_clip=10.0 --save_milestones_sec=3600 --with_wandb=False --wandb_project=Quad-Swarm-RL --wandb_group=single --wandb_user=multi-drones --seed=3333 --experiment=test_seed3333
