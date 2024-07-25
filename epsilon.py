from sc2.bot_ai import BotAI  # parent class we inherit from
from sc2.data import Difficulty, Race  # difficulty for bots, race for the 1 of 3 races
from sc2.main import run_game  # function that facilitates actually running the agents in games
from sc2.player import Bot, Computer  #wrapper for whether or not the agent is one of your bots, or a "computer" player
from sc2 import maps  # maps method for loading maps to play in.
from sc2.ids.unit_typeid import UnitTypeId
import random
import math
import numpy as np
import sys
import pickle
import time


class epsilon(BotAI):  #base bot
   async def on_step(self, iteration: int): 
      print(f"iteration #{iteration}")

run_game(
   maps.get("AbyssalReefLE"),
   [Bot(Race.Protoss, epsilon()),
    Computer(Race.Zerg, Difficulty.Easy)],
    realtime=False,
)

