from random import randint

facts = [
    "Highest Innings total, 413–5 (50 overs) v Bermuda, India won by 257 runs, 12th Match, Group B, ICC Cricket World Cup at Port of Spain, Mar 19 2007",
    "2nd Highest Innings total, 373-6 (50 overs) v Sri Lanka, India won by 157 runs, 21st Match, ICC Cricket World Cup at Taunton, May 26 1999",
    "3rd Highest Innings total, 370–4 (50 overs) v Bangladesh, India won by 87 runs, 1st Match, Group B (D/N), ICC Cricket World Cup at Dhaka, Feb 19 2011",
    "4th Highest Innings total, 352–5 (50 overs) v Australia, India won by 36 runs, 14th match, ICC Cricket World Cup at The Oval, Jun 9 2019",
    "5th Highest Innings total, 338 (49.5 overs) v England, Match tied, 11th Match, Group B (D/N), ICC Cricket World Cup at Bengaluru, Feb 27 2011",
    "Lowest Completed Innings, 125(41.4 overs)	v Australia, Australia won by 9 wickets, 11th Match, ICC World Cup at Centurion, Feb 15 2003",
    "2nd Lowest Completed Innings, 158 (37.5 overs)	v Australia, Australia won by 162 runs, 11th Match, ICC Cricket World Cup at Nottingham, Jun 13 1983",
    "3rd Lowest Completed Innings, 182 (55.5 overs)	v New Zealand, New Zealand won by 8 wickets, 6th Match, ICC Cricket World Cup at Leeds, Jun 13 1979",
    "4th Lowest Completed Innings, 183 (54.4 overs)	v West Indies,  India won by 43 runs, Final, ICC Cricket World Cup at Lord's, Jun 25 1983",
    "5th Lowest Completed Innings, 185 (43.3 overs)	v Sri Lanka, Sri Lanka won by 69 runs, 20th Match, Group B, ICC World Cup at Port of Spain, Mar 23 2007",
    "Best Bowling Innings Figures, 6–23 (10 overs) Ashish Nehra v England, India won by 82 runs, 30th Match (D/N), ICC World Cup at Durban, Feb 26 2003",
    "2nd Best Bowling Innings Figures, 5–27 (9.3 overs) Venkatesh Prasad v Pakistan, India won by 47 runs, 4th Super, ICC World Cup at Manchester, Jun 8 1999",
    "3rd Best Bowling Innings Figures, 5–31 (9.3 overs) Robin Singh	v Sri Lanka, India won by 157 runs, 21st Match, ICC World Cup at Taunton, May 26 1999",
    "4th Best Bowling Innings Figures, 5–31 (10 overs) Yuvraj Singh v Ireland, India won by 5 wickets, 22nd Match, Group B (D/N), ICC Cricket World Cup at Bengaluru, Mar 6 2011",
    "5th Best Bowling Innings Figures, 5–43 (12 overs) Kapil Dev v Australia, Australia won by 162 runs, 11th Match, ICC Cricket World Cup at Nottingham, Jun 13 1983",
    "In ICC Cricket World Cup Year 1975, at England, India's last position was - Group stage, Games Played 3, Won 1, No result 0, Lost 2, with Captain S Venkataraghavan",
    "In ICC Cricket World Cup Year 1979, at England, India's last position was - Group stage, Games Played 3, Won 0, No result 0, Lost 3, with Captain S Venkataraghavan",
    "In ICC Cricket World Cup Year 1983, at England, India's last position was - Champions, Games Played 8, Won 6, No result 0, Lost 2, with Captain Kapil Dev",
    "In ICC Cricket World Cup Year 1987, at India Pakistan, India's last position was - Semi-finals, Games Played 7, Won 5, No result 0, Lost 2, with Captain Kapil Dev",
    "In ICC Cricket World Cup Year 1992, at Australia New Zealand, India's last position was - India's last position was at Round-robin, Games Played 8, Won 2, No result 1, Lost 5, with Captain M Azharuddin",
    "In ICC Cricket World Cup Year 1996, at India Pakistan Sri Lanka, India's last position was - Semi-finals, Games Played 7, Won 4, No result 0, Lost 3, with Captain M Azharuddin",
    "In ICC Cricket World Cup Year 1999, at England Scotland Ireland Netherlands, India's last position was - Super Six, Games Played 8, Won 4, No result 0, Lost 4, with Captain M Azharuddin",
    "In ICC Cricket World Cup Year 2003, at South Africa Zimbabwe Kenya, India's last position was - Runners-up,	Games Played 11, Won 9, No result 0, Lost 2, with Captain Sourav Ganguly",
    "In ICC Cricket World Cup Year 2007, at West Indies Cricket Board, India's last position was - Group stage, Games Played 3, Won 1, No result 0, Lost 2, with Captain Rahul Dravid",
    "In ICC Cricket World Cup Year 2011, at India Bangladesh Sri Lanka, India's last position was - Champions, Games Played 9, Won 7, No result 1, Lost 1, with Captain MS Dhoni",
    "In ICC Cricket World Cup Year 2015, at Australia New Zealand, India's last position was - Semi-finals, Games Played 8, Won 7, No result 0, Lost 1, with Captain MS Dhoni",
    "In ICC Cricket World Cup Year 2019, at England Wales, India's last position was - Semi-finals, Games Played 10, Won 7, No result 1, Lost 2, with Captain Virat Kohli",
    "India's Record in ICC Cricket World Cup, Wins: 2, Total Games Played: 85, Won: 53, No Result: 3, Lost: 29",
    "In ICC Cricket World Cup, India's record against Australia: Match Played 12, Won 4, Lost 8, Tied 0, No Result 0, Win % 33.33, First Match Played on 13 June 1983",
    "In ICC Cricket World Cup, India's record against Afghanistan: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 22 June 2019",
    "In ICC Cricket World Cup, India's record against Bangladesh: Match Played 4, Won 3, Lost 1, Tied	0, No Result 0, Win % 75.00, First Match Played on 17 March 2007",
    "In ICC Cricket World Cup, India's record against Bermuda: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 19  March 2007",
    "In ICC Cricket World Cup, India's record against East Africa: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 11 June 1975",
    "In ICC Cricket World Cup, India's record against England: Match Played 8, Won 3, Lost 4, Tied	1, No Result 0, Win % 37.5, First Match Played on 7 June 1975",
    "In ICC Cricket World Cup, India's record against Ireland: Match Played 2, Won 2, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 6   March 2011",
    "In ICC Cricket World Cup, India's record against Kenya: Match Played 4, Won 4, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 18 February 1996",
    "In ICC Cricket World Cup, India's record against Namibia: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 23 February 2003",
    "In ICC Cricket World Cup, India's record against Netherlands: Match Played 2, Won 2, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 12 February 2003",
    "In ICC Cricket World Cup, India's record against New Zealand: Match Played 8, Won 3, Lost 5, Tied	0, No Result 0, Win % 37.5, First Match Played on 4 June 1975",
    "In ICC Cricket World Cup, India's record against Pakistan: Match Played 7, Won 7, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 4 March 1992",
    "In ICC Cricket World Cup, India's record against South Africa: Match Played 5, Won 2, Lost 3, Tied	0, No Result 0, Win % 40, First Match Played on 15 March 1992",
    "In ICC Cricket World Cup, India's record against Sri Lanka: Match Played 9, Won 4, Lost 4, Tied	0, No Result 1, Win % 44.44, First Match Played on 18 June 1979",
    "In ICC Cricket World Cup, India's record against United Arab Emirates: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100, First Match Played on 28 February 2015",
    "In ICC Cricket World Cup, India's record against West Indies: Match Played 9, Won 6, Lost 3, Tied	0, No Result 0, Win % 66.66, First Match Played on 9 June 1979",
    "In ICC Cricket World Cup, India's record against Zimbabwe: Match Played 9, Won 8, Lost 1, Tied	0, No Result 0, Win % 88.89, First Match Played on 11 June 1983",
    "Highest partnerships in ICC Cricket World Cup, Total Runs 318 (2nd wicket), Sourav Ganguly (183) & Rahul Dravid (145) Against Sri Lanka	at Taunton in 1999",
    "2nd Highest partnerships in ICC Cricket World Cup, Total Runs 244 (2nd wicket), Sachin Tendulkar (152) & Sourav Ganguly (111) Against Namibia at Pietermaritzburg in 2003",
    "3rd Highest partnerships in ICC Cricket World Cup, Total Runs 237* (3rd wicket), Rahul Dravid (104*) & Sachin Tendulkar (140*) Against Kenya at Bristol in 1999",
    "4th Highest partnerships in ICC Cricket World Cup, Total Runs 203 (3rd wicket), Virender Sehwag (175) & Virat Kohli (100) Against Bangladesh at Dhaka in 2011",
    "5th Highest partnerships in ICC Cricket World Cup, Total Runs 202 (2nd wicket), Sourav Ganguly (89) & Virender Sehwag (114) Against Bermuda at Port of Spain in 2007",
    "Highest partnership for 1st wicket in ICC Cricket World Cup, 189 by, Rohit Sharma (103) & K. L. Rahul (111) Against Sri Lanka at Leeds in year 2019",
    "Highest partnership for 2nd wicket in ICC Cricket World Cup, 318 by, Sourav Ganguly (183) & Rahul Dravid (145) Against Sri Lanka at Taunton	in year 1999",
    "Highest partnership for 3rd wicket in ICC Cricket World Cup, 237* by, Rahul Dravid (104*) & Sachin Tendulkar (140*) Against Kenya at Bristol in year 1999",
    "Highest partnership for 4th wicket in ICC Cricket World Cup, 142 by, Navjot Singh Sidhu (80) & Vinod Kambli (106) Against Zimbabwe at Kanpur in year 1996",
    "Highest partnership for 5th wicket in ICC Cricket World Cup, 196* by, Suresh Raina (110*) & Mahendra Singh Dhoni (85*) Against Zimbabwe at Auckland	in year 2015",
    "Highest partnership for 6th wicket in ICC Cricket World Cup, 74* by, Suresh Raina (34*) & Yuvraj Singh (57*) Against Australia at Ahmedabad	in year 2011",
    "Highest partnership for 7th wicket in ICC Cricket World Cup, 116 by, Ravindra Jadeja (77) & Mahendra Singh Dhoni (50) Against New Zealand at Manchester	in year 2019",
    "Highest partnership for 8th wicket in ICC Cricket World Cup, 82* by, Kapil Dev (72*) & Kiran More (42*) Against New Zealand	at Bangalore in year 1987",
    "Highest partnership for 9th wicket in ICC Cricket World Cup, 126* by, Kapil Dev (175*) & Syed Kirmani (24*) Against Zimbabwe at Tunbridge Wells	in year 1983",
    "Highest partnership for 10th wicketh in ICC Cricket World Cup, 32 by, Zaheer Khan (15) & Munaf Patel (15) Against Bangladesh	at Port of Spain in year 2007",
    "South Africa played ICC Cricket World Cup for the first time in 1992, Record Win % 61.9",
    "In ICC Cricket World Cup, Australia's record from 1975 to 2019, total games 94, Won 69, Lost 23, Tied 1, No Result 1, Win % 74.73  is Best of all.",
    "In ICC Cricket World CUp, 2nd best win margin by highest runs is 257 runs, India (413–5) beat Bermuda (156) at Queen's Park Oval, Port of Spain, Trinidad on 19 March 2007",
    "In ICC Cricket World CUp, best win margin by highest runs is 275 runs, Australia (417–6) beat Afghanistan (142) at WACA, Perth on 4 March 2015",
    "In ICC Cricket World CUp, best win margin by lower runs is Boundary Count, England (241) Super Over (15-0) beat New Zealand (241-8) Super Over(15-1) won on boundary count (26-17) at Lord's Cricket Ground, London 14 July 2019"
    "In ICC Cricket World CUp, best win margin by lower runs is 1 run when Australia (270–6) beat India (269) at M. A. Chidambaram Stadium, Chennai on 9 October 1987",
    "In ICC Cricket World CUp, best win margin by lower runs is 1 run when Australia (237–9) beat India (234) [Target 236 (D/L Method)]	at The Gabba, Brisbane on 1 March 1992"
]



# if __name__ == "__main__":
#     length = len(facts)
#     print(f'length -> {length}')

#     random_number = randint(0,length-1)
#     print(f'random -> {random_number}')
#     print(f'Fact -> {facts[random_number]}')

