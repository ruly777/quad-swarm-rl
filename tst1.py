import pyglet
from pyglet.gl import *

# Создаем окно
window = pyglet.window.Window(width=800, height=600, caption='OpenGL Test')

# Включаем текстуры
glEnable(GL_TEXTURE_2D)

# Создаем простой квадрат с текстурой
@window.event
def on_draw():
    window.clear()
    
    # Рисуем квадрат
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Красный цвет
    glVertex2f(100, 100)
    glVertex2f(300, 100) 
    glVertex2f(300, 300)
    glVertex2f(100, 300)
    glEnd()

# Добавляем вращение
angle = 0
def update(dt):
    global angle
    angle += 90 * dt  # Вращение 90 градусов в секунду

pyglet.clock.schedule_interval(update, 1/60.0)  # 60 FPS

# Запускаем приложение
pyglet.app.run()
