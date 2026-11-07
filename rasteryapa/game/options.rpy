define config.name = "Растяпа. Между этажами"
define config.version = "1.2.0"
define config.save_directory = "rasteryapa-mezhdu-etazhami-1"
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.game_menu_action = MainMenu(confirm=True)
define config.window_title = "Растяпа. Между этажами"
define build.name = "rasteryapa"
define config.check_conflicting_properties = True

define config.webaudio_required_types = ["audio/mpeg"]

init python:
    renpy.music.register_channel("ambience", mixer="music", loop=True, stop_on_mute=False)
