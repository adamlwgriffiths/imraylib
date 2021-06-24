import raylib as rl
import imgui
import testwindow
from imraylib import renderer


def main():
    rl.init_window(800, 450, "Raylib + Imgui")
    rl.set_target_fps(60)

    imgui.create_context()
    imgui_renderer = renderer.RaylibRenderer()

    while not rl.window_should_close():
        # process events
        # these are not done automatically so we can filter inputs
        # Eg. "In an FPS, ignore key presses until the user pushes
        # the 'use' key and starts interacting with the UI"
        # alternatively use: renderer.send_all_events(imgui_renderer)
        imgui_renderer.set_display_size(*renderer.raylib_screen_size())
        imgui_renderer.set_framebuffer_scale(1., 1.)
        imgui_renderer.set_keyboard_keys(renderer.raylib_keyboard_key_state())
        imgui_renderer.set_mouse_position(*renderer.raylib_mouse_position())
        imgui_renderer.set_mouse_buttons(renderer.raylib_mouse_button_state())
        imgui_renderer.set_mouse_wheel(*renderer.raylib_mouse_wheel_movement())
        imgui_renderer.set_frame_time(renderer.raylib_frame_time())

        rl.begin_drawing()
        imgui.new_frame()

        rl.clear_background(rl.RAYWHITE)

        # raylib text
        rl.draw_text("Congrats! You created your first window!", 190, 200, 20, rl.LIGHTGRAY)

        # basic imgui
        imgui.begin("Custom window", True)
        imgui.text("Bar")
        imgui.end()

        # complex imgui example
        testwindow.show_test_window()

        imgui.render()
        imgui_renderer.render(imgui.get_draw_data())
        rl.end_drawing()

    imgui_renderer.shutdown()
    rl.close_window()

if __name__ == '__main__':
    main()
