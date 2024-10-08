from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import *
import csv


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
    

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
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
