import random
import numpy as np
import matplotlib.pyplot as plt

ppl = 4
total_cards = np.arange(8, 101, 4)
plot_avg = []

for i in total_cards:
    #---------------
    win_cards = [1, 1]
    lose_cards = [0]*(i-2)
    all_cards = win_cards + lose_cards

    cards_pp = int(len(all_cards)/ppl)
    times = 10_000

    assert i%4 == 0, '--- not dividable by 4 ---'

    avg_count = []
    for _ in range(10):
        count = 0
        for _ in range(times):
            random.shuffle(all_cards)
            for j in range(ppl):
                if sum(all_cards[j*cards_pp:(j+1)*cards_pp]) == 2:
                    count += 1
        avg_count.append((count/times)*100)
    plot_avg.append(np.mean(avg_count))
    print(f'total card: {i} --- {np.mean(avg_count)}')

plt.plot(plot_avg)
plt.show()