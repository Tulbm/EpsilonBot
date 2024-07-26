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

      await self.distribute_workers() #idle workers
      if self.townhalls: #at least one nexus
         nexus = self.townhalls.random  
         if nexus.is_idle and self.can_afford(UnitTypeId.PROBE):
             nexus.train(UnitTypeId.PROBE)
             
         elif self.supply_left < 3 and self.already_pending(UnitTypeId.PYLON) == 0: #pylons
            if self.can_afford(UnitTypeId.PYLON):
               if self.structures(UnitTypeId.PYLON).amount == 0:  #first pylon
                  await self.build(UnitTypeId.PYLON,near=nexus)  
               else:
                  target_pylon = self.structures(UnitTypeId.PYLON).closest_to(self.enemy_start_locations[0]) #pylon closes to the enemy
                  pos = target_pylon.position.towards(self.enemy_start_locations[0], random.randrange(8, 15))
                  await self.build(UnitTypeId.PYLON, near=pos)

         elif not self.structures(UnitTypeId.GATEWAY):  
            if self.can_afford(UnitTypeId.GATEWAY):
               target_pylon = self.structures(UnitTypeId.PYLON).random
               await self.build(UnitTypeId.GATEWAY,near=target_pylon)

         elif self.structures(UnitTypeId.GATEWAY)      

      else: #if no nexus
         if self.can_afford(UnitTypeId.NEXUS): 
                await self.expand_now()  
      




run_game(
   maps.get("AbyssalReefLE"),
   [Bot(Race.Protoss, epsilon()),
    Computer(Race.Zerg, Difficulty.Easy)],
    realtime=False,
)


