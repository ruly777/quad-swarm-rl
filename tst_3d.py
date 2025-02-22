import pyglet
from pyglet.gl import *

# Создаем окно
window = pyglet.window.Window(800, 600, caption='2D Test')

@window.event
def on_draw():
    window.clear()
    
    # Создаем вершины с помощью нового API
    vertices = [-50,-50, 50,-50, 50,50, -50,50]
    colors = [255,0,0, 0,255,0, 0,0,255, 255,255,0]
    
    # Рисуем примитивы напрямую
    pyglet.graphics.draw(4, GL_QUADS,
        ('v2f', vertices),
        ('c3B', colors)
    )

# Запускаем приложение
pyglet.app.run()
