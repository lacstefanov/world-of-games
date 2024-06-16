import os


def add_score(difficulty): 
    points_won_by_user = (difficulty * 3) + 5
    print(f'Points won by user: {points_won_by_user}')

    #file_path = r"C:\Users\lstefanov\Documents\Knowledge\DevOps\Main Project\Assignment 2\Scores.txt"
    file_path = "/app/Scores.txt"

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            current_score = int(file.read().strip())

            new_score = current_score + points_won_by_user

        with open(file_path, 'w') as file:
            file.write(str(new_score))

    else:
        with open(file_path, 'w') as file:
            file.write(str(points_won_by_user))