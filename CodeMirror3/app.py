from flask import Flask, render_template, request
from flask import jsonify
from lxml import etree
from lxml import isoschematron
import os
import datetime


app = Flask(__name__)

def check_xml(xml_file,schema_file):

    xml = open(xml_file,'r')
    
    schema = open(schema_file,'r')

    parse_schema = etree.parse(schema)
    schematron = isoschematron.Schematron(parse_schema,store_report=True)

    parse_xml = etree.parse(xml)

    is_valid = schematron.validate(parse_xml)

    if is_valid:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_xml', methods=['POST'])
def process_xml():
    data = request.json
    data = data['msg']
    return data


@app.post("/edit_xml")
def edit_xml():
    data = request.json
    name = datetime.datetime.utcnow().timestamp()*1000000
    name = f'{name}.xml'
    xml_data = data['json']
    print(xml_data)
    f = open(name, "a")
    f.write(xml_data)
    f.close()

    valid = check_xml(name,'schema.sch')
    if valid :
        return {'valid':valid}
    else:
        os.remove(name)
        return {'valid':valid}



if __name__ == '__main__':
    app.run(debug=True)

