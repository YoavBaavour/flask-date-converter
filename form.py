from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

MIN_DAY, MAX_DAY = 1, 31
MIN_MONTH, MAX_MONTH = 1, 12
MONTH_30_DAYS = {4, 6, 9, 11}

# define the acceptable range of years
MIN_YEAR, MAX_YEAR = 1000, 9999


# a form that holds the given date
class DateForm(FlaskForm):
    # custom validator - check if given date is valid before submitting
    @staticmethod
    def validate_date(day, month, year):
        flag = False
        if day and month and year:
            # check if value range is valid:
            if not (MIN_DAY <= day <= MAX_DAY and
                    MIN_MONTH <= month <= MAX_MONTH and
                    MIN_YEAR <= year <= MAX_YEAR):
                flag = True

            # check if given dd/mm/yyyy is a valid date:
            leap = True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False

            if leap and day > 29 and month == 2:
                flag = True
            elif not leap and day > 28 and month == 2:
                flag = True
            elif month in MONTH_30_DAYS and day > 30:
                flag = True

            if flag:
                return False
            else:
                return True

    # day attribute that holds an integer
    day = IntegerField('dd', validators=[DataRequired()])

    # day attribute that holds an integer
    month = IntegerField('mm', validators=[DataRequired()])

    # day attribute that holds an integer
    year = IntegerField('yyyy', validators=[DataRequired()])

    # submit button
    submit = SubmitField('Convert')









