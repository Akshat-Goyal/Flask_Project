import requests

BASE_URL = "http://127.0.0.1:5000"  #LOCAL HOST

def test_checkServer():
	timeout=5
	try:
		_= requests.get(BASE_URL, timeout=timeout)
		print("SERVER responding as expected!!")
		return True
	except requests.ConnectionError:
		print("Server Not Connected")
		return False


def test_link():
	links = ["/introduction","/theory","/objective","/experiment","/quizzes","/procedure","/readings"]

	for current in links:
		response = requests.get(BASE_URL + current)
		assert response.status_code == 200,current
		code = str(response.status_code)
		print(BASE_URL + current + " : ")
		print("status code=" + code + "; Link responding as expected!!")


print("All links are functional!!")
