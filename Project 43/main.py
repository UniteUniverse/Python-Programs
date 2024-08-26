from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import *
import csv


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

coffee_ratings=['✘','☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️']
power_ratings=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌' ]
wifi_ratings=['✘', '💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪']
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', [InputRequired()])
    location = StringField('Location URL', [InputRequired(), URL(require_tld=False, message='Enter the valid URL.')])
    open = StringField('Open Time', [InputRequired()])
    close = StringField('Closing Time', [InputRequired()])
    coffee = SelectField('Coffee Rating',[InputRequired()], choices=[(int(i),coffee_ratings[i] ) for i in range(6)])
    wifi = SelectField('WiFi Rating',[InputRequired()], choices=[(int(i),wifi_ratings[i] ) for i in range(6)])
    power = SelectField('Power Rating',[InputRequired()], choices=[(int(i),power_ratings[i] ) for i in range(6)])
    submit = SubmitField('Submit')
    
# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
        with open('cafe-data.csv', 'a', encoding='utf-8') as file:
            file.write(f'\n{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},{coffee_ratings[int(form.coffee.data)]},{wifi_ratings[int(form.wifi.data)]},{power_ratings[int(form.power.data)]}')
            
    return render_template('add.html', form=form, )


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
