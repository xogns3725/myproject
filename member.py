import hashlib

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        hash_password = hashlib.sha256(self.password.encode())
        self.hex_dig = hash_password.hexdigest()

    def display(self):
        print(f'회원 이름: {self.name} 회원 아이디: {self.username}')


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f'게시글 제목: {self.title} 게시글 내용: {self.content}'

# 회원 생성
def create_member(Member):
    members = []
    while True:
        member = Member(*input('이름, 아이디, 비밀번호를 입력하시오: ').split())
        members.append(member)
        mem_add = input('회원을 추가하시겠습니까? (y/n): ').lower()
        if mem_add == 'y':
            continue
        elif mem_add == 'n':
            break
    return members

# 게시글 작성
def create_post(members):
    posts = []
    for member in members:
        member.display()

        while True:
            post = Post(*input('게시글 제목, 내용을 입력하시오: ').split(), author=member.username)
            posts.append(post)
            post_add = input('글을 더 작성하시겠습니까? (y/n): ').lower()
            if post_add == 'y':
                continue
            elif post_add == 'n':
                break
    return posts

# 특정 검색
def search_post(posts):
    while True:
        choice = int(input('작성자 검색은 1, 특정 단어 검색은 2, 종료하시려면 3을 눌러주세요: '))
        if choice == 1:
            parti_author = input('작성자의 아이디를 입력하시오: ')
            for post in posts:
                if post.author == parti_author:
                    print(post)
        elif choice == 2:
            find_content = input('검색할 내용을 입력하시오: ')
            for post in posts:
                if find_content in post.content:
                    print(post)
        elif choice == 3:
            break
        
# 메인 함수 실행
class Main():
    members = create_member(Member)
    posts = create_post(members)
    search_post(posts)