import pyglet
from pyglet.gl import *

def get_display(display):
    if display is None:
        return pyglet.canvas.get_display()
    return display

class WindowTarget:
    def __init__(self, width, height, resizable=True, display=None):
        print("Starting full project simulation...")
        
        display = get_display(display)
        print(f"Display initialized: {display}")
        
        config = pyglet.gl.Config(
            double_buffer=True,
            depth_size=16,
            sample_buffers=0,
            samples=0
        )
        print("OpenGL configuration set")
        
        self.window = pyglet.window.Window(
            display=display,
            width=width, 
            height=height, 
            resizable=resizable,
            visible=True, 
            vsync=False,
            config=config
        )
        print("Window fully initialized")

    def render(self):
        self.window.clear()

# Запускаем полное тестирование
window_target = WindowTarget(800, 600)
pyglet.app.run()
