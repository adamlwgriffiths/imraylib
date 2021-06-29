# Imraylib

Integrates Imgui with Raylib.

The integration does not directly connect Imgui with Raylib.
This permits you to selectively filter events to prevent them being sent to Imgui.

For example: if you had a number of different Imgui interfaces or possibly even
one rendered inside a first-person game. You don't want them receiving events
until the player begins interacting with the specific Imgui interface.

If you don't care about this, there is a convenience function `send_all_events`
which will send all Raylib data to Imgui and "just work".

## Installation

`pip install imraylib`

Until [raylibpy](https://github.com/overdev/raylib-py) merges the `raylibpy-3.7` branch to master,
you must manually install it from Git.


## Dependencies

* [raylibpy](https://github.com/overdev/raylib-py) - Specifically the `raylibpy-3.7` branch.
* [raylib-py-flat](https://github.com/adamlwgriffiths/raylib-py-flat) - Simplifies `raylibpy` imports
* [pyimgui](https://github.com/swistakm/pyimgui)


## Example

See [example/demo.py](example/demo.py) for an example
