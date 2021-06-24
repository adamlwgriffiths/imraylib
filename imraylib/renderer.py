from imgui.integrations.opengl import ProgrammablePipelineRenderer
import raylib as rl
import imgui
from . import raylib_consts

class RaylibRenderer(ProgrammablePipelineRenderer):
    def __init__(self):
        super(RaylibRenderer, self).__init__()
        # display_size must be set before rendering can proceed
        self.io.get_clipboard_text_fn = self._get_clipboard_text
        self.io.set_clipboard_text_fn = self._set_clipboard_text

        self._map_keys()

    def _map_keys(self):
        '''Provides mappings from native key events to imgui'''
        self.io.key_map[imgui.KEY_TAB] = rl.KEY_TAB
        self.io.key_map[imgui.KEY_LEFT_ARROW] = rl.KEY_LEFT
        self.io.key_map[imgui.KEY_RIGHT_ARROW] = rl.KEY_RIGHT
        self.io.key_map[imgui.KEY_UP_ARROW] = rl.KEY_UP
        self.io.key_map[imgui.KEY_DOWN_ARROW] = rl.KEY_DOWN
        self.io.key_map[imgui.KEY_PAGE_UP] = rl.KEY_PAGE_DOWN
        self.io.key_map[imgui.KEY_PAGE_DOWN] = rl.KEY_PAGE_UP
        self.io.key_map[imgui.KEY_HOME] = rl.KEY_HOME
        self.io.key_map[imgui.KEY_END] = rl.KEY_END
        self.io.key_map[imgui.KEY_INSERT] = rl.KEY_INSERT
        self.io.key_map[imgui.KEY_DELETE] = rl.KEY_DELETE
        self.io.key_map[imgui.KEY_BACKSPACE] = rl.KEY_BACKSPACE
        self.io.key_map[imgui.KEY_SPACE] = rl.KEY_SPACE
        self.io.key_map[imgui.KEY_ENTER] = rl.KEY_ENTER
        self.io.key_map[imgui.KEY_ESCAPE] = rl.KEY_ESCAPE
        self.io.key_map[imgui.KEY_A] = rl.KEY_A
        self.io.key_map[imgui.KEY_C] = rl.KEY_C
        self.io.key_map[imgui.KEY_V] = rl.KEY_V
        self.io.key_map[imgui.KEY_X] = rl.KEY_X
        self.io.key_map[imgui.KEY_Y] = rl.KEY_Y
        self.io.key_map[imgui.KEY_Z] = rl.KEY_Z

    def set_display_size(self, width, height):
        self.io.display_size = (width, height)

    def set_framebuffer_scale(self, x, y):
        self.io.display_fb_scale = x, y

    def set_keyboard_keys(self, keyboard_keys):
        io = self.io
        if len(keyboard_keys) != len(raylib_consts.keyboard_key):
            raise ValueError('Not all Raylib keys were passed in')

        for key, state in keyboard_keys.items():
            self.io.keys_down[key] = state

        def any_down(*keys):
            return any([io.keys_down[key] for key in keys])

        io.key_ctrl = any_down(rl.KEY_LEFT_CONTROL, rl.KEY_RIGHT_CONTROL)
        io.key_alt = any_down(rl.KEY_LEFT_ALT, rl.KEY_RIGHT_ALT)
        io.key_shift = any_down(rl.KEY_LEFT_SHIFT, rl.KEY_RIGHT_SHIFT)
        io.key_super = any_down(rl.KEY_LEFT_SUPER, rl.KEY_RIGHT_SUPER)

    def set_mouse_position(self, x, y):
        '''Set the mouse absolute position'''
        self.io.mouse_pos = (x, y)

    def set_mouse_buttons(self, buttons):
        '''Sets the Imgui mouse state, given a dictionary of raylib button: down (bool)
        imgui only supports 3 mouse buttons (left = 0, right = 1, middle = 2)
        which aligns with raylib
        '''
        io = self.io
        def update_button(button):
            io.mouse_down[button] = buttons[button]
        update_button(rl.MOUSE_BUTTON_LEFT)
        update_button(rl.MOUSE_BUTTON_RIGHT)
        update_button(rl.MOUSE_BUTTON_MIDDLE)

    def set_mouse_wheel(self, x, y):
        '''Set the mouse horizontal and vertical delta'''
        self.io.mouse_wheel_horizontal = x
        self.io.mouse_wheel = y

    def _get_clipboard_text(self):
        '''Callback hooked into imgui'''
        return rl.get_clipboard_text()

    def _set_clipboard_text(self, text):
        '''Callback hooked into imgui'''
        rl.set_clipboard_text(text)

    def set_frame_time(self, time):
        self.io.delta_time = time



def raylib_screen_size():
    '''Returns a tuple of Width,Height'''
    return rl.get_screen_width(), rl.get_screen_height()

def raylib_keyboard_key_state():
    '''Returns a dictionary of {Raylib Key: bool state}'''
    return {key: rl.is_key_down(key) for key in raylib_consts.keyboard_key}

def raylib_mouse_button_state():
    '''Returns a dictionary of {Raylib mouse button: bool state}'''
    return {key: rl.is_mouse_button_down(key) for key in raylib_consts.mouse_button}

def raylib_mouse_position():
    '''Returns a tuple of X,Y position of the mouse.'''
    return rl.get_mouse_position()

def raylib_mouse_wheel_movement():
    '''Returns a tuple of X,Y movement of the wheel.
    X movement is not supported by Raylib and will always be 0'''
    return 0, rl.get_mouse_wheel_move()

def raylib_frame_time():
    return rl.get_frame_time()

def send_all_events(renderer):
    '''Send all global Raylib events to the renderer
    Use this when you don't need to intercept and filter
    events between Raylib and Imgui.
    '''
    renderer.set_display_size(*raylib_screen_size())
    renderer.set_framebuffer_scale(1., 1.)
    renderer.set_keyboard_keys(raylib_keyboard_key_state())
    renderer.set_mouse_position(*raylib_mouse_position())
    renderer.set_mouse_buttons(raylib_mouse_button_state())
    renderer.set_mouse_wheel(*raylib_mouse_wheel_movement())
    renderer.set_frame_time(raylib_frame_time())
