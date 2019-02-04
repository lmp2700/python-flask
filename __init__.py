from flask import Flask, render_template, request, flash, url_for, redirect, logging
from wtforms import Form, StringField, validators
from flask_mysqldb import MySQL
from address import Address
from usps import USPSApi, AddressValidate
import requests

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Indigo37*'
app.config['MYSQL_DB'] = 'addresses'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

app.debug = True

### ROUTES START HERE ###
@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/addressbook/')
def addressBook():
    cur = mysql.connection.cursor()
    results = cur.execute("SELECT * from addresses")
    addresses = cur.fetchall()
    return render_template('addressbook.html', addresses = addresses)
    cur.close()

class NewAddress(Form):
    surname = StringField('Surname', [validators.Length(min = 1, max = 100)])
    address_1 = StringField('Address_1', [validators.Length(min = 4, max = 200)])
    address_2 = StringField('Address_2', [validators.Length(min = 4, max = 200)])
    city = StringField('City', [validators.Length(min = 3, max = 50)])
    state = StringField('State', [validators.Length(min = 2, max = 25)])
    zipcode = StringField('Zipcode', [validators.Length(min = 3, max = 10)])

@app.route('/newaddress/', methods=['GET', 'POST'])
def newAddress():
    form = NewAddress(request.form)
    if request.method == 'POST' and form.validate():
        surname = form.surname.data
        address_1 = form.address_1.data
        address_2 = form.address_2.data
        city = form.city.data
        state = form.state.data
        zipcode = form.zipcode.data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO addresses(surname, address_1, address_2, city, state, zipcode) VALUES(%s, %s, %s, %s, %s, %s, %s)", (id, surname, address_1, address_2, city, state, zipcode))
        mysql.connection.commit()
        cur.close()
        flash('Address added', 'success')
        return redirect(url_for('addressBook'))
    return render_template('newaddress.html', form = form)

class ZipCodeSearch(Form):
    name = StringField('Name', [validators.Length(max = 100)])
    address_1 = StringField('Address_1', [validators.Length(min = 4, max = 200)])
    address_2 = StringField('Address_2', [validators.Length(min = 4, max = 200)])
    city = StringField('City', [validators.Length(min = 3, max = 50)])
    state = StringField('State', [validators.Length(max = 25)])
    zipcode = StringField('Zipcode', [validators.Length(max = 10)])

@app.route('/search/', methods=['GET', 'POST'])
def search():
    form = ZipCodeSearch(request.form)
    if request.method == 'POST' and form.validate():
        address = Address(
            name = form.name.data,
            address_1 = form.address_1.data,
            address_2 = form.address_2.data,
            city = form.city.data,
            state = form.state.data,
            zipcode = form.zipcode.data
        )
        usps = USPSApi('646STUDE1062', test=True)
        validation = usps.validate_address(address)
        # flash('Address is %s, %s, %s, %s, %s, %s', 'success')
        flash(validation.result, 'success')
        return redirect(url_for('newaddress'))
    return render_template('search.html', form = form)

@app.route('/deleteAddress/<int:id>', methods=['POST'])
def deleteAddress(id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM addresses WHERE id = %s', [id])
        mysql.connection.commit()
        cur.close()
        flash('Address removed', 'success')
        return redirect(url_for('addressBook'))

if __name__ == '__main__':
    app.secret_key = "girl_scout_cookies_are_back_in_stock"
    app.run()