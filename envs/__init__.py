from gym.envs.registration import (
    registry,
    register,
    make,
    spec,
    load_env_plugins as _load_env_plugins,
)

# Hook to load plugins from entry points
_load_env_plugins()



)

# Mujoco
# ----------------------------------------

# 2D
register(
    id="Thrower-v2",
    entry_point="gym.envs.mujoco:ThrowerEnv",
    max_episode_steps=100,
    reward_threshold=0.0,
)

register(
    id="Striker-v2",
    entry_point="gym.envs.mujoco:StrikerEnv",
    max_episode_steps=100,
    reward_threshold=0.0,
)
