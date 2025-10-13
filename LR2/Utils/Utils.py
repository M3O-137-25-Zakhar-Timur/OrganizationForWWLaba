def strike_through(text):
    return ''.join([char + '\u0336' for char in text])

def rus_len(text):
    """Подсчитывает длину строки с учетом кириллицы (2 символа на кириллицу)"""
    length = 0
    for char in text:
        # Кириллические символы занимают 2 позиции, латиница - 1
        if '\u0400' <= char <= '\u04FF' or char in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            length += 2
        else:
            length += 1
    return length

def pad_text(text, total_width):
    """Добавляет пробелы для выравнивания с учетом кириллицы"""
    current_length = rus_len(text)
    spaces_needed = total_width - current_length
    return text + ' ' * max(0, spaces_needed)


def create_progress_bar(current, maximum, is_mana=False):
    """Создает визуальный прогресс-бар с фиксированной шириной"""
    fill_cell = "■"
    empty_cell = "◻"

    if is_mana:
        fill_cell = "■"
        empty_cell = "◻"

    if maximum <= 0:
        return "∎∎∎∎∎"

    percentage = current / maximum
    bars_count = int(percentage * 10)  # 10 сегментов в баре

    # Создаем строку с заполненными и пустыми сегментами
    filled_bars = fill_cell * bars_count
    empty_bars = empty_cell * (10 - bars_count)

    return f"{filled_bars}{empty_bars} {current:.0f}/{maximum:.0f}"

