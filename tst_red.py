import pyglet
from pyglet.gl import *
import math
import random

# Enable modern OpenGL profile
config = pyglet.gl.Config(major_version=3, minor_version=3)
window = pyglet.window.Window(800, 600, caption='Advanced Camera Control', config=config)

# Camera parameters
camera_x = 400
camera_y = 300
camera_zoom = 1.0

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-100, 100)
        self.vy = random.uniform(-100, 100)
        self.size = 32
        self.color = (random.randint(100,255), random.randint(100,255), random.randint(100,255), 255)

squares = [Square(400, 300) for _ in range(5)]

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    global camera_zoom
    camera_zoom += scroll_y * 0.1
    camera_zoom = max(0.1, min(camera_zoom, 3.0))

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global camera_x, camera_y
    if buttons & pyglet.window.mouse.LEFT:
        camera_x -= dx
        camera_y -= dy

def update(dt):
    for square in squares:
        square.x += square.vx * dt
        square.y += square.vy * dt
        if square.x < 0 or square.x > window.width:
            square.vx *= -1
        if square.y < 0 or square.y > window.height:
            square.vy *= -1

@window.event
def on_draw():
    window.clear()
    
    for square in squares:
        x = square.x - camera_x
        y = square.y - camera_y
        x = (x - window.width//2) * camera_zoom + window.width//2
        y = (y - window.height//2) * camera_zoom + window.height//2
        
        texture = pyglet.image.SolidColorImagePattern(square.color).create_image(64, 64)
        texture = texture.get_texture()
        texture.blit(x - square.size, y - square.size)

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()

