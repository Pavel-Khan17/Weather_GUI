from PyQt5 import QtWidgets
from weather_gui import Ui_MainWindow
import requests

class MainWin(QtWidgets.QMainWindow):
  
  def __init__(self):
    super(MainWin, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.submitButton.clicked.connect(self.submit_location)
    self.show()
  
  
  def fetch_weather(self, location):
    api_key = 'a1ee49ea3c3fb6c222714c37786f87c7'  # Replace 'API_KEY' with your API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    try:
      response = requests.get(url)
      data = response.json()
      if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        QtWidgets.QMessageBox.information(None, "Weather Information",
                                          f"Location : {location}\n" 
                                          f"Weather: {weather_description}\n"
                                          f"Temperature: {temperature}°C\n"
                                          f"Humidity: {humidity}%\n"
                                          f"Wind Speed: {wind_speed} m/s")
      else:
        QtWidgets.QMessageBox.critical(None, "Error", "Unable to fetch weather data.")
    except Exception as e:
      QtWidgets.QMessageBox.critical(None, "Error", str(e))
    self.ui.locationInput.setEnabled(True)
    self.ui.submitButton.setEnabled(True)
  
  
  def submit_location(self):
    location = self.ui.locationInput.text().strip()
    if location:
      self.ui.locationInput.clear()
      self.ui.locationInput.setEnabled(False)
      self.ui.submitButton.setEnabled(False)
      loading_popup = QtWidgets.QMessageBox(None)
      loading_popup.setWindowTitle("Loading...")
      loading_popup.setText("Loading...")
      loading_popup.show()
      
      self.fetch_weather(location)



if __name__ == '__main__':
  import sys
  app = QtWidgets.QApplication(sys.argv)
  obj = MainWin()
  sys.exit(app.exec_())