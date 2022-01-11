from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from roommates_bill import room, reports
from random import randint
import time


app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BuildFormPage(MethodView):

    def get(self):
        bill_form = BuildForm()
        return render_template('bill_form_page.html',
                               bill_form=bill_form)

    def post(self):
        bill_form = BuildForm(request.form)

        the_bill = room.Bill(bill_form.service.data, float(bill_form.amount.data), bill_form.period.data)
        roommate1 = room.Roommate(bill_form.roommate1_name.data, int(bill_form.roommate1_days.data))
        roommate2 = room.Roommate(bill_form.roommate2_name.data, int(bill_form.roommate2_days.data))

        return render_template('bill_form_page.html',
                               result=True,
                               bill_form=bill_form,
                               name1=roommate1.name,
                               amount1=roommate1.pays(the_bill, roommate2),
                               name2=roommate2.name,
                               amount2=roommate2.pays(the_bill, roommate1))


# class ResultsPage(MethodView):
#
#     def post(self):
#         bill_form = BuildForm(request.form)
#
#         the_bill = room.Bill(bill_form.service.data, float(bill_form.amount.data), bill_form.period.data)
#         roommate1 = room.Roommate(bill_form.roommate1_name.data, int(bill_form.roommate1_days.data))
#         roommate2 = room.Roommate(bill_form.roommate2_name.data, int(bill_form.roommate2_days.data))
#
#         return render_template('results_page.html',
#                                name1=roommate1.name,
#                                amount1=roommate1.pays(the_bill, roommate2),
#                                name2=roommate2.name,
#                                amount2=roommate2.pays(the_bill, roommate1))


class BuildForm(Form):
    month = time.strftime("%B %Y")
    service = StringField(label="Bill: ", default='Electricity')
    amount = StringField(label="Bill Amount: ", default=randint(50, 200))
    period = StringField(label="Bill Period: ", default=month)
    roommate1_name = StringField(label="Your Name: ", default='John')
    roommate1_days = StringField(label="Days in the House: ", default=randint(15, 30))
    roommate2_name = StringField(label="Roommate's Name: ", default='Mary')
    roommate2_days = StringField(label="Days in the House: ", default=randint(15, 30))

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form',
                 view_func=BuildFormPage.as_view('build_form_page'))
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)
