from flask import Flask, render_template,request
import requests
import smtplib
my_email="t9940472@gmail.com"
password="vbqj xpse uvtk ncmm"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/db888bc550195cd97fa4").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['POST','GET'])
def contact():
    if request.method=='POST':
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="pratyush.snj@gmail.com",msg=f"Subject:Message\n\nName {request.form['username']}\nEmail {request.form['useremail']}\nMobile No. {request.form['usernumber']}\n Message {request.form['usermessage']}")
        return render_template("contact.html")
    return render_template("contact.html")
    

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
