import random

text = "qwertyuiopasdfghjklzxcvbnm"

# Eng jalb etuvchi emoji-lar ro'yxati
emojilar = [
    "•", "°", ".", "-", "~", "∘", "·"
]

# 50 xil uslubdagi yozuvlar
yozuv = [
    "𝓆𝓌𝑒𝓇𝓉𝓎𝓊𝒾𝑜𝓅𝒶𝓈𝒹𝒻𝑔𝒽𝒿𝓀𝓁𝓏𝓍𝒸𝓋𝒷𝓃𝓂",   # Yozma uslub
    "𝓠𝓦𝓔𝓡𝓣𝓨𝓤𝓘𝓞𝓟𝓐𝓢𝓓𝓕𝓖𝓗𝓙𝓚𝓛𝓩𝓧𝓒𝓥𝓑𝓝𝓜",   # Katta yozma
    "𝕼𝖂𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒",   # Gotik shrift
    "𝑄𝑊𝐸𝑅𝑇𝒴𝒰𝐼𝒪𝒫𝒜𝒮𝒟𝑭𝑮𝑯𝑱𝒦𝑳𝒵𝒳𝑪𝒱𝒷𝒩𝑴",   # Katta va kichik harflar
    "𝐐𝐖𝐄𝐑𝐓𝐘𝐔𝐈𝐎𝐏𝐀𝐒𝐃𝐅𝐆𝐇𝐉𝐊𝐋𝐌",   # Qalin shrift
    "🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼",  # Quti shrift
    "ⓠⓦⓔⓡⓣⓨⓤⓘⓞⓟⓐⓢⓓⓕⓖⓗⓙⓚⓛⓩⓧⓒⓥⓑⓝⓜ",   # Doiralar bilan
    "𝙌𝙒𝙀𝙍𝙏𝙔𝙐𝙄𝙊𝙋𝘼𝙎𝘿𝙁𝙂𝙃𝙅𝙆𝙇𝙕𝙓𝘾𝙑𝘽𝙉𝙈",  # Matritsa uslubi
    "🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜",  # Doiradagi shriftlar
    "𝖖𝖜𝖊𝖗𝖙𝖞𝖚𝖎𝖔𝖕𝖆𝖘𝖉𝖋𝖌𝖍𝖏𝖐𝖑𝖟𝖝𝖈𝖛𝖇𝖓𝖒",   # Gotik qora shrift
    "𝑞𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝𝑎𝑠𝑑𝑓𝑔𝑕𝑗𝑘𝑙𝑧𝑥𝑐𝑣𝑏𝑛𝑚",   # Qiyshiq shrift
    "🅢🅘🅜🅑🅞🅛🅢",   # Emoji simvol uslublar
    "𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪",  # Yana bir gotik
    "𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞",  # O'rta asr uslubi
    "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶",  # Moslashgan
    "𝔅𝔬𝔩𝔡",  # Bold o'xshash
    "₵Ⱡ₳₴₴Ɽ₳", # Noodatiy harflar
    "🆂🅴🆁🅸🅴🆂",  # Oddiy emoji harflar
    "🄰🄱🄲🄳", # Emoji bilan shrift
    "ⓈⓅⒺⒸⒾⒶⓁ", # Maxsus emoji bilan
    "꧁༺Nick༻꧂", # Dekorativ yozuv
    "★𝓢𝓽𝔂𝓵𝓲𝓼𝓱★", # Yulduzchalar bilan
    "•†•𝓒𝓻𝓮𝓪𝓽𝓲𝓿𝓮•†•", # Yana bir dekorativ
    "▂▃▅▆█Fancy█▆▅▃▂", # Barlar bilan stilizatsiya
    "╰☆☆Nick☆☆╮", # Qavslar va yulduzlar bilan
    "×º°”˜`”°º×", # Dekorativ elementlar bilan
    "𝑄𝑊𝐸𝑅𝑇𝑌𝑈𝐼𝑂𝑃𝐴𝑆𝐷𝐹𝐺𝐻𝐽𝐾𝐿𝑍𝑋𝐶𝑉𝐵𝑁𝑀",
    "🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼",
    "𝙌𝙒𝙀𝙍𝙏𝙔𝙐𝙄𝙊𝙋𝘼𝙎𝘿𝙁𝙂𝙃𝙅𝙆𝙇𝙕𝙓𝘾𝙑𝘽𝙉𝙈",
    "𝚀𝚾𝙴𝚹𝚸𝙸𝙾𝙿𝙰𝚲𝙳𝙵𝙶𝙷𝙹𝙺𝙻𝚹𝚾𝙲𝚸𝙱𝙽𝙼",
     "★彡🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼彡★",
     "Ɋᗯᗴᖇ丅ƳᑌᎥᗝᑭᗩᔕᗪᖴǤᕼᒎᛕᒪ乙᙭ᑕᐯᗷᑎᗰ",
     "QŴĔŔŤŶÚĨŐРĂŚĎŦĞĤĴĶĹŹЖČVβŃМ",
]



def add_stylized_effects(text):
    special_chars = [" "]
    result = ""
    for char in text:
        result += char + random.choice(special_chars)
    return result

def nick_generator(name):
    result = []
    for fon in yozuv:
        min_length = min(len(text), len(fon))
        my_name = name.lower()
        for i in range(min_length):
            my_name = my_name.replace(text[i], fon[i])
        
        # Tasodifiy emoji qo'shish
        random_emoji = random.choice(emojilar)
        stylized_name = add_stylized_effects(my_name)
        my_name_with_emoji = f"{random_emoji} {stylized_name} {random_emoji}"
        
        result.append(my_name_with_emoji)
    return result



def long_nick(text, style_number):
    if 1 <= style_number <= len(yozuv):
        fon = yozuv[style_number - 1]
        m_name = text.lower()
        stylized_name = add_stylized_effects(m_name)
        # stylized_name = ""
        for char in text:
            index = text.find(char)
            if index < len(fon):
                stylized_name += fon[index]
            else:
                stylized_name += char

        # Add random emoji
        random_emoji = random.choice(emojilar)
        my_name_with_emoji = f"{random_emoji} {add_stylized_effects(stylized_name)} {random_emoji}"
        return my_name_with_emoji
    else:
        return "Noto'g'ri raqam. Iltimos, 1 dan {} gacha bo'lgan raqamni kiriting.".format(len(yozuv))

# Test the long_nick function
print(long_nick("Boborahim", 4))



def nick_uzun(text,style_number):
    result = []
    if not (1 <= style_number <= 33):
        raise ValueError("Style number must be between 1 and 33")

    # Example function to add stylized effects
    def add_stylized_effects(name):
        # Add your stylized effects logic here
        return name

    # Select a style based on the style_number
    fon = yozuv[style_number - 1]  # Adjust indexing to match your list

    min_length = max(len(text), len(fon))
    m_name = text.lower()

    # Apply the selected style
    # Note: Ensure your implementation for applying styles
    stylized_name = add_stylized_effects(m_name)

    # Add random emojis
    random_emoji = random.choice(emojilar)
    my_name_with_emoji = f"{random_emoji} {stylized_name} {random_emoji}"

    result.append(my_name_with_emoji)
    return result


print(nick_uzun("Boborahim", 5))