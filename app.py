from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
	return 'rvce.edu.in'
if __name__== '__main__':
 app.run(debug=True)

app.route('\rv')
def rvce():
	return 'rvitm rocks'
	app.add_url_rule('/','rvce',rvce)