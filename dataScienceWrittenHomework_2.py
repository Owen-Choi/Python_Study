import numpy as np
import math

scores = [28, 35, 26, 32, 28, 28, 35, 34, 46, 42, 37]

print("***** Standard scaling *****")

print("Mean :", '%.2f' % np.mean(scores))
print("Standard Deviation :", '%.2f' % np.std(scores))

mean = np.mean(scores)
std = np.std(scores)

normalized_scores = []
for value in scores:
    normalized_num = (value - mean) / std
    normalized_scores.append(round(normalized_num, 2))
print("Standard Scores :", normalized_scores)

print("***** Robust scaling *****")

scores.sort()
N = len(scores)
Q1_index = 0.25 * (N + 1)
Q3_index = 0.75 * (N + 1)
Q2_index = 0.5 * (N + 1)

if Q1_index.is_integer() :
    Q1 = scores[int(Q1_index)]
else :
    Q1_under = Q1_index.__trunc__()
    Q1_upper = Q1_index.__ceil__()
    Q1 = ( scores[int(Q1_under)] + scores[int(Q1_upper)] ) / 2

if Q2_index.is_integer() :
    Q2 = scores[int(Q2_index)]
else :
    Q2_under = Q2_index.__trunc__()
    Q2_upper = Q2_index.__ceil__()
    Q2 = (scores[int(Q2_under)] + scores[int(Q2_upper)]) / 2

if Q3_index.is_integer() :
    Q3 = scores[int(Q3_index)]
else :
    Q3_under = Q3_index.__trunc__()
    Q3_upper = Q3_index.__ceil__()
    Q3 = (scores[int(Q3_under)] + scores[int(Q3_upper)]) / 2

print("Q1 :", Q1, "Q2 :", Q2, "Q3 :", Q3)

new_scores = []

for i in scores :
    new_scores.append((i-Q1) / (Q3 - Q1))

print("scailed values : ")
print(new_scores)