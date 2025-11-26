
import gymnasium as gym


def env_creator(**kwargs):
    """
    make env `BipedalWalkerHardcore-v3` from `Box2d`
    """
    try:
        return gym.make("BipedalWalkerHardcore-v3", render_mode="rgb_array")
    except AttributeError:
        raise ModuleNotFoundError("Warning: Box2d is not installed")
