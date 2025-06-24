from enum import Enum
import pygame as pg


class Action(Enum):
    JUMP = 'jump'
    JUMP_STOP = 'jump_stop'
    LEFT = 'left'
    LEFT_STOP = 'left_stop'
    RIGHT = 'right'
    RIGHT_STOP = 'right_stop'
    SHOOT = 'shoot'
    SHOOT_STOP = 'shoot_stop'


action_event_map = {
    Action.JUMP: pg.event.Event(pg.KEYDOWN, key=pg.K_UP),
    Action.JUMP_STOP: pg.event.Event(pg.KEYUP, key=pg.K_UP),
    Action.LEFT: pg.event.Event(pg.KEYDOWN, key=pg.K_LEFT),
    Action.LEFT_STOP: pg.event.Event(pg.KEYUP, key=pg.K_LEFT),
    Action.RIGHT: pg.event.Event(pg.KEYDOWN, key=pg.K_RIGHT),
    Action.RIGHT_STOP: pg.event.Event(pg.KEYUP, key=pg.K_RIGHT),
    Action.SHOOT: pg.event.Event(pg.KEYDOWN, key=pg.K_LSHIFT),
    Action.SHOOT_STOP: pg.event.Event(pg.KEYUP, key=pg.K_LSHIFT),
}


def post_action(action: Action):
    pg.event.post(action_event_map[action])
