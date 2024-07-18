from django.test import SimpleTestCase
from django.template import Template, Context
from datetime import datetime
from l2l.templatetags.l2l_extras import l2l_dt


# Create your tests here.

class TemplateTagsTests(SimpleTestCase):

  def test_l2l_dt_with_datetime_object(self):
    template = Template("{% load l2l_extras %}{{ value|l2l_dt }}")
    context = Context({"value": datetime(2024, 7, 18, 21, 25)})
    rendered = template.render(context)
    self.assertEqual(rendered, "2024-07-18 21:25:00")

  def test_l2l_dt_with_string_format(self):
    template = Template("{% load l2l_extras %}{{ value|l2l_dt }}")
    context = Context({"value": "2024-07-18T21:25:00"})
    rendered = template.render(context)
    self.assertEqual(rendered, "2024-07-18 21:25:00")

  def test_l2l_dt_with_invalid_string(self):
    template = Template("{% load l2l_extras %}{{ value|l2l_dt }}")
    context = Context({"value": "Invalid Date String"})
    rendered = template.render(context)
    self.assertEqual(rendered, "Invalid Date String")

  def test_l2l_dt_with_non_date(self):
    template = Template("{% load l2l_extras %}{{ value|l2l_dt }}")
    context = Context({"value": 1234567890})
    rendered = template.render(context)
    self.assertEqual(rendered, "1234567890")


