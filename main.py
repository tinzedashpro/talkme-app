# -- main.py --
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def vigenere_encrypt(text, key):
    key = key.upper()
    result = ""
    j = 0
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            k = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(char) - offset + k) % 26 + offset)
            j += 1
        else:
            result += char
    return result


def vigenere_decrypt(text, key):
    key = key.upper()
    result = ""
    j = 0
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            k = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(char) - offset - k + 26) % 26 + offset)
            j += 1
        else:
            result += char
    return result


class VigenereTab(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.encryption_layout = BoxLayout(orientation='vertical')
        self.enc_input = TextInput(hint_text="Enter text to encrypt")
        self.enc_key = TextInput(hint_text="Enter key")
        self.enc_button = Button(text="Encrypt")
        self.enc_result = Label(text="Encrypted text here")
        self.enc_button.bind(on_press=self.encrypt)

        self.encryption_layout.add_widget(self.enc_input)
        self.encryption_layout.add_widget(self.enc_key)
        self.encryption_layout.add_widget(self.enc_button)
        self.encryption_layout.add_widget(self.enc_result)
        self.add_widget(self.create_tab("Encrypt", self.encryption_layout))

        self.decryption_layout = BoxLayout(orientation='vertical')
        self.dec_input = TextInput(hint_text="Enter text to decrypt")
        self.dec_key = TextInput(hint_text="Enter key")
        self.dec_button = Button(text="Decrypt")
        self.dec_result = Label(text="Decrypted text here")
        self.dec_button.bind(on_press=self.decrypt)

        self.decryption_layout.add_widget(self.dec_input)
        self.decryption_layout.add_widget(self.dec_key)
        self.decryption_layout.add_widget(self.dec_button)
        self.decryption_layout.add_widget(self.dec_result)
        self.add_widget(self.create_tab("Decrypt", self.decryption_layout))

    def create_tab(self, title, layout):
        from kivy.uix.tabbedpanel import TabbedPanelItem
        tab = TabbedPanelItem(text=title)
        tab.add_widget(layout)
        return tab

    def encrypt(self, instance):
        self.enc_result.text = vigenere_encrypt(self.enc_input.text, self.enc_key.text)

    def decrypt(self, instance):
        self.dec_result.text = vigenere_decrypt(self.dec_input.text, self.dec_key.text)


class TalkMeApp(App):
    def build(self):
        return VigenereTab()


if __name__ == "__main__":
    TalkMeApp().run()
