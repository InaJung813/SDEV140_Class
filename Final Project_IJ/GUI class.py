from breezypythongui import EasyFrame  # breezypythongui에서 EasyFrame 클래스를 임포트
import tkinter as tk  # tkinter 모듈을 tk로 임포트

class MainFrame(EasyFrame):  # EasyFrame을 상속받는 MainFrame 클래스 정의
    
    def __init__(self):
        EasyFrame.__init__(self, title="Game", height=500, width=500)  # MainFrame의 생성자, 창의 제목, 높이, 너비 설정
        self.round_w = 0  # 라운드 승리 카운트를 위한 변수
        self.round_1 = 0  # 라운드 패배 카운트를 위한 변수
        
        self.addButton(text="Round Won", row=1, column=0, command=self.round_won)  # "Round Won" 버튼 추가
        self.addButton(text="Round Lost", row=1, column=1, command=self.round_lost)  # "Round Lost" 버튼 추가
        
    def round_won(self):
        pass  # 라운드 승리시 수행할 동작
    def round_lost(self):
        pass  # 라운드 패배시 수행할 동작

class Match(EasyFrame):  # EasyFrame을 상속받는 Match 클래스 정의
    def __init__(self):
        EasyFrame.__init__(self, title="Game", height=500, width=500)  # Match의 생성자, 창의 제목, 높이, 너비, 배경색 설정
        self.config(bg="green")
        self.round_w = 0  # 라운드 승리 카운트를 위한 변수
        self.round_1 = 0  # 라운드 패배 카운트를 위한 변수
        

def start_match():
    global match_window
    match_window = Match()  # Match 인스턴스 생성
    match_window.grid(row=0, column=0, sticky ="NSEW")  # Match 창 배치
    finish_btn = tk.Button(match_window, text="Finish Match", command=finish_match)  # "Finish Match" 버튼 추가
    finish_btn.grid(row=0, column=0)  # 버튼 배치


def edit_match():
    global edit_window
    edit_window = Match()  # Match 인스턴스 생성
    edit_window.grid(row=0, column=0, sticky ="NSEW")  # Match 창 배치
    finish_btn = tk.Button(edit_window, text="Finish Match", command=finish_match2)  # "Finish Match" 버튼 추가
    finish_btn.grid(row=0, column=0)  # 버튼 배치

    
def finish_match():
    match_window.grid_forget()  # "Finish Match" 버튼 클릭시 Match 창 숨기기

def finish_match2():
    edit_window.grid_forget()



def Main() :
    
    root = tk.Tk()  # tkinter의 메인 창 생성
    main_window = MainFrame()  # MainFrame 인스턴스 생성 및 그리드 시스템을 통한 배치
    main_window.grid(row=0, column=0)

    match_window = None  # Match 인스턴스를 저장할 전역 변수 초기화

    # 메인 창에 "Start Match" 버튼 추가 및 start_match 함수 연결
    start_btn = tk.Button(main_window, text="Start Match", command=start_match)
    start_btn.grid(row=0, column=0)
    
    edit_window = None

    edit_btn = tk.Button(main_window, text="Edit Match", command=edit_match)
    edit_btn.grid(row=2, column=2)
    
    

    root.mainloop()  # 이벤트 루프 시작, 창 활성 상태 유지

if __name__ == "__main__" :
    Main()
    
