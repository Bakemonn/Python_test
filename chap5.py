import tkinter
import time

root = tkinter.Tk()
root.title("棒グラフをソートして表示する")

canvas = tkinter.Canvas(root, width = 640, height = 480)
canvas.create_rectangle(40, 40, 600, 440, fill = "gray78")
canvas.pack()

start_x = 60
start_y = 60
width_px = 5
height_px = 32
distance_px = 4

list = [70, 15, 66, 21, 19, 97, 33, 44, 30, 2]

for k in range(len(list) - 1, 0, -1):
    for j in range(0, k):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
        x = start_x
        y = start_y
        root.update()
        time.sleep(0.5)
        canvas.delete("graph")
        for i in list:
            canvas.create_rectangle(x, y, x + i * width_px, y + height_px, fill = "blue", outline = "blue", tag = "graph")
            y = y + height_px + distance_px

root.mainloop()
