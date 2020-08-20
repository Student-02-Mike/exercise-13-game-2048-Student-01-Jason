import json

from behave import *
from demo import *


@Given('the game have a series of numbers {numbers}')
def step_impl(context, numbers):
    game = Game()
    game.list = json.loads(numbers)
    context.game = game


@When('the player give a command {cmd}')
def step_impl(context, cmd):
    context.cmd = cmd


@Then('the series should be changed to {new}')
def step_impl(context, new):
    #TODO
