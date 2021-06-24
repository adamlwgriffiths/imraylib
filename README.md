# Imraylib

Integrates Imgui with Raylib.

The integration does not directly connect Imgui with Raylib.
This permits you to selectively filter events to prevent them being sent to Imgui.

For example: if you had a number of different Imgui interfaces or possibly even
one rendered inside a first-person game. You don't want them receiving events
until the player begins interacting with the specific Imgui interface.

If you don't care about this, there is a convenience function `send_all_events`
which will send all Raylib data to Imgui and "just work".


## Dependencies

* [raylibpy](https://github.com/overdev/raylib-py) (specifically the `raylibpy-3.7` branch)
* [raylib-py-flat](https://github.com/adamlwgriffiths/raylibpy-flat)
* [pyimgui](https://github.com/swistakm/pyimgui)
