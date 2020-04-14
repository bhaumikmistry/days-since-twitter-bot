from random import randint

facts = [
    "Highest Innings total, 413–5 (50 overs) v Bermuda, India Won by 257  Runs, 12th Match, Group B, ICC Cricket World Cup at Port of Spain, Mar 19 2007",
    "2nd Highest Innings total, 373-6 (50 overs) v Sri Lanka, India Won by 157  Runs, 21st Match, ICC Cricket World Cup at Taunton, May 26 1999",
    "3rd Highest Innings total, 370–4 (50 overs) v Bangladesh, India Won by 87  Runs, 1st Match, Group B (D/N), ICC Cricket World Cup at Dhaka, Feb 19 2011",
    "4th Highest Innings total, 352–5 (50 overs) v Australia, India Won by 36  Runs, 14th match, ICC Cricket World Cup at The Oval, Jun 9 2019",
    "5th Highest Innings total, 338 (49.5 overs) v England, Match tied, 11th Match, Group B (D/N), ICC Cricket World Cup at Bengaluru, Feb 27 2011",
    "Lowest Completed Innings, 125(41.4 overs) v Australia, Australia Won by 9 wickets, 11th Match, ICC World Cup at Centurion, Feb 15 2003",
    "2nd Lowest Completed Innings, 158 (37.5 overs) v Australia, Australia Won by 162  Runs, 11th Match, ICC Cricket World Cup at Nottingham, Jun 13 1983",
    "3rd Lowest Completed Innings, 182 (55.5 overs) v New Zealand, New Zealand Won by 8 wickets, 6th Match, ICC Cricket World Cup at Leeds, Jun 13 1979",
    "4th Lowest Completed Innings, 183 (54.4 overs) v West Indies, India Won by 43  Runs, Final, ICC Cricket World Cup at Lord's, Jun 25 1983",
    "5th Lowest Completed Innings, 185 (43.3 overs) v Sri Lanka, Sri Lanka Won by 69  Runs, 20th Match, Group B, ICC World Cup at Port of Spain, Mar 23 2007",
    "Best Bowling Innings Figures, 6–23 (10 overs) Ashish Nehra v England, India Won by 82  Runs, 30th Match (D/N), ICC World Cup at Durban, Feb 26 2003",
    "2nd Best Bowling Innings Figures, 5–27 (9.3 overs) Venkatesh Prasad v Pakistan, India Won by 47  Runs, 4th Super, ICC World Cup at Manchester, Jun 8 1999",
    "3rd Best Bowling Innings Figures, 5–31 (9.3 overs) Robin Singh v Sri Lanka, India Won by 157  Runs, 21st Match, ICC World Cup at Taunton, May 26 1999",
    "4th Best Bowling Innings Figures, 5–31 (10 overs) Yuvraj Singh v Ireland, India Won by 5 wickets, 22nd Match, Group B (D/N), ICC Cricket World Cup at Bengaluru, Mar 6 2011",
    "5th Best Bowling Innings Figures, 5–43 (12 overs) Kapil Dev v Australia, Australia Won by 162  Runs, 11th Match, ICC Cricket World Cup at Nottingham, Jun 13 1983",
    "In ICC Cricket World Cup Year 1975, at England, India's last position was - Group stage, Games Played 3, Won 1, No result 0, Lost 2, with Captain S Venkataraghavan",
    "In ICC Cricket World Cup Year 1979, at England, India's last position was - Group stage, Games Played 3, Won 0, No result 0, Lost 3, with Captain S Venkataraghavan",
    "In ICC Cricket World Cup Year 1983, at England, India's last position was - Champions, Games Played 8, Won 6, No result 0, Lost 2, with Captain Kapil Dev",
    "In ICC Cricket World Cup Year 1987, at India Pakistan, India's last position was - Semi-finals, Games Played 7, Won 5, No result 0, Lost 2, with Captain Kapil Dev",
    "In ICC Cricket World Cup Year 1992, at Australia New Zealand, India's last position was - India's last position was at Round-robin, Games Played 8, Won 2, No result 1, Lost 5, with Captain M Azharuddin",
    "In ICC Cricket World Cup Year 1996, at India Pakistan Sri Lanka, India's last position was - Semi-finals, Games Played 7, Won 4, No result 0, Lost 3, with Captain M Azharuddin",
    "In ICC Cricket World Cup Year 1999, at England Scotland Ireland Netherlands, India's last position was - Super Six, Games Played 8, Won 4, No result 0, Lost 4, with Captain M Azharuddin",
    "In ICC Cricket World Cup Year 2003, at South Africa Zimbabwe Kenya, India's last position was - Runners-up, Games Played 11, Won 9, No result 0, Lost 2, with Captain Sourav Ganguly",
    "In ICC Cricket World Cup Year 2007, at West Indies Cricket Board, India's last position was - Group stage, Games Played 3, Won 1, No result 0, Lost 2, with Captain Rahul Dravid",
    "In ICC Cricket World Cup Year 2011, at India Bangladesh Sri Lanka, India's last position was - Champions, Games Played 9, Won 7, No result 1, Lost 1, with Captain MS Dhoni",
    "In ICC Cricket World Cup Year 2015, at Australia New Zealand, India's last position was - Semi-finals, Games Played 8, Won 7, No result 0, Lost 1, with Captain MS Dhoni",
    "In ICC Cricket World Cup Year 2019, at England Wales, India's last position was - Semi-finals, Games Played 10, Won 7, No result 1, Lost 2, with Captain Virat Kohli",
    "India's Record in ICC Cricket World Cup, Wins: 2, Total Games Played: 85, Won: 53, No Result: 3, Lost: 29",
    "In ICC Cricket World Cup, India's record against Australia: Match Played 12, Won 4, Lost 8, Tied 0, No Result 0, Win % 33.33, First Match Played on 13 June 1983",
    "In ICC Cricket World Cup, India's record against Afghanistan: Match Played 1, Won 1, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 22 June 2019",
    "In ICC Cricket World Cup, India's record against Bangladesh: Match Played 4, Won 3, Lost 1, Tied 0, No Result 0, Win % 75.00, First Match Played on 17 March 2007",
    "In ICC Cricket World Cup, India's record against Bermuda: Match Played 1, Won 1, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 19 March 2007",
    "In ICC Cricket World Cup, India's record against East Africa: Match Played 1, Won 1, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 11 June 1975",
    "In ICC Cricket World Cup, India's record against England: Match Played 8, Won 3, Lost 4, Tied 1, No Result 0, Win % 37.5, First Match Played on 7 June 1975",
    "In ICC Cricket World Cup, India's record against Ireland: Match Played 2, Won 2, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 6 March 2011",
    "In ICC Cricket World Cup, India's record against Kenya: Match Played 4, Won 4, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 18 February 1996",
    "In ICC Cricket World Cup, India's record against Namibia: Match Played 1, Won 1, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 23 February 2003",
    "In ICC Cricket World Cup, India's record against Netherlands: Match Played 2, Won 2, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 12 February 2003",
    "In ICC Cricket World Cup, India's record against New Zealand: Match Played 8, Won 3, Lost 5, Tied 0, No Result 0, Win % 37.5, First Match Played on 4 June 1975",
    "In ICC Cricket World Cup, India's record against Pakistan: Match Played 7, Won 7, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 4 March 1992",
    "In ICC Cricket World Cup, India's record against South Africa: Match Played 5, Won 2, Lost 3, Tied 0, No Result 0, Win % 40, First Match Played on 15 March 1992",
    "In ICC Cricket World Cup, India's record against Sri Lanka: Match Played 9, Won 4, Lost 4, Tied 0, No Result 1, Win % 44.44, First Match Played on 18 June 1979",
    "In ICC Cricket World Cup, India's record against United Arab Emirates: Match Played 1, Won 1, Lost 0, Tied 0, No Result 0, Win % 100, First Match Played on 28 February 2015",
    "In ICC Cricket World Cup, India's record against West Indies: Match Played 9, Won 6, Lost 3, Tied 0, No Result 0, Win % 66.66, First Match Played on 9 June 1979",
    "In ICC Cricket World Cup, India's record against Zimbabwe: Match Played 9, Won 8, Lost 1, Tied 0, No Result 0, Win % 88.89, First Match Played on 11 June 1983",
    "Highest partnerships in ICC Cricket World Cup, Total  Runs 318 (2nd wicket), Sourav Ganguly (183) & Rahul Dravid (145) Against Sri Lanka at Taunton in 1999",
    "2nd Highest partnerships in ICC Cricket World Cup, Total  Runs 244 (2nd wicket), Sachin Tendulkar (152) & Sourav Ganguly (111) Against Namibia at Pietermaritzburg in 2003",
    "3rd Highest partnerships in ICC Cricket World Cup, Total  Runs 237* (3rd wicket), Rahul Dravid (104*) & Sachin Tendulkar (140*) Against Kenya at Bristol in 1999",
    "4th Highest partnerships in ICC Cricket World Cup, Total  Runs 203 (3rd wicket), Virender Sehwag (175) & Virat Kohli (100) Against Bangladesh at Dhaka in 2011",
    "5th Highest partnerships in ICC Cricket World Cup, Total  Runs 202 (2nd wicket), Sourav Ganguly (89) & Virender Sehwag (114) Against Bermuda at Port of Spain in 2007",
    "Highest partnership for 1st wicket in ICC Cricket World Cup, 189 by, Rohit Sharma (103) & K. L. Rahul (111) Against Sri Lanka at Leeds in year 2019",
    "Highest partnership for 2nd wicket in ICC Cricket World Cup, 318 by, Sourav Ganguly (183) & Rahul Dravid (145) Against Sri Lanka at Taunton in year 1999",
    "Highest partnership for 3rd wicket in ICC Cricket World Cup, 237* by, Rahul Dravid (104*) & Sachin Tendulkar (140*) Against Kenya at Bristol in year 1999",
    "Highest partnership for 4th wicket in ICC Cricket World Cup, 142 by, Navjot Singh Sidhu (80) & Vinod Kambli (106) Against Zimbabwe at Kanpur in year 1996",
    "Highest partnership for 5th wicket in ICC Cricket World Cup, 196* by, Suresh Raina (110*) & Mahendra Singh Dhoni (85*) Against Zimbabwe at Auckland in year 2015",
    "Highest partnership for 6th wicket in ICC Cricket World Cup, 74* by, Suresh Raina (34*) & Yuvraj Singh (57*) Against Australia at Ahmedabad in year 2011",
    "Highest partnership for 7th wicket in ICC Cricket World Cup, 116 by, Ravindra Jadeja (77) & Mahendra Singh Dhoni (50) Against New Zealand at Manchester in year 2019",
    "Highest partnership for 8th wicket in ICC Cricket World Cup, 82* by, Kapil Dev (72*) & Kiran More (42*) Against New Zealand at Bangalore in year 1987",
    "Highest partnership for 9th wicket in ICC Cricket World Cup, 126* by, Kapil Dev (175*) & Syed Kirmani (24*) Against Zimbabwe at Tunbridge Wells in year 1983",
    "Highest partnership for 10th wicketh in ICC Cricket World Cup, 32 by, Zaheer Khan (15) & Munaf Patel (15) Against Bangladesh at Port of Spain in year 2007",
    "South Africa played ICC Cricket World Cup for the first time in 1992, Record Win % 61.9",
    "In ICC Cricket World Cup, Australia's record from 1975 to 2019, total games 94, Won 69, Lost 23, Tied 1, No Result 1, Win % 74.73 is Best of all.",
    "In ICC Cricket World CUp, 2nd best win margin by  Runs is 257  Runs, India (413–5) beat Bermuda (156) at Queen's Park Oval, Port of Spain, Trinidad on 19 March 2007",
    "In ICC Cricket World CUp, best win margin by  Runs is 275  Runs, Australia (417–6) beat Afghanistan (142) at WACA, Perth on 4 March 2015",
    "Highest match aggregate is 714-13 (100 overs) between Australia (381-5) v Bangladesh (333-8) in ICC Cricket World Cup at Trent Bridge, Nottingham on 20 June 2019",
    "2nd Highest match aggregate is 688–18 (96.2 overs) between Australia (376–9) v Sri Lanka (312–9) in ICC Cricket World Cup at Sydney Cricket Ground, Sydney on 8 March 2015",
    "3rd Highest match aggregate is 682–17 (100 overs) between Pakistan (348–8) v England (334–9) in ICC Cricket World Cup at Trent Bridge, Nottingham on 3 June 2019",
    "4th Highest match aggregate is 676–18 (99.5 overs) between India (338) v England (338–8) in ICC Cricket World Cup at M. Chinnaswamy Stadium, Bangalore on 27 February 2011",
    "5th Highest match aggregate is 671–16 (98.0 overs) between Australia (377–6) v South Africa (294) in ICC Cricket World Cup at Warner Park Sporting Complex, Basseterre on 24 March 2007",
    "Lowest match aggregate is 73–11 (23.2 overs) between Sri Lanka (37–1) v Canada (36) in ICC Cricket World Cup at Boland Park, Paarl on 19 February 2003",
    "2nd Lowest match aggregate is 91–12 (54.2 overs) between England (46–2) v Canada (45) in ICC Cricket World Cup at Old Trafford, Manchester on 13 June 1979",
    "3rd Lowest match aggregate is 117–11 (31.1 overs) between West Indies (59–1) v Bangladesh (58) in ICC Cricket World Cup at Sher-e-Bangla National Stadium, Dhaka on 4 March 2011",
    "4th Lowest match aggregate is 138–12 (41.4 overs) between West Indies (70–2) v Scotland (68) in ICC Cricket World Cup at Grace Road, Leicester on 27 May 1999",
    "5th Lowest match aggregate is 141–10 (31.5 overs) between New Zealand (72–0) v Kenya (69) in ICC Cricket World Cup at M. A. Chidambaram Stadium, Chennai on 20 February 2011",
    "Highest run chase is 329–7 (49.1 overs) by team Ireland against team England in ICC Cricket World Cup at M. Chinnaswamy Stadium, Bengaluru on 2 March 2011",
    "2nd Highest run chase is 322–3 (41.3 overs) by team Bangladesh against team West Indies in ICC Cricket World Cup at County Ground, Taunton on 17 June 2019",
    "3rd Highest run chase is 322–4 (48.1 overs) by team Bangladesh against team Scotland in ICC Cricket World Cup at Saxton Oval, Nelson on 5 March 2015",
    "4th Highest run chase is 313–7 (49.2 overs) by team Sri Lanka against team Zimbabwe in ICC Cricket World Cup at Pukekura Park, New Plymouth on 23 February 1992",
    "5th Highest run chase is 312–1 (47.2 overs) by team Sri Lanka against team England in ICC Cricket World Cup at Westpac Stadium, Wellington on 1 March 2015",
    "In the 2011 Cricket World Cup, Highest run chase could have been 338-8 when England scored 338–8 in the second innings to tie their game against India, Match resulted in tie."
    "In ICC Cricket World Cup 2007, Team Australia achieved a 100% win record, total Matches played 11 ",
    "In ICC Cricket World Cup 2003, Team Australia achieved a 100% win record, total Matches played 11",
    "In ICC Cricket World Cup 1996, Team Sri Lanka achieved a 100% win record, total Matches played 8, which includes 2 wins on forfeit",
    "In ICC Cricket World Cup 1975, Team West Indies achieved a 100% win record, total Matches played 5",
    "In ICC Cricket World Cup 1979, Team West Indies achieved a 100% win record, total Matches played 5, which includes one no result",
    "In ICC Cricket World Cup, 2nd best win margin by highest  Runs is 257  Runs, India (413–5) beat Bermuda (156) at Queen's Park Oval, Port of Spain, Trinidad on 19 March 2007",
    "In ICC Cricket World Cup, best win margin by highest  Runs is 275  Runs, Australia (417–6) beat Afghanistan (142) at WACA, Perth on 4 March 2015",
    "In ICC Cricket World Cup, best win margin by lower  Runs is Boundary Count, England (241) Super Over (15-0) beat New Zealand (241-8) Super Over(15-1) Won on boundary count (26-17) at Lord's Cricket Ground, London 14 July 2019"
    "In ICC Cricket World Cup, 2nd best win margin by lower  Runs is 1 run when Australia (270–6) beat India (269) at M. A. Chidambaram Stadium, Chennai on 9 October 1987",
    "In ICC Cricket World Cup, 2nd best win margin by lower  Runs is 1 run when Australia (237–9) beat India (234) [Target 236 (D/L Method)] at The Gabba, Brisbane on 1 March 1992",
    "In ICC Cricket World Cup, Highest innings totals is 417–6 (50 overs) Australia vs Afghanistan at WACA Ground, Perth on 4 March 2015",
    "In ICC Cricket World Cup, second Highest innings totals is 413–5 (50 overs) India vs Bermuda at Queen's Park Oval, Port of Spain on 19 March 2007",
    "In ICC Cricket World Cup, third Highest innings totals is 411–4 (50 overs) South Africa vs Ireland at Manuka Oval, Canberra on 3 March 2015",
    "In ICC Cricket World Cup, fourth Highest innings totals is 408–5 (50 overs) South Africa vs West Indies at Sydney Cricket Ground, Sydney on 27 February 2015",
    "In ICC Cricket World Cup, fifth Highest innings totals is 398–5 (50 overs) Sri Lanka vs Kenya Asgiriya Stadium, Kandy on 6 March 1996",
    "In ICC Cricket World Cup History, 2,278  Runs scored by Sachin Tendulkar of India in 45 Matches and 44 Innings with High Score of 152 and Average 56.95, total 100's:6, 50's:15 in period 1992-2011",
    "In ICC Cricket World Cup History, 1,743  Runs scored by Ricky Ponting of Australia in 46 Matches and 42 Innings with High Score of 140* and Average 45.86, total 100's:5, 50's:6 in period 1996–2011",
    "In ICC Cricket World Cup History, 1,532  Runs scored by Kumar Sangakkara of Sri Lanka in 37 Matches and 35 Innings with High Score of 124 and Average 56.74, total 100's:5, 50's:7 in period 2003–2015",
    "In ICC Cricket World Cup History, 1,225  Runs scored by Brian Lara of West Indies in 34 Matches and 33 Innings with High Score of 116 and Average 42.24, total 100's:2, 50's:7 in period 1992–2007",
    "In ICC Cricket World Cup History, 1,207  Runs scored by AB de Villiers of South Africa in 23 Matches and 23 Innings with High Score of 162* and Average 63.52, total 100's:4, 50's:6 in period 2007–2015",
    "In ICC Cricket World Cup History Highest individual scores is 237*  Runs by Martin Guptil of New Zealand in 163 Balls with 24 4s 11 6s with 145.39 SR against West Indies at Venue Wellington, New Zealand on 21 March 2015",
    "In ICC Cricket World Cup History 2nd Highest individual scores is 215  Runs by Chris Gayle of West Indies Cricket Board in 147 Balls with 10 4s 16 6s with 146.25 SR against Zimbabwe at Venue Manuka Oval, Canberra on 24 February 2015",
    "In ICC Cricket World Cup History 3rd Highest individual scores is 188  Runs by Gary Kirsten of South Africa in 159 Balls with 13 4s 4 6s with 118.23 SR against United Arab Emirates at Rawalpindi Cricket Stadium, Rawalpindi on 16 February 1996",
    "In ICC Cricket World Cup History 4th Highest individual scores is 183  Runs by Sourav Gangulyof India in 158 Balls with 17 4s 7 6s with 115.82 SR against Sri Lanka at Venue County ground, Taunton on 26 May 1999",
    "In ICC Cricket World Cup History 5th Highest individual scores is 181  Runs by Viv Richards of West Indies Cricket Board in 125 Balls with 16 4s 7 6s 144.80 SR against Sri Lanka National Stadium, Karachi on 13 October 1987",
    "In ICC Cricket World Cup History Highest average is 124.00 by Lance Klusener of South Africa in 14 Matches and 11 Innings with 8 Not Out, total of 372  Runs in 1999–2003 span",
    "In ICC Cricket World Cup History 2nd Highest average is 103.0 by Andrew Symonds of Australia in 18 Matches and 13 Innings with 8 Not Out, total of 515  Runs in 2003–2007 span",
    "In ICC Cricket World Cup History 3rd Highest average is 66.42 by Ben Stokes of England in 11 Matches and 10 Innings with 3 Not Out, total of 465  Runs in 2019-2019 span",
    "In ICC Cricket World Cup History 4th Highest average is 65.20 by Rohit Sharma of India in 17 Matches and 17 Innings with 2 Not Out, total of 978  Runs in 2015–2019 span",
    "In ICC Cricket World Cup History 5th Highest average is 63.52 by AB de Villiers of South Africa in 23 Matches and 22 Innings with 3 Not Out, total of 1207  Runs in 2007–2015 span"
    "In ICC Cricket World Cup History Highest Strike Rate is 169.25 by Glenn Maxwell of Australia with 18 Matches and 16 Innings, with 501  Runs and 296 Ball Faced in 2015–2019 span",
    "In ICC Cricket World Cup History 2nd Highest Strike Rate is 126.53 by Jos Buttler of England with 17 Matches and 14 Innings, with 453  Runs and 358 Ball Faced in 2015–2019 span",
    "In ICC Cricket World Cup History 3rd Highest Strike Rate is 121.17 by Lance Klusener of South Africa with 14 Matches and 11 Innings, with 372  Runs and 307 Ball Faced in 1999–2003 span",
    "In ICC Cricket World Cup History 4th Highest Strike Rate is 120.84 by Brendon McCullum of New Zealand with 34 Matches and 27 Innings, with 742  Runs and 614 Ball Faced in 2003–2015 span",
    "In ICC Cricket World Cup History 5th Highest Strike Rate is 117.94 by David Miller of South Africa wiht 14 Matches and 11 Innings, with 460  Runs and 390 Ball Faced in 2015–2019 span"
    "Cricket World Cup year 1975 winner West Indies with score 291–8, runner-up Australia with score 274, Result West Indies won by 17 runs.",
    "Cricket World Cup year 1979	winner West Indies with score 286–9, runner-up England with score 194, Result West Indies won by 92 runs",
    "Cricket World Cup year 1983	winner India with score 183, runner-up West Indies with score 140, Result India won by 43 runs",
    "Cricket World Cup year 1987	winner Australia with score 253–5, runner-up England with score 246–8, Result Australia won by 7 runs",
    "Cricket World Cup year 1992	winner Pakistan with score 249–6, runner-up England with score 227, Result Pakistan won by 22 runs",
    "Cricket World Cup year 1996	winner Sri Lanka with score 245–3, runner-up Australia with score 241, Result Sri Lanka won by 7 wickets"

]


Cricket World Cup year 1999	winner Australia with score 133–2, runner-up Pakistan with score 132, Result Australia won by 8 wickets
Cricket World Cup year 2003	winner Australia with score 359–2, runner-up India with score 234, Result Australia won by 125 runs
Cricket World Cup year 2007	winner Australia with score 281–4, runner-up Sri Lanka  with score 215–8, Result Australia won by 53 runs
Cricket World Cup year 2011	winner India with score 277–4, runner-up Sri Lanka with score 274–6, Result India won by 6 wickets
Cricket World Cup year 2015	winner Australia with score 186–3, runner-up New Zealand with score 183, Result Australia won by 7 wickets
Cricket World Cup year 2019	winner England with score 241, runner-up New Zealand with score 241–8, Result Match tied after regular play and super over; England won on boundary count


# if __name__ == "__main__":
#     length = len(facts)
#     print(f'length -> {length}')

#     random_number = randint(0,length-1)
#     print(f'random -> {random_number}')
#     print(f'Fact -> {facts[random_number]}')

