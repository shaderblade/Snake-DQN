import pygame
import torch
from game import SnakeGameAI
from agent import Agent

def test():
    agent = Agent()
    agent.model.load_state_dict(torch.load('model/model.pth'))
    game = SnakeGameAI()

    while True:
        state = agent.get_state(game)
        action = agent.get_action(state, test_mode=True)
        reward, game_over, score = game.play_step(action)

        if game_over:
            print(f"\nGame over! Score: {score}\n")
            pygame.quit()
            quit()

if __name__ == '__main__':
    test()