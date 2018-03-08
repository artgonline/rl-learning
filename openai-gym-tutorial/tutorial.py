import gym


def run_env(env_name='CartPole-v0', render=True):
    env = gym.make(env_name)
    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            if render:
                env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break


def main():
    # run_env()
    # run_env('MountainCar-v0')
    # run_env('MsPacman-v0')
    # run_env('Hopper-v2')
    run_env('Blackjack-v0', False)


if __name__ == '__main__':
    main()