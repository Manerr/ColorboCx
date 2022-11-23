#Run app with Ctrl+R
#Lance l'app avec Ctrl+R


from ti_draw import *
from ti_system import get_key,disp_clr,readST,writeST,get_mouse
from sys import exit
w=1
try:
 rgb=readST("rgb")
except:
 rgb=[255,188,88]
 writeST("rgb",str(rgb))
 rgb="[[255,188,88],]"

rgb=[int(i) for i in eval(rgb)[0]]
#its because the variable return a list of da list

first=1
line=0
h=1
while w:
  g=get_key(-1)
  if g:
    if g=="esc":w=0
    elif g=="up":line-=1
    elif g=="down":line+=1
    elif g=="left":rgb[line]-=8
    elif g=="right":rgb[line]+=8
    elif g=="-":rgb[line]-=1
    elif g=="+":rgb[line]+=1
    elif g=="(":rgb[line]=0
    elif g==")":rgb[line]=255
    elif g=="doc":h=not h
    elif g=="center":
      ms=get_mouse()
      x,y=ms
      if x<60:x=60
      if x>163:x=163
      if x>=60 and x<=163:
        c=0
        if y>=23 and y<=27:
          line=0;c=1
        if y>=55 and y<=59:
          line=1;c=1
        if y>=87 and y<=91:
          line=2;c=1
        if c:rgb[line]=int(((x-63)/100)*255)
    if line==3:line=0
    if line==-1:line=2
    if rgb[line]<0:rgb[line]=0
    if rgb[line]>255:rgb[line]=255
  if g or first:
    use_buffer()
    first=0
    clear()
    set_color(242,242,232)
    fill_rect(0,0,320,240)
    
    set_color(255,255,255)   
    fill_rect(198,12,108,108)
    fill_rect(12,12,168,98)
    fill_rect(198,144,108,40)
    if h:fill_rect(12,128,168,72)
    set_color(*rgb)
    set_pen(2,0)
    draw_rect(208,22,88,88)
    fill_rect(208,22,88,88)
    
    for i in range(200,-100,-100):
     set_color(i,i+20,i+10)
     set_pen(i//100,0)
     draw_rect(198,12,108,108)
     draw_rect(12,12,168,98)
     if h:draw_rect(12,128,168,72)
     draw_rect(198,144,108,40)
     for j in range(3):
      set_color(int(i*0.5)+100,int(i*0.5)+100,int(i*0.5)+100)
      draw_line(60,25+j*32,163,25+j*32)
      set_color(10,148,224)
      plot_xy(60+(rgb[j]/255)*103,25+j*32,10)
      if j==line:
       set_color(10,255,184)
       plot_xy(60+(rgb[j]/255)*103,25+j*32,8)
      clr=[0,]*3
      clr[j]=rgb[j]
      set_color(tuple(clr))
      draw_text(50+(rgb[j]/255)*103,45+j*32,rgb[j])
    set_color(10,25,25)
    draw_text(27,32,"Red")
    draw_text(22,64,"Green")
    draw_text(25,96,"Blue")
    if h:
      draw_text(20,144,"◆ doc▾  : display help")
      draw_text(20,158,"◆ ↕  : change value to set")
      draw_text(20,172,"◆ ↔  : change value")
      draw_text(20,186,"◆ ( )  : extremum values")
      draw_text(20,200,"◆ + -  : more precise set")
    draw_text(222,202,"esc to quit")
    string=""
    for i in rgb:
      l=str(hex(i))
      if len(l)==3:l="0x0"+l[-1]
      string+=l[2:]
      print("\b"*3)
    draw_text(225,172,string.upper())
    string_size("tiny")
    paint_buffer()
disp_clr()
writeST("rgb",str(rgb))
exit(-1)
