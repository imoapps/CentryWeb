import sys,sqlite3
from bottle import route, run,template,get,post,request
""" License@ MIT:
Copyright (c) 2012, Marcel Hellkamp.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE."""

mytable = """<table>
<tr>
<th>French styled Doors </th>
<th>Windows </th>
</tr>
<tr>
<td>900, 2080</td>
<td>1200 , 1000</td>
</tr>
<tr>
<td>850, 2080</td>
<td>600 , 600</td>
</tr>

</table>"""

@route('/myip')
def show_ip():
    ip= request.environ.get('REMOTE_ADDR')
    return "your IP is : {}".format(ip)
    

@route('/login') # or @route
def login():
    return'''
                    <form action ="/login" method="post">
                            Username: <input name="username" type="text" />
                            Password: <input  name="password"  type="password" />
                            <input value="Login" type="submit" />
                    </form>
                    '''
@route('/login', method='POST') ## or @route('/login' method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p> Login failed.</p>"


@route('/incomming')
def incomming():
    conn = sqlite3.connect("J:\incomming.db")
    cursor = conn.execute("SELECT ID, DATE, AGENT, REFERENCE_No,\
                           AMOUNT FROM Incomming_Transactions")
    data = cursor.fetchall()
    output = template('incomming_Transactions',  rows = data)
    return output
#nano  incomming_Transactions.tpl
@route('/help')
def get_help():
    out = template('help')
    return out
    

@route('/projects')
def projects():
    return   '<h1>Centry Projects base!</h1>',mytable

@route('/workers')
def workers():
    return '<h1> Centry Workers</h1>'

run(host ='0.0.0.0', port = 8080)

