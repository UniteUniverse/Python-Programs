from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response=requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    blog_title1=response.json()[0]["title"]
    blog_subtitle1=response.json()[0]["subtitle"]
    blog_body1=response.json()[0]["body"]
    blog_title2=response.json()[1]["title"]
    blog_subtitle2=response.json()[1]["subtitle"]
    blog_body2=response.json()[1]["body"]
    return render_template("index.html",blog_subtitle1=blog_subtitle1,
                           blog_body1=blog_body1, blog_title1=blog_title1,
                            blog_body2=blog_body2, blog_subtitle2=blog_subtitle2,
                             blog_title2=blog_title2 )

@app.route('/post/<int:num>')
def blog(num):
    response=requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    blog_title=response.json()[num-1]["title"]
    blog_subtitle=response.json()[num-1]["subtitle"]
    blog_body=response.json()[num-1]["body"]
    return render_template("post.html",blog_body=blog_body, blog_subtitle=blog_subtitle,blog_title=blog_title)
if __name__ == "__main__":
    app.run(debug=True)
