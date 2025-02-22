from sample_factory.launcher.run_description import RunDescription, Experiment, ParamGrid
from swarm_rl.runs.single_quad.baseline import QUAD_BASELINE_CLI

_params = ParamGrid([
    ('seed', [1111, 0000, 2222, 3333]),
])

SINGLE_CLI = QUAD_BASELINE_CLI + (
    ' --with_wandb=False --wandb_project=Quad-Swarm-RL --wandb_group=single --wandb_user=multi-drones'
)

_experiment = Experiment(
    'single',
    SINGLE_CLI,
    _params.generate_params(randomize=False),
)

RUN_DESCRIPTION = RunDescription('paper_quads_multi_mix_baseline_8a_attn_v116', experiments=[_experiment])
print(RUN_DESCRIPTION)
print(RUN_DESCRIPTION.experiments[0].cmd)  # Выведет полную команду запуска
print(RUN_DESCRIPTION.experiments[0].params)  # Выведет все параметры


# Command to use this script on local machine: Please change num_workers to the physical cores of your local machine
# python -m sample_factory.launcher.run --run=swarm_rl.runs.quad_multi_mix_baseline --backend=processes --max_parallel=4 --pause_between=1 --experiments_per_gpu=1 --num_gpus=4
