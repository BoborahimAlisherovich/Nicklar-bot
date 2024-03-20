text = "qwertyuiopasdfghjklzxcvbnm"
fonts = ["🅠🅦🅔🅡🅣🅨🅤🅘🅞🅟🅐🅢🅓🅕🅖🅗🅙🅚🅛🅩🅧🅒🅥🅑🅝🅜","🅀🅆🄴🅁🅃🅈🅄🄸🄾🄿🄰🅂🄳🄵🄶🄷🄹🄺🄻🅉🅇🄲🅅🄱🄽🄼","𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞"]
emoji = "⛄️✨⭐️⚽️"
import random

def nick_generator(name):
    result = []
    for font in fonts:
        my_name = name
        for i in range(len(text)):
            my_name = my_name.replace(text[i],font[i])
        e = random.choice(emoji)
        result.append(e+my_name+e)
    return result

