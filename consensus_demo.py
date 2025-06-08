import random

# PoW: select highest power
miner = {'Alice': random.randint(1, 100), 'Bob': random.randint(1, 100)}
pow_winner = max(miner, key=miner.get)
print(f"[PoW] Winner: {pow_winner}, Power: {miner[pow_winner]}")

# PoS: select highest stake
staker = {'Charlie': random.randint(1, 100), 'Dave': random.randint(1, 100)}
pos_winner = max(staker, key=staker.get)
print(f"[PoS] Winner: {pos_winner}, Stake: {staker[pos_winner]}")

# DPoS: majority vote
delegates = ['Eve', 'Frank', 'Grace']
votes = random.choices(delegates, k=5)
vote_counts = {d: votes.count(d) for d in delegates}
dpos_winner = max(vote_counts, key=vote_counts.get)
print(f"[DPoS] Votes: {votes}")
print(f"[DPoS] Winner: {dpos_winner}, Votes: {vote_counts[dpos_winner]}")
