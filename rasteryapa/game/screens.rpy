init -2 python:
    gui.init(720, 1280)

define ink = "#151719"
define paper = "#f8efdf"
define muted = "#cbbba7"
define amber = "#ffc087"

transform on_landing:
    xalign 0.5
    ypos 92
    xysize (720, 836)
    fit "contain"

style default:
    font "DejaVuSans.ttf"
    color paper
    size 30

style landing_button:
    background Solid("#343033")
    hover_background Solid("#614737")
    xfill True
    padding (22, 14)
    yminimum 58

style landing_button_text:
    color paper
    hover_color "#ffffff"
    size 26

style landing_bar:
    left_bar Solid("#f1a873")
    right_bar Solid("#454043")
    thumb None
    thumb_shadow None
    ysize 8

screen sound_switch():
    $ sound_label = "Звук выкл." if preferences.get_mute("music") else "Звук вкл."

    textbutton sound_label:
        text_size 22
        text_color paper
        text_hover_color amber
        action Preference("all mute", "toggle")

screen landing_status():
    zorder 10

    frame:
        xfill True
        ysize 92
        padding (32, 14)
        background Solid(ink)

        vbox:
            xsize 330
            spacing 8
            text "СИМПАТИЯ  [sympathy] / [sympathy_goal]" size 22 color amber
            bar value StaticValue(sympathy, sympathy_goal) style "landing_bar"

        hbox:
            xalign 1.0
            yalign 0.5
            spacing 18

            use sound_switch

            textbutton "В меню":
                text_size 23
                text_color paper
                text_hover_color amber
                action MainMenu(confirm=True)

screen say(who, what):
    window:
        id "window"
        xfill True
        yalign 1.0
        ysize 352
        padding (36, 30)
        background Solid(ink)

        vbox:
            spacing 12
            if who is not None:
                text who id "who" size 24
            text what id "what" size 33 line_spacing 6

        text "КАСАНИЕ  /  ДАЛЬШЕ":
            xalign 1.0
            yalign 1.0
            color muted
            size 19

screen choice(items):
    modal True

    frame:
        xfill True
        yalign 1.0
        yminimum 352
        padding (36, 24)
        background Solid(ink)

        vbox:
            xfill True
            spacing 9
            text "ТВОЙ ОТВЕТ" size 20 color amber
            for item in items:
                textbutton item.caption action item.action style "landing_button"

screen main_menu():
    tag menu

    add Solid(ink)
    add "cg arrival" at on_landing

    frame:
        xfill True
        ysize 92
        padding (36, 26)
        background Solid(ink)
        text "ИСТОРИЯ О СЛУЧАЙНОЙ ВСТРЕЧЕ" size 22 color amber yalign 0.5

        hbox:
            xalign 1.0
            yalign 0.5
            use sound_switch

    frame:
        xfill True
        yalign 1.0
        ysize 352
        padding (36, 28)
        background Solid(ink)

        vbox:
            spacing 10
            text "Растяпа." size 58
            text "Между этажами" size 45 color amber
            text "Пять выборов  ·  Четыре концовки" size 24 color muted
            null height 6
            textbutton "Начать историю" action Start() style "landing_button"

screen ending(title):
    modal True

    frame:
        xfill True
        yalign 1.0
        ysize 352
        padding (36, 28)
        background Solid(ink)

        vbox:
            spacing 12
            text "КОНЦОВКА" size 20 color amber
            text title size 46
            text "Симпатия  [sympathy] / [sympathy_goal]" size 23 color muted
            textbutton "Сыграть ещё раз" action Return() style "landing_button"
            textbutton "Главное меню" action MainMenu(confirm=False) style "landing_button"

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    key "game_menu" action no_action

    add Solid("#000b")

    frame:
        align (0.5, 0.5)
        xsize 600
        padding (32, 32)
        background Solid(ink)

        vbox:
            spacing 14
            text "Вернуться в меню?"
            text "Текущее прохождение закончится." size 25 color muted
            textbutton "В меню" action yes_action style "landing_button"
            textbutton "Продолжить" action no_action style "landing_button"
