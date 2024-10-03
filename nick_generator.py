import random

text = "qwertyuiopasdfghjklzxcvbnm"

# Eng jalb etuvchi emoji-lar ro'yxati
# emojilar = [
#     "•", "°", ".", "-", "~", "∘", "·"
# ]

# 50 xil uslubdagi yozuvlar
yozuv = [
    "𝓠𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶"
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
    "🅢🅘🅜🅑🅞🅛🅢",   # Emoji simvol uslublar
    "𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪",  # Yana bir gotik
    "𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞",  # O'rta asr uslubi
    "𝓺𝔀𝓮𝓻𝓽𝔂𝓾𝓲𝓸𝓹𝓪𝓼𝓭𝓯𝓰𝓱𝓳𝓴𝓵𝔃𝔁𝓬𝓿𝓫𝓷𝓶",  # Moslashgan
    "𝔅𝔬𝔩𝔡",  # Bold o'xshash
    "₵Ⱡ₳₴₴Ɽ₳", # Noodatiy harflar
    "🆂🅴🆁🅸🅴🆂",  # Oddiy emoji harflar
    "▂▃▅▆█Fancy█▆▅▃▂", # Barlar bilan stilizatsiya
    "╰☆☆Nick☆☆╮", # Qavslar va yulduzlar bilan
    "×º°”˜`”°º×", # Dekorativ elementlar bilan
    "𝑄𝑊𝐸𝑅𝑇𝑌𝑈𝐼𝑂𝑃𝐴𝑆𝐷𝐹𝐺𝐻𝐽𝐾𝐿𝑍𝑋𝐶𝑉𝐵𝑁𝑀",
    "𝙌𝙒𝙀𝙍𝙏𝙔𝙐𝙄𝙊𝙋𝘼𝙎𝘿𝙁𝙂𝙃𝙅𝙆𝙇𝙕𝙓𝘾𝙑𝘽𝙉𝙈",
    "𝚀𝚾𝙴𝚹𝚸𝙸𝙾𝙿𝙰𝚲𝙳𝙵𝙶𝙷𝙹𝙺𝙻𝚹𝚾𝙲𝚸𝙱𝙽𝙼",
     "★彡🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼彡★",
     "Ɋᗯᗴᖇ丅ƳᑌᎥᗝᑭᗩᔕᗪᖴǤᕼᒎᛕᒪ乙᙭ᑕᐯᗷᑎᗰ",
     "QŴĔŔŤŶÚĨŐРĂŚĎŦĞĤĴĶĹŹЖČVβŃМ",
    "𝑞𝑤𝑒𝑟𝑡𝑦𝑢𝑖𝑜𝑝𝑎𝑠𝑑𝑓𝑔𝑕𝑗𝑘𝑙𝑧𝑥𝑐𝑣𝑏𝑛𝑚",   # Qiyshiq shrift
    "🅢🅘🅜🅑🅞🅛🅢",   # Emoji simvol uslublar
    "𝙌𝙒𝙀𝙍𝙏𝙔𝙐𝙄𝙊𝙋𝘼𝙎𝘿𝙁𝙂𝙃𝙅𝙆𝙇𝙕𝙓𝘾𝙑𝘽𝙉𝙈",
    'ợฬєгՇץยเ๏קคร๔Ŧﻮђןкɭչאςש๒ภ๓',
    "qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ",
    "qЩΣЯƬyЦiӨpΛƧdfgΉjkᄂzxᄃvbПm",
    "Ɋ山乇尺ㄒㄚㄩ丨ㄖ卩卂丂ᗪ千Ꮆ卄ﾌҜㄥ乙乂匚ᐯ乃几爪",
    "ꆰꅐꏂꋪ꓄ꌦ꒤꒐ꄲꉣꋬꇙ꒯ꊰꍌꁝ꒻ꀘ꒒ꁴꉧꉔ꒦ꃳꋊꂵ",
    "𝘲𝘸𝘦𝘳𝘵𝘺𝘶𝘪𝘰𝘱𝘢𝘴𝘥𝘧𝘨𝘩𝘫𝘬𝘭𝘻𝘹𝘤𝘷𝘣𝘯𝘮",
    "ҩω૯Ր੮עυɿ૦ƿคςძԲ૭ҺʆқՆઽ૪८౮ცՈɱ",
    "qwₑᵣ𝚝yᵤᵢₒ𝐩ₐ𝘴𝚍fg𝓱ⱼ𝓴ᄂzₓ𝚌ᵥ𝚋𝚗ᗰ",
    "ϙɯҽɾƚყυισραʂԃϝɠԋʝƙʅȥxƈʋႦɳɱ",
    "ｑώⒺℝ𝓣ч𝕌𝕚ᵒƤＡ𝕤Ⓓ𝕗قĦנｋ𝕃𝕫ˣ𝐜𝕧𝔟ภ𝓶",
    "Q₩ɆⱤ₮ɎɄłØ₱₳₴Đ₣₲ⱧJ₭ⱠⱫӾ₵V฿₦₥", 


]




def add_stylized_effects(text):
    special_chars = [""]
    result = ""
    for char in text:
        result += char + random.choice(special_chars)
    return result



# def nick_generator(name, son=None):
def nick_generator(name,son=None):
    result = []
    if son:
        fon = yozuv[son-1]
        min_length = max(len(text), len(fon))
        my_name = name.lower()
        for i in range(min_length):
          if i < len(name) and i < len(fon):  # Indeksdan tashqarida chiqish oldini olish

            my_name = my_name.replace(text[i], fon[i])
            
            
        return my_name
    
    else:
        for fon in yozuv:
            min_length = min(len(text), len(fon))
            my_name = name.lower()
            for i in range(min_length):
                my_name = my_name.replace(text[i], fon[i])
            
            # Tasodifiy emoji qo'shish
            # random_emoji = random.choice(emojilar)
            stylized_name = add_stylized_effects(my_name)
            my_name_with_emoji = f" {stylized_name}"
            
            result.append(my_name_with_emoji)
        return result



