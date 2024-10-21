import telebot
from telebot import types
import random

TOKEN = '6699461604:AAE85p8XuOT4bhyi3nLdSk5hZdjBWHTor8g'  # Вставьте ваш токен от BotFather
bot = telebot.TeleBot(TOKEN)


def create_default_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('⁂ КАРТА ДНЯ ⁂')
    keyboard.add(button)
    return keyboard


def send_random_image_and_text(chat_id):

    sets = [
        {
            "image_url": 'https://ibb.co/FHD3QmK',
            "text": "Бабушка гадала, да надвое сказала: то ли дождь, то ли снег, то ли будет, то ли нет. Карта предлагает задуматься, взвесить все ЗА и ПРОТИВ и не торопиться с решением, так как исход пока неясен и может пойти в любую сторону"
        },
        {
            "image_url": 'https://ibb.co/0nGjXrX',
            "text": "Отёкшие красные плечи неистово горят от тяжести груза. Эта карта говорит о важности отдыха и умения вовремя распознать свои пределы, чтобы не истощиться полностью"
        },
  	{
            "image_url": 'https://ibb.co/dmgRyYX',
            "text": "Скоро всё прояснится. Карта предлагает задуматься о том, как мы справляемся с неопределенностью и ожиданием, и как это влияет на наше внутреннее состояние"
        },
	{
            "image_url": 'https://ibb.co/rvzdJq9',
            "text": "И мольбы муравья долетают до небес. Карта может подчеркивать важность организации и планирования в условиях постоянного движения и множества дел."
        },
	{
            "image_url": 'https://ibb.co/BsDSMcg',
            "text": "Безвкусный сок пресных побед. Карта побуждает принимать достойно нелёгкое восстановление."
        },
	{
            "image_url": 'https://ibb.co/pvwgcyQ',
            "text": "Строил коттедж, а получилась будка. Карта призывает работать с тем, что есть, а не с тем, чего нет."
        },
	{
            "image_url": 'https://ibb.co/wJ8PV63',
            "text": "Никто не хочет, чтоб на нём катались (даже лошади). Карта призывает не рассеиваться на милосердие."
        },
	{
            "image_url": 'https://ibb.co/cJzqsrz',
            "text": "Потерял на станке указательный палец, как теперь креститься? Карта говорит, что просить или ждать помощи - не стыдно."
        },
	{
            "image_url": 'https://ibb.co/pZfjkz8',
            "text": "Нам нужна свобода! Эта карта побуждает к действию. Время перестать прятаться за условностями и страхами, время освободиться от всего, что мешает вам быть искренними и настоящими."
        },
	{
            "image_url": 'https://ibb.co/dkGxZvX',
            "text": "Сложно достичь одиночества, они всегда рядом. Эта карта призывает принять те аспекты жизни, которые неизмены и постоянны"
        },
	{
            "image_url": 'https://ibb.co/zQs8Vhh',
            "text": "Наличие решётки не оставляет свободы никому. Эта карта просит не забывать, что свобода твоих помыслов иллюзорна."
        },
	{
            "image_url": 'https://ibb.co/cQWbGK3',
            "text": "Плети свой кокон, не спрашивая зачем и почему. Карта рекомендует не покидать своей зоны ком форта."
        },
	{
            "image_url": 'https://ibb.co/2qGkWg3',
            "text": "Пусть и не козырная, но зато моя! Карта напоминает нам о важности быть верными себе и своим убеждениям. Принятие своей уникальности и следование своим истинным желаниям принесет вам гармонию и удовлетворение."
        },
	{
            "image_url": 'https://ibb.co/F7dN99W',
            "text": "Шоры не ограничивают, а спасают от лишнего. Карта учит не отвлекаться и не переживать, если цель вне зоны видимости."
        },
	{
            "image_url": 'https://ibb.co/zxRKtxq',
            "text": "Чем выбивать клин, которым выбивали клин, которым выбивали клин? Карта просит пересмотреть методы борьбы с проблемой."
        },
	{
            "image_url": 'https://ibb.co/8jdXNtp',
            "text": "Обида вываривает нутро наживую, но не приносит облегчения. Карта не рекомендует жить пассивным негативным отношением."
        },
	{
            "image_url": 'https://ibb.co/XpYWc3z',
            "text": "Жители твоих неубранных кладовок. Карта служит напоминанием подразбрестись."
        },
	{
            "image_url": 'https://ibb.co/yVXgQtb',
            "text": "Тогда не вышло, и сейчас не получится. Карта призывает страшиться настояшего."
        },
	{
            "image_url": 'https://ibb.co/n0wMkP6',
            "text": "Симметрия — враг искусства, но такой красивый. Карта предлагает побыть предсказуемым и избегать ассиметрии."
        },
	{
            "image_url": 'https://ibb.co/NWmcvnh',
            "text": "Если не умеешь кататься на велосипеде, то придёт договариваться с тем, кто умеет. Карта одобряет нет-воркинг."
        },
	{
            "image_url": 'https://ibb.co/ZBFpm7X',
            "text": "Превращаясь в ракету, нужно не забыть не взорваться. Эта карта напоминает нам о важности контроля над своими эмоциями и ответственном подходе к действиям."
        },
	{
            "image_url": 'https://ibb.co/J2vSPrn',
            "text": "Лень порождает процесс и множит уродства. Эта карта препятствует проявлению любой халатности."
        },
	{
            "image_url": 'https://ibb.co/nzwrJkT',
            "text": "Аж перетекает за край! Эта карта уверена, что сейчас самое время."
        },
	{
            "image_url": 'https://ibb.co/yWKn7Hg',
            "text": "Жернова языков перетрут самые твёрдые зёрна. Эта карта советует черпать решение в разговорах."
        },
	{
            "image_url": 'https://ibb.co/LP06L1C',
            "text": "Я бы с радостью всё исполнил, но не разобрался в требованиях. Эта карта указывает на необходимость крепкого софт-скилла."
        },
	{
            "image_url": 'https://ibb.co/CWghCsj',
            "text": "Бред танцует тихо, пока не затанцуешь ты. Эта карта рекомендует прислушиваться не танцует ли у него в голове дилириум."
        },
	{
            "image_url": 'https://ibb.co/ZWTmy41',
            "text": "Создайте свой герб! Создайте свою валюту! Защищайте свой язык! Эта карта призывает объявить независимость."
        },
	{
            "image_url": 'https://ibb.co/CKnqgDW',
            "text": "Лежебоке и солнце не в пору всходит. Эта карта предупреждает: много спать — мало жить, что проспано, то прожито."
        },
	{
            "image_url": 'https://ibb.co/KVxN14h',
            "text": "Отдых для ума и сердца. Эта карта призывает к перекуру."
        },
	{
            "image_url": 'https://ibb.co/hZmNkjK',
            "text": "Есть мертвецы, в которых жизни больше, чем в живых. Карта просит не консервировать дружбу."
        },
	{
            "image_url": 'https://ibb.co/NKH5Tqh',
            "text": "Вонифатий Римский поможет тем, кто страдает алкоголизмом, а не наслаждается. Эта карта просит не наслаждаться пороком."
        },
	{
            "image_url": 'https://ibb.co/4N05FLc',
            "text": "Про что вообще разговор?. Эта карта напоминает о важности коннекта."
        },
	{
            "image_url": 'https://ibb.co/0VGPSYh',
            "text": "Регулярные обновления в комплекте. Эта карта хочет, чтобы человек был себе интересен."
        },
	{
            "image_url": 'https://ibb.co/J7fpSmp',
            "text": "Не проигрывает тот, кто не играет. Эта карта считает риск неотьемлемой частью жизни любого живого существа"
        },
	{
            "image_url": 'https://ibb.co/0GvVC7W',
            "text": "Нон-конформизм на трёх зубочистках. Эта карта отвергает общепринятую концепцию что-то означать."
        },
	{
            "image_url": 'https://ibb.co/NjzpDLB',
            "text": "Лямки рюкзака скоро лопнут. Эта карта советует рационально использовать пространство в голове и сердце."
        },
	{
            "image_url": 'https://ibb.co/pdJPsHd',
            "text": "Конвертирование из мысли в материю провалено. Эта карта олицетворяет сложность воплощения задуманного."
        },
	{
            "image_url": 'https://ibb.co/FxzBHmX',
            "text": "Мечты составляют половину реальности. Эта карта разграничивает выдумку и явь"
        },
	{
            "image_url": 'https://ibb.co/y8hZVdv',
            "text": "Икара, например, хорошенько пропекла его гордыня . Эта карта напоминает о теневой стороне вещей, которые кажутся слишком яркими и привлекательными."
        },
	{
            "image_url": 'https://ibb.co/8dNQVwV',
            "text": "На первый взгляд общего языка мы не найдём. Эта карта требует отбросить предвзятость."
        },
	{
            "image_url": 'https://ibb.co/vZkxS8f',
            "text": "Кто бы мог подумать, что позже их раскидает во все стороны? Эта карта взывает к готовности к резким переменам."
        },
	{
            "image_url": 'https://ibb.co/wL5xGMy',
            "text": "С таких высот я вижу всё. Эта карта предлагает лишний раз не высовывать своё лицо."
        },
	{
            "image_url": 'https://ibb.co/kMgpKZz',
            "text": "Нэчыстый дух злицца вельми на свист. Эта карта рекомендует не испытывать терпение чертей."
        },
	{
            "image_url": 'https://ibb.co/N9FHjDp',
            "text": "Цацки тянут вниз. Эта карта освобождает от необходимости думать о своей внешности."
        },
	{
            "image_url": 'https://ibb.co/C7JfCKX',
            "text": "КВАлифицированный монарх. Эта карта приказывает фильтровать приказы."
        },
	{
            "image_url": 'https://ibb.co/LPP482z',
            "text": "Передом щапит, а затылок вши выели. Эта карта выступает за равномерное развитие. "
        },
	{
            "image_url": 'https://ibb.co/NFTSFjZ',
            "text": "Я буду стоять в нём сколько захочу! Эта карта проецирует вашу самокритику, её недостаток или избыток."
        },
	{
            "image_url": 'https://ibb.co/6ZJbf1z',
            "text": "Тройной побег от себя. Эта карта требует развивать уже созданное, а не начинать новое."
        },
	{
            "image_url": 'https://ibb.co/T4g2yjD',
            "text": "Да не раздувай ты! Эта карта сравнивает тревогу с рыбой фугу, не умея обращаться с которой можно отравиться."
        },
	{
            "image_url": 'https://ibb.co/q07zZLh',
            "text": "Дать-то бы ничто, да было б за что. Эта карта взывает к милосердию."
        },
	{
            "image_url": 'https://ibb.co/K9BZB8r',
            "text": "Мои уши не готовы к таким речам. Эта карта напоминает о важности слов и их воздействие на нас и окружающих."
        },
	{
            "image_url": 'https://ibb.co/w04qvhL',
            "text": "Смелый через портал шагает, новых миров не боится. Эта карта нацелена на место любопытства в жизни."
        },
	{
            "image_url": 'https://ibb.co/YWrjVCt',
            "text": "Тазик с горячим вином никогда не подводил. Эта карта советует беречь основы."
        },
	{
            "image_url": 'https://ibb.co/nDR6D1s',
            "text": "Каждый раз дно оказывается выступом перед новой глубокой шелью. Эта карта настаивает на продолжении поиска."
        },
	{
            "image_url": 'https://ibb.co/mtcsbq9',
            "text": "Лучше ты один, чем мы все. Эта карта жертвует частью ради целого."
        },
	{
            "image_url": 'https://ibb.co/gwWLnF8',
            "text": "Слово не может ранить так, как нож. Эта карта говорит не забывать сказанного."
        },
	{
            "image_url": 'https://ibb.co/V937xYc',
            "text": "Кручусь как рыба, а денег не надыбал. Эта карта молчит."
        },
	{
            "image_url": 'https://ibb.co/wsc5dqh',
            "text": "Трое — уже толпа. Эта карта обещает невероятные высоты при грамотной кооперации."
        },
	{
            "image_url": 'https://ibb.co/jM3sdSc',
            "text": "Вот и рухнул кошкин дом, погорел со всем добром! Эта карта учит не жить прошлым."
        },
	{
            "image_url": 'https://ibb.co/DrRsMfL',
            "text": "С той стороны всё по-другому, не так, как у нас.Эта карта просит не бояться изучать неизведанное."
        },
	{
            "image_url": 'https://ibb.co/0hBFJns',
            "text": "Парадокс автора, шокирующий читателя, находится не в произведении, а в голове читателя. Эта карта борется с необъяснимым и проигрывает."
        },
	{
            "image_url": 'https://ibb.co/02TqC3t',
            "text": "Проснулись = ужаснулись. Эта карта предупреждает, что не стоит игнорировать сны и интуитивные ощущения."
        },
	{
            "image_url": 'https://ibb.co/GWKhjm9',
            "text": "Отрезвляет и опьяняет одновременно. Эта карта предостерегает от излишних мер по приведению себя в чувства"
        },
	{
            "image_url": 'https://ibb.co/0rL564H',
            "text": "Медленно, но верно я перестаю быть собой. Эта карта призывает быть готовым к тому, что с ростом приходят изменения."
        },
	{
            "image_url": 'https://ibb.co/YN4FY9G',
            "text": "С тобой говорит маньяк за тонким стеклом. Эта карта призывает к фильтру информации."
        },
	{
            "image_url": 'https://ibb.co/Xbys8hL',
            "text": "Дегельминтизация. Эта карта хотела бы ампутировать всё лишнее."
        },
	{
            "image_url": 'https://ibb.co/D8S8pCt',
            "text": "И взрослым, и детям, и молодёжи — долой уныние! Эта карта подчёркивает, что уныние и лень — это смертный грех."
        },
	{
            "image_url": 'https://ibb.co/frrVfQw',
            "text": "Кошку погубило любопытство, аможет и спасло. Эта карта говорит о неоднозначности любопытства."
        },
	{
            "image_url": 'https://ibb.co/kKGb1JL',
            "text": "Волнушка - груздьям подружка. Эта карта указывает на сложную взаимосвязь всех нас."
        },
	{
            "image_url": 'https://ibb.co/6NxZyTR',
            "text": "Медовая речь стекает из мандрилы прямо в ушную раковину. Эта карта рекомендует иногда не только слушать, но и смотреть."
        },
	{
            "image_url": 'https://ibb.co/Lz97nVg',
            "text": "Душа или туша? Эта карта ловит равновесие между плотским и духовным."
        },
	{
            "image_url": 'https://ibb.co/PjFfbF1',
            "text": "Сначала оденутся так, а потом жалуются, что их избегают. Эта карта вдохновляет на самовыражение и подчёркивает важность быть верным себе."
        }
    ]

    chosen_set = random.choice(sets)

    bot.send_photo(chat_id, chosen_set['image_url'])
    bot.send_message(chat_id, chosen_set['text'])


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Создаем клавиатуру
    keyboard = create_default_keyboard()

    if message.text == '⁂ КАРТА ДНЯ ⁂':
        send_random_image_and_text(message.chat.id)
    else:
        bot.send_message(message.chat.id, "Нажмите кнопку ⁂ КАРТА ДНЯ ⁂, чтобы начать самокопание", reply_markup=keyboard)


bot.polling(none_stop=True)