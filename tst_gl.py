import pyglet
window = pyglet.window.Window()

print(f"OpenGL версия: {window.context.get_info().get_version()}")
print("\nПоддерживаемые расширения:")
extensions = window.context.get_info().get_extensions()
for ext in sorted(extensions):
    print(f"- {ext}")

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
