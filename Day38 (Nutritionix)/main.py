import requests
from datetime import datetime


#Your personal data. Used by Nutritionix to calculate calories.
GENDER= "male"
WEIGHT_KG= 64
HEIGHT_CM= 178
AGE= 22
#Nutritionix app-id and api-key


APP_ID= "6f34b0e2 for example"
API_KEY= "34c216998c9ffa201a90fa8d993c961e for example "
sheet_endpoint= "https://api.sheety.co/e0396226528caedbf2700dbcf56591c8/workoutTracking/workouts for example "

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise for example "

exercise_text = input("Tell me which exercises you did: ")

#Nutritionix api call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result}")

#adding date and time
today_date= datetime.now().strftime("%d/%m/%Y")
time= datetime.now().strftime("%X")

#Sheety project API. check your Google sheet name
GOOGLE_SHEET_NAME= "workout"

for exercise in result["exercises"]:
    sheet_inputs= {
        "workout" :{
            "date": today_date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    sheet_response= requests.post(sheet_endpoint,
                                  json=sheet_inputs,
                                  auth=(
                                      "umer-fareed",
                                      "09876543"
                                  ))
    print(sheet_response.text)