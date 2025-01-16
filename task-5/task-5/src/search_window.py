from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PySide6.QtGui import QPixmap, QPalette, QBrush
from PySide6.QtCore import Qt
import requests


class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(850, 600) 
        self.setWindowTitle("Pokemon Search")

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.set_background_image("/home/pranav/amfoss-tasks/task-5/assets/landing.jpg")

        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter Pokémon Name")
        self.textbox.setGeometry(50, 50, 280, 40)

        label1 = QLabel("Enter the name of the Pokémon:", self)
        label1.setGeometry(50, 5, 600, 70)

        self.enter_button = QPushButton("Search", self)
        self.enter_button.setGeometry(50, 100, 160, 43)
        self.enter_button.clicked.connect(self.fetch_pokemon)

        self.capture_button = QPushButton("Capture", self)
        self.capture_button.setGeometry(50, 150, 160, 43)
        self.capture_button.clicked.connect(self.capture_pokemon)

        self.display_button = QPushButton("Display Captured", self)
        self.display_button.setGeometry(50, 200, 160, 43)
        self.display_button.clicked.connect(self.display_captured_pokemon)
        self.pokemon_image_label = QLabel(self)
        self.pokemon_image_label.setGeometry(400, 50, 200, 200)

        self.details_area = QWidget(self)
        self.details_area.setGeometry(400, 250, 400, 250)
        self.details_layout = QVBoxLayout(self.details_area)
        self.details_area.setLayout(self.details_layout)

        self.name_label = QLabel("Name: ", self.details_area)
        self.details_layout.addWidget(self.name_label)

        self.abilities_label = QLabel("Abilities: ", self.details_area)
        self.details_layout.addWidget(self.abilities_label)

        self.types_label = QLabel("Types: ", self.details_area)
        self.details_layout.addWidget(self.types_label)

        self.stats_label = QLabel("Stats: ", self.details_area)
        self.details_layout.addWidget(self.stats_label)

        self.capture_label = QLabel("Captured: ", self.details_area)
        self.details_layout.addWidget(self.capture_label)

        self.captured_pokemon = []

    def set_background_image(self, image_path):
        pixmap = QPixmap(image_path).scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)

    def fetch_pokemon(self):
        pokemon_name = self.textbox.text().lower()
        if pokemon_name:
            pokemon_info = self.get_pokemon_info(pokemon_name)
            if pokemon_info:
                self.display_pokemon_info(pokemon_info)
            else:
                self.name_label.setText(f"Failed to fetch data for {pokemon_name}. Please try again.")
        else:
            self.name_label.setText("Please enter a Pokémon name.")

    def get_pokemon_info(self, name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def display_pokemon_info(self, pokemon_info):
        self.name_label.setText(f"Name: {pokemon_info['name'].capitalize()}")
        abilities = ', '.join([ability['ability']['name'] for ability in pokemon_info['abilities']])
        self.abilities_label.setText(f"Abilities: {abilities}")
        types = ', '.join([t['type']['name'] for t in pokemon_info['types']])
        self.types_label.setText(f"Types: {types}")
        stats = '\n'.join([f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}" for stat in pokemon_info['stats']])
        self.stats_label.setText(f"Stats:\n{stats}")

        if 'sprites' in pokemon_info and pokemon_info['sprites']['front_default']:
            self.update_pokemon_image(pokemon_info['sprites']['front_default'])
        else:
            self.pokemon_image_label.setText("No image available.")

        self.current_pokemon_info = pokemon_info

    def update_pokemon_image(self, image_url):
    se = requests.get(image_url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.pokemon_image_label.setPixmap(pixmap)
            self.pokemon_image_label.setScaledContents(True)
        else:
            self.pokemon_image_label.setText("Failed to load image.")

    def capture_pokemon(self):
        if hasattr(self, 'current_pokemon_info'):
            self.captured_pokemon.append(self.current_pokemon_info)
            self.capture_label.setText(f"Captured: {self.current_pokemon_info['name'].capitalize()}")
        else:
            self.capture_label.setText("No Pokémon to capture. Please search first.")

    def display_captured_pokemon(self):
        if self.captured_pokemon:
            captured_names = "\n".join([pokemon['name'].capitalize() for pokemon in self.captured_pokemon])
            self.name_label.setText(f"Captured Pokémon:\n{captured_names}")
            self.abilities_label.setText("")
            self.types_label.setText("")
            self.stats_label.setText("")
            self.capture_label.setText("")
            self.pokemon_image_label.clear()
        else:
            self.name_label.setText("No Pokémon captured yet.")

            self.abilities_label.setText("")
            self.types_label.setText("")
            self.stats_label.setText("")
            self.capture_label.setText("")
            self.pokemon_image_label.clear() 


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
