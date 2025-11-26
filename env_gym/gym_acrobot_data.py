import gymnasium as gym


def env_creator(**kwargs):
    return gym.make("Acrobot-v1")
