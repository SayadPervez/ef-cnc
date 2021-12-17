import os
import cairo
from numpy import pi, sqrt,cos,sin
from numpy.core.arrayprint import _object_format

def svgResize2Drawing(path):
    if("./" in path):
        pass
    else:
        if("/" in path):
            p = path[:path.rindex("/")+1]
            path = path[path.rindex("/")+1:]
        else:
            pass
    os.system(f'inkscape --batch-process --actions="FitCanvasToDrawing;export-filename:{path};export-do;" {path}')

def svgRotate(path,angle,outputFileName = "new"):
    if("./" in path):
        pass
    else:
        if("/" in path):
            p = path[:path.rindex("/")+1]
            path = path[path.rindex("/")+1:]
        else:
            pass
    os.system(f'inkscape --batch-process --actions="select-all:all;transform-rotate:{str(angle)};FitCanvasToDrawing;export-filename:{path};export-do;" {path}')

def createCanvas(width,height):
    width=mm2pt(width)
    height=mm2pt(height)
    with cairo.SVGSurface("canvas.svg", width,height) as surface:
        context = cairo.Context(surface)
        context.scale(700, 700)
        #context.stroke()


def Square(side,angle=0,name="Square"):
    side=mm2pt(side)
    filename=name+".svg"
    with cairo.SVGSurface(filename,side*2 ,side*2) as surface:
        cr = cairo.Context(surface)
        cr.rectangle(0,0,side,side)
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename)

def Rectangle(l,b,angle=0,name="Rectangle"):
    l=mm2pt(l)
    b=mm2pt(b)
    filename=name+".svg"
    with cairo.SVGSurface(filename,sqrt(l**2 + b**2) , sqrt(l**2+b**2)) as surface:
        cr = cairo.Context(surface)
        cr.rectangle(0,0,l,b)
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename) 

def Circle(radius,name="Circle"):
    radius=mm2pt(radius)
    filename=name+".svg"
    with cairo.SVGSurface(filename,2.5*radius , 2.5*radius) as surface:
        cr = cairo.Context(surface)
        theta1=0
        theta2=2*pi
        cr.arc(radius+2,radius+2,radius,theta1,theta2)
        cr.fill()
        svgResize2Drawing(filename) 

def Cone(radius,height,angle=0,name="Cone"):
    radius=mm2pt(radius)
    height=mm2pt(height)
    filename=name+".svg"
    l=sqrt(radius**2 + height**2)
    theta1=0
    theta2=(radius/l)*(2*pi)
    with cairo.SVGSurface(filename,2.5*l,2.5*l) as surface:
        cr = cairo.Context(surface)
        cr.move_to(l+2,l+2)
        cr.arc(l+2,l+2,l,theta1,theta2)
        cr.close_path()
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename)
def sector(radius,sector_angle,angle=0,name="Sector"):
    filename=name+".svg"
    l=mm2pt(radius)
    sector_angle=sector_angle*pi/180
    with cairo.SVGSurface(filename,2.5*l,2.5*l) as surface:
        cr = cairo.Context(surface)
        cr.move_to(l+2,l+2)
        cr.arc(l+2,l+2,l,0,sector_angle)
        cr.close_path()
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename)

def frustum(R,r,h,angle=0,name="Frustum"):
    filename=name+".svg"
    R=mm2pt(R)
    r=mm2pt(r)
    h=mm2pt(h)
    t=sqrt(h**2 + (R-r)**2)
    L=t*R/(R-r)
    theta=(R/L)*(2*pi)
    l=L-t
    with cairo.SVGSurface(filename,2.5*L,2.5*L) as surface:
        cr = cairo.Context(surface)
        X1,Y1=xy(L,0)
        X2,Y2=xy(L,theta/2)
        X3,Y3=xy(L,theta)
        x1,y1=xy(l,0)
        x2,y2=xy(l,theta/2)
        x3,y3=xy(l,theta)
        cr.curve_to(X1+L,Y1+L,X2+L,Y2+L,X3+L,Y3+L)
        cr.line_to(x3+L,y3+L)
        cr.curve_to(x3+L,y3+L,x2+L,y2+L,x1+L,y1+L)
        cr.line_to(X1+L,Y1+L)
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename)

def xy(r,theta):
    x=r*cos(theta)
    y=r*sin(theta)
    return x,y

def segment(R,r,segment_angle,angle=0,name="Segment"):
    filename=name+".svg"
    R=mm2pt(R)
    r=mm2pt(r)
    theta=segment_angle*pi/180
    with cairo.SVGSurface(filename,2.5*R,2.5*R) as surface:
        cr = cairo.Context(surface)
        X1,Y1=xy(R,0)
        X2,Y2=xy(R,theta/2)
        X3,Y3=xy(R,theta)
        x1,y1=xy(r,0)
        x2,y2=xy(r,theta/2)
        x3,y3=xy(r,theta)
        cr.curve_to(X1+R,Y1+R,X2+R,Y2+R,X3+R,Y3+R)
        cr.line_to(x3+R,y3+R)
        cr.curve_to(x3+R,y3+R,x2+R,y2+R,x1+R,y1+R)
        cr.line_to(X1+R,Y1+R)
        cr.fill()
        svgRotate(filename,angle,outputFileName=name)
        svgResize2Drawing(filename)


def mm2pt(x):
    return x*2.83465

def svg2dxf(source,destinationPath):
    os.system("inkscape --export-filename="+str(source) + " " +str(destinationPath))


def extract(file):
    s=0; 
    k=0; 
    with open(file, "r") as file:
        data = file.readlines()
    for i,line in enumerate(data):
        if(line.split()[0] =='<g'):
            s=i
            break
    for j,line in enumerate(data):
        if(line.split()[0]=='</g>'):
            k=j
    return data[s:k+1]

def canvas_extract(data):
    k=0; 
    for j,line in enumerate(data):
        if(line.split()[0]=='</g>'):
            k=j
    return k

def placeSVG(canvas,objectSVG,x,y):
    x=mm2pt(x)
    y=mm2pt(y)
    with open(canvas,"r") as a:
        can=a.readlines()
    if type(objectSVG)==type([]):
        objectSVG=objectSVG
    else:
        objectSVG=[objectSVG]
    for i,shapes in enumerate(objectSVG):
        s=extract(shapes)
        k=canvas_extract(can)
        s=s[1:len(s)-1]
        s.insert(0,'<g id="id'+"-"+ str(i)+'"' + ' transform="translate('+str(x)+','+str(y)+')">\n' )
        can[k:k]=s
    c=open(canvas,'w') 
    c.writelines(can)





        


    



