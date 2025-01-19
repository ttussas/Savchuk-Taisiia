from utils import process_phone_numbers

def main():
    # задаём входной и выходной файлы
    input_file = 'phone_numbers.xlsx'  # имя входного файла
    output_file = 'phone_numbers_cleared.xlsx'  # имя выходного файла
    
    # запускаем обработку
    process_phone_numbers(input_file, output_file)

if name == '__main__':
    main()
