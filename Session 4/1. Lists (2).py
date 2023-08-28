
# Average With sum() Method:
# scores = [12, 14, 8, 20, 18, 17, 9]
# sum_scores = 0
# for score in scores:
#     sum_scores = sum(scores)
# N = len(scores)
# print(sum_scores/N)


# Average Without sum() Method:
# scores = [12, 14, 8, 20, 18, 17, 9]
# sum_scores = 0
# for score in scores:
#     sum_scores += score
# N = len(scores)
# print(sum_scores/N)


# Maximum With max() Method
# scores = [12, 14, 8, 20, 18, 17, 9]
# max_scores = max(scores)
# print(max_scores)


# Maximum Without max() Method
# scores = [12, 14, 8, 20, 18, 17, 9]
# max_scores = 0
# for score in scores:
#     if score > max_scores:
#         max_scores = score
#
# print(max_scores)


# Minimum Without max() Method
# scores = [12, 14, 8, 20, 18, 17, 9]
# min_scores = 20
# for score in scores:
#     if score < min_scores:
#         min_scores = score
#
# print(min_scores)


# A Solution for Long Lists :
# scores = [12, 14, 8, 20, 18, 17, 9, 500, 123, 3, 50, 40, 1, 2]
# Maxs = 0
# sMaxs= 0
# for S in scores:
#     if S > sMaxs:
#         if S > Maxs:
#             sMaxs = Maxs
#             Maxs = S
#         else:
#             sMaxs = S

# print(Maxs, sMaxs)


# Count of Failed Scores :
# scores = [12, 14, 8, 20, 18, 17, 9, 200, 500, 3, 50, 40, 1, 2]
#
# N_failed = 0
# for S in scores:
#     if S < 10:
#         N_failed += 1
#
# print(N_failed)


# Split Lists Method (1):
# scores = "12 93 83 72 10 28 4 123"

# new_scores = scores.split()

# print(new_scores)


# Split Lists Method (2):
scores = "12 93 83 72 10 28 4 123"

print([int(s) for s in scores.split()])
