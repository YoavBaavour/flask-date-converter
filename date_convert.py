import requests as re
from flask import Flask, render_template, request, redirect, flash, url_for
from form import DateForm         # import my form module

app = Flask(__name__)
app.config['SECRET_KEY'] = '295072870ea55e07d52889cbd8abb832'

# execute convert_date when entering this route
@app.route("/", methods=['GET', 'POST'])
def convert_date():
    message = ''
    # create instance of DateForm to send to the date-converting app
    form = DateForm(request.form)

    # check if filled form passes validations set to each field (input boxes\button)
    if form.validate_on_submit():
        # check if given date is a valid date
        is_valid_date = form.validate_date(form.day.data, form.month.data, form.year.data)
        message = '' if is_valid_date else 'invalid date.'

    if not message and request.method == 'POST':
        g2h = 1         # api flag gregorian-to-hebrew
        cfg = 'json'    # api flag to return data in json
        # url format for the date-converter API
        url = f"https://www.hebcal.com/converter?cfg={cfg}&gy={form.year.data}&gm={form.month.data}&gd={form.day.data}&g2h={g2h}"
        response = re.get(url)

        if response.status_code == 200:     # success
            res_json = response.json()
            message = f"{form.day.data}/{form.month.data}/{form.year.data}\n{res_json['hebrew']}"
        else:
            message = 'Oops, something went wrong!'
        flash(message)
        return redirect(url_for('convert_date'))
    # render HTML page from given template
    flash(message)
    return render_template('date_convert_website.html', form=form)


if __name__ == '__main__':
    app.run(debug='False')         # set debug='True' for auto-refresh when running the app from here









