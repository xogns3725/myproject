import random


def play_game():
    win_count = 0
    lose_count = 0
    draw_count = 0

    random_rsp = random.randint(1, 3)
    if random_rsp == 1:
        random_rsp = 'rock'
    elif random_rsp == 2:
        random_rsp = 'scissors'
    elif random_rsp == 3:
        random_rsp = 'paper'

    while True:
        rsp = input("rock, scissors, paper : ").lower()
        if rsp not in ['rock', 'scissors', 'paper']:
            print('rock, scissors, paper를 입력하세요')
            continue

        if rsp == 'rock':
            if random_rsp == 'rock':
                print('무승부!')
                draw_count += 1
            elif random_rsp == 'scissors':
                print('사용자 승!')
                win_count += 1
                break
            elif random_rsp == 'paper':
                print('컴퓨터 승!')
                lose_count += 1
                break
        elif rsp == 'scissors':
            if random_rsp == 'rock':
                print('컴퓨터 승!')
                lose_count += 1
                break
            elif random_rsp == 'scissors':
                print('무승부!')
                draw_count += 1
            elif random_rsp == 'paper':
                print('사용자 승!')
                win_count += 1
                break
        elif rsp == 'paper':
            if random_rsp == 'rock':
                print('사용자 승!')
                win_count += 1
                break
            elif random_rsp == 'scissors':
                print('컴퓨터 승!')
                lose_count += 1
                break
            elif random_rsp == 'paper':
                print('무승부!')
                draw_count += 1
    return win_count, lose_count, draw_count


def main():
    result = [0, 0, 0]
    while True:
        result = [x+y for x, y in zip(result, play_game())]

        retry = input('다시 도전하시겠습니까? (y/n) ')

        if retry == 'n':
            print('게임을 종료합니다')
            print(f'승: {result[0]} 패: {result[1]} 무승부: {result[2]}')
            break
        elif retry == 'y':
            print('게임을 재시작합니다')


if __name__ == "__main__":
    main()
