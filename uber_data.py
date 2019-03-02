from flask import Flask
from flask import render_template
from uber_data_helper import getData

app = Flask(__name__)
@app.route('/')

def data():
	blood_test_data = [[34.2048, -118.2158, "btest"],[34.0547, -118.2653, "btest"], [34.0464, -118.2605, "btest"], [34.0633, -118.2387, "mammogram"], [34.0528, - 118.2640, "mammogram"], [34.1181, -118.1511, "mammogram"]]
	blood_test = ["USC Verdugo Hills Hospital", "Good Samaritan Hospital", " Keck Medicine – Downtown Los Angeles"]
	b_test_out = []

	for hospital in blood_test_data:
		b_test_out.append(getData(hospital[0], hospital[1], hospital[2]))
	

	
	return render_template("index.html", name=b_test_out)

if __name__ == "__main__":
	app.run()



