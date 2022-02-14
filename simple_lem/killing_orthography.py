import pandas as pd
import re

rt='с̑'[1]
qt='҃'
def kill_orthography (word):
    word = str(word)
    word = re.sub(r'агг҃ел', r'ангел',word)
    word = re.sub(r'агг҃л', r'ангел',word)
    word = re.sub(r'аг҃гл', r'ангел',word)
    word = re.sub(r'анг҃л', r'ангел',word)
    word = re.sub(r'апс̑л([аоеуЕиыья]|$)', r'апостол\1',word)
    word = re.sub(r'апс̑лс', r'апостольс',word)
    word = re.sub(r'апс̑лми', r'апостолами',word)
    word = re.sub(r'апс̑то?л', r'апостол',word)
    word = re.sub(r'бг҃([аоеуЕиы$])', r'бог\1',word)
    word = re.sub(r'бг҃ъ?$', r'бог',word)
    word = re.sub(r'бг҃([^аоеуЕиы])', r'бого\1',word)
    word = re.sub(r'бго҃', r'бого',word)
    word = re.sub(r'бж҃([аоеуЕиы])', r'бож\1',word)
    word = re.sub(r'бж҃ств', r'божеств',word)
    word = re.sub(r'бж҃тв', r'божеств',word)
    word = re.sub(r'бз҃([еЕи])', r'боз\1',word)
    word =re.sub(r'бл҃з', r'блаз',word)
    word =re.sub(r'бл҃г', r'благ',word)
    word =re.sub(r'блг̑в', r'благов',word)
    word =re.sub(r'блгд̑т', r'благодат',word)
    word =re.sub(r'бл҃ж', r'блаж',word)
    word = re.sub(r'бжс̑тв', r'божеств',word)
    word = re.sub(r'блгс̑в', r'благослов',word)
    word = re.sub(r'блгс̑лов', r'благослов',word)
    word = re.sub(r'блгс̑т', r'благост',word)
    word = re.sub(r'блд̑гт', r'благодат',word)
    word = re.sub(r'ближ̑н', r'ближн',word)
    word = re.sub(r'блс̑гв', r'благослов',word)	
    word = re.sub(r'б(ц|ч)д̑', r'богороди\1',word)
    word =re.sub(r'без̑я', r'безъя',word)
    word =re.sub(r'вл҃к', r'владык',word)
    word =re.sub(r'влд̑чц', r'владычиц',word)
    word =re.sub(r'влд̑(к|ц|ч)', r'влады\1',word)	
    word =re.sub(r'воз̑я', r'возъя',word)
    word =re.sub(r'воскрс̑(н$|ни.)', r'воскресе\1',word)
    word =re.sub(r'воскрс̑л', r'воскресил',word)
    word =re.sub(r'воскрс̑', r'воскрес',word)
    word =re.sub(r'воскс̑рша', r'воскресша',word)
    word =re.sub(r'гл҃гол', r'глагол',word)
    word =re.sub(r'гл҃([аоеуЕиыяю]|$)', r'глагол\1',word)
    word =re.sub(r'гла҃', r'глагола',word)
    word =re.sub(r'гдс̑ьс?тв', r'господств',word)
    word =re.sub(r'гдс̑([^врк])', r'господ\1',word)
    word =re.sub(r'гдс̑в', r'господев',word)
    word =re.sub(r'гдс̑к', r'господск',word)
    word =re.sub(r'гдс̑рн', r'государын',word)
    word =re.sub(r'гдс̑р', r'государ',word)
    word =re.sub(r'глв̑а', r'глава',word)
    word =re.sub(r'глс̑', r'глаc',word)
    word =re.sub(r'гпс̑ж', r'госпож',word)
    word =re.sub(r'дх҃н', r'дохн',word)
    word =re.sub(r'двд̑', r'давид',word)
    word =re.sub(r'дв҃д', r'давид',word)
    word =re.sub(r'дв҃', r'дев',word)
    word =re.sub(r'д҃в', r'дев',word)
    word =re.sub(r'дн҃ь$', r'день',word)
    word =re.sub(r'дс҃([Еи])', r'дус\1',word)
    word =re.sub(r'дх҃([аоуеЕиы]|$)', r'дух\1',word)
    word =re.sub(r'дш҃([аоуеЕиыю]|$)', r'душ\1',word)
    word =re.sub(r'дав̑ше', r'давше',word)
    word =re.sub(r'двж̑а', r'дважды',word)
    word =re.sub(r'двс̑т', r'девст',word)
    word =re.sub(r'дерз̑новенно', r'дерзновенно',word)
    word =re.sub(r'домов̑ная', r'домовная',word)
    word =re.sub(r'ен̑н', r'енн',word)
    word =re.sub(r'евг̑а?л', r'евангел',word)
    word = re.sub(r'епкс̑па', r'епископа',word)
    word = re.sub(r'епс̑ко?п', r'епископ',word)
    word =re.sub(r'ии҃л(т|с)', r'израиль\1',word)
    word =re.sub(r'ии҃л', r'израил',word)
    word =re.sub(r'ии҃с(?!ус)', r'иисус',word)
    word =re.sub(r'(?<!и)ис҃([аоуеЕы]|$)(?!ус)', r'иисус\1',word)
    word = re.sub(r'иер?с̑л', r'иерусал', word)
    word = re.sub(r'избав̑л', r'избавл', word)
    word = re.sub(r'из̑(?!я)', r'из', word)
    word = re.sub(r'из̑я', r'изъя', word)
    word = re.sub(r'кн҃г', r'княг', word)
    word = re.sub(r'кн҃з', r'княз', word)
    word = re.sub(r'кн҃ж', r'княж', word)
    word = re.sub(r'кр҃с', r'крес', word)
    word = re.sub(r'крс̑т', r'крест', word)
    word = re.sub(r'кр҃щ', r'крещ', word)
    word = re.sub(r'кр҃ш', r'креш', word)
    word = re.sub(r'л̑ст', r'лест', word)
    word = re.sub(r'л̑щ', r'льщ', word)	
    word =re.sub(r'мт҃ер', r'матер',word)
    word =re.sub(r'мт҃р', r'матер',word)
    word =re.sub(r'мт҃', r'мат',word)
    word =re.sub(r'мл҃тв', r'молитв',word)
    word =re.sub(r'мл҃итв', r'молитв',word)
    word =re.sub(r'мл҃ст', r'милост',word)
    word =re.sub(r'млс̑т', r'милост',word)
    word =re.sub(r'млс̑рд', r'милосерд',word)
    word =re.sub(r'мл҃ч', r'молч',word)
    word =re.sub(r'мр҃и', r'мари',word)
    word =re.sub(r'мч҃ни', r'мучени',word)
    word =re.sub(r'мч҃ени', r'мучени',word)
    word =re.sub(r'мч҃н([^и])', r'мучени\1',word)
    word =re.sub(r'мд̑р', r'мудр',word)
    word =re.sub(r'мрд̑с', r'мудрос',word)
    word =re.sub(r'мрд̑', r'мудр',word)
    word =re.sub(r'млд̑н', r'младен',word)
    word =re.sub(r'млнд̑', r'младен',word)
    word =re.sub(r'млнд̑', r'младен',word)
    word =re.sub(r'мнс̑т', r'монаст',word)
    word =re.sub(r'мс̑ц', r'месяц',word)
    word =re.sub(r'мс̑ч', r'месяч',word)
    word =re.sub(r'м(ц|ч)с̑', r'меся\1',word)
    word =re.sub(r'нн҃Е', r'нынЕ',word)
    word =re.sub(r'нб҃([аоеуЕ])', r'неб\1',word)
    word =re.sub(r'нб҃с', r'небес',word)
    word =re.sub(r'н҃бс', r'небес',word)
    word =re.sub(r'нбс̑', r'небес',word)
    word =re.sub(r'ндл̑', r'недел',word)
    word =re.sub(r'нлд̑', r'недел',word)
    word = re.sub(r'от҃ч', r'отеч',word)
    word = re.sub(r'отч҃', r'отече',word)
    word = re.sub(r'оч҃ь', r'отечь',word)
    word = re.sub(r'оч҃е?(?=с[кт])', r'отече',word)
    word = re.sub(r'оч҃', r'отч',word)
    word =re.sub(r'оц҃$', r'отец',word)
    word =re.sub(r'оц҃', r'отц',word)
    word =re.sub(r'пл҃т', r'плот',word)
    word =re.sub(r'пл҃щ', r'площ',word)
    word =re.sub(r'прпд̑бн$', r'преподобен',word)
    word =re.sub(r'прпд҃б', r'преподоб',word)
    word =re.sub(r'прпд̑б', r'преподоб',word)
    word =re.sub(r'прпд̑н', r'преподобн',word)
    word =re.sub(r'прпд̑бс', r'преподобс',word)
    word =re.sub(r'прс̑н', r'присн',word)
    word =re.sub(r'прс̑тол', r'престол',word)
    word =re.sub(r'псл҃ом', r'псалом',word)
    word =re.sub(r'првд̑н$', r'праведен',word)
    word =re.sub(r'првд̑н(.)', r'праведн\1',word)
    word =re.sub(r'првд̑вн', r'праведн',word)
    word =re.sub(r'првд̑ен', r'праведен',word)
    word =re.sub(r'прд̑вен', r'праведен',word)
    word =re.sub(r'прд̑е', r'пред',word)	
    word =re.sub(r'прд̑те?ч', r'предтеч',word)
    word =re.sub(r'пнд̑е', r'понедельник',word)
    word =re.sub(r'пнд̑л', r'понедел',word)
    word =re.sub(r'под̑я', r'подъя',word)
    word =re.sub(r'про̑рк', r'пророк',word)
    word =re.sub(r'прро̑к', r'пророк',word)
    word =re.sub(r'прро̑чц', r'пророчиц',word)
    word =re.sub(r'ржд̑н', r'рожден',word)
    word =re.sub(r'ржс̑т', r'рождест',word)
    word = re.sub(r'см҃рт', r'смерт',word)
    word = re.sub(r'смр̑т', r'смерт',word)
    word =re.sub(r'сп҃с', r'спас',word)
    word =re.sub(r'спс̑н', r'спасен',word)
    word =re.sub(r'спс̑те', r'спасите',word)
    word =re.sub(r'спс̑', r'спас',word)
    word =re.sub(r'сн҃([аоеуЕиыю]|$)', r'сын\1',word)
    word =re.sub(r'сл҃в', r'слав',word)
    word =re.sub(r'слв̑', r'слов',word)
    word =re.sub(r'сл҃нц', r'солнц',word)
    word =re.sub(r'сл҃не?ч', r'солнеч',word)
    word =re.sub(r'ср҃д', r'серд',word)
    word =re.sub(r'срд̑ц(.)', r'сердц\1',word)
    word =re.sub(r'срд̑ц$', r'сердец',word)
    word =re.sub(r'срд̑ч', r'сердеч',word)
    word =re.sub(r'срцд̑ы', r'сердцы',word)
    word =re.sub(r'сщ҃([аоеуяыи])', r'свящ\1',word)
    word =re.sub(r'ст҃([аоеуяЕыи]|$)', r'свят\1',word)
    word =re.sub(r'прс̑т([аоеуяЕыи]|$)', r'свят\1',word)
    word =re.sub(r'ст҃л', r'святител',word)
    word =re.sub(r'ст҃т', r'святит',word)
    word =re.sub(r'стрс̑т(?!ерп)', r'страст',word)
    word =re.sub(r'стрс̑терп', r'страстотерп',word)
    word = re.sub(r'стх̑р', r'стихир', word)
    word =re.sub(r'телст̑в', r'тельств',word)
    word =re.sub(r'тел̑ств', r'тельств',word)
    word =re.sub(r'тел̑н', r'тельн',word)
    word =re.sub(r'тови҃', r'товит',word)
    word =re.sub(r'тро̑(ц|ч)', r'трои\1',word)
    word =re.sub(r'уч҃ни', r'учени',word)
    word =re.sub(r'учн҃и', r'учени',word)
    word =re.sub(r'учн҃(к|ц|ч)', r'учени\1',word)
    word =re.sub(r'уч҃н(к|ц|ч)', r'учени\1',word)
    word =re.sub(r'уч҃те?л', r'учител',word)
    word =re.sub(r'учте?҃л', r'учител',word)
    word =re.sub(r'х҃с', r'христос',word)
    word =re.sub(r'хрс̑т', r'христ',word)
    word =re.sub(r'цр҃([аоеуЕиыюсья])', r'цар\1',word)
    word =re.sub(r'цр҃ц', r'цариц',word)
    word =re.sub(r'цр҃кв(?!ь)', r'церкв',word)
    word =re.sub(r'цр҃квь', r'церковь',word)
    word =re.sub(r'цр҃ков', r'церков',word)
    word =re.sub(r'црс̑(т|к)', r'царст\1',word)
    word =re.sub(r'цс̑рт', r'царст',word)
    word =re.sub(r'ч҃лв', r'челов',word)
    word =re.sub(r'чл҃о?в', r'челов',word)
    word =re.sub(r'чл҃(к|ч|ц)', r'челове\1',word)
    word =re.sub(r'члчс̑к', r'человеческ',word)
    word =re.sub(r'благочс̑т', r'благочест',word)
    word =re.sub(r'благочтс̑и', r'благочести',word)
    word =re.sub(r'чс̑т([^н]|$)', r'чист\1',word)
    word =re.sub(r'чтс̑([^н]|$)', r'чист\1',word)
    word =re.sub(r'чтс̑е?н$', r'честен',word)
    word =re.sub(r'чс̑те?н$', r'честен',word)
    word =re.sub(r'чтс̑н(.)', r'честн\1',word)	
    word =re.sub(r'чс̑тн(.)', r'честн\1',word)
    word =re.sub(r'чтс̑н(.)', r'честн\1',word)	
    word =re.sub(r'единочс̑тн', r'единочестн',word)
    word =re.sub(r'многочс̑тн', r'многочестн',word)
    word =re.sub(r'нечс̑т([^н])', r'нечист\1',word)
    word =re.sub(r'^очтс̑и', r'очисти',word)
    word =re.sub(r'^очс̑ти', r'очисти',word)
    word =re.sub(r'и(м҃ре|мр̑)къ', r'имярек',word)
    word =re.sub(r'нш҃ихъ', r'наших',word)
    word =re.sub(rt, r'',word)
    word =re.sub(qt, r'',word)
    word =re.sub('҂', r'',word)
    word =re.sub(r'ъ$', r'',word)
    word =re.sub(r'Е', r'е',word)
    word = re.sub(r'ы́'[1],r'',word)
    word = re.sub(r'я̂'[1],r'',word)
    word = re.sub(r'і',r'и',word)
    word = re.sub(r'ѡ',r'о',word)
    word = re.sub(r'ѻ',r'о',word)
    word = re.sub(r'[ѣє]',r'е',word)
    word = re.sub(r'(е|а|о)ѵ',r'\1в',word)
    word = re.sub(r'ѵ',r'и',word)
    word = re.sub(r'ѳ',r'ф',word)
    word = re.sub(r'ѱ',r'пс',word)
    word = re.sub(r'ѯ',r'кс',word)
    word = re.sub(r'ѕ',r'з',word)
    word =re.sub(r'я̀'[1], r'',word)
    word =re.sub(r'(?<=а)гг(?=(ай|е|ее|еева|еево|ей|ею|ея|ие|ий||я|а|ю||л|ла|лу|ле|лом|лов|лы|ли|льстии|лино)$)', r'ГГ',word)
    word =re.sub(r'гг', r'нг',word)
    word =re.sub(r'гк', r'нк',word)
    word =re.sub(r'гх', r'нх',word)
    word =re.sub(r'ГГ', r'гг',word)
    return word.lower()

#polyakov = pd.read_csv("polyakov_dic.tsv", sep = '\t', converters = {
#        'sort': kill_tilda,
#        'lex': kill_orthography
#    })

#voc = pd.read_csv('polyakov_dic.tsv', sep = '\t')

voc = pd.read_csv("polyakov_dic.tsv", sep = '\t', converters = {
        'sort': kill_orthography,
        'lex': kill_orthography
    }).sort_values(by = 'freq', ascending = False)
pronouns = pd.read_excel('addit_dict.xls', sheet_name = 'pronum', converters = {
        'lex': kill_orthography,
        'sort': kill_orthography
}).sort_values(by = 'freq', ascending = False)
numbers = pd.read_excel('addit_dict.xls', sheet_name = 'num', converters = {
        'lex': kill_orthography,
        'sort': kill_orthography
}).sort_values(by = 'freq', ascending = False)

longdict = pd.concat([voc, numbers, pronouns], sort = False)
del longdict['id']
longdict.sort_values(by='freq', ascending = False)

longdict.to_csv('voc.csv', sep = '\t', index = None)

