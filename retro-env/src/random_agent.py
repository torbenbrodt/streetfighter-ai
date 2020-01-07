import retro


# https://retro.readthedocs.io/en/latest/getting_started.html
# Random agent

def main():
    env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis')
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            obs = env.reset()
    env.close()


if __name__ == "__main__":
    main()