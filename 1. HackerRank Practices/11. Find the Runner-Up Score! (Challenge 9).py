
if __name__ == '__main__':
    n = int(input("Enter the n (Number of Scores): "))
    arr = map(int, input("Enter the Scores, Separated by Spaces: ").split())


def runner_up(arr):
    scores = list(arr)
    scores.sort(reverse=True)
    
    for i in range(len(scores) - 1):
        current_value = scores[i]
        next_value = scores[i + 1]
        
        if current_value > next_value:
            return next_value
        else:
            continue


print("The runner-up score is:", runner_up(arr))
