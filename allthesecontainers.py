import random
import subprocess


class ATC:
    def __init__(self):
        pass

    def get_password(self):
        return f"{random.randint(0000, 9999):04d}"

    def get_container_name(self):
        name_choices = "abcdefghijklmnopqrstuvwxyz"
        container_name = ""

        for i in range(0, 10):
            container_name += random.choice(name_choices)

        return container_name + ".hc"

    def get_random_size(self):
        size = str(random.randint(1, 10))
        return size + "M"

    def create_veracrypt_image(self):
        """
        Creates a VeraCrypt hard drive image.

        Args:
            image_path (str): Full path of the image file to be created.
            size (str): Size of the image, e.g., "200M" for 200 megabytes.
            password (str): Password for the encrypted image.
        """
        image_path = self.get_container_name()
        size = self.get_random_size()
        password = self.get_password()

        command = [
            "c:\\Program Files\\VeraCrypt\\VeraCrypt Format.exe",
            "/create",  # Create volume
            image_path,
            "/size", size,
            "/password", password,
            "/hash", "sha512",  # Example, you can choose the desired hash
            "/encryption", "AES",  # Example, choose your encryption algorithm
            "/filesystem", "EXFAT",  # Example, choose your filesystem
            "/silent"
        ]

        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print("VeraCrypt image created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating image: {e.stderr}")


atc = ATC()
for i in range(0, 100):
    atc.create_veracrypt_image()
