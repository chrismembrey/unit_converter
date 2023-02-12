
from flask import Flask, render_template, request
import requests


def create_app():
    app = Flask(__name__)


    @app.route("/chemistry", methods=["GET", "POST"])
    def chemistry():
        result = None
        if request.method == "POST":
            value = float(request.form.get("value"))
            conversion_type = request.form.get("conversion_type")
            if conversion_type == "molality_to_molarity":
                result = value * 1000
            elif conversion_type == "molarity_to_molality":
                result = value / 1000
            elif conversion_type == "avogadro_to_molecules":
                result = value * 6.022140857 * 10**23
            elif conversion_type == "molecules_to_avogadro":
                result = value / (6.022140857 * 10**23)
            elif conversion_type == "joules_to_calories":
                result = value / 4.184
            elif conversion_type == "calories_to_joules":
                result = value * 4.184
            elif conversion_type == "kelvin_to_celsius":
                result = value - 273.15
            elif conversion_type == "celsius_to_kelvin":
                result = value + 273.15
            elif conversion_type == "atm_to_pa":
                result = value * 101325
            elif conversion_type == "pa_to_atm":
                result = value / 101325
            elif conversion_type == "l_to_ml":
                result = value * 1000
            elif conversion_type == "ml_to_l":
                result = value / 1000
            elif conversion_type == "g_to_kg":
                result = value / 1000
            elif conversion_type == "kg_to_g":
                result = value * 1000
            elif conversion_type == "mph_to_kph":
                result = value * 1.609344
            elif conversion_type == "kph_to_mph":
                result = value / 1.609344
            elif conversion_type == "ft_to_m":
                result = value / 3.2808
            elif conversion_type == "m_to_ft":
                result = value * 3.2808
            elif conversion_type == "in_to_cm":
                result = value * 2.54
            elif conversion_type == "cm_to_in":
                result = value / 2.54
            elif conversion_type == "lb_to_kg":
                result = value * 0.453592


            result = round(result,2)

        return render_template("chemistry.html", result=result)



    @app.route("/physics", methods=["GET", "POST"])
    def physics():
        result = None
        if request.method == "POST":
            value = float(request.form.get("value"))
            conversion_type = request.form.get("conversion_type")
            if conversion_type == "joule_to_electron_volt":
                result = value / 1.602176634 * 10**-19
            elif conversion_type == "electron_volt_to_joule":
                result = value * 1.602176634 * 10**-19
            elif conversion_type == "meter_to_angstrom":
                result = value * 10**10
            elif conversion_type == "angstrom_to_meter":
                result = value / 10**10
            elif conversion_type == "hertz_to_wavenumber":
                result = value / 2.99792458 * 10**10
            elif conversion_type == "wavenumber_to_hertz":
                result = value * 2.99792458 * 10**10
            elif conversion_type == "newton_to_dyne":
                result = value * 10**5
            elif conversion_type == "dyne_to_newton":
                result = value / 10**5
            elif conversion_type == "pascal_to_bar":
                result = value / 10**5
            elif conversion_type == "bar_to_pascal":
                result = value * 10**5
            elif conversion_type == "meters_per_second_to_kilo_meters_per_hour":
                result = value * 3.6
            elif conversion_type == "kilo_meters_per_hour_to_meters_per_second":
                result = value / 3.6
            elif conversion_type == "coulombs_to_elementary_charge":
                result = value / 1.602176634 * 10**-19
            elif conversion_type == "elementary_charge_to_coulombs":
                result = value * 1.602176634 * 10**-19
            elif conversion_type == "joules_to_electron_volts":
                result = value / 1.602176634 * 10**-19
            elif conversion_type == "electron_volts_to_joules":
                result = value * 1.602176634 * 10**-19
            elif conversion_type == "meters_to_feet":
                result = value * 3.2808
            elif conversion_type == "feet_to_meters":
                result = value / 3.2808
            elif conversion_type == "meters_to_inches":
                result = value / 0.0254
            elif conversion_type == "inches_to_meters":
                result = value * 0.0254
            elif conversion_type == "kilograms_to_pounds":
                result = value * 2.20462

            result = result

        return render_template("physics.html", result=result)



    @app.route("/currency", methods=['GET', "POST"])
    def currency():
        if request.method == 'POST':
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']
            amount = float(request.form['amount'])

            response = requests.get("https://openexchangerates.org/api/latest.json?app_id=de928af235ca420a9c396aa8bdfb0a45")
            data = response.json()
            conversion_rate = data["rates"][to_currency] / data["rates"][from_currency]
            converted_amount = amount * conversion_rate

            return render_template('currency.html', converted_amount=converted_amount,
                                   to_currency=to_currency, amount=amount)

        return render_template('currency.html')


    @app.route("/", methods=['GET', "POST"])
    def home():
        return render_template('home.html')

    return app


