from google.appengine.ext import webapp

register = webapp.template.create_template_register()

def minus( value, arg ):
    value = int( value )
    arg = int( arg )
    if arg: return value - arg

captions = {
1 : "Eoin 1 day old, john and liz, 25th March 1980",
2 : "eon's christening, frank curran, maurice sheehy, 4months old summer 1980",
3 : "eoin smiling at his mum, about 5 months",
4 : "at home, maybe watching tv",
5 : "first steps in bushy part, circa may 1981",
6 : "jan or feb 1982 with baby darragh",
7 : "1981, green saab, first driving..",
8 : "christmas checkup for mum, probably 3.5",
9 : "1985, trip to the zoo with darragh and triona",
10 : "Summer Family holidays with the Griffins, 1987, comeeknowel Co Kerry",
11 : "Summer Holidays with the sheehys, no inchydoney, billy, nuala, gran 1988",
12 : "Circa 1988/1989 with John and Liz",
13 : "In Fota wildlife park, circa 1989",
14 : "In St Pats Drmcondra, After Logo programming",
15 : "About 12 resting up",
16 : "Trophy awarded for scoring a perfect 800 in SAT math aged 15.",
17 : "With Naoise Gaffney in a hot spring, on green tortoise tour across us (summer I went with kuss? or earlier)",
18 : "With Darragh, in MBC chamonix.   (07)",
19 : "Family portrait time",
20 : "Eoin, Donal and Darragh, Argentierre, Chamonix Valley France, (07?",
21 : "Eoin, caught off guard at home in flat, serpentine avenue, dublin",
22 : "On Safari, new years 06/07, tanzania, with Dode.",
23 : "Overlooking gorge, tanzania (site of old human remains)",
24 : "Overlooking gorge, tanzania (site of old human remains)",
25 : "managing to avoid any serious panda eyes,",
26 : "With cousin billy (check where)",
27 : "Camping with digans, in the sleeve blooms (roughly when)",
28 : "with siblings (ask triona when/what occasion)",
29 : "top of petit aug verge, after climbing first, and last :( north face (in winter!)",
30 : "ski touring, argentierre glacier, chamonix",
31 : "athgoe road, doing some heavy landscaping",
32 : "Operating dangerous machinery, with trademark concentration tongue",
33 : "flying the baby kite, sandy mount strand",
34 : "the best man, on darraghs wedding morning.",
35 : "delivering the best best man speech ever",
36 : "At electric picnic, with Marcal and Billy",
37 : "Tucking into some of Mrs Johnstons Christmas Ham, xmas eve 2008",
38 : "Tucking into some of Mrs Johnstons Christmas Ham, xmas eve 2008",
39 : "Eoin and Harry? needing it up over xmas 09",
40 : "wrapped up warm beside the fire. 09",
41 : "Ow. Brian bit my finger.",
42 : "The Godfather, and Brian.",
43 : "Playing jenga, NYC.",
44 : "Billy, Jack, Eoin, Western style.",
45 : "Google earth, google office NYC.",
46 : "On a boat. Kite surfing course? I think?",
47 : "Beech in Donegal (ask eilis where and when/)",
}

def caption ( page ):
    page = int(page)
    if page in captions:
        return captions[page]
    return ""

def progress( page ):
    page = int(page)
    if page < 10:
        return "progress-1"
    elif page < 20:
        return "progress-2"
    elif page < 30:
        return "progress-3"
    elif page < 40:
        return "progress-4"
    elif page < 50:
        return "progress-5"
    return "XXXX" + page

register.filter(minus)
register.filter(caption)
register.filter(progress)