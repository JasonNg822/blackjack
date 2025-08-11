# 扑克牌21点
# 一位庄家，最多6位玩家
# Ace 算10点吗？

# 多位“庄家”


import random

while True: # 问多少玩家
    try:
        np = int(input("How many player? ")) # np = number of player
        if np > 6 or np < 1:
            print("Number of player min is 1 and max is 6")
        else: 
            break
    except ValueError:
        print("Number of player min is 1 and max is 6")
        continue

while True: # 问Ace可以算10点吗？
    at = input("Ace can be 10? ").strip().upper()
    if at == "YES" or at == "Y" or at == "NO" or at == "N":
        break
    else:
        continue

while True: # 玩家15点可以不玩吗？
    ft = input("If 2 card get 15, who can don't play? ").strip().upper()
    if ft == "HOST" or ft == "PLAYER AND HOST" or ft == "PLAYER" or ft == "NO" or ft == "N":
        break
    else:
        print("Please key in 'Host' or 'Player' or 'Player and Host' or 'N' for no one")

while True: # 两张一样的算赢吗？
    pairs = input("Is that get pair at the first 2 card win double? ").strip().upper()
    if pairs == "YES" or pairs == "Y" or pairs == "NO" or pairs == "N":
        break
    else:
        print("Please key in 'YES' or 'Y' or 'NO' or 'N'")

# hcard = hold card
host_hcard = set()
player1_hcard = set()
player2_hcard = set()
player3_hcard = set()
player4_hcard = set()
player5_hcard = set()
player6_hcard = set()
used_card = set()
pairp = set()
ftnp = set()

card_value = {
    "s1": 1, "h1": 1, "c1": 1, "d1": 1,
    "s2": 2, "h2": 2, "c2": 2, "d2": 2,
    "s3": 3, "h3": 3, "c3": 3, "d3": 3,
    "s4": 4, "h4": 4, "c4": 4, "d4": 4,
    "s5": 5, "h5": 5, "c5": 5, "d5": 5,
    "s6": 6, "h6": 6, "c6": 6, "d6": 6,
    "s7": 7, "h7": 7, "c7": 7, "d7": 7,
    "s8": 8, "h8": 8, "c8": 8, "d8": 8,
    "s9": 9, "h9": 9, "c9": 9, "d9": 9,
    "s10": 10, "h10": 10, "c10": 10, "d10": 10,
    "sJ": 10, "hJ": 10, "cJ": 10, "dJ": 10,
    "sQ": 10, "hQ": 10, "cQ": 10, "dQ": 10,
    "sK": 10, "hK": 10, "cK": 10, "dK": 10,
    }

def ftn(card, pn):
        if ft == "HOST" and (len(host_hcard) == 2 and calculate(host_hcard) == 15):
            wp = input("Host get 15, want play or not? ").strip().upper()
            if wp == "NO" or wp == "N":
                print("Host get 15 and choose to don't play")
                print("Game End")
                ftnp.add("Host")
                return 1
            elif wp == "YES" or wp == "Y":
                return 0
            else:
                print("Please key in 'YES' or 'Y' or 'NO' 'N'")
        elif ft == "PLAYER AND HOST" and (len(card) == 2 and calculate(card) == 15):
            wp = input(f"{pn} get 15, want play or not? ").strip().upper()
            if (wp == "NO" or wp == "N") and pn == "Host":
                print("Host get 15 and choose to don't play")
                print("Game End")
                ftnp.add("Host")
                return 1
            elif wp == "NO" or wp == "N":
                print(f"{pn} get 15 and choose to don't play")
                ftnp.add(pn)
                return 0
            elif wp == "YES" or wp == "Y":
                return 0
            else:
                print("Please key in 'YES' or 'Y' or 'NO' 'N'")
        elif ft == "PLAYER" and (len(card) == 2 and calculate(card) == 15):
            wp = input(f"{pn} get 15, want play or not? ").strip().upper()
            if wp == "NO" or wp == "N":
                print(f"{pn} get 15 and choose to don't play")
                ftnp.add(pn)
            elif wp == "YES" or wp == "Y":
                return 0
            else:
                print("Please key in 'YES' or 'Y' or 'NO' 'N'")


def pair(card, pn):
    for pa in range(1):
        if "Host" in ftnp:
            break
        if pairs == "YES" or pairs == "Y":
            if len(card) == 2 and card[0][-1] == card[1][-1]:
                pairp.add(pn)
                return 1
            else:
                return 
        

def give_card():
    for p in range((np + 1) * 2): # np + 1 = 庄家 + 玩家数量 
        if np < 6:
            if p == np:
                p = host_hcard
                pn = "Host first card"
            elif p == (np * 2) + 1:
                p = host_hcard
                pn = "Host second card"
            elif p == np + 1:
                p = player1_hcard
                pn = "Player1 second card"
            elif p == np + 2:
                p = player2_hcard
                pn = "Player2 second card"
            elif p == np + 3:
                p = player3_hcard
                pn = "Player3 second card"
            elif p == np + 4:
                p = player4_hcard
                pn = "Player4 second card"
            elif p == np + 5:
                p = player5_hcard
                pn = "Player5 second card"
            elif p == 0:
                p = player1_hcard
                pn = "Player1 first card"
            elif p == 1:
                p = player2_hcard
                pn = "Player2 first card"
            elif p == 2:
                p  = player3_hcard
                pn = "Player3 first card"
            elif p == 3:
                p = player4_hcard
                pn = "Player4 first card"
            elif p == 4:
                p = player5_hcard
                pn = "Player5 first card"
            # hc = hold card
            hc = random.choice([
                "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK",
                "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK",
                "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK",
                "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK"
            ])
            if hc not in used_card:
                used_card.add(hc)
                p.add(hc)
            else:
                while True:
                    if hc in used_card:
                        hc = random.choice([
                            "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK",
                            "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK",
                            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK",
                            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK"
                        ])
                    elif hc not in used_card:
                        used_card.add(hc)
                        p.add(hc)
                        break
            print(pn, "get", hc)
        elif np == 6:
            if p == 0:
                p = player1_hcard
                pn = "Player1 first card"
            elif p == 1:
                p = player2_hcard
                pn = "Player2 first card"
            elif p == 2:
                p  = player3_hcard
                pn = "Player3 first card"
            elif p == 3:
                p = player4_hcard
                pn = "Player4 first card"
            elif p == 4:
                p = player5_hcard
                pn = "Player5 first card"
            elif p == 5:
                p = player6_hcard
                pn = "Player6 first card"
            elif p == 6:
                p = host_hcard
                pn = "Host first card"
            elif p == 7:
                p = player1_hcard
                pn = "Player1 second card"
            elif p == 8:
                p  = player2_hcard
                pn = "Player2 second card"
            elif p == 9:
                p = player3_hcard
                pn = "Player3 second card"
            elif p == 10:
                p = player4_hcard
                pn = "Player4 second card"
            elif p == 11:
                p = player5_hcard
                pn = "Player5 second card"
            elif p == 12:
                p = player6_hcard
                pn = "Player6 second card"
            elif p == 13:
                p = host_hcard
                pn = "Host second card"
            # hc = hold card
            hc = random.choice([
                "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK",
                "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK",
                "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK",
                "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK"
            ])
            if hc not in used_card:
                used_card.add(hc)
                p.add(hc)
            else:
                while True:
                    if hc in used_card:
                        hc = random.choice([
                            "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK",
                            "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK",
                            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK",
                            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK"
                        ])
                    elif hc not in used_card:
                        used_card.add(hc)
                        p.add(hc)
                        break
            print(pn, "get", hc)


def draw_card():
    for d in range(np + 1):
        if d == np:
            d = host_hcard
            dn = "Host"
        elif d == 0:
            d = player1_hcard
            dn = "Player1"
        elif d == 1:
            d = player2_hcard
            dn = "Player2"
        elif d == 2:
            d = player3_hcard
            dn = "Player3"
        elif d == 3:
            d = player4_hcard
            dn = "Player4"
        elif d == 4:
            d = player5_hcard
            dn = "Player5"                
        elif d == 5:
            d = player6_hcard
            dn = "Player6"
        elif d == 6:
            d = host_hcard
            dn = "Host"
        
        if "Host" in ftnp:
            break
        elif dn in ftnp:
            print(f"{dn} get 15, don't want to play")
            continue
            
        if dn in pairp:
            print(f"{dn}, get pair and win double already, skip turn")
            continue
        while True:            
            # wd = want to draw?
            print(f"{dn},", end="")
            wd = input(" You want to draw a card? ").upper().strip()
            if wd == "Yes" or wd == "Y":
                # dc = draw card
                dc = random.choice([
                "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK",
                "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK",
                "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK",
                "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK"
                ])
                if dc not in used_card:
                    used_card.add(dc)
                    d.add(dc)
                else:
                    while True:
                        if dc in used_card:
                            dc = random.choice([
                            "s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK",
                            "h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK",
                            "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK",
                            "d1", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK"
                            ])
                            if dc not in used_card:
                                used_card.add(dc)
                                d.add(dc)
                                break
                print(dn, "get", dc)
            elif wd == "NO" or wd == "N":
                break


def calculate(card):
    total = sum(card_value[c] for c in card)
    ace = 0
    if at == "NO" or at == "N":
        for c in card:
            if card_value[c] == 1:
                ace += 1
            else:
                continue
        
        for c in range(ace):
            if total + 10 < 22:
                total += 10
    elif at == "YES" or at == "Y":
        for c in card:
            if card_value[c] == 1:
                ace += 1
            else:
                continue

        for c in range(ace):
            if total + 10 < 22:
                total += 10
            elif total + 9 < 22:
                total += 9
    return total


def gp():
    for p in range(np + 1): # np = number of player
        if p == np:
            p = host_hcard
            pn = "Host"
        elif p == 0:
            p = player1_hcard
            pn = "Player1"
        elif p == 1:
            p = player2_hcard
            pn = "Player2"
        elif p == 2:
            p  = player3_hcard
            pn = "Player3"
        elif p == 3:
            p = player4_hcard
            pn = "Player4"
        elif p == 4:
            p = player5_hcard
            pn = "Player5"
        elif p == 5:
            p = player6_hcard
            pn = "Player6"
        
        if "Host" in ftnp:
            break
        print(pn, "have", len(p), "Point:", calculate(p))


def rule():
    for p in range(np):
        h = "Host"
        host_hcardl = list(host_hcard)
        player1_hcardl = list(player1_hcard)
        player2_hcardl = list(player2_hcard)
        player3_hcardl = list(player3_hcard)
        player4_hcardl = list(player4_hcard)
        player5_hcardl = list(player5_hcard)
        player6_hcardl = list(player6_hcard)
        if p == 0:
            p = player1_hcard
            pl = player1_hcardl
            pn = "Player1"
        elif p == 1:
            p = player2_hcard
            pl = player2_hcardl
            pn = "Player2"
        elif p == 2:
            p = player3_hcard
            pl = player3_hcardl
            pn = "Player3"
        elif p == 3:
            p = player4_hcard
            pl = player4_hcardl
            pn = "Player4"
        elif p == 4:
            p = player5_hcard
            pl = player5_hcardl
            pn = "Player5"
        elif p == 5:
            p = player6_hcard
            pl = player6_hcardl
            pn = "Player6"
        if "Host" in ftnp:
            break
        elif pn in ftnp:
            print(f"{pn} not playing this round")
            continue

                                                                                # 玩家不是5张牌少过16点和不是pair
        if len(p) != 5 and calculate(p) < 16 and pair(pl, pn) != 1:
            if calculate(host_hcard) < 16:                                              # 庄家也少过16点
                print(pn, "draw with host")
            elif calculate(host_hcard) > 21:                                            # 庄家爆
                print(pn, "not enough 16, lose")
            elif calculate(host_hcard) < 21:                                            # 庄家多过15点没爆
                print(pn, "not enough 16, lose")
        elif len(host_hcard) != 5 and (calculate(host_hcard) < 16 and calculate(p) > 15):
            print("Host not enough 16,", pn, "win")

        elif pair(pl, pn) == 1 and pair(host_hcardl, h) == 1:
            if pl[0][-1] == host_hcardl[0][-1]:
                print(f"{pn} draw with host")
            if pl[0][-1] == "1" and host_hcardl[0][-1] != "1":
                print(f"{pn} win triple")
            else:
                print(f"{pn} lose triple")
            if pl[0][-1] == "K" and (host_hcardl[0][-1] not in ("K", "1")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "Q" and (host_hcardl[0][-1] not in ("Q", "K", "1")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "J" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "0" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1", "0")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "9" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1", "0", "9")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "8" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1", "0", "9", "8")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "7" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1", "0", "9", "8", "7")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "6" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1", "0", "9", "8", "7", "6")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "5" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1", "0", "9", "8", "7", "6", "5")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "4" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1", "0", "9", "8", "7", "6", "5", "4")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "3" and (host_hcardl[0][-1] not in ("J", "Q", "K", "1", "0", "9", "8", "7", "6", "5", "4", "3")):
                print(f"{pn} get pair biggier than host win double")
            else:
                print(f"{pn} lose double")
            if pl[0][-1] == "2" and (host_hcardl[0][-1] == "2"):
                print(f"{pn} lose double")
            else:
                print(f"{pn} draw with host")
        elif pair(pl, pn) == 1 and pair(host_hcardl, h) != 1:
            if len(host_hcard) == 2 and calculate(host_hcard) == 21:
                print(f"{pn} lose double")
            else:
                print(f"{pn} win double")
                                                                                #玩家和庄家都是不是5张牌
        elif len(p) != 5 and len(host_hcard) != 5:
            if calculate(p) == 21 and calculate(host_hcard) == 21:                      # 玩家21点，庄家21点
                print(pn, "draw with host")
            elif calculate(p) == 21 and calculate(host_hcard) != 21:                    # 玩家21点， 庄家少过或多过21点
                print(pn, "win double")
            elif calculate(p) != 21 and calculate(host_hcard) == 21:                    # 玩家少过或多过21，庄家21点
                print(pn, "lose double")
            elif calculate(p) < calculate(host_hcard) and calculate(host_hcard) < 21:   # 玩家和庄家都不是21点，玩家小过庄家
                print(pn, "lose")
            elif calculate(p) > calculate(host_hcard) and calculate(p) < 21:            # 玩家和庄家都不是21点，玩家大过庄家
                print(pn, "win")
            elif calculate(p) > 21 and calculate(host_hcard) < 21:                      # 玩家爆，庄家没爆 
                print(pn, "lose")
            elif calculate(p) > 21 and calculate(host_hcard) > 21:                      # 玩家和庄家都爆
                print(pn, "draw with host")
            elif calculate(p) < 21 and calculate(host_hcard) > 21:                       # 玩家没爆，庄家包
                print(pn, "win")
            elif calculate(p) == calculate(host_hcard) and calculate(host_hcard) < 22: # 玩家和庄加都没爆和一样点数
                print(pn, "draw with host")
                                                                                #玩家和庄家都5张牌
        elif len(p) == 5 and len(host_hcard) == 5:
            if calculate(p) == 21 and calculate(host_hcard) == 21:                      # 玩家和庄家都是21点
                print(pn, "draw with host")
            elif calculate(p) == 21 and calculate(host_hcard) != 21:                    #玩家21点，庄家少过或多过21点
                print(pn, "win triple")
            elif calculate(p) != 21 and calculate(host_hcard) == 21:                    # 玩家少过或多过21点，庄家21点
                print(pn, "lose triple")
            elif calculate(p) < calculate(host_hcard) and calculate(host_hcard) < 21:   # 玩家和撞击都没爆，玩家少过庄家
                print(pn, "lose")
            elif calculate(p) > calculate(host_hcard) and calculate(p) < 21:             # 玩家和撞击都没爆，玩家大过庄家
                print(pn, "win")
            elif calculate(p) > 21 and calculate(host_hcard) > 21:                       # 玩家和庄家都爆
                print(pn, "lose double")
            elif calculate(p) > 21 and calculate(host_hcard) < 21:                      # 玩家爆，庄家少过21点
                print(pn, "lose double")
            elif calculate(p) < 21 and calculate(host_hcard) > 21:                      # 玩家少过21点，庄家爆
                print(pn, "win double")
                                                                                # 玩家5张牌，庄家不是5张牌
        elif len(p) == 5 and len(host_hcard) != 5:
            if calculate(p) == 21:                                                      # 玩家21点
                print(pn, "win triple")
            elif calculate(p) < 21:                                                     # 玩家少过21点
                print(pn, "win double")
            elif calculate(p) > 21:                                                     # 玩家大过21点
                print(pn, "lose double")
                                                                                    # 玩家不是5张牌，庄家5张牌
        elif len(p) != 5 and len(host_hcard) == 5:
            if calculate(host_hcard) == 21:                                              # 庄家21点
                print(pn, "lose triple")
            elif calculate(host_hcard) < 21:                                             #庄家少过21点
                print(pn, "lose double")
            elif calculate(host_hcard) > 21 and calculate(p) < 21:                       # 玩家没爆， 庄家爆
                print(pn, "win double")
            elif calculate(host_hcard) > 21 and calculate(p) > 21:                        # 庄家和玩家都爆
                print(pn, "draw with host")


def main():
    for m in range(1):
        give_card()
        host_hcardl = list(host_hcard)
        player1_hcardl = list(player1_hcard)
        player2_hcardl = list(player2_hcard)
        player3_hcardl = list(player3_hcard)
        player4_hcardl = list(player4_hcard)
        player5_hcardl = list(player5_hcard)
        player6_hcardl = list(player6_hcard)
        if ft == "PLAYER AND HOST":
            for p in range(np + 1): 
                if p == np:
                    p = host_hcard
                    pn = "Host"
                elif p == 0:
                    p = player1_hcard
                    pn = "Player1"
                elif p == 1:
                    p = player2_hcard
                    pn = "Player2"
                elif p == 2:
                    p  = player3_hcard
                    pn = "Player3"
                elif p == 3:
                    p = player4_hcard
                    pn = "Player4"
                elif p == 4:
                    p = player5_hcard
                    pn = "Player5"
                elif p == 5:
                    p = player6_hcard
                    pn = "Player6"
                if ftn(p, pn) == 1:
                    break
            
        for p in range(np): 
            if p == 0:
                p = player1_hcard
                pn = "Player1"
            elif p == 1:
                p = player2_hcard
                pn = "Player2"
            elif p == 2:
                p  = player3_hcard
                pn = "Player3"
            elif p == 3:
                p = player4_hcard
                pn = "Player4"
            elif p == 4:
                p = player5_hcard
                pn = "Player5"
            elif p == 5:
                p = player6_hcard
                pn = "Player6"
            if ft == "PLAYER":
                if ftn(p, pn) == 1:
                    break

        if ft == "HOST":
            if ftn(host_hcard, pn) == 1:
                break

        for p in range(np + 1): # 检查是否有pair
            if p == np:
                p = host_hcardl
                pn = "Host"
            elif p == 0:
                p = player1_hcardl
                pn = "Player1"
            elif p == 1:
                p = player2_hcardl
                pn = "Player2"
            elif p == 2:
                p  = player3_hcardl
                pn = "Player3"
            elif p == 3:
                p = player4_hcardl
                pn = "Player4"
            elif p == 4:
                p = player5_hcardl
                pn = "Player5"
            elif p == 5:
                p = player6_hcardl
                pn = "Player6"
            pair(p, pn)
        draw_card()
        gp()
        rule()


main()