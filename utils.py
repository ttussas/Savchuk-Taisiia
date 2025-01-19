import pandas as pd
import re

def clean_phone_number(phone):
    
    # очищаем номер телефона от всех символов, кроме цифр.
    if pd.isna(phone):  # проверка
        return ""
    # убираем все символы, кроме цифр
    return re.sub(r'\D', '', str(phone))


def process_phone_numbers(input_file, output_file):
   # обрабатывает номера телефонов в указанном файле и сохраняет результат в новый файл.
    try:
        # чтение файла 
        df = pd.read_excel(input_file)
        
        # проверка наличия колонки с телефонами
        if 'phone_number' not in df.columns:
            raise ValueError("Входной файл не содержит колонку с названием 'phone_number'")
        
        # Очистка номеров телефонов
        df['phone_number'] = df['phone_number'].apply(clean_phone_number)
        
        # Сохранение в новый файл
        df.to_excel(output_file, index=False)
        print(f"Обработанные данные сохранены в файл: {output_file}")
    except Exception as e:
        print(f"Ошибка обработки файла: {e}")
