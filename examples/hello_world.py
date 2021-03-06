import trio

import deartriogui
from dearpygui.dearpygui import *

import deartriogui


async def subtask(sender, data):
    print('Hello from', sender, data)
    await trio.sleep(5)
    print('Bye!')


async def main():
    log_info('Hello from Async!')
    for x in range(1000):
        log_debug(f'Step {x}')
        await trio.sleep(0.1)
    log_info('Done...')
    await trio.sleep(0.5)
    return 'Hello World'

add_button('Start subtask', callback=deartriogui.async_callback(subtask))

with deartriogui.container(add_collapsing_header, 'Foo'):
    add_text('Hello World Yeah!')

add_text('Outside')
show_logger()
set_log_level(0)

assert deartriogui.run(main) == 'Hello World'
