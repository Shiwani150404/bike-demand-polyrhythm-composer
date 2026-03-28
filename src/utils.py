def predict_demand(model, hr, temp, hum, windspeed):
    data = [[hr, temp, hum, windspeed]]
    prediction = model.predict(data)
    return prediction[0]