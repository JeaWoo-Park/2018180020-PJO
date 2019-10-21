from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, L_DASH_ON, R_DASH_ON, L_DASH_OFF, R_DASH_OFF, DASH_TIMER = range(9)

# fill here


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYDOWN, SDLK_LSHIFT): L_DASH_ON,
    (SDL_KEYDOWN, SDLK_RSHIFT): R_DASH_ON,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYUP, SDLK_LSHIFT): L_DASH_OFF,
    (SDL_KEYUP, SDLK_RSHIFT): R_DASH_OFF,
}


# Boy States
class IdleState:
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class DashState:
    @staticmethod
    def enter(boy, event):
        boy.timer = 100

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity * 2
        boy.x = clamp(25, boy.x, 800 - 25)
        if boy.timer == 0:
            boy.add_event(DASH_TIMER)

    @staticmethod
    def draw(boy):
        if boy.velocity == 3:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class RunState:
    @staticmethod
    def enter(boy, event):

        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


next_state_table = {
    # fill here
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                R_DASH_ON: IdleState, L_DASH_ON: IdleState,
                R_DASH_OFF: IdleState, L_DASH_OFF: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               R_DASH_ON: DashState, L_DASH_ON: DashState,
               R_DASH_OFF: RunState, L_DASH_OFF: RunState},
    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                L_DASH_OFF: RunState, R_DASH_OFF: RunState,
                L_DASH_ON: DashState, R_DASH_ON: DashState,
                DASH_TIMER: RunState}
}


class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        pass

    def change_state(self, state):
        # fill here
        pass

    def add_event(self, event):
        # fill here
        self.event_que.insert(0, event)
        pass

    def update(self):
        # fill here
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        # fill here
        self.cur_state.draw(self)
        pass

    def handle_event(self, event):
        # fill here
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass
