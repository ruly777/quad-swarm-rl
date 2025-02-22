import pyglet

print("Pyglet version:", pyglet.version)

# Создаем окно с заданными размерами
window = pyglet.window.Window(width=400, height=300, caption="Graphics Test")

# Создаем текстовую метку
label = pyglet.text.Label('Тест графики',
                         font_name='Arial',
                         font_size=36,
                         x=window.width//2,
                         y=window.height//2,
                         anchor_x='center',
                         anchor_y='center')

# Создаем фигуры для отрисовки
circle = pyglet.shapes.Circle(x=100, y=100, radius=50, color=(255, 0, 0))
rectangle = pyglet.shapes.Rectangle(x=200, y=200, width=100, height=50, color=(0, 255, 0))

@window.event
def on_draw():
    window.clear()
    label.draw()
    circle.draw()
    rectangle.draw()

print("Window created successfully")
pyglet.app.run()
