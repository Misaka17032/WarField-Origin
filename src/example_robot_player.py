from warfield import *
import random
import time

random.seed(25252 + int(time.time() * 1000) % 1000)

class RobotPlayer(object):
	spawnable_robot = [RobotType("troop"), RobotType("miner"), RobotType("drone")]
	directions = [Direction.north(), Direction.north(), Direction.north_east(), Direction.east(), Direction.south_east(), Direction.south(), Direction.south_west(), Direction.west(), Direction.north_west()]
	
	def __init__(self):
		super(RobotPlayer, self).__init__()
		self.turn_count = 0

	def run(self, rc):
		self.turn_count += 1
		if rc.get_type().robot_type == "base":
			self.run_base(rc)
		elif rc.get_type().robot_type == "troop":
			self.run_troop(rc)
		elif rc.get_type().robot_type == "miner":
			self.run_miner(rc)
		else:
			self.run_drone(rc)
		return rc

	def run_base(self, rc):
		to_build = self.random_spawnable_robot_type()
		energy = 50
		for dir in self.directions:
			if rc.can_build_robot(to_build, dir, energy):
				rc.build_robot(to_build, dir, energy)
				break
		if rc.can_charge(1):
			rc.charge(1)

	def run_troop(self, rc):
		enemy = rc.get_team().opponent()
		action_radius = rc.get_type().action_radius
		attackable = rc.sense_nearby_robots(radius=action_radius, team=enemy)
		if attackable != [] and rc.can_invade(action_radius):
			rc.invade(action_radius)
		self.try_move(rc, self.random_direction())

	def run_miner(self, rc):
		self.try_move(rc, self.random_direction())

	def run_drone(self, rc):
		enemy = rc.get_team().opponent()
		action_radius = rc.get_type().action_radius
		for scanner in rc.sense_nearby_robots(radius=action_radius, team=enemy):
			if scanner.type.robot_type == "miner":
				if rc.can_analyze(scanner.location):
					rc.analyze(scanner.location)
					break
		self.try_move(rc, self.random_direction())
			
	def random_direction(self):
		return random.choice(self.directions)

	def random_spawnable_robot_type(self):
		return random.choice(self.spawnable_robot)

	def try_move(self, rc, dir):
		if rc.can_move(dir):
			rc.move(dir)
			return True
		else:
			return False