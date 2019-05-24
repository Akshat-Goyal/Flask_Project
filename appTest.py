from flask import request, jsonify
import requests
import pytest

c=0;

def test_form_exp1(var1,var2):

	files = {
		'option': (None,var1),
	}

	response = requests.post('http://127.0.0.1:5000/form-exp1', files=files)
	try :
		assert response.json()["message"] == var2
		print("Test passed")
	except AssertionError:
		print ("form_exp1 test failed")
		global c
		c=c+1


test_form_exp1("1","data fetched successfully!")
test_form_exp1("2","data fetched successfully!")
test_form_exp1("0","Unable to fetch data!")

print("Tests Failed = "+str(c))