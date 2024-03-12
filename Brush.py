from ursina import *

def update():
    # color in
    if erase == False:
        if held_keys['left mouse']:
            if mouse.x < 0.55:
                voxel = Voxel(position = (mouse.x * 8,mouse.y * 8))
                list.append(voxel)
    # eraser
    eraser.position = (mouse.x * 8,mouse.y * 8)
    eraser.scale = scale
    if erase == True:
        hit_info = eraser.intersects()
        if hit_info.hit:
            if hit_info.entity in list:
                destroy(hit_info.entity)
app = Ursina()
# brush scale and color
scale = 0.1
R,G,B = 0,0,0

# this allow the player to add lines with the brush 
list = []
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__()
        global scale, R,G,B
        self.parent = scene
        self.position = position
        self.model = 'quad'
        self.scale = scale
        self.highlight_color = self.color
        self.color = color.rgb(R,G,B)

# update size
def scale_box():
    global scale
    scale = slider.value

slider = Slider(0,5,text='scale',default=0.1,on_value_changed = scale_box,x = 0.6,scale = 0.5)

# update color
def color_change():
    global R,G,B
    R = round(Red.value)
    G = round(Green.value)
    B = round(Blue.value)

Red = Slider(0,255,text='red',default=0,on_value_changed = color_change,x = 0.6,y = 0.1,scale = 0.5)
Green = Slider(0,255,text='green',default=0,on_value_changed = color_change,x = 0.6,y = 0.2,scale = 0.5)
Blue = Slider(0,255,text='blue',default=0,on_value_changed = color_change,x = 0.6,y = 0.3,scale = 0.5)
# eraser
def Clear():
    global erase
    if erase == False:
        erase = True
        eraser_button.color = color.red
    else:
        erase = False
        eraser_button.color = color.blue
# button to activate the erase
erase = False
eraser_button = Button(model = 'quad',scale = 1,collider = 'box',position = (6,-2),parent = scene,color = color.blue)
eraser_button.on_click = Clear
eraser = Entity(model = 'quad',collider = 'box',scale = 0.1)
app.run()
