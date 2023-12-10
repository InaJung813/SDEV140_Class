import tkinter as tk
from breezypythongui import EasyFrame as ef
from tkinter import PhotoImage
from JungInaFinalProject import MoneyClipApp

class Create_plan(MoneyClipApp):
            
    def __init__(self):
        self.projects = []

    def add_new_plan(self, project_name, budget, start_date, end_date):
        project_info = {
            "project_name": project_name,
            "budget": budget,
            "start_date": start_date,
            "end_date": end_date
        }
        self.projects.append(project_info)

    def print_projects(self):
        for project in self.projects:
            print(f"Project Name: {project['project_name']}, Budget: {project['budget']}, Start Date: {project['start_date']}, End Date: {project['end_date']}")

    
 # 사용 예시
plan = Create_plan()
plan.add_new_plan("Project A", 10000, "2023-01-01", "2023-12-31")
plan.add_new_plan("Project B", 20000, "2023-02-01", "2023-11-30")

plan.print_projects()
            
            
            
"""            
            
            
          
    def __init__(self):
        ef.__init__(self, title="Money Clip", width=800, height=880)
        root = tk.Tk()
        background_image = PhotoImage(file='image/budget_back.png')
        background_label = tk.Label(root, image=background_image)
        background_label.place(relwidth=1, relheight=1)  # Cover the entire window

        creat_plan_label = tk.Label(root, text="Make Your Plan", font=("Arial", 40), fg="#385492", bg="#7FE7FE")
        creat_plan_label.place(x= 350, y=10) 
        
        new_plan_button = ef.addButton(text="Creat New Plan", row=1, column=0, command=self.new_plan)
        chang_plan_button = ef.addButton(text="Creat New Plan", row=1, column=1, command=self.change_plan)
        

    
    def change_plan(self):
        pass




    


def create_project():
    # 사용자로부터 각 정보를 입력받음
    plan_name = input("Plan Name: ")
    total_budget = float(input("Total Budget amount (소숫점 두자리 소수): "))
    
    # 날짜 형식의 입력을 받아 Date 객체로 변환
    try:
        start_date = datetime.strptime(input("Starting Date (MM/DD/YY): "), "%m/%d/%y").date()
        end_date = datetime.strptime(input("Ending Date (MM/DD/YY): "), "%m/%d/%y").date()
    except ValueError:
        print("날짜 형식이 잘못되었습니다. MM/DD/YY 형식으로 입력해주세요.")
        return
    
    # 정보를 프로젝트 리스트에 저장
    project_infor = [plan_name, total_budget, start_date, end_date]
    
    return project_info

# 프로젝트 정보를 입력받아 리스트에 저장
project_data = create_project()

# 결과 출력
if project_data:
    print("프로젝트 정보:", project_data)
else:
    print("프로젝트 정보를 올바르게 입력해주세요.")
"""

