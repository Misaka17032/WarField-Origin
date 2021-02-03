## RobotController

### 方法

#### def adjacent_location(self, dir):

返回自身位置向目标方向移动后的位置（MapLacation）

#### def charge(self, energy):

设定基地充能数量

#### def build_robot(self, type, dir, energy):

花费（int）点能量在（Direction）方向建造（RobotType）种类的机器人

#### def can_charge(self, energy):

返回True或False，判断是否可以充指定数量的能量

#### def can_build_robot(self, type, dir, energy):

返回True或False，判断是否可以花费（int）点能量在（Direction）方向建造（RobotType）种类的机器人

#### def can_detect_location(self, loc):

返回True或False，判断是否可以探测目标位置

#### def can_detect_radius(self, radius):

返回True或False，判断是否可以探测目标距离

#### def can_invade(self, radius):

返回True或False，判断是否可以入侵目标距离

#### def can_analyze(self, temp):

返回True或False，判断是否可以分析目标距离

#### def can_get_flag(self, ID):

返回True或False，判断是否可以获得指定ID机器人的旗帜

#### def can_move(self, dir):

返回True或False，判断是否可以向目标方向（Direction）移动

#### def can_sense_location(self, loc):

返回True或False，判断是否可以感知目标位置

#### def can_sense_radius(self, radius):

返回True或False，判断是否可以感知目标距离

#### def can_sense_robot(self, ID):

返回True或False，判断是否可以感知指定ID的机器人

#### def can_set_flag(self, flag):

返回True或False，判断是否可以改变自身旗帜颜色至指定值

#### def detect_nearby_robots(self, radius):

返回一个list\[\]，包括了指定半径内所有机器人的位置（MapLocation）

#### def invade(self, radius):

在指定半径发动入侵

#### def analyze(self, temp):

分析指定位置（MapLocation）或者指定ID的机器人

#### def get_defence(self):

返回自身的防护值

#### def get_cooldown_turns(self):

返回自身还有几回合才可以行动

#### def get_invade_factor(self, team, rounds):

返回指定队伍（Team）在指定轮数时的入侵增益

#### def get_flag(self, ID):

返回目标ID的机器人的旗帜颜色

#### def get_ID(self):

返回自身的ID

#### def get_energy(self):

返回自身的能量值

#### def get_location(self):

返回自身的位置（MapLocation）

#### def get_round_num(self):

返回当前的轮数

#### def get_team(self):

返回自身的队伍（Team）

#### def get_charge_point(self):

返回自己队伍的能量点

#### def get_type(self):

返回自身的类型（RobotType）

#### def is_location_occupied(self, loc):

返回True或False，判断目标位置是否被机器人占领

#### def is_ready(self):

返回True或False，判断自身的冷却值是否小于1

#### def move(self, dir):

向指定的方向（Direction）移动

#### def on_the_map(self, loc):

返回True或False，判断目标位置是否在地图上

#### def resign(self):

投降

#### def sense_nearby_robots(self, center=None, radius=None, team=None):

返回一个list\[\]，包含了以（MapLocation）为中心，以（int）为半径，团队属于（Team）的所有机器人（RobotInfo）

#### def sense_passability(self, loc):

返回目标位置的可通过性

#### def sense_robot(self, ID):

返回目标ID的机器人的信息（RobotInfo）

#### def sense_robot_at_location(self, loc):

返回目标位置上的机器人的信息（RobotInfo）

#### def set_flag(self, flag):

改变自身的旗帜颜色至指定值
