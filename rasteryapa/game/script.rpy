define ananas = Character("Ананас", color="#a9d8e5")
define ras = Character("Растяпа", color="#ffc49b")
define sympathy_goal = 100

default sympathy = 0
default duck_detective = False
default offered_umbrella = False

image cg window = "images/board_window.webp"
image cg arrival = "images/cg01.webp"
image cg greeting = "images/board_greeting.webp"
image cg duck = "images/board_duck.webp"
image cg cake = "images/board_cake.webp"
image cg care = "images/cg03.webp"
image cg roof = "images/board_roof.webp"
image cg rain = "images/board_rain.webp"
image cg near = "images/board_near.webp"
image cg kiss = "images/board_kiss.webp"
image cg sofa = "images/board_sofa.webp"
image cg photo = "images/board_photo.webp"
image cg sunset = "images/board_sunset.webp"
image cg friends = "images/board_friends.webp"
image cg look back = "images/board_look_back.webp"
image cg stairs = "images/board_stairs.webp"
image cg alone = "images/board_alone.webp"
image cg red flag = "images/board_red_flag.webp"
image cg red exit = "images/board_red_exit.webp"
image cg boundary = "images/board_boundary.webp"
image cg threshold = "images/board_threshold.webp"
image cg regret = "images/board_regret.webp"

label start:
    $ sympathy = 0
    $ duck_detective = False
    $ offered_umbrella = False

    play music window_theme fadein 1.5 if_changed
    play ambience window_rain fadein 1.2 if_changed

    scene expression Solid(ink)
    show cg window at on_landing
    show screen landing_status
    with dissolve

    "В июне подоконник между вторым и третьим этажом прогревался до самого вечера."
    "Сегодня на нём остывал чай. Рядом с чаем кто-то негромко торговался."

    show cg arrival at on_landing
    with dissolve
    ras "Если ключи найдутся до темноты, тебе клубника."
    "Жёлтая утка на её плече промолчала."
    ananas "Она дорого берёт."
    show cg greeting at on_landing
    with dissolve
    ras "Это он. И он хотя бы не предлагает поискать там, где я уже искала."
    ananas "Ананас."
    ras "Это вы про рубашку?"
    ananas "Про себя. Рубашка уже всё сказала."

    menu:
        "Подержать чай, пока ты проверяешь сумку?":
            $ sympathy += 20
            ras "Подержи. Только осторожно, стакан липкий."
            ananas "Я взрослый человек. У меня дома липнет целый стол."
        "Составлю тебе компанию, если ты не против.":
            $ sympathy += 10
            ras "Составляй. Только оставь мне место у окна."
        "Ты весь подъезд в детский сад превратила?":
            ananas "Ты весь подъезд в детский сад превратила?"
            jump ending_red_flag

    ras "Меня Растяпа зовут. Можешь не искать тут связь с ключами. Я уже нашла."

    show cg duck at on_landing
    with dissolve
    "У утки были такие же красные очки, как у Растяпы. Одно стёклышко держалось на скотче."
    ananas "А у него есть имя?"
    ras "Семён. Он со мной переехал. Пережил четыре коробки и одного бывшего."

    menu:
        "Семён, когда вы видели ключи в последний раз?":
            $ sympathy += 20
            $ duck_detective = True
            ras "Мой клиент видел, как я ставила стакан. И слышал, как что-то упало."
            ananas "Хороший свидетель. Говорит через адвоката."
        "Очки ему идут. Это твои старые?":
            $ sympathy += 10
            ras "Из кукольного набора. Свои я бы ему не доверила."
        "Похоже, он тут давно. Дашь взглянуть на сумку?":
            ras "Я сама проверю. В ней такой порядок, что только я умею им пользоваться."

    show cg cake at on_landing
    with dissolve
    ras "Раз уж ты здесь. Разрежешь пирожное?"
    ananas "Ровно пополам?"
    ras "Да. Половину с клубникой мне, половину без клубники тебе."
    "Он подвинул к ней блюдце. Их пальцы на секунду встретились на фарфоре."
    ras "У тебя тёплые руки."
    ananas "У тебя холодные."
    ras "Я про твои сказала, потому что мне понравилось."

    show cg care at on_landing
    with dissolve
    play sound earbud_tap
    "Растяпа положила голову на руки. Один наушник стукнул о дерево и свесился на проводе."
    ras "Я с шести на ногах. Если усну, разбуди минут через пять."
    ananas "Пять настоящих или пять твоих?"
    ras "Моих. В настоящие я даже заснуть не успею."

    menu:
        "Останусь здесь. Можешь немного отдохнуть.":
            $ sympathy += 20
            "Ананас отодвинул стакан от её локтя. Растяпа закрыла глаза, пока дождь стучал по стеклу."
            ras "Хорошо, когда рядом можно помолчать."
        "Хочешь, я схожу за водой?":
            $ sympathy += 10
            ras "Чай ещё есть. Сядь, а то у меня шея устала на тебя снизу смотреть."
        "Когда захочешь идти, скажи.":
            ras "Скажу. Мне надо просто минуту посидеть."

    if duck_detective:
        ananas "Семён слышал, как что-то упало. Гляну за батареей?"
    else:
        ananas "Погоди. За батареей что-то белое. Это ромашка?"
    play sound keys_jingle
    "Ананас подцепил связку за кольцо. На брелоке из белой ромашки осталось три лепестка."
    ras "Домой можно. А мы ещё можем не идти."
    ananas "Есть куда?"
    ras "Я знаю крышу, с которой наш двор почти красивый."

    stop ambience fadeout 1.8
    show cg roof at on_landing
    with fade
    "На крыше ветер сдувал тепло с кирпичей. Над двором из-под туч проступила розовая полоса."
    ras "Когда переехала, каждый вечер сюда ходила. В квартире было так тихо, что я телевизор включала, пока ела."
    ananas "И что смотрела?"
    ras "Один раз полчаса смотрела, как мужик чинит табуретку. Досмотрела из уважения к табуретке."
    "Она придвинулась, чтобы показать, в каком окне живёт. Её плечо осталось у его плеча."

    play ambience window_rain fadein 1.0 if_changed
    show cg rain at on_landing
    with dissolve
    "Дождь вернулся без предупреждения. Ананас раскрыл зонт. Ветер сразу вывернул один угол."
    ras "Дай я сама подойду. Тут скользко."
    ananas "Тебе хватает места?"
    ras "Пока да. Погоди, не тяни меня."

    menu:
        "Подвинуть зонт в её сторону и дать ей подойти.":
            $ sympathy += 20
            $ offered_umbrella = True
            ras "Вот так. Держи выше, а то Семёну опять голову намочим."
            "Растяпа взяла Ананаса под локоть. Он почувствовал сквозь мокрую ткань тепло её ладони."
        "Убрать зонт и предложить укрыться в подъезде.":
            $ sympathy += 10
            ras "Пойдём. Я ещё не готова менять чай на простуду."
        "Притянуть её за талию, несмотря на просьбу.":
            $ sympathy = max(0, sympathy - 30)
            jump ending_boundaries

    show cg near at on_landing
    with dissolve
    "Они остановились у двери на лестницу. Из-за края зонта по стеклу текла вода."
    if offered_umbrella:
        ras "Ты весь мокрый с одной стороны."
        ananas "С моей. Твоя сухая."
        ras "Сухая только половина рукава. Но попытка хорошая."
    else:
        ras "Слышишь? Здесь дождь в крышу барабанит совсем иначе."
        ananas "Здесь можно стоять и никого не будить."
    "Растяпа подняла очки на переносицу. Ананас заметил, что смотрит ей на губы, и отвёл взгляд."
    ras "Ты хотел что-то сказать?"

    menu:
        "Мне хочется тебя поцеловать. Можно?":
            $ sympathy = min(sympathy_goal, sympathy + 30)
            ananas "Мне хочется тебя поцеловать. Можно?"
            if sympathy == sympathy_goal:
                jump ending_kiss
            ras "Мне приятно, что ты спросил. Но я хочу, чтобы сегодня мы просто разошлись по домам."
        "Мне понравился этот вечер. Повторим как друзья?":
            ananas "Мне понравился этот вечер. Повторим как друзья?"
            ras "Давай. В следующий раз я возьму два пирожных."
        "Пожелать спокойной ночи.":
            ananas "Спокойной ночи, Растяпа."
            ras "Спокойной, Ананас. Спасибо, что посидел со мной."
    jump ending_friends

label ending_red_flag:
    show cg red flag at on_landing
    with dissolve
    ras "Стой. Если тебе смешно надо мной, мы на этом закончили."
    "Она забрала чай и сунула Семёна в сумку."
    show cg red exit at on_landing
    with dissolve
    play sound stairs_steps
    "Ананас открыл рот, но она уже свернула на следующий пролёт."
    call finish("Красный флаг")
    jump start

label ending_boundaries:
    show cg boundary at on_landing
    with dissolve
    "Ананас взял её за талию. Растяпа тут же отступила."
    ras "Убери руку. Я просила подождать."
    "Он отпустил. Растяпа поправила ремень сумки."
    ras "Я дальше сама."
    show cg threshold at on_landing
    with dissolve
    play sound stairs_steps
    "Она спустилась и вышла под дождь. Ананас остался на площадке с раскрытым зонтом."
    show cg regret at on_landing
    with dissolve
    play sound door_downstairs
    "Только когда хлопнула дверь, он сложил зонт. С него натекла лужа."
    call finish("Личные границы")
    jump start

label ending_friends:
    show cg friends at on_landing
    with dissolve
    ananas "Семён тоже остаётся в друзьях?"
    ras "Семён сам решает. Но сегодня он хорошо о тебе отзывался."
    show cg look back at on_landing
    with dissolve
    "У поворота Растяпа обернулась, чтобы помахать."
    show cg stairs at on_landing
    with dissolve
    play sound stairs_steps
    "Шаги стихли. Потом звякнула связка у её двери."
    show cg alone at on_landing
    with dissolve
    "Ананас ещё немного постоял у окна. Во дворе зажглись фонари, и каждый отражался в двух или трёх лужах."
    call finish("Не в этот раз")
    jump start

label ending_kiss:
    ras "Да. Только спустимся на площадку. Тут у меня пальцы уже не слушаются."
    "Под лампочкой Растяпа вытерла пальцем каплю с его очков."
    ras "А теперь иди сюда."
    play music kiss_theme fadeout 0.6 noloop
    show cg kiss at on_landing
    with dissolve
    "Она первой коснулась его губ. Ананас провёл ладонью по её щеке. Растяпа подалась ближе, и второй поцелуй вышел медленнее."
    play sound duck_squeak
    ras "Слышал? Семён требует отдельного приглашения."
    ananas "А куда мы идём?"
    ras "Ко мне. Если хочешь ещё немного побыть рядом."

    stop ambience fadeout 1.5
    play music window_theme fadein 2.0
    show cg sofa at on_landing
    with fade
    "У неё они укрылись одним пледом. Растяпа прижалась к его боку и закинула ноги ему на колени."
    ras "Не вставай пока. Я только согрелась."
    ananas "Я и не собирался."
    show cg photo at on_landing
    with dissolve
    "На снимке, который она сделала перед его уходом, Ананас моргнул. Растяпа оставила его таким."
    show cg sunset at on_landing
    with dissolve
    "На следующий вечер они снова поднялись на крышу. Пирожных было два. Семёну досталась клубника."
    call finish("Между этажами")
    jump start

label finish(title):
    hide screen landing_status
    call screen ending(title)
    return
