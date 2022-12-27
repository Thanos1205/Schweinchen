import random
import numpy as np
import matplotlib.pyplot as plt

# ------------------------
ppl = 4
times = 10_000
# ------------------------
total_cards = np.arange(8, 101, 4)
plot_count = []

for i in total_cards: 
    count = 0
    for _ in range(times):  #run 1_000 times
        cards = list(np.arange(i))
        cards_pp = int(i/ppl)

        wincard_1 = random.choice(cards)
        wincard_2 = random.choice([x for x in cards if x != wincard_1])
        
        chunks = [cards[x*cards_pp : (x+1)*cards_pp] for x in range(ppl)]   #e.g. [[0,1], [2,3], [4,5], [6,7]]
        ace_player = [x for x in chunks if wincard_1 in x][0]               #find first Ace
        if wincard_2 in ace_player:                                         #check if second Ace in list
            count += 1

    prob = (count/times)
    plot_count.append(prob)
    print(f'total card: {i} --- {round(prob*100, 2)}%')
plt.plot(total_cards, plot_count)
plt.xlabel('Total cards')
plt.ylabel("prob. of 'Schweinchen'")
plt.show()