# Устанавливаем в вертуальное окружение библиотеки из requirement.txt 
# вставляем в па

from rembg import remove
from PIL import Image
from pathlib import Path

def remove_bg():
    list_of_extensions = ['*.png','*.jpg'] # Разширение каторые нужны
    all_files = []                         # пустой список для последованостей

    for ext in list_of_extensions:
        all_files.extend(Path("F:\Python\Python_today\in_image").glob(ext)) # Путь к последованостям (файлам)
    print(all_files)

    for index ,item in enumerate(all_files):                # пробегаемся по списку путей index c enumerate для визуализации
        input_path = Path(item)                             # Получение пути файла
        file_name = input_path.stem                         # свойства stem возврашает имя файла с его пути
  
        output_path = f"F:\Python\Python_today\out_image\{file_name}_output.png"
            
        input_img = Image.open(input_path)     # открытие изоброжения через модул PIL
        output_img = remove(input_img)         # удаляем задный фон (begrund, bg) из модуля rembg
        output_img.save(output_path)           # сохронияем файл по  адресу

        print(f"Completed: {index+1}/{len(all_files)}")  

def main():
    remove_bg()

if __name__=="__main__":
    main()