# browser_history.py
# 제목: 웹 브라우저 히스토리 기능 시뮬레이션 (스택 2개 활용)

class BrowserHistory:
    def __init__(self, homepage):
        # '뒤로 가기'를 위한 페이지들을 저장하는 스택
        self.back_stack = []
        # '앞으로 가기'를 위한 페이지들을 저장하는 스택
        self.forward_stack = []
        # 현재 보고 있는 페이지
        self.current_page = homepage
        print(f"브라우저 시작! 현재 페이지: {self.current_page}")

    def visit(self, url):
        """새로운 페이지를 방문합니다."""
        # 현재 페이지를 back_stack에 추가
        self.back_stack.append(self.current_page)
        # 현재 페이지를 새로운 url로 변경
        self.current_page = url
        # 새로운 페이지 방문 시, forward 기록은 모두 사라짐
        self.forward_stack.clear()
        print(f"방문: {self.current_page}")

    def back(self):
        """뒤로 가기 기능을 수행합니다."""
        if not self.back_stack:
            print("더 이상 뒤로 갈 페이지가 없습니다.")
            return
        
        # 현재 페이지를 forward_stack에 추가
        self.forward_stack.append(self.current_page)
        # back_stack에서 가장 최근 페이지를 꺼내 현재 페이지로 설정
        self.current_page = self.back_stack.pop()
        print(f"뒤로 가기 -> 현재 페이지: {self.current_page}")

    def forward(self):
        """앞으로 가기 기능을 수행합니다."""
        if not self.forward_stack:
            print("더 이상 앞으로 갈 페이지가 없습니다.")
            return
        
        # 현재 페이지를 back_stack에 추가
        self.back_stack.append(self.current_page)
        # forward_stack에서 페이지를 꺼내 현재 페이지로 설정
        self.current_page = self.forward_stack.pop()
        print(f"앞으로 가기 -> 현재 페이지: {self.current_page}")
        
# 시뮬레이션
browser = BrowserHistory("www.google.com")
browser.visit("www.naver.com")
browser.visit("www.youtube.com")

browser.back()      # youtube -> naver
browser.back()      # naver -> google
browser.back()      # 뒤로 갈 페이지 없음

browser.forward()   # google -> naver
browser.forward()   # naver -> youtube
browser.forward()   # 앞으로 갈 페이지 없음

browser.visit("www.github.com") # youtube에서 github 방문
browser.forward()   # 앞으로 갈 페이지 없음 (새 페이지 방문으로 기록 삭제됨)
browser.back()      # github -> youtube