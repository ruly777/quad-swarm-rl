import pyglet
from pyglet.gl import *

# Простая конфигурация OpenGL
config = pyglet.gl.Config(
    double_buffer=True,
    depth_size=16,
    sample_buffers=0,
    samples=0
)

# Создаем окно с базовой конфигурацией
window = pyglet.window.Window(config=config, width=800, height=600)

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
