from ursina import *

app = Ursina()

class Stickman(Entity):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            model='quad',
            scale=(0.2, 0.6),
            color=color.white,
            position=position,
            collider='box',
        )

    def attack(self):
        self.animate_scale_y(0.1, duration=0.1, curve=curve.linear)
        invoke(self.reset_attack, delay=0.2)

    def reset_attack(self):
        self.animate_scale_y(0.6, duration=0.1, curve=curve.linear)

class Street(Entity):
    def __init__(self):
        super().__init__(
            model='quad',
            texture='street_texture.png',  # Replace with your street texture image
            scale=(10, 1, 1),
            z=-1  # Place the street behind the stickman characters
        )

player = Stickman(position=(-2, 0, 0))
enemy = Stickman(position=(2, 0, 0))
street = Street()

def update():
    if held_keys['a']:
        player.x -= 0.1
    if held_keys['d']:
        player.x += 0.1
    if held_keys['space']:
        player.attack()

def on_mouse_down():
    enemy.attack()

app.run()
