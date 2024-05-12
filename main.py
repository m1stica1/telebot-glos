import telebot
from telebot import types

bot = telebot.TeleBot('7114509067:AAGzqBnNnquqc48A1euTEQzl3zaLGzVwu5M')

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Текст, который будет отправлен после команды /start
    start_text = "Привет! Это бот. Как дела?"
    # Создаем клавиатуру с инлайн кнопками
    inline_keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Текстиль", callback_data='textile')
    button2 = types.InlineKeyboardButton("Обувь", callback_data='shoes')
    inline_keyboard.add(button1, button2)
    # Отправляем сообщение с текстом и инлайн кнопками
    bot.send_message(message.chat.id, start_text, reply_markup=inline_keyboard)

# Обработчик нажатий на кнопки (тестиль + обувь + верх)
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_button_click(call):
    # Определяем текст для каждой кнопки (Кнопка Текстиль)
    if call.data == 'textile':
        # Создаем новую клавиатуру с дополнительными кнопками (Все по текстилю)
        inline_keyboard = types.InlineKeyboardMarkup()
        button3 = types.InlineKeyboardButton("ActivChill", callback_data='button3')
        button4 = types.InlineKeyboardButton("ACTIVCHILL+DREAMBLEND", callback_data='button4')
        button5 = types.InlineKeyboardButton("MOTIONFRESH", callback_data='button5')
        button6 = types.InlineKeyboardButton("LYCRA® FITSENSE ™", callback_data='button6')
        button7 = types.InlineKeyboardButton("GORE-TEX", callback_data='button7')
        button8 = types.InlineKeyboardButton("CORDURA®", callback_data='button8')
        button9 = types.InlineKeyboardButton("RBK – CHILL", callback_data='button9')
        button10 = types.InlineKeyboardButton("RBK – CHILL+", callback_data='button10')
        button11 = types.InlineKeyboardButton("RBK – FRESH", callback_data='button11')
        button12 = types.InlineKeyboardButton("RBK-DRY", callback_data='button12')
        button13 = types.InlineKeyboardButton("Speedwick", callback_data='button13')
        button14 = types.InlineKeyboardButton("RBK - ENDURE", callback_data='button14')
        button15 = types.InlineKeyboardButton("DREAMBLEND COTTON", callback_data='button15')
        button16 = types.InlineKeyboardButton("LUX CONTOUR", callback_data='button16')
        button17 = types.InlineKeyboardButton("Thinsulate", callback_data='button17')
        button18 = types.InlineKeyboardButton("THERMOWARM + GRAPHENE", callback_data='button18')
        button19 = types.InlineKeyboardButton("SOFTSHELL", callback_data='button19')
        button20 = types.InlineKeyboardButton("ВЛАГОСТОЙКОСТЬ (WATERRESSISTANCE)", callback_data='button20')
        button21 = types.InlineKeyboardButton("NATURAL DYE", callback_data='button21')
        button22 = types.InlineKeyboardButton("Ткань French Terry", callback_data='button22')

        inline_keyboard.add(button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16, button17, button18, button19, button20, button21, button22)
        # Отправляем сообщение с дополнительной клавиатурой
        bot.send_message(call.message.chat.id, "Выберите технологию:", reply_markup=inline_keyboard)

    elif call.data in ['button3', 'button4', 'button5', 'button6', 'button7', 'button8', 'button9', 'button10', 'button11', 'button12', 'button13', 'button14', 'button15', 'button16', 'button17', 'button18', 'button19', 'button20', 'button21', 'button22']:
        text = {
            'button3': "ActivChill - плетение нитей в форме пятиугольника – одежда «дышит», пропуская потоки воздуха и способствуя лучшей вентиляции, что позволяет тренироваться намного интенсивнее и дольше",
            'button4': "ACTIVCHILL+DREAMBLEND -  смешение между собой охлаждающий эффект с «плюшевым» комфортом из линейки премиального хлопка DREAMBLEND COTTON.",
            'button5': "MOTIONFRESH - нанесение на внутренней стороне продукта, которое предотвращает «прилипание» бактерий к ткани. Это не только устраняет неприятный запах в первоисточнике, но и предотвращает постоянный запах. Такое нанесение также продлевает срок службы одежды, уменьшая необходимость в частой стирке.",
            'button6': "LYCRA® FITSENSE ™ - Технология представляет собой запатентованный раствор на водной основе, который не содержит растворителей и включает те же молекулы, что и волокно LYCRA®. Состав наносится тончайшей трафаретной печатью непосредственно на внутреннюю или внешнюю сторону ткани, изготовленной из волокна LYCRA®. Это позволяет использовать более легкие ткани в одежде, избегать необходимости в тяжелых прочных тканях, вшитых панелях для усиления прочности, нетканых материалах и т.п. и удовлетворять при этом потребности покупательниц в поддержке",
            'button7': "GORE-TEX - несколько разновидностей водонепроницаемых материалов толщиной 0,01 мм, располагающихся между прокладкой и верхом обуви. Основные свойства GORE-TEX это 100% водостойкость, непроницаемость и защита от ветра. Ткань имеет такое строение, что ее поры в 20 000 раз меньше капли воды, поэтому не пропускают влагу внутрь обуви, и в то же время в 700 раз больше молекулы водяного пара, благодаря чему испарения выводятся наружу, что позволяет ноге «дышать» и оставаться сухой.",
            'button8': "CORDURA® является зарегистрированной торговой маркой сертифицированного нейлона от американской компании INVISTA. Кордура представляет из себя толстую нейлоновую ткань с особой структурой нити, с водоотталкивающей пропиткой, полиуретановым покрытием и небольшим добавлением хлопка.   ПРЕИМУЩЕСТВА:  • Высокая прочность и устойчивость к внешним воздействиям;   • Износостойкость, устойчивость к истиранию;   • Водоотталкивающие свойства;   • Плотность ткани не препятствует воздухообмену;   • Сравнительно проста в уходе, легко чистится.   НЕДОСТАТКИ:   • Не сравнится с мембраной, способна со временем пропускать воду;   • Намокшая ткань долго сохнет;   • Теряет свойства при температуре ниже -25°",
            'button9': "RBK – CHILL – это обновление знаменитой технологии ACTIVCHILL. Свойства аналогичны технологии ACTIVCHILL",
            'button10': "RBK – CHILL+ – это обновление знаменитой технологии ACTIVCHILL +DREAMBLEND. Свойства аналогичны технологии ACTIVCHILL +DREAMBLEND",
            'button11': "RBK – FRESH – это обновление технологии MOTIONFRESH. Свойства аналогичны технологии MOTIONFRESH.",
            'button12': "RBK-DRY это обновленная технология SPEEDWICK. Она отводит излишки влаги с кожи, оставляя ощущение сухости и комфорта.",
            'button13': "Speedwick - отводит излишки влаги с кожи, оставляя ощущение сухости и комфорта.",
            'button14': "RBK - ENDURE-износостойкость, облегченный материал из смеси полиэстера и хлопка для активных тренировок.",
            'button15': "DREAMBLEND COTTON- Изделия из DREAMBLEND сделаны из чрезвычайно мягкого хлопка двойной вязки, переработанного полиэстера и эластана для максимально комфортного ощущения на коже. Так же, все модели этой коллекции выполнены из экологичного хлопка Better Cotton Initiative.",
            'button16': "LUX CONTOUR - Облегающий силуэт, поддерживающие контурные вставки и инновационные решения, повышающие уверенность в себе, призваны подчеркнуть ее смелость и обеспечить максимальный комфорт, необходимый для любой тренировки.",
            'button17': "Thinsulate – волокно в 50 -70 раз тоньше человеческого волоса, очень упругое (при любом смятии всё равно держит объем). В этом объеме сохраняется большой объем воздуха за счет микроскопической тонкости волокон. А воздух – самый лучший изолятор от холода.Thinsulate имеет высший международный сертификат качества ISO 9002, он гипоаллергенен и обладает великолепными гигиеническими свойствами.   Преимущества Thinsulate:   • Самый легкий из всех синтетических наполнителей   • В 1.5 раза теплее натурального пуха   • Обладает уникальными терморегулирующими свойствами   • Не впитывает влагу   • Великолепно сохраняет форму после стирки и сушки   • Не вызывает аллергии   • Имеет европейский экологический сертификат   • Прекрасно вентилируется",
            'button18': "THERMOWARM + GRAPHENE (графен) - самый прочный, легкий и тонкий материал на Земле, также самый теплопроводный  материал,то есть он может поглощать и удерживать больше тепла, чем любое другое вещество на Земле. Графеновый принт представляет собой непрерывную геометрическую сетку, с наложенными на нее топографическими линиями Исландии. Тепло тела будет поглощаться и удерживаться на всех печатных панелях, содержащих графен, чтобы помочь потребителю оставаться в тепле в холодных погодных условиях.",
            'button19': "SOFTSHELL- Это искусственный материал средней плотности – гладкий снаружи и флисовый внутри. свойства: основная задача материала softshell – сохранять тепло, при этом позволяя телу дышать, модели из softshell легкие и тонкие, но могут заменить несколько слоев одежды, прочные и долговечные.",
            'button20': "ВЛАГОСТОЙКОСТЬ (WATERRESSISTANCE) – это свойство ткани не намокать и не пропускать воду. достигается благодаря нанесению на материал полимерного покрытия или за счет соединения материала с мембраной.",
            'button21': "NATURAL DYE- выполнены из экологичного хлопка с применением натуральных минеральных красителей, чтобы снизить негативный эффект от производства на окружающую среду.",
            'button22': "Ткань French Terry — это высокопористый вид трикотажа, обладающий мягкой воздушной структурой. Она отличается особым способом плетения и подходит для производства толстовок, худи, джемперов, брюк, одежды для младенцев, футболок, платьев и юбок",
        }

        # Отвечаем на нажатие кнопки
        bot.send_message(call.message.chat.id, text[call.data])
    
    elif call.data == 'shoes':
        # Создаем новую клавиатуру с дополнительными кнопками (Обувь)
        inline_keyboard = types.InlineKeyboardMarkup()
        button23 = types.InlineKeyboardButton("EVA", callback_data='button23')
        button24 = types.InlineKeyboardButton("CMEVA", callback_data='button24')
        button25 = types.InlineKeyboardButton("IMEVA", callback_data='button25')
        button26 = types.InlineKeyboardButton("FLOATRIDE ENERGY ™", callback_data='button26')
        button27 = types.InlineKeyboardButton("FLOATRIDE+", callback_data='button27')
        button28 = types.InlineKeyboardButton("FLOATIRDE FUEL", callback_data='button28')
        button29 = types.InlineKeyboardButton("FUELFOAM", callback_data='button29')
        button31 = types.InlineKeyboardButton("FLEXWEAVE", callback_data='button31')
        button32 = types.InlineKeyboardButton("SPEEDSHIFT 2.0", callback_data='button32')
        button33 = types.InlineKeyboardButton("Lift & Run (L.A.R)", callback_data='button33')
        button34 = types.InlineKeyboardButton("ROPEPRO", callback_data='button34')
        button35 = types.InlineKeyboardButton("X-PLATE", callback_data='button35')
        button36 = types.InlineKeyboardButton("ZIG ENERGY BANDS", callback_data='button36')
        button37 = types.InlineKeyboardButton("PUMP", callback_data='button37')
        button38 = types.InlineKeyboardButton("HEXALITE", callback_data='button38')
        button39 = types.InlineKeyboardButton("GORE-TEX", callback_data='button39')
        button40 = types.InlineKeyboardButton("Vibram", callback_data='button40')
        button41 = types.InlineKeyboardButton("eVent", callback_data='button41')
        button42 = types.InlineKeyboardButton("CORDURA®", callback_data='button42')
        button43 = types.InlineKeyboardButton("MEMORYTECH", callback_data='button43')
        button44 = types.InlineKeyboardButton("ORTHOLITE", callback_data='button44')
        button45 = types.InlineKeyboardButton("DMX Moving Air", callback_data='button45')
        button46 = types.InlineKeyboardButton("KineticFit", callback_data='button46')
        button47 = types.InlineKeyboardButton("DMX Foam", callback_data='button47')
        button48 = types.InlineKeyboardButton("MICHELIN", callback_data='button48')
        button49 = types.InlineKeyboardButton("SOFTSHELL", callback_data='button49')
        button50 = types.InlineKeyboardButton("ВЛАГОСТОЙКОСТЬ/(WATERRESSISTANCE)", callback_data='button50')
        button51 = types.InlineKeyboardButton("RS (Running System)", callback_data='button51')
        button52 = types.InlineKeyboardButton("Softfoam", callback_data='button52')
        button53 = types.InlineKeyboardButton("Nitro", callback_data='button53')
        button54 = types.InlineKeyboardButton("ZIGTECH", callback_data='button54')
        button55 = types.InlineKeyboardButton("ZIG ENERGY SHELL", callback_data='button55')
        button56 = types.InlineKeyboardButton("DMX Microbubbles", callback_data='button56')
        
        inline_keyboard.add(button23, button24, button25, button26, button27, button28, button29, button31, button32, button33, button34, button35, button36, button37, button38, button39, button40, button41, button42, button43, button44, button45, button46, button47, button48, button49, button50, button51, button52, button53, button54, button55, button56)
        # Отправляем сообщение с дополнительной клавиатурой
        bot.send_message(call.message.chat.id, "Выберите технологию:", reply_markup=inline_keyboard)
    elif call.data in ['button23', 'button24', 'button25', 'button26', 'button27', 'button28', 'button29', 'button31', 'button32', 'button33', 'button34', 'button35', 'button36', 'button37', 'button38', 'button39', 'button40', 'button41', 'button42', 'button43', 'button44', 'button45', 'button46', 'button47', 'button48', 'button49', 'button50', 'button51', 'button52', 'button53', 'button54', 'button55', 'button56']:
        text = {
            'button23': "EVA (Ethylene-vinyl acetate) этиленвинилацетат (ЭВА). Один из первых технологичных материалов, появившийся в промежуточной подошве кроссовок на замену резине. Легкий, экологичный, эластичный материал с высокими амортизационными свойствами, однако значительно уступает современным пеноматериалам, появившимся в последнее десятилетие, ввиду чего всё реже используется в технологичной обуви. Материал достаточно устойчив к температурам, но при воздействии низких температур теряет большую часть своих амортизационных свойств.",
            'button24': "CMEVA (Compression Molded EVA) - производная от пены ЭВА, но отформованная под давлением (сompression (англ.) компрессия, давление). Компрессионное формование, как следует из названия, представляет собой процесс прессования блока пены ЭВА внутри металлической формы. Когда к форме прикладываются тепло и давление, материал расширяется и заполняет внутреннюю часть формы. Под давлением ЭВА принимает форму полости этой самой формы, включая рисунок, выгравированный на ее боках.",
            'button25': "IMEVA (Injection molded EVA) - производная от пены ЭВА, но отформованная методом впрыскивания (injection (англ.) впрыскивание). Перегретая жидкая масса из пены ЭВА и вспенивающего агента впрыскивается в форму, размер которой составляет менее половины размера фактической подошвы. Как и форма для прессования, форма для литья под давлением также имеет эти маркировки или гравировки, которые переносятся на дизайн подошвы.",
            'button26': "FLOATRIDE ENERGY – пеноматериал на основе ТРЕ (Thermoplastic elastomer), выполненный с использованием газообразного азота. Легкая пена с отзывчивой амортизацией, превосходящая по качеству пену ЭВА. Обеспечивает правильную динамику отталкивания и гасит ударные нагрузки.",
            'button27': "FLOATRIDE+ - пеноматериал на основе РЕВА (polyether block amine), выполненная с использованием газообразного азота. Самая легкая пена кроссовок Reebok. Мягкий перекат в шаге и отзывчивая амортизация.",
            'button28': "FLOATIRDE FUEL - пеноматериал на основе CMEVA с высокими амортизирующими свойствами. Гасит ударные нагрузки и способствует возврату вложенной при беге энергии. На сегодняшний день позиционируется брендом Reebok как лучшая пена на рынке в данном ценовом сегменте.",
            'button29': "FUELFOAM - пеноматериал на основе IMEVA обеспечивает амортизацию и гасит ударные нагрузки. Данный пеноматериал используется как в беговой, так и в повседневной обуви Reebok.",
            'button31': "FLEXWEAVE — инновационная технология плетения волокон в виде «8», за счет него кроссовки становятся гибкими и прочными одновременно. Технология может быть применена к волокнам разного состава",
            'button32': "SPEEDSHIFT 2.0 - современный технологичный материал верха. Легкий, дышащий, устойчивый к внешним воздействиям.",
            'button33': "Lift & Run (сокращенно (L.A.R) - представляет из себя конструкцию в пятке состоящую из куполообразного элемента из TPU, окруженного пеной Floatride. TPU затвердевает под нагрузкой для устойчивости, а затем размягчается, когда находится не под ней и в силу вступает пена, которая работает на отталкивание и отзывчивую амортизацию Задача технологии с одной стороны усилить стабилизационные свойства тренировочной обуви для работы с весами, с другой – усилить амортизацию и возврат энергии.",
            'button34': "ROPEPRO - представляет собой ребристую поверхность внутренней части кроссовка для надежного сцепления при лазании по канату.",
            'button35': "X-PLATE - Торсионная пластина в промежуточной подошве – Благодаря увеличению торсионной жесткости (уменьшению способности скручиваться) увеличилась рекомендованная дистанция, что добавляет моделям универсальности, делает их подходящими как на короткие дистанции, так и на длинные, включая полумарафон (21 км).",
            'button36': "ZIG ENERGY BANDS - резиновые полоски на подметке сжимаются и разжимаются, усиливая возврат энергии с каждым шагом.",
            'button37': "PUMP - технология, позволяющая накачивать воздух в воздушную камеру внутри кроссовка. Таким образом, накачиваемый внутрь кроссовок воздух заполняет свободное пространство вокруг ноги, идеально облегая ее и создавая превосходную посадку.",
            'button38': "HEXALITE - Сотовая, легковесная, амортизирующая деталь, которая располагается в подошве обуви, в области наиболее сильных ударных нагрузок, в основном в пяточной части. При силовом воздействии происходит изгиб стенок (перегородок) сотовых ячеек, каждая из которых соприкасается с 6-ю соседними, обеспечивая перераспределение приложенного усилия по всей поверхности сот. После каждого внешнего воздействия принимает изначальную форму.",
            'button39': "GORE-TEX - несколько разновидностей водонепроницаемых материалов толщиной 0,01 мм, располагающихся между прокладкой и верхом обуви. Основные свойства GORE-TEX это 100% водостойкость, непроницаемость и защита от ветра. Ткань имеет такое строение, что ее поры в 20 000 раз меньше капли воды, поэтому не пропускают влагу внутрь обуви, и в то же время в 700 раз больше молекулы водяного пара, благодаря чему испарения выводятся наружу, что позволяет ноге «дышать» и оставаться сухой.",
            'button40': "Технология Vibram - Элементы протектора классической подошва Vibram расположены на определенной высоте, на выверенном расстоянии и также под определенным углом по отношению друг к другу. Это позволяет сохранять устойчивость на любой поверхности, даже в экстремальных условиях, а также не забиваться.   ГЛАВНЫЕ КАЧЕСТВА ПОДОШВЫ VIBRAM:   • не забивается,   • плохо подвержена износу,   • не скользит, обеспечивая максимальное сцепление на скользких, скалистых или мокрых поверхностях",
            'button41': "eVent - Технология представляет из себя серию водонепроницаемых тканей (мембран), используемых в одежде и обуви для активного отдыха и спорта. Основное назначение – комфорт использования экипировки в самых непредсказуемых и изменчивых погодных условиях. Главным преимуществом является непревзойденные дышащие свойства при высочайшем уровне защиты от влаги.",
            'button42': "CORDURA® является зарегистрированной торговой маркой сертифицированного нейлона от американской компании INVISTA. Кордура представляет из себя толстую нейлоновую ткань с особой структурой нити, с водоотталкивающей пропиткой, полиуретановым покрытием и небольшим добавлением хлопка.   ПРЕИМУЩЕСТВА:   • Высокая прочность и устойчивость к внешним   воздействиям;   • Износостойкость, устойчивость к истиранию;  • Водоотталкивающие свойства;   • Плотность ткани не препятствует воздухообмену; • Сравнительно проста в уходе, легко чистится.   НЕДОСТАТКИ:   • Не сравнится с мембраной, способна со временем   пропускать воду;   • Намокшая ткань долго сохнет;   • Теряет свойства при температуре ниже -25°",
            'button43': "MEMORYTECH- технология стельки с эффектом памяти, гарантирует комфортную посадку за счет эффекта памяти.",
            'button44': "ORTHOLITE - технология, осуществляющая антибактериальную функцию в стельках.",
            'button45': "DMX Moving Air – технология амортизации, представляющая из себя систему воздушных подушек, размещенных в промежуточной подошве обуви. Основные свойства технологии DMX Moving Air: обеспечивает комфорт в динамике, активизируясь в том месте, куда перетекает давление стопы в конкретный момент;гасит ударные нагрузки;возвращает энергию.",
            'button46': "KineticFit – технология позволяющая верху кроссовка повторять движения стопы за счет специальных сетчатых вставок.",
            'button47': "DMX Foam - упругий материал межподошвы. Выполняет главную цель — обеспечить амортизацию в самых необходимых местах. Универсальность материала достигается с помощью двух слоёв, верхний из которых более комфортный и мягкий, а нижний — плотный и более устойчивый к резким ударам.",
            'button48': "технология michelin особенность данной технологии состоит в том, что подошвы изготовлены с применением элементов от шин автомобилей и мотоциклов. обеспечивают 100% сцепление с любой поверхностью - от сухой и сыпучей до влажной и скользкой • закругленные ламели обеспечивают быстрое, безопасное и эффективное движение. скосенное расположение ламелей улучшает отвод воды и грязи, гарантируя более надежное сцепление • адаптивны к движению благодаря своей гибкости. защищают от небольших ударов и неровностей грунта • долговечны",
            'button49': "SOFTSHELL- это искусственный материал средней плотности – гладкий снаружи и флисовый внутри. свойства: основная задача материала softshell – сохранять тепло, при этом позволяя телу дышать, модели из softshell легкие и тонкие, но могут заменить несколько слоев одежды, прочные и долговечные.",
            'button50': "ВЛАГОСТОЙКОСТЬ (WATERRESSISTANCE) – это свойство ткани не намокать и не пропускать воду. достигается благодаря нанесению на материал полимерного покрытия или за счет соединения материала с мембраной. ",
            'button51': "RS (Running System) — флагманская технология амортизации в беговых силуэтах PUMA 80-х. Кроссовки из серии RS отличались продвинутой стабилизацией, стильным видом и высоким уровнем комфорта.",
            'button52': "Стелька с технологией Softfoam - технология, которая используется в обуви, предназначенной как для занятий спортом, так и для повседневного использования. Особая мягкая пена в стельке (с эффектом памяти) принимает форму стопы, обеспечивая индивидуальный комфорт и защиту от травм.",
            'button53': "Nitro- Новая технология изготовления пены, направленная на высокую амортизацию и возврат энергии при сохранении маленького веса.Создана с использованием азота. На 50% легче чем EVA. В заготовку впрыскивают азот, выведенный с помощью суперкритического процесса, что увеличивает объем, позволяя получить чрезвычайно маленький вес.",
            'button54': "ZIGTECH - основанная на разработке 2010 года зигзагообразная промежуточная подошва обеспечивает дополнительный возврат энергии благодаря своей форме.",
            'button55': "ZIG ENERGY SHELL-Зигзагообразный ТПУ каркас обеспечивает стабилизацию, направляя и возвращая кинетическую энергию. Одновременно каркас является образующим элементом дизайна.",
            'button56': "DMX Microbubbles- Технологичная подошва с рядом соединенных между собой воздушных камер. Обеспечивает больше комфорта, амортизации и стабилизации в каждом шаге."
            }

        # Отвечаем на нажатие кнопки
        bot.send_message(call.message.chat.id, text[call.data])


# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)




bot.polling(none_stop=True)