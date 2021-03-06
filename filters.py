from google.appengine.ext import webapp

register = webapp.template.create_template_register()

def minus( value, arg ):
    value = int( value )
    arg = int( arg )
    if arg: return value - arg

captions = {
1 : "Eoin, 1 day old with proud Mum and Dad, 25th March 1980",
2 : "Eoin's christening with his doting grandfathers Frank Curran and Maurice Sheehy, Summer 1980",
3 : "Smiling at his Mum, 5 months old",
4 : "Chilling at home...watching TV perhaps",
5 : "First Steps in Bushy Park, circa May 1981",
6 : "With Baby Darragh, February 1982",
7 : "First driving with Mum, Green Saab, 1981",
8 : "Christmas checkup for Mum, 3 years old",
9 : "Trip to the zoo with Darragh and Triona, 1985",
10 : "Summer family holiday with the griffins, Coomenoole beach, Kerry 1987",
11 : "Holidaying in Inchydoney with the Sheehys and Granny, 1988",
12 : "With Mum and Dad, 1989",
13 : "Fota wildlife Park on summer holidays to Cork, 1989",
14 : "In St Pats, Drmcondra, after some competitive Logo programming",
15 : "Resting up, aged 12",
16 : "Trophy awarded for scoring perfect 800 in SAT Maths, aged 15",
17 : "With Naoise Gaffney in a hot spring on Green Tortoise tour across the US 2001",
18 : "Apr&egrave;s-ski with Darragh in the Micro Brasserie de Chamonix, 2007",
19 : "Family portrait time!",
20 : "Donal, Darragh and Eoin, Argentierre, Chamonix Valley, March 2007",
21 : "Caught off guard at home in Serpentine Avenue, Dublin",
22 : "On Safari in Tanzania, New Years 06/07 with Dode",
23 : "Overlooking Olduvai Gorge in Tanzania - lots of really really old humanoid remains",
24 : "Overlooking Olduvai Gorge in Tanzania - lots of really really old humanoid remains",
25 : "Managing to avoid any serious panda eyes",
26 : "With cousin Billy in a pub in Clifden",
27 : "Camping with digans, in the sleeve blooms, 2008",
28 : "Farewell drinks for Triona and Liam before their trip to oz, June 2008",
29 : "Top of the Petite Aiguille Verte. Eoin's first winter north face",
30 : "Ski touring, Argenti&egrave;re Glacier, Chamonix",
31 : "Heavy landscaping in Athgoe road with Dad and Darragh, summer 2009",
32 : "Operating dangerous machinery, with trademark concentration tongue",
33 : "Flying the baby kite, sandy mount strand",
34 : "The best man, on Darragh's wedding morning",
35 : "Delivering the best best man speech ever",
36 : "At electric picnic, with Mar&ccedil;al and Billy, September 2009",
37 : "Tucking into some of Ms Johnston's Christmas Ham, Xmas eve 2008",
38 : "Tucking into some of Ms Johnston's Christmas Ham, Xmas eve 2008",
39 : "Eoin and Harry nerding it up over Xmas 2009",
40 : "Wrapped up warm beside the fire in Mums chair, Christmas 2009",
41 : "Ow. Brian bit my finger",
42 : "With his treasured godson Brian",
43 : "Playing Jenga, NYC, Summer 2010",
44 : "Eoin, Jack and Billy - western style. the boardwalk, Ocean city, Maryland",
45 : "Google Earth Holodeck, Google office NYC",
46 : "",
47 : "Machaire Rabhartaigh, Donegal, 1st Janruary 2009",
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