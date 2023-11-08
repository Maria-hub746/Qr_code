from path import Path
from main import gen_qr_code


text = "https://www.linkedin.com/in/mariia-volochniuk/"
path_to_download = pictures/img.png #Path().joinpath("pictures", "img.png")  # Путь до фона qr кода
path_to_save = qr_codes/img.png #Path().joinpath("qr_codes", "img.png")  # Куда сохранять результат и под каким именем (обязательно в png)

gen_qr_code(text, path_to_download, path_to_save)