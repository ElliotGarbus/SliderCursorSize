from kivy.app import App
from kivy.lang import Builder
from kivy.uix.slider import Slider

kv = '''
<StretchSlider>
    Image:
        pos: (root.value_pos[0] - root.cursor_width / 2, root.center_y - root.cursor_height / 2) if root.orientation == 'horizontal' else (root.center_x - root.cursor_width / 2, root.value_pos[1] - root.cursor_height / 2)
        size: root.cursor_size 
        source: root.cursor_disabled_image if root.disabled else root.cursor_image
        allow_stretch: True
        
BoxLayout:
    orientation: 'vertical'
    Label:
        size_hint_y:.1
        text: 'Original'
        font_size: '20sp'
    BoxLayout:
        BoxLayout:
            orientation: 'vertical'
            Slider:
                orientation: 'vertical'
                cursor_image: 'cursor_16.png'
            Label:
                size_hint_y: .1
                text: '16x16'
        BoxLayout:
            orientation: 'vertical'
            Slider:
                orientation: 'vertical'
                cursor_image: 'cursor_32.png'
            Label:
                size_hint_y: .1
                text: '32x32'
        BoxLayout:
            orientation: 'vertical'
            Slider:
                orientation: 'vertical'
                cursor_image: 'cursor_64.png'
            Label:
                size_hint_y: .1
                text: '64x64'   
        BoxLayout:
            orientation: 'vertical'
            Slider:
                orientation: 'vertical'
                cursor_image: 'cursor_128.png'
            Label:
                size_hint_y: .1
                text: '128x128'
                
    Label:
        size_hint_y:.4
        text: 'Allow Stretch'
        font_size: '20sp'
    BoxLayout:
        BoxLayout:
            orientation: 'vertical'
            StretchSlider:
                orientation: 'vertical'
                cursor_image: 'cursor_16.png'
            Label:
                size_hint_y: .1
                text: '16x16'
        BoxLayout:
            orientation: 'vertical'
            StretchSlider:
                orientation: 'vertical'
                cursor_image: 'cursor_32.png'
            Label:
                size_hint_y: .1
                text: '32x32'
        BoxLayout:
            orientation: 'vertical'
            StretchSlider:
                orientation: 'vertical'
                cursor_image: 'cursor_64.png'
            Label:
                size_hint_y: .1
                text: '64x64'   
        BoxLayout:
            orientation: 'vertical'
            StretchSlider:
                orientation: 'vertical'
                cursor_image: 'cursor_128.png'
            Label:
                size_hint_y: .1
                text: '128x128'
'''


class StretchSlider(Slider):
    pass


class SliderCursorSizeApp(App):

    def build(self):
        return Builder.load_string(kv)


SliderCursorSizeApp().run()
