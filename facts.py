from random import randint

facts = [
    "1st Highest Innings total, 413–5 (50 overs) v Bermuda, India won by 257 runs, 12th Match, Group B, ICC Cricket World Cup at Port of Spain, Mar 19 2007",
    "2nd Highest Innings total, 373-6 (50 overs) v Sri Lanka, India won by 157 runs, 21st Match, ICC Cricket World Cup at Taunton, May 26 1999",
    "3rd Highest Innings total, 370–4 (50 overs) v Bangladesh, India won by 87 runs, 1st Match, Group B (D/N), ICC Cricket World Cup at Dhaka, Feb 19 2011",
    "4th Highest Innings total, 352–5 (50 overs) v Australia, India won by 36 runs, 14th match, ICC Cricket World Cup at The Oval, Jun 9 2019",
    "5th Highest Innings total, 338 (49.5 overs) v England, Match tied, 11th Match, Group B (D/N), ICC Cricket World Cup at Bengaluru, Feb 27 2011",
    "1st Lowest Completed Innings, 125(41.4 overs)	v Australia, Australia won by 9 wickets, 11th Match, ICC World Cup at Centurion, Feb 15 2003",
    "2nd Lowest Completed Innings, 158 (37.5 overs)	v Australia, Australia won by 162 runs, 11th Match, ICC Cricket World Cup at Nottingham, Jun 13 1983",
    "3rd Lowest Completed Innings, 182 (55.5 overs)	v New Zealand, New Zealand won by 8 wickets, 6th Match, ICC Cricket World Cup at Leeds, Jun 13 1979",
    "4th Lowest Completed Innings, 183 (54.4 overs)	v West Indies,  India won by 43 runs, Final, ICC Cricket World Cup at Lord's, Jun 25 1983",
    "5th Lowest Completed Innings, 185 (43.3 overs)	v Sri Lanka, Sri Lanka won by 69 runs, 20th Match, Group B, ICC World Cup at Port of Spain, Mar 23 2007",
    "1st Best Bowling Innings Figures, 6–23 (10 overs)	Ashish Nehra v England, India won by 82 runs, 30th Match (D/N), ICC World Cup at Durban, Feb 26 2003",
    "2nd Best Bowling Innings Figures, 5–27 (9.3 overs)	Venkatesh Prasad v Pakistan, India won by 47 runs, 4th Super, ICC World Cup at Manchester, Jun 8 1999",
    "3rd Best Bowling Innings Figures, 5–31 (9.3 overs)	Robin Singh	v Sri Lanka, India won by 157 runs, 21st Match, ICC World Cup at Taunton, May 26 1999",
    "4th Best Bowling Innings Figures, 5–31 (10 overs)	Yuvraj Singh v Ireland, India won by 5 wickets, 22nd Match, Group B (D/N), ICC Cricket World Cup at Bengaluru, Mar 6 2011",
    "5th Best Bowling Innings Figures, 5–43 (12 overs)	Kapil Dev v Australia, Australia won by 162 runs, 11th Match, ICC Cricket World Cup at Nottingham, Jun 13 1983",
    "ICC Cricket World Cup Year 1975, at England, India's last position was at Round - Group stage, Games Played 3, Won 1, No result 0, Lost 2, with Captain S Venkataraghavan",
    "ICC Cricket World Cup Year 1979, at England, India's last position was at Round - Group stage, Games Played 3, Won 0, No result 0, Lost 3, with Captain S Venkataraghavan",
    "ICC Cricket World Cup Year 1983, at England, India's last position was at Round - Champions, Games Played 8, Won 6, No result 0, Lost 2, with Captain Kapil Dev",
    "ICC Cricket World Cup Year 1987, at India Pakistan, India's last position was at Round - Semi-finals, Games Played 7, Won 5, No result 0, Lost 2, with Captain Kapil Dev",
    "ICC Cricket World Cup Year 1992, at Australia New Zealand, India's last position was at Round - India's last position was at Round-robin, Games Played 8, Won 2, No result 1, Lost 5, with Captain M Azharuddin",
    "ICC Cricket World Cup Year 1996, at India Pakistan Sri Lanka, India's last position was at Round - Semi-finals, Games Played 7, Won 4, No result 0, Lost 3, with Captain M Azharuddin",
    "ICC Cricket World Cup Year 1999, at England Scotland Ireland Netherlands, India's last position was at Round - Super Six, Games Played 8, Won 4, No result 0, Lost 4, with Captain M Azharuddin",
    "ICC Cricket World Cup Year 2003, at South Africa Zimbabwe Kenya, India's last position was at Round - Runners-up,	Games Played 11, Won 9, No result 0, Lost 2, with Captain Sourav Ganguly",
    "ICC Cricket World Cup Year 2007, at West Indies Cricket Board, India's last position was at Round - Group stage, Games Played 3, Won 1, No result 0, Lost 2, with Captain Rahul Dravid",
    "ICC Cricket World Cup Year 2011, at India Bangladesh Sri Lanka, India's last position was at Round - Champions, Games Played 9, Won 7, No result 1, Lost 1, with Captain MS Dhoni",
    "ICC Cricket World Cup Year 2015, at Australia New Zealand, India's last position was at Round - Semi-finals, Games Played 8, Won 7, No result 0, Lost 1, with Captain MS Dhoni",
    "ICC Cricket World Cup Year 2019, at England Wales, India's last position was at Round - Semi-finals, Games Played 10, Won 7, No result 1, Lost 2, with Captain Virat Kohli",
    "ICC Cricket World Cup Wins: 2, Total Games Played: 85, Won: 53, No Result: 3, Lost: 29",
    "ICC Cricket World Cup, India's record against Australia: Match Played 12, Won 4, Lost 8, Tied 0, No Result 0, Win % 33.33 First Played on13 June 1983",
    "ICC Cricket World Cup, India's record against Afghanistan: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 22 June 2019",
    "ICC Cricket World Cup, India's record against Bangladesh: Match Played 4, Won 3, Lost 1, Tied	0, No Result 0, Win % 75.00 First Played on 17 March 2007",
    "ICC Cricket World Cup, India's record against Bermuda: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 19  March 2007",
    "ICC Cricket World Cup, India's record against East Africa: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 11 June 1975",
    "ICC Cricket World Cup, India's record against England: Match Played 8, Won 3, Lost 4, Tied	1, No Result 0, Win % 37.5 First Played on 7 June 1975",
    "ICC Cricket World Cup, India's record against Ireland: Match Played 2, Won 2, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 6   March 2011",
    "ICC Cricket World Cup, India's record against Kenya: Match Played 4, Won 4, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 18 February 1996",
    "ICC Cricket World Cup, India's record against Namibia: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 23 February 2003",
    "ICC Cricket World Cup, India's record against Netherlands: Match Played 2, Won 2, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 12 February 2003",
    "ICC Cricket World Cup, India's record against New Zealand: Match Played 8, Won 3, Lost 5, Tied	0, No Result 0, Win % 37.5 First Played on 4 June 1975",
    "ICC Cricket World Cup, India's record against Pakistan: Match Played 7, Won 7, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 4 March 1992",
    "ICC Cricket World Cup, India's record against South Africa: Match Played 5, Won 2, Lost 3, Tied	0, No Result 0, Win % 40 First Played on 15 March 1992",
    "ICC Cricket World Cup, India's record against Sri Lanka: Match Played 9, Won 4, Lost 4, Tied	0, No Result 1, Win % 44.44 First Played on 18 June 1979",
    "ICC Cricket World Cup, India's record against United Arab Emirates: Match Played 1, Won 1, Lost 0, Tied	0, No Result 0, Win % 100 First Played on 28 February 2015",
    "ICC Cricket World Cup, India's record against West Indies: Match Played 9, Won 6, Lost 3, Tied	0, No Result 0, Win % 66.66 First Played on 9 June 1979",
    "ICC Cricket World Cup, India's record against Zimbabwe: Match Played 9, Won 8, Lost 1, Tied	0, No Result 0, Win % 88.89 First Played on 11 June 1983",
    "1st Highest partnerships in ICC Cricket World Cup, Total Runs 318 (2nd wicket), Sourav Ganguly (183) & Rahul Dravid (145) Against Sri Lanka	at Taunton in 1999",
    "2nd Highest partnerships in ICC Cricket World Cup, Total Runs 244 (2nd wicket), Sachin Tendulkar (152) & Sourav Ganguly (111) Against Namibia at Pietermaritzburg in 2003",
    "3rd Highest partnerships in ICC Cricket World Cup, Total Runs 237* (3rd wicket), Rahul Dravid (104*) & Sachin Tendulkar (140*) Against Kenya at Bristol in 1999",
    "4th Highest partnerships in ICC Cricket World Cup, Total Runs 203 (3rd wicket), Virender Sehwag (175) & Virat Kohli (100) Against Bangladesh at Dhaka in 2011",
    "5th Highest partnerships in ICC Cricket World Cup, Total Runs 202 (2nd wicket), Sourav Ganguly (89) & Virender Sehwag (114) Against Bermuda at Port of Spain in 2007"
]


if __name__ == "__main__":
    length = len(facts)
    print(f'length -> {length}')

    random_number = randint(0,length-1)
    print(f'random -> {random_number}')
    print(f'Fact -> {facts[random_number]}')

