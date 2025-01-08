import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

class ExcelGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Excel Data GUI")
        self.master.geometry("800x600")

        # 엑셀 파일 읽기
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        # excel_file_path = os.path.join(desktop_path, 'Ebeam Path.xlsx')
        # self.df = pd.read_excel(excel_file_path, sheet_name='Sheet1')
        excel_file_path = r'C:\cripto\Ebeam\Ebeam Path.xlsx'
        self.df = pd.read_excel(excel_file_path, sheet_name='Sheet1')
        self.filtered_df = self.df.copy()
        
        
        

        self.create_widgets()

    def create_widgets(self):
        # 리스트박스와 레이블 생성
        columns = ['회사', '공법', 'PartID', 'Ebeam', '계정', 'cd']
        self.listboxes = {}

        for i, col in enumerate(columns):
            label = tk.Label(self.master, text=col)
            label.grid(row=0, column=i, padx=5, pady=5)

            listbox = tk.Listbox(self.master, exportselection=False)
            listbox.grid(row=1, column=i, padx=5, pady=5)
            listbox.bind('<<ListboxSelect>>', lambda e, col=col: self.update_next_listbox(col))

            self.listboxes[col] = listbox

        # 초기 리스트박스 값 설정
        self.update_listbox('회사')

        # Path 출력 버튼
        self.path_button = tk.Button(self.master, text="Path 출력", command=self.show_path)
        self.path_button.grid(row=2, column=0, columnspan=6, pady=10)

        # Path 표시 텍스트박스
        self.path_text = tk.Text(self.master, height=3, width=80)
        self.path_text.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

    def update_listbox(self, column):
        listbox = self.listboxes[column]
        listbox.delete(0, tk.END)
        unique_values = self.filtered_df[column].unique()
        for value in unique_values:
            listbox.insert(tk.END, value)

    def update_next_listbox(self, column):
        columns = ['회사', '공법', 'PartID', 'Ebeam', '계정', 'cd']
        current_index = columns.index(column)
        self.filter_data(columns[:current_index+1])
        
        for next_column in columns[current_index+1:]:
            self.update_listbox(next_column)

    def filter_data(self, columns):
        self.filtered_df = self.df.copy()
        for col in columns:
            selected_indices = self.listboxes[col].curselection()
            if selected_indices:
                selected_value = self.listboxes[col].get(selected_indices[0])
                self.filtered_df = self.filtered_df[self.filtered_df[col] == selected_value]

    def show_path(self):
        self.filter_data(['회사', '공법', 'PartID', 'Ebeam', '계정', 'cd'])
        if not self.filtered_df.empty:
            path = self.filtered_df['Path'].values[0]
            self.path_text.delete('1.0', tk.END)
            self.path_text.insert(tk.END, path)
        else:
            self.path_text.delete('1.0', tk.END)
            self.path_text.insert(tk.END, "No path found for the selected criteria.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelGUI(root)
    root.mainloop()
