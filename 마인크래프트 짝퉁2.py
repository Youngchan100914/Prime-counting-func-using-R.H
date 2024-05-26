from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
blocks = [load_texture('assetss/img_14.png'),
          load_texture('assetss/img_2.png'),
          load_texture('assetss/img_3.png'),
          load_texture('assetss/lol_map.png'),
          load_texture('assetss/img_5.png'),
          load_texture('assetss/img_6.png'),
          load_texture('assetss/img_10.png'),
          load_texture('assetss/img_9.png'),
          load_texture('assetss/img_12.png'),
          load_texture('assetss/img_13.png')
          ]
block_id = 1
space = Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('assetss/img_20.png'),
    scale=5000,
    double_sided=True
)


def input(key):
    global block_id, hand
    if key.isdigit():
        block_id = int(key)
        if block_id >= len(blocks):
            block_id = len(blocks) - 1
        hand.texture = blocks[block_id]


hand = Entity(
    parent=camera.ui,
    model='cube',
    texture=blocks[block_id],
    scale=0.6,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.6, -0.6)
)


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assetss/img_17.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=(1, 1, 1)
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])

            elif key == 'right mouse down':
                destroy(self)


for z in range(-40, 40):
    for x in range(-40, 40):
        box = Voxel(position=(x, -3, z), texture='assetss/img_9.png')


player = FirstPersonController()


def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)


app.run()