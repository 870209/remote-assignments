from flask import Flask,request,render_template,make_response
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, My Server!!'


@app.route('/data')
def data(number=0):
    number=request.args.get('number',number)
    if number==0:
        return "Lack of Parameter"
    elif number.isdigit():
        i=1
        total=0
        while i <= int(number):
            total+=i
            i+=1
        return render_template('sum.html',total=total)
    else:
        return "Wrong Parameter"


@app.route('/myName')
def get_cookies():
    cookies = request.cookies.get('userID')
    if cookies == None:
        return render_template('cookies.html')
    else:
        return cookies


@app.route('/trackName',methods = ['POST', 'GET'])
def setcookies():
        name= request.form['nm']
        resp = make_response(render_template('cookies.html'))
        resp.set_cookie('userID',name)
        return redirect(url_for('myName'))
    



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)
