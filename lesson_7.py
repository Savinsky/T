# -*- coding: utf-8 -*-

#from docxtpl import InlineImage
#from docx.shared import Cm
from docxtpl import DocxTemplate
#def get_context(brand, model, consumption, cost):
#    return {
#        'brand': brand,
#        'model': model,
#        'consumption': consumption,
#        'cost': cost
#    }
#def from_template():#brand, model, consumption, cost):
#    template = DocxTemplate("my_doc.docx")
#    context = get_context()#brand, model, consumption, cost)
#    template.render(context)
#    template.save("generated.docx")

doc = DocxTemplate("my_doc.docx")
context = { 'brand': 'brand',
            'model': 'model',
            'consumption': 'consumption',
            'cost': 'cost'

            }
doc.render(context)
doc.save("generated.docx")
#def generate_report(brand, model, consumption, cost, template):
#    template = 'report.docx'
#    document = from_template(brand, model, consumption, cost, template)
