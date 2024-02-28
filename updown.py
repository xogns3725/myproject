import random

def play_game():
    random_number = random.randint(1, 100)
    count = 0

    while True:
        
        try:
            num = int(input("숫자를 입력하세요 : "))
            if num < 1 or num > 100:
                print('유효한 범위 내의 숫자를 입력하세요')
            else:
                count += 1
                if num < random_number:
                    print('업')
                elif num > random_number:
                    print('다운')
                elif num == random_number:
                    break
        except ValueError:
            print('정수를 입력하세요')

    print('맞았습니다')
    print('시도 횟수 : ', count)
    return count

def main():
    max_count = 0

    while True:
        count = play_game()
        if count > max_count:
            max_count = count

        retry = input('다시 도전하시겠습니까? (y/n) ')

        if retry == 'n':
            print('게임을 종료합니다')
            break
        elif retry == 'y':
            print('게임을 재시작합니다')
            print('이전 게임 플레이어 최고 시도 횟수 : ', max_count)

if __name__ == "__main__":
    main()
