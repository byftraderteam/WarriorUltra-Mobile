from kivy.app import App
from kivy.uix.button import Button

class WarriorApp(App):
    def build(self):
        return Button(
            text="TRADING ULTRA-AGGRESSIF", 
            size_hint=(0.8, 0.3),
            on_press=self.start_trading
        )
    
    def start_trading(self, _):
        print("Lancement de la stratégie...")

WarriorApp().run()
