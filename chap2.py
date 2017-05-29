#cording
import tkinter

root = tkinter.Tk()
root.title("リリーにしつもん！")
root.minsize(640,480)
root.option_add("*font", ["MS Pゴシック", 22])

#画像表示
canvas = tkinter.Canvas(bg = "black", width = 640, height = 480)
canvas.place(x = 0, y = 0)
img = tkinter.PhotoImage(file="img3/chap3-back.gif")
canvas.create_image(320, 240, image = img)

root.mainloop()
