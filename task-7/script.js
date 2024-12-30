document.getElementById("get-weather").addEventListener("click", function () {
  const city = document.getElementById("city-input").value.trim();
  const apiKey = "d51846552b6570b9a4c3a90e10bd9670"; // Replace with your OpenWeatherMap API key
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  if (!city) {
    alert("Please enter a city name.");
    return;
  }

  fetch(url)
    .then(response => {
      if (!response.ok) {
        if (response.status === 404) throw new Error("City not found.");
        throw new Error("Unable to fetch weather data.");
      }
      return response.json();
    })
    .then(data => {
      document.getElementById("weather-result").classList.remove("hidden");
      document.getElementById("city-name").textContent = `Weather in ${data.name}, ${data.sys.country}`;
      document.getElementById("temperature").textContent = `Temperature: ${data.main.temp}°C`;
      document.getElementById("description").textContent = `Description: ${data.weather[0].description}`;
      document.getElementById("humidity").textContent = `Humidity: ${data.main.humidity}%`;
      document.getElementById("wind").textContent = `Wind Speed: ${data.wind.speed} m/s`;
    })
    .catch(error => {
      document.getElementById("weather-result").classList.add("hidden");
      alert(error.message);
    });
});
