import random
import subprocess


def get_password() -> str:
    """Generates a random 4-digit numeric password.

    Returns:
        str: A 4-digit string representing the password.
    """
    return f"{random.randint(0000, 9999):04d}"


def get_container_name() -> str:
    """Generates a random container name ending in '.hc'.

    Returns:
        str: A 10-character random lowercase name with the '.hc' extension.
    """
    name_choices = "abcdefghijklmnopqrstuvwxyz"
    container_name = ""

    for i in range(0, 10):
        container_name += random.choice(name_choices)

    return container_name + ".hc"


def get_random_size() -> str:
    """Generates a random image size between 1M and 10M.

    Returns:
        str: Size with the 'M' suffix for megabytes (e.g., "7M").
    """
    size = str(random.randint(1, 10))
    return size + "M"


def create_veracrypt_image() -> None:
    """Creates a VeraCrypt hard drive image with a random name, size, and password.
    """
    image_path = get_container_name()
    size = get_random_size()
    password = get_password()

    command = [
        "c:\\Program Files\\VeraCrypt\\VeraCrypt Format.exe",
        "/create",
        image_path,
        "/size", size,
        "/password", password,
        "/hash", "sha512",
        "/encryption", "AES",
        "/filesystem", "EXFAT",
        "/silent"
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("VeraCrypt image created successfully.")
        with open("passwords.lst", "a") as file:
            file.write(password + '\n')
            file.close()

    except subprocess.CalledProcessError as e:
        print(f"Error creating image: {e.stderr}")


def main() -> None:
    """Creates 100 VeraCrypt images."""
    for i in range(0, 100):
        create_veracrypt_image()

    print(f"[+] Passwords saved to: password.lst")


if __name__ == "__main__":
    main()
