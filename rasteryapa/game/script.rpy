define ananas = Character("Ананас", color="#a9d8e5")
define ras = Character("Растяпа", color="#ffc49b")
define sympathy_goal = 100

default sympathy = 0
default offered_help = False
default duck_witness = False

image cg arrival = "images/cg01.webp"
image cg greeting = "images/cg02.webp"
image cg sill = "images/cg03.webp"
image cg duck = "images/cg04.webp"
image cg earpiece = "images/cg05.webp"
image cg keys = "images/cg06.webp"
image cg closer = "images/cg07.webp"
image cg kiss = "images/cg08.webp"
image cg alone = "images/cg09.webp"
image cg rain = "images/rain_window.webp"
image cg earbud detail = "images/earbud_detail.webp"
image cg keys detail = "images/keys_detail.webp"
image cg circus = "images/ending_circus.webp"
image cg price = "images/ending_price.webp"

label start:
    $ sympathy = 0
    $ offered_help = False
    $ duck_witness = False

    play music window_theme fadein 1.5 if_changed
    play ambience window_rain fadein 1.2 if_changed

    scene expression Solid(ink)
    show cg rain at on_landing
    show screen landing_status
    with dissolve

    "По двору шёл дождь. В подъезде горела одна лампочка на два этажа."
    show cg arrival at on_landing
    with dissolve
    "Между третьим и вторым этажом Ананас услышал, как кто-то спорит с подоконником."
    ras "Ну и сиди там. Мне самой домой не очень-то хотелось."
    ananas "Это ты окну?"
    show cg greeting at on_landing
    with dissolve
    ras "Ключам. А окну я, наоборот, благодарна. Оно держит мой чай."
    "На её плече сидела жёлтая игрушечная утка в таких же красных очках."

    menu:
        "Помочь поискать?":
            $ sympathy += 20
            $ offered_help = True
            ras "Если найдёшь, тебе полпирожного. Я бы обещала целое, но половину уже съела."
        "Подоконник на двоих рассчитан?":
            $ sympathy += 10
            ras "На двоих и одного адвоката. Вон он, на плече."
        "Скажи, что она устроила цирк.":
            ananas "Ты всегда устраиваешь цирк, когда теряешь вещи?"
            jump ending_circus

    show cg sill at on_landing
    with dissolve
    "Девушка опустила голову на сложенные руки. За окном шины шуршали по мокрому двору."
    ras "Растяпа."
    ananas "Я ничего не сказал."
    ras "А я представилась. Теперь твоя очередь."

    menu:
        "Ананас. Рад познакомиться, Растяпа.":
            $ sympathy += 20
            ras "Ты первый, кто повторил и не переспросил."
            ananas "Я вообще плохо запоминаю имена. Твоё уже запомнил."
        "Ананас. Меня тоже можно звать Растяпой.":
            $ sympathy += 10
            ras "Тогда придётся делить имя по расписанию. По четвергам я."
        "Ананас. Я с пятого этажа.":
            ras "О. А я думала, на пятом живёт только кто-то с дрелью."
            ananas "Дрель на шестом. Мы под ней страдаем."

    show cg duck at on_landing
    with dissolve
    ras "А этого зовут Семён. Если будешь задавать неудобные вопросы, он вступит в дело."
    "Утка качнулась у неё на плече. Ананас подставил ладонь, и Растяпа пересадила Семёна ему на пальцы."

    menu:
        "Семён, где вы были в момент пропажи?":
            $ sympathy += 20
            $ duck_witness = True
            ras "Мой клиент был у окна. Видел, как подозреваемая уронила наушник."
            ananas "Свидетель, значит. Повысим."
        "Очки у него тоже по рецепту?":
            $ sympathy += 10
            ras "Мои старые. Он говорит, в них люди выглядят добрее."
        "Вернуть утку и оглядеть ступени.":
            ras "Посади его рядом с чаем. Он любит тепло."

    show cg earbud detail at on_landing
    with dissolve
    play sound earbud_tap
    "Из рукава Растяпы выскользнул наушник. Он ударился о дерево и покатился к краю."
    show cg earpiece at on_landing
    with dissolve
    ananas "Поймал."
    ras "У тебя сегодня дежурство по потерянным вещам?"
    if offered_help:
        ananas "До первой найденной связки. Потом у меня перерыв на пирожное."
    else:
        ananas "Случайная смена. Я вообще-то шёл за хлебом."
    "Она протянула руку за наушником."

    menu:
        "Положить наушник ей в ладонь.":
            $ sympathy += 20
            ras "Спасибо. В нём дождь."
            ananas "У нас за окном тоже."
            ras "В наушнике он в размер."
        "Положить наушник рядом с чаем.":
            $ sympathy += 10
            ras "Вот. Теперь у чая есть компания."
        "Убрать наушник за спину и попросить поцелуй за него.":
            $ sympathy = max(0, sympathy - 30)
            ananas "Верну за поцелуй."
            jump ending_price

    show cg keys at on_landing
    with dissolve
    "Из-под подоконника сквозило. Ананас наклонился и заметил блеск между трубой и стеной."
    if duck_witness:
        ananas "Семён, ваша подсказка сработала. Ключи там же, где и наушник. Только на этаж ниже, если считать от подоконника."
    else:
        ananas "У батареи что-то блестит. Брелок с ромашкой твой?"
    ras "Мой. Я его купила, чтобы ключи не терялись."
    show cg keys detail at on_landing
    with dissolve
    play sound keys_jingle
    "Ананас выудил связку из-за трубы и положил её на подоконник."
    show cg keys at on_landing
    with dissolve
    "Растяпа убрала ключи в сумку и почему-то не встала."
    ras "Ну что, Ананас? Ты куда теперь?"

    menu:
        "Хочешь, досидим здесь, пока дождь не стихнет?":
            $ sympathy = min(sympathy_goal, sympathy + 30)
            if sympathy == sympathy_goal:
                jump ending_kiss
            ras "Я всё-таки пойду домой. У окна я уже сегодня насиделась."
        "Может, как-нибудь выпьем чаю?":
            ras "Как-нибудь. Если Семён снова назначит приём."
        "До встречи, Растяпа.":
            ras "До встречи, Ананас."
    jump ending_departure

label ending_circus:
    ras "Довольно. Я сама разберусь."
    "Она забрала стакан и сумку. Семён нырнул в карман."
    show cg circus at on_landing
    with dissolve
    play sound door_downstairs
    "Ананас остался на площадке. Внизу хлопнула входная дверь."
    call finish("Чужой подъезд")
    jump start

label ending_price:
    ras "Ананас. Отдай."
    "Он разжал ладонь. Она забрала наушник и перекинула сумку через плечо."
    ras "Ключи я поищу потом."
    show cg price at on_landing
    with dissolve
    play sound stairs_steps
    "Она спустилась быстрым шагом. На последней ступени снова надела наушник."
    call finish("Без сделки")
    jump start

label ending_departure:
    play sound stairs_steps
    "Растяпа махнула ему Семёном и пошла вниз."
    show cg alone at on_landing
    with dissolve
    "Ананас ещё немного постоял у окна. На подоконнике проступал круг от её стакана."
    stop ambience fadeout 2.0
    "Когда он вышел во двор, дождь уже стих."
    call finish("Окно на двоих")
    jump start

label ending_kiss:
    ras "Досидим. Хотя Семён уже просит оставить нас вдвоём."
    "Она подвинулась, освобождая край подоконника. Ананас подошёл ближе."
    ananas "Можно тебя поцеловать?"
    ras "Можно. Я всё ждала, когда ты спросишь."
    show cg closer at on_landing
    with dissolve
    "Они наклонились друг к другу, и очки тихо стукнулись."
    play music kiss_theme fadeout 0.6 noloop
    show cg kiss at on_landing
    with dissolve
    play sound duck_squeak
    "Они поцеловались. Семён качнулся у неё на плече и пискнул."
    ras "Завтра возьмём два пирожных?"
    ananas "Три. Семёну за работу."
    call finish("Между этажами")
    jump start

label finish(title):
    hide screen landing_status
    call screen ending(title)
    return
