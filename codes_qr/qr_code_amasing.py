from path import Path
from main import gen_qr_code


text = "https://www.linkedin.com/in/mariia-volochniuk/"
path_to_download = Path().joinpath("pictures", "img.png")
path_to_save = Path().joinpath("qr_codes", "img.png")
gen_qr_code(text, path_to_download, path_to_save)