import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state
import game_world

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10

animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/" + name + " (%d)" % i + ".png") for i in
                                       range(1, 11)]

    def __init__(self):
        positions = [(43, 750), (1118, 750), (1050, 530), (575, 220), (235, 33), (575, 220), (1050, 530), (1118, 750)]
        self.patrol_positons = []
        for p in positions:
            self.patrol_positons.append((p[0], 1024 - p[1]))
        self.patrol_order = 1
        self.target_x, self.target_y = None, None
        self.target = None
        self.x, self.y = random.randint(100, 1000), random.randint(100, 900)
        self.load_images()
        self.dir = random.random() * 2 * math.pi  # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0
        self.build_behavior_tree()
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 0

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def find_big_ball(self):
        balls = main_state.get_big_ball()
        distance = 100000000
        if len(balls) == 0:
            return BehaviorTree.FAIL
        for ball in balls:
            dist = (ball.x - self.x) ** 2 + (ball.y - self.y) ** 2
            if distance > dist:
                distance = dist
                self.dir = math.atan2(ball.y - self.y, ball.x - self.x)
                self.target = ball
                self.target_x, self.target_y = ball.x, ball.y
        return BehaviorTree.SUCCESS

    def find_small_ball(self):
        balls = main_state.get_small_ball()
        distance = 100000000
        if len(balls) == 0:
            return BehaviorTree.FAIL
        for ball in balls:
            dist = (ball.x - self.x) ** 2 + (ball.y - self.y) ** 2
            if distance > dist:
                distance = dist
                self.dir = math.atan2(ball.y - self.y, ball.x - self.x)
                self.target = ball
                self.target_x, self.target_y = ball.x, ball.y
        return BehaviorTree.SUCCESS

    def find_player(self):
        boy = main_state.get_boy()
        distance = (boy.x - self.x) ** 2 + (boy.y - self.y) ** 2
        if distance < (PIXEL_PER_METER * 10) ** 2:
            self.dir = math.atan2(boy.y - self.y, boy.x - self.x)
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def move_to_player(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        return BehaviorTree.SUCCESS
        pass

    def get_next_position(self):
        self.target_x, self.target_y = self.patrol_positons[self.patrol_order % len(self.patrol_positons)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        return BehaviorTree.SUCCESS
        pass

    def move_to_big_ball(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2
        if main_state.collide(self.target, self):
            self.hp += self.target.hp
            game_world.remove_object(self.target)
            main_state.big_ball.remove(self.target)
            # self.target, self.target.x, self.target.y = None, None, None
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        pass

    def move_to_small_ball(self):
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x) ** 2 + (self.target_y - self.y) ** 2
        if main_state.collide(self.target, self):
            self.hp += self.target.hp
            game_world.remove_object(self.target)
            main_state.small_ball.remove(self.target)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        pass

    def build_behavior_tree(self):
        find_big_ball_node = LeafNode("Find Big Ball", self.find_big_ball)
        move_to_big_ball_node = LeafNode("Move To Big Ball", self.move_to_big_ball)
        find_small_ball_node = LeafNode("Find Small Ball", self.find_small_ball)
        move_to_small_ball_node = LeafNode("Move To Small Ball", self.move_to_small_ball)
        get_big_ball_node = SequenceNode("Get Big Ball")
        get_big_ball_node.add_children(find_big_ball_node, move_to_big_ball_node)
        get_small_ball_node = SequenceNode("Get Small ball")
        get_small_ball_node.add_children(find_small_ball_node, move_to_small_ball_node)
        find_player_node = LeafNode("Find Player", self.find_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase")
        chase_node.add_children(find_player_node, move_to_player_node)

        root_node = SelectorNode("RootNode")
        root_node.add_children(get_big_ball_node, get_small_ball_node, chase_node)
        self.bt = BehaviorTree(root_node)
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        self.bt.run()
        pass

    def draw(self):
        self.font.draw(self.x - 20, self.y + 50, 'HP : %d' % self.hp, (255, 255, 0))
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)

    def handle_event(self, event):
        pass
