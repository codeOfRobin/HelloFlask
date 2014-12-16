from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')




def multiply(num1=5,num2=5):
#     return """
#     <head>
# 	<title>Robin's Python server</title>
# </head>

# <body>
# 	<h1>{}</h1>
# </body>
#     """.format(str(num1*num2))
	return render_template("add.html",num1=num1, num2=num2)

app.run(debug=True,port=8000,host='0.0.0.0')
