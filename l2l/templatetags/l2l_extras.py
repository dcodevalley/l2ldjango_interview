# myapp/templatetags/l2l_extras.py
from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='l2l_dt')
def l2l_dt(value):
    """
    Custom template filter to convert datetime string format.
    Input format: "%Y-%m-%dT%H:%M:%S"
    Output format: "%Y-%m-%d %H:%M:%S"
    """

    try:
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")

        if isinstance(value, str):
            try:
                # Parsing with the "Month day, year, hour:minute am/pm" format
                datetime_obj = datetime.strptime(value, "%B %d, %Y, %I:%M %p")
            except ValueError:
                try:
                    # Parsing with the "%Y-%m-%dT%H:%M:%S" format
                    datetime_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                except ValueError:
                    return value

            return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(f"Error in l2l_dt filter: {e}")
        return value # Return the original value if an error occurs

    return value
