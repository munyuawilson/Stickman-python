from ursina import *

app = Ursina()

stickman = Entity(model='stickman', color=color.red,animator='fight_animation')
stickman.position = (0, 0, 0)
stickman.scale = (0.05, 0.05, 0.05)  # Adjust the scale to reduce the size
# Remove the rotation line to keep the stickman straight
def update():
    if held_keys['f']:  # Trigger the fight animation when the 'f' key is held
        stickman.animator.play('fight_animation')
    elif held_keys['w']:  # Trigger the walk animation when the 'w' key is held
        stickman.animator.play('walk_animation')
    else:
        stickman.animator.stop()  # Stop the animation when no key is pressed


app.run()
