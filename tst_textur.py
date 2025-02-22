import pyglet
from pyglet.gl import *

window = pyglet.window.Window(800, 600, caption='OpenGL Texture Test')

@window.event
def on_draw():
    window.clear()
    print("Current GL error:", glGetError())
    
    # Пробуем включить текстуры
    try:
        glEnable(GL_TEXTURE_2D)
        print("GL_TEXTURE_2D enabled successfully")
    except Exception as e:
        print("Error enabling GL_TEXTURE_2D:", e)

pyglet.app.run()
