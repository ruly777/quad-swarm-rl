import pyglet
window = pyglet.window.Window()
print(f"OpenGL версия: {window.context.get_info().get_version()}")

