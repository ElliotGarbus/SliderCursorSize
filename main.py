from kivy.app import App
from kivy.lang import Builder

kv = '''
<StretchSlider@Slider>:
    Image:
        pos: (root.value_pos[0] - root.cursor_width / 2, root.center_y - root.cursor_height / 2) if root.orientation == 'horizontal' else (root.center_x - root.cursor_width / 2, root.value_pos[1] - root.cursor_height / 2)
        size: root.cursor_size 
        source: root.cursor_disabled_image if root.disabled else root.cursor_image
        allow_stretch: True

<ComboSlider@BoxLayout>:
    orientation: 'vertical'
    cursor_image: 'initial'
    text: 'initial'
    BoxLayout:
        orientation: 'vertical'
        Slider:
            orientation: 'vertical'
            cursor_image: root.cursor_image
        Label:
            size_hint_y: .1
            text: root.text

<ComboStretchSlider@BoxLayout>:
    orientation: 'vertical'
    cursor_image: 'initial'
    text: 'initial'
    BoxLayout:
        orientation: 'vertical'
        StretchSlider:
            orientation: 'vertical'
            cursor_image: root.cursor_image
        Label:
            size_hint_y: .1
            text: root.text
        
BoxLayout:
    orientation: 'vertical'
    Label:
        size_hint_y:.1
        text: 'Original'
        font_size: '20sp'
    BoxLayout:
        ComboSlider:
            cursor_image: 'cursor_16.png'
            text: '16x16'
        ComboSlider:
            cursor_image: 'cursor_32.png'
            text: '32x32'
        ComboSlider:
            cursor_image: 'cursor_64.png'
            text: '64x64'   
        ComboSlider:
            cursor_image: 'cursor_128.png'
            text: '128x128'               
    Label:
        size_hint_y:.4
        text: 'Allow Stretch'
        font_size: '20sp'
    BoxLayout:
        ComboStretchSlider:
            cursor_image: 'cursor_16.png'
            text: '16x16'
        ComboStretchSlider:
            cursor_image: 'cursor_32.png'
            text: '32x32'
        ComboStretchSlider:
            cursor_image: 'cursor_64.png'
            text: '64x64'
        ComboStretchSlider:
            cursor_image: 'cursor_128.png'
            text: '128x128'
'''


class SliderCursorSizeApp(App):

    def build(self):
        return Builder.load_string(kv)


SliderCursorSizeApp().run()
