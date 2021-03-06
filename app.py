from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sgpa.html')

@app.route('/result', methods=['GET','POST'])
def home():
    a = int(request.form['a'])
    #b = int(request.form['b'])
    d = int(request.form['d'])
    #e = int(request.form['e'])
    g = int(request.form['g'])
    #h = int(request.form['h'])
    j = int(request.form['j'])
    #k = int(request.form['k'])
    m = int(request.form['m'])
    #n = int(request.form['n'])
    p = int(request.form['p'])
    #q = int(request.form['q'])
    s = int(request.form['s'])
    #t = int(request.form['t'])
    v = int(request.form['v'])
    #w = int(request.form['w'])
    #y = int(request.form['y'])
    #z = int(request.form['z'])

    # Subject 1
    if a>=90:
        c=10*4
        
    elif a>=80 and a<90:
        c=9*4

    elif a>=70 and a<80:
        c=8*4

    elif a>=60 and a<70:
        c=7*4

    elif a>=50 and a<60:
        c=6*4

    elif a>=45 and a<50:
        c=5*4

    elif a>=40 and a<45:
        c=4*4

    elif a<40:
        c=0*4

    # Subject 2
    if d>=90:
        f=10*4

    elif d>=80 and d<90:
        f=9*4

    elif d>=70 and d<80:
        f=8*4

    elif d>=60 and d<70:
        f=7*4

    elif d>=50 and d<60:
        f=6*4

    elif d>=45 and d<50:
        f=5*4

    elif d>=40 and d<45:
        f=4*4

    elif d<40:
        f=0*4

    # Subject 3
    if g>=90:
        i=10*4

    elif g>=80 and g<90:
        i=9*4

    elif g>=70 and g<80:
        i=8*4

    elif g>=60 and g<70:
        i=7*4

    elif g>=50 and g<60:
        i=6*4

    elif g>=45 and g<50:
        i=5*4

    elif g>=40 and g<45:
        i=4*4

    elif g<40:
        i=0*4

    # Subject 4
    if j>=90:
        l=10*3

    elif j>=80 and j<90:
        l=9*3

    elif j>=70 and j<80:
        l=8*3

    elif j>=60 and j<70:
        l=7*3

    elif j>=50 and j<60:
        l=6*3

    elif j>=45 and j<50:
        l=5*3

    elif j>=40 and j<45:
        l=4*3

    elif j<40:
        l=0*3

    # Subject 5
    if m>=90:
        o=10*3

    elif m>=80 and m<90:
        o=9*3

    elif m>=70 and m<80:
        o=8*3

    elif m>=60 and m<70:
        o=7*3

    elif m>=50 and m<60:
        o=6*3

    elif m>=45 and m<50:
        o=5*3

    elif m>=40 and m<45:
        o=4*3

    elif m<40:
        o=0*3

    # Subject 6
    if p>=90:
        r=10*2

    elif p>=80 and p<90:
        r=9*2

    elif p>=70 and p<80:
        r=8*2

    elif p>=60 and p<70:
        r=7*2

    elif p>=50 and p<60:
        r=6*2

    elif p>=45 and p<50:
        r=5*2

    elif p>=40 and p<45:
        r=4*2

    elif p<40:
        r=0*2

    # Subject 7
    if s>=90:
        u=10*2

    elif s>=80 and s<90:
        u=9*2

    elif s>=70 and s<80:
        u=8*2

    elif s>=60 and s<70:
        u=7*2

    elif s>=50 and s<60:
        u=6*2

    elif s>=45 and s<50:
        u=5*2

    elif s>=40 and s<45:
        u=4*2

    elif s<40:
        u=0*2

    #subject 8
    if v>=90:
        x=10*2

    elif v>=80 and v<90:
        x=9*2

    elif v>=70 and v<80:
        x=8*2

    elif v>=60 and v<70:
        x=7*2

    elif v>=50 and v<60:
        x=6*2

    elif v>=45 and v<50:
        x=5*2

    elif v>=40 and v<45:
        x=4*2

    elif v<40:
        x=0*2

    # subject 9
    """if y>=90:
        A=10*z

    elif z>=80 and z<90:
        A=9*y

    elif y>=70 and y<80:
        A=8*z

    elif y>=60 and y<70:
        A=7*z

    elif y>=50 and y<60:
        A=6*z

    elif y>=45 and y<50:
        A=5*z

    elif y>=40 and y<45:
        A=4*z

    elif y<40:
        A=0*z"""


    # Calculation

    #B=float((c+f+i+l+o+r+u+x)/(4+4+4+3+3+2+2+2))
    B = (c+f+i+l+o+r+u+x)/(4+4+4+3+3+2+2+2)
    B = round(B,4)

    return render_template('sgpa.html', data="SGPA : {}".format(B))


if __name__ == "__main__":
    app.run(debug=True)
