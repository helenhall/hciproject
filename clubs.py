all_clubs = {
    1: ['Maison', 'YVAC'], 
    2: ['Film thing (replace)', 'YVAC'], 
    3: ['YVAC', 'Design for America'], 
    4: ['YVAC', 'Yale Daily News', 'Record'], 
    5: ['Smart Women Securities', 'Yale Undergraduate Consulting Group'], 
    6: ['Yale Undergraduate Consulting Group'], 
    7: ['Yale Net Impact', 'Dwight Hall'], 
    8: ['Yale Entrepreneurial Society', 'Eli Ventures'], 
    9: ['Club Basketball', 'Club Volleyball', 'Club Ice Hockey', 'Club Soccer', 'Club Rugby'], 
    10: ['Club Rugby', 'Club Soccer', 'Yale Cycling Team', 'Yale Outdoors', 'Yale Climbing Club', 'Archery'], 
    11: ['Club Rugby', 'Club Ice Hockey'], 
    12: ['Club Ice Hockey', 'Club Figure Skating'], 
    13: ['Baker\'s Dozen', 'Doox', 'Magevet', 'Mixed Co', 'Out of the Blue', 'Pitches and Tones', 'Proof of the Pudding', 'Redhot & Blue', 'Shades', 'Something Extra', 'Spizzwinks', 'The New Blue', 'Society of Orpheus and Bacchus', 'Alley Cats', 'Whiffenpoofs', 'Yale Slavic Chorus'], 
    14: ['Yale Dancers', 'Rhythmic Blue', 'Rangeela', 'Bhangra', 'Ballet Folklorico'], 
    15: ['Danceworks', 'Ballet Folklorico', 'Ballroom Dance'], 
    16: ['Yale Dramatic Association', 'Oye!', 'Yale Children\'s Theater Project'], 
    17: ['Just Add Water', 'The Odd Ducks', 'The Purple Crayon', 'The Viola Question'], 
    18: ['Red Hot Poker', 'The Cucumber', 'Fifth Humor', 'The Record'], 
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
    29: ['Yale Daily News', 'The Yale Herald', "The Yale Politic","Yale Record"],
    30: ['Yale Daily News', 'Yale Historical Review', "Broad Recognition", "Yale Herald"],
    31: ['Rumpus Magazine', 'Yale Record'],
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
        "Yale Record",
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
        "Yale Net Impact"
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
        "Volleyball"
    ),
    15: Club(
        "Ice Hockey"
    ),
    16: Club(
        "Soccer"
    ),
    17: Club(
        "Rugby"
    ),
    18: Club(
        "Cycling Team"
    ),
    19: Club(
        "Outdoors"
    ),
    20: Club(
        "Climbing Club"
    ),
    21: Club(
        "Archery"
    ),
    22: Club(
        "Figure skating"
    ),
    23: Club(
        "Baker\'s Dozen"
    ),
    24: Club(
        "Doox"
    ),
    25: Club(
        "Magevet"
    ),
    26: Club(
        "Mixed Co"
    ),
    27: Club(
        "Out of the Blue"
    ),
    28: Club(
        "Pitches and Tones"
    ),
    29: Club(
        "Yale Dancers"
    ),
    30: Club(
        "Rhythmic Blue"
    ),
    31: Club(
        "Rangeela"
    ),
    32: Club(
        "Bhangra"
    ),
    33: Club(
        "Danceworks"
    ),
    34: Club(
        "Ballet Folklorico"
    ),
    35: Club(
        "Yale Dramatic Association"
    ),
    36: Club(
        "Oye!"
    ),
    37: Club(
        "Yale Children’s Theater Project"
    ),
    38: Club(
        "Just Add Water"
    ),
    39: Club(
        "The Odd Ducks"
    ),
    40: Club(
        "The Purple Crayon"
    ),
    41: Club(
        "Red Hot Poker"
    ),
    42: Club(
        "The Cucumber"
    ),
    43: Club(
        "Fifth Humor"
    ),
    44: Club(
        "Guild of Carillonneurs"
    ),
    45: Club(
        "Tangled Up in Blue"
    ),
    46: Club(
        "Viola Question"
    ),
    47: Club(
        "Yale Dramat"
    ),
    48: Club(
        "Women and Gender Minorities in CS"
    ),
    49: Club(
        "Yale Computer Society"
    ),
    50: Club(
        "YHack"
    ),
    51: Club(
        "Yale Scientific Magazine"
    ),
    52: Club(
        "Women in Physics"
    ),
    53: Club(
        "Yale Undergraduate Aerospace Association"
    ),
    54: Club(
        "Yale undergraduate science olympiad"
    ),
    55: Club(
        "National Society of Black Engineers"
    ),
    56: Club(
        "Bluddogs Racing Team"
    ),
    57: Club(
        "Engineers Without Borders"
    ),
    58: Club(
        "Medical Professions Outreach"
    ),
    59: Club(
        "Yale Data Science"
    ),
    60: Club(
        "Yale Political Union"
    ),
    61: Club(
        "William F. Buckley Jr. Program"
    ),
    62: Club(
        "Alexander Hamilton Society"
    ),
    63: Club(
        "Party of the Left"
    ),
    64: Club(
        "Conservative Party"
    ),
    65: Club(
        "Federalist Party"
    ),
    66: Club(
        "Liberal Party"
    ),
    67: Club(
        "Independent Party"
    ),
    68: Club(
        "Tory Party"
    ),
    69: Club(
        "Yale College Democrats"
    ),
    70: Club(
        "Yale Model UN"
    ),
    71: Club(
        "Model Congress Association"
    ),
    72: Club(
        "Yale Political Union"
    ),
    73: Club(
        "Yale College Council"
    ),
    74: Club(
        "William F. Buckley Jr. Program"
    ),
    75: Club(
        "The Yale Herald"
    ),
    76: Club(
        "The Yale Politic"
    ),
    77: Club(
        "Yale Historical Review"
    ),
    78: Club(
        "Broad Recognition"
    ),
    79: Club(
        "Rumpus Magazine"
    ),
    80: Club(
        "Accent Multilingual magazine"
    ),
    81: Club(
        "China Hands magazine"
    ),
    82: Club(
        "The Yale Globalist"
    ),
    83: Club(
        "Yale Global Health Review"
    )
}

