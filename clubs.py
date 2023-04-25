all_clubs = {
    1: ['Maison', 'YVAC'], 
    2: ['Yale Film Society', 'YVAC'], 
    3: ['YVAC', 'Design for America'], 
    4: ['YVAC', 'Yale Daily News', 'The Yale Record'], 
    5: ['Yale Undergraduate Consulting Group'], 
    6: ['Yale Undergraduate Consulting Group'], 
    7: ['Yale Net Impact', 'Dwight Hall'], 
    8: ['Yale Entrepreneurial Society', 'Eli Ventures'], 
    9: ["Yale Club Men's Basketball Team", "Yale Club Women's Basketball Team", 'Volleyball', 'Ice Hockey', 'Soccer', 'Rugby'], 
    10: ['Rugby', 'Soccer', 'Cycling Team', 'Outdoors', 'Climbing Club', 'Archery'], 
    11: ['Rugby', 'Ice Hockey'], 
    12: ['Ice Hockey', 'Figure skating'], 
    13: ["Baker's Dozen", 'Doox', 'Magevet', 'Mixed Co', 'Out of the Blue', 'Pitches and Tones'], 
    14: ['Yale Dancers', 'Rhythmic Blue', 'Rangeela', 'Bhangra', 'Ballet Folklorico'], 
    15: ['Danceworks', 'Ballet Folklorico'], 
    16: ['Yale Dramatic Association', 'Oye!', "Yale Children's Theater Project"], 
    17: ['Just Add Water', 'The Odd Ducks', 'The Purple Crayon'], 
    18: ['Red Hot Poker', 'The Cucumber', 'Fifth Humor', 'The Yale Record'], 
    19: ['Just Add Water', 'Guild of Carillonneurs', 'Tangled Up in Blue'], 
    20: ['Red Hot Poker', 'Viola Question', 'Yale Dramat'], 
    21: ['Women and Gender Minorities in CS', 'Yale Computer Society', 'YHack', 'Yale Scientific Magazine', 'National Society of Black Engineers'], 
    22: ['Women in Physics', 'Yale Scientific Magazine', 'Yale Undergraduate Aerospace Association', 'Yale Undergraduate Science Olympiad', 'National Society of Black Engineers'], 
    23: ['Bluddogs Racing Team', 'Engineers Without Borders', 'Design for America', 'YHack'], 
    24: ['Medical Professions Outreach', 'Yale Data Science', 'Yale Undergraduate Science Olympiad'], 
    25: ['Yale Political Union', 'William F. Buckley Jr. Program', 'Alexander Hamilton Society'], 
    26: ['Party of the Left', 'Conservative Party', 'Federalist Party', 'Liberal Party', 'Independent Party', 'Tory Party', 'Yale College Democrats', 'Yale College Republicans', 'Yale Political Union'], 
    27: ['Yale Model UN', 'Model Congress Association', 'Yale Political Union', 'Yale College Council'], 
    28: ['Yale Political Union', 'Yale College Council', 'William F. Buckley Jr. Program'],
    29: ['Yale Daily News', 'The Yale Herald', "The Yale Politic","The Yale Record"],
    30: ['Yale Daily News', 'Yale Historical Review', "Broad Recognition", "The Yale Herald"],
    31: ['Rumpus Magazine', 'The Yale Record'],
    32: ['Accent Multilingual magazine', 'Broad Recognition', "China Hands magazine", "The Yale Globalist","Yale Global Health Review"]
}



def get_unique_strings_from_dict(dictionary):
    unique_strings = set()
    for values in dictionary.values():
        for value in values:
            unique_strings.add(value)
    return list(unique_strings)

unique_clubs = get_unique_strings_from_dict(all_clubs)










class Club:
    def __init__(self, name: str, url: str = None) -> None:
        self.name = name
        self.url = url
    def get_name(self):
        return self.name

# clubs = {
#     "Maison": "https://yaleconnect.yale.edu/mby/home/",
#     "YVAC": "https://yaleconnect.yale.edu/YVAC/web_officers",
    
# }

clubs = {
    1: Club(
        "Maison",
        "https://yaleconnect.yale.edu/mby/home/"
    ),
    2: Club(
        "YVAC",
        "https://yaleconnect.yale.edu/YVAC/web_officers"
    ),
    3: Club(
        "Design for America",
        "https://yaleconnect.yale.edu/feeds?type=club&type_id=34533&tab=home"
    ),
    4: Club(
        "Yale Daily News",
        "https://yaledailynews.com/join"
    ),
    5: Club(
        "Record",
        "http://yalerecord.org/"
    ),
    6: Club(
        "Yale Smart Woman Securities",
        "https://www.linkedin.com/company/smart-woman-securities/"
    ),
    7: Club(
        "Yale Undergraduate Consulting Group",
        "https://www.yaleconsulting.org/"
    ),
    8: Club(
        "Yale Net Impact",
        "http://www.yalenetimpact.com/"
    ),
    9: Club(
        "Dwight Hall",
        "https://dwighthall.org/"
    ),
    10: Club(
        "Yale Entrepreneurial society",
        "https://www.yesatyale.org"
    ),
    11: Club(
        "Eli Ventures",
        "https://admissions.yale.edu/eli-ventures"
    ),
    12: Club(
        "Yale Club Men's Basketball Team",
        "https://yaleconnect.yale.edu/YCMBASKETBALL/web_officers"
    ),
    13: Club(
        "Yale Club Women's Basketball Team",
        "https://yaleconnect.yale.edu/feeds?type=club&type_id=46684&tab=home"
    ),
    14: Club(
        "Volleyball",
        "https://yaleconnect.yale.edu/YCMVOLLEYBALL/"
    ),
    15: Club(
        "Ice Hockey",
        "https://yaleconnect.yale.edu/YCMICEHOCKEY/https://yaleconnect.yale.edu/YCMICEHOCKEY/"
    ),
    16: Club(
        "Soccer",
        "https://yaleconnect.yale.edu/YCWSOCCERC1"
    ),
    17: Club(
        "Rugby",
        "https://yaleconnect.yale.edu/YCMRUGBY/"
    ),
    18: Club(
        "Cycling Team",
        "http://yalecycling.squarespace.com/landing"
    ),
    19: Club(
        "Outdoors",
        "https://yaleconnect.yale.edu/OREC/"
    ),
    20: Club(
        "Climbing Club",
        "https://yaleconnect.yale.edu/YCOCAY/"
    ),
    21: Club(
        "Archery",
        "https://yaleconnect.yale.edu/YCARCHERY/"
    ),
    22: Club(
        "Figure skating",
        "https://yaleconnect.yale.edu/YCFIGURESKATING/"
    ),
    23: Club(
        "Baker's Dozen",
        "http://www.bakersdozenyale.com/" 
    ),
    24: Club(
        "Doox",
        "https://dooxofyale.com/"
    ),
    25: Club(
        "Magevet",
        "http://magevet.weebly.com/"
    ),
    26: Club(
        "Mixed Co",
        "http://www.mixedcompanyofyale.com/"
    ),
    27: Club(
        "Out of the Blue",
        "https://yaleootb.com/"
    ),
    28: Club(
        "Pitches and Tones",
        "https://www.instagram.com/yalepitchesandtones/?hl=en"
    ),
    29: Club(
        "Yale Dancers",
        "https://collegearts.yale.edu/organizations/alliance-dance-yale/dance-groups/yaledancers-yd"
    ),
    30: Club(
        "Rhythmic Blue",
        "https://campuspress.yale.edu/rhythmicblue/"
    ),
    31: Club(
        "Rangeela",
        "https://collegearts.yale.edu/organizations/alliance-dance-yale/dance-groups/rangeela"
    ),
    32: Club(
        "Bhangra",
        "https://collegearts.yale.edu/organizations/alliance-dance-yale/dance-groups/yale-jashan-bhangra-yjb"
    ),
    33: Club(
        "Danceworks",
        "https://campuspress.yale.edu/danceworks"
    ),
    34: Club(
        "Ballet Folklorico",
        "https://bfmdey.sites.yale.edu/"
    ),
    35: Club(
        "Yale Dramatic Association",
        "https://yaledramat.org/"
    ),
    36: Club(
        "Oye!",
        "https://www.facebook.com/oyespokenword/"
    ),
    37: Club(
        "Yale Children's Theater Project",
        "https://collegearts.yale.edu/organizations/yale-drama-coalition/performance-groups/yale-childrens-theater-project"
    ),
    38: Club(
        "Just Add Water",
        "http://www.justaddwateryale.com/"
    ),
    39: Club(
        "The Odd Ducks",
        "https://www.facebook.com/profile.php?id=100063867860214"
    ),
    40: Club(
        "The Purple Crayon",
        "https://www.facebook.com/YaleCrayon/"
    ),
    41: Club(
        "Red Hot Poker",
        "https://www.rhpcomedy.com/"
    ),
    42: Club(
        "The Cucumber",
        "https://www.facebook.com/events/the-cucumber-yales-only-open-mic-stand-up-comedy-night/562051107200458/?paipv=0&eav=AfaGR54FukZ_4fQckYfg45T3Q_MAb_anrE_3p7s39bQtVoEnqzCFCNzNhrfYZUZ1-VY&_rdr"
    ),
    43: Club(
        "Fifth Humor",
        "https://www.instagram.com/thefifthhumour/?hl=en" 
    ),
    44: Club(
        "Guild of Carillonneurs",
        "http://yalecarillon.org/"
    ),
    45: Club(
        "Tangled Up in Blue",
        "https://www.yaletuib.com/"
    ),
    46: Club(
        "Viola Question",
        "http://public.violaquestion.com/"
    ),
    47: Club(
        "Yale Dramat",
        "https://yaledramat.org/"
    ),
    48: Club(
        "Women and Gender Minorities in CS",
        "http://yalewics.com/"
    ),
    49: Club(
        "Yale Computer Society"
        "http://yalecompsociety.org/"
    ),
    50: Club(
        "YHack",
        "https://www.instagram.com/whyhackatyhack/?hl=en"
    ),
    51: Club(
        "Yale Scientific Magazine",
        "https://www.yalescientific.org/"
    ),
    52: Club(
        "Women in Physics",
        "https://physics.yale.edu/women-physics-and-women-physics"
    ),
    53: Club(
        "Yale Undergraduate Aerospace Association",
        "https://yaleaerospace.org/"
    ),
    54: Club(
        "Yale undergraduate science olympiad",
        "https://yuso.yale.edu/"
    ),
    55: Club(
        "National Society of Black Engineers",
        "https://yaleconnect.yale.edu/ycnsbe/home"
    ),
    56: Club(
        "Bluddogs Racing Team",
        "http://bulldogsracing.com/"
    ),
    57: Club(
        "Engineers Without Borders",
        "https://ewb.sites.yale.edu/"
    ),
    58: Club(
        "Medical Professions Outreach",
        "https://yalemedprofoutreach.wixsite.com/home"
    ),
    59: Club(
        "Yale Data Science",
        "https://statistics.yale.edu/"
    ),
    60: Club(
        "Yale Political Union",
        "https://ypu.sites.yale.edu/"
    ),
    61: Club(
        "William F. Buckley Jr. Program",
        "https://buckleyinstitute.com/"
    ),
    62: Club(
        "Alexander Hamilton Society",
        "https://buckleyinstitute.com/"
    ),
    63: Club(
        "Party of the Left",
        "https://partyoftheleft.sites.yale.edu/"
    ),
    64: Club(
        "Conservative Party",
        "https://yaleconservativeparty.squarespace.com/"
    ),
    65: Club(
        "Federalist Party",
        "https://sites.google.com/view/yalefederalistparty/home"
    ),
    66: Club(
        "Liberal Party",
        "https://libs.sites.yale.edu/"
    ),
    67: Club(
        "Independent Party",
        "https://independentparty.sites.yale.edu"
    ),
    68: Club(
        "Tory Party",
        "https://yaletoryparty.com/"
    ),
    69: Club(
        "Yale College Democrats",
        "https://www.yaledemocrats.com/"
    ),
    70: Club(
        "Yale Model UN",
        "https://ymun.org/"
    ),
    71: Club(
        "Model Congress Association",
        "http://www.yalemodelcongress.org/"
    ),
    72: Club(
        "Yale Political Union",
        "https://ypu.sites.yale.edu/"
    ),
    73: Club(
        "Yale College Council",
        "https://www.ycc.yale.edu"
    ),
    74: Club(
        "William F. Buckley Jr. Program",
        "https://buckleyinstitute.com/"
    ),
    75: Club(
        "The Yale Herald",
        "https://yale-herald.com/"
    ),
    76: Club(
        "The Yale Politic",
        "https://thepolitic.org/"
    ),
    77: Club(
        "Yale Historical Review",
        "https://yalehistoricalreview.ghost.io/"
    ),
    78: Club(
        "Broad Recognition",
        "http://www.broadsatyale.com/"
    ),
    79: Club(
        "Rumpus Magazine",
        "http://yalerumpus.net/"
    ),
    80: Club(
        "Accent Multilingual magazine",
        "https://www.accentmultilingualmagazine.com/"
    ),
    81: Club(
        "China Hands magazine",
        "https://chinahandsmagazine.org/"
    ),
    82: Club(
        "The Yale Globalist",
        "https://globalist.yale.edu/"
    ),
    83: Club(
        "Yale Global Health Review",
        "https://yaleglobalhealthreview.com/"
    ),
    84: Club(
        "The Yale Record",
        "http://yalerecord.org/"
    ), 
    85: Club(
        'Club Ice Hockey',
        'https://yaleclubhockey.sites.yale.edu/'
    ), 
    86: Club(
        'Club Rugby', 
        'https://www.yalerugby.com/'
    ), 
    87: Club(
        'Yale Film Society', 
        'https://linktr.ee/yalefilm'
    ), 
    88: Club(
        'Yale College Republicans', 
        'https://www.facebook.com/yalegop/'
    )
}


