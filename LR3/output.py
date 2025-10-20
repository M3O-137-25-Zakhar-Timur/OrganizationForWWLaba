import random
import os
import sys
import re
import logging
from matplotlib import pyplot as plt
from matplotlib import animation
from LR3.data import Data
from LR3.algorithms import *

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename="lr3_log.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
    force=True
)

stype_dic = {'all': -1,
             'insertion-sort': 0, 'shell-sort': 1, 'selection-sort': 2,
             'merge-sort': 3, 'quick-sort': 4, 'heap-sort': 5,
             'bubble-sort': 6, 'comb-sort': 7, 'monkey-sort': 8}
titles = [r'Insertion Sort ($O(n^2)$)', r'Shell Sort ($O(n \cdot log_2(n)^2)$)', r'Selection Sort ($O(n^2)$)',
          r'Merge Sort ($O(n \cdot log_2(n))$)', r'Quick Sort ($O(n \cdot log_2(n))$)',
          r'Heap Sort ($O(n \cdot log_2(n))$)',
          r'Bubble Sort ($O(n^2)$)', r'Comb Sort ($O(n \cdot log_2(n))$)', r'Monkey Sort ($O(n!)$)', ]
funs = [insertion_sort, shell_sort, selection_sort,
        merge_sort, quick_sort, heap_sort,
        bubble_sort, comb_sort, monkey_sort]


def create_original_data(dtype):
    data = []
    if dtype == 'random':
        # Генерируем случайные числа от 0 до 100
        data = [random.randint(0, 100) for _ in range(Data.data_count)]
    elif dtype == 'reversed':
        data = list(range(Data.data_count, 0, -1))
    elif dtype == 'few-unique':
        d = Data.data_count // 4
        for i in range(0, d):
            data.append(d)
        for i in range(d, d * 2):
            data.append(d * 2)
        for i in range(d * 2, d * 3):
            data.append(d * 3)
        for i in range(d * 3, Data.data_count):
            data.append(Data.data_count)
        random.shuffle(data)
    elif dtype == 'almost-sorted':
        data = list(range(1, Data.data_count + 1))
        a = random.randint(0, Data.data_count - 1)
        b = random.randint(0, Data.data_count - 1)
        while a == b:
            b = random.randint(0, Data.data_count - 1)
        data[a], data[b] = data[b], data[a]

    logging.info(f"Created {dtype} data with {Data.data_count} elements: {data}")
    return data


def draw_chart(stype, original_data, frame_interval):
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Data(d) for d in original_data]
    axs = fig.add_subplot(111)
    axs.set_xticks([])
    axs.set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)

    logging.info(f"Starting {titles[stype]} animation")
    frames = funs[stype](data_set)
    frame_count = len(frames)
    logging.info(f'{re.findall(r"\w+ Sort", titles[stype])[0]}: {frame_count} frames.')
    print('%s: %d frames.' % (re.findall(r'\w+ Sort', titles[stype])[0], frame_count))

    def animate(fi):
        bars = []
        if (len(frames) > fi):
            axs.cla()
            axs.set_title(titles[stype])
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(Data.data_count)),
                            [d.value for d in frames[fi]],
                            1,
                            color=[d.color for d in frames[fi]]
                            ).get_children()
        return bars

    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=frame_interval)
    logging.info(f"Animation created for {titles[stype]} with {frame_count} frames")
    return plt, anim


def draw_all_charts(original_data, frame_interval):
    axs = []
    frames = []
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Data(d) for d in original_data]
    for i in range(9):
        axs.append(fig.add_subplot(331 + i))
        axs[-1].set_xticks([])
        axs[-1].set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)

    logging.info("Starting all sorting algorithms animation")
    for i in range(8):
        frames.append(funs[i](data_set))
    frames.append(funs[8](data_set, max(len(f) for f in frames) + 50))

    names = []
    max_name_length = 0
    frame_counts = []
    max_frame_length = 0
    for i in range(9):
        names.append(re.findall(r'\w+ Sort', titles[i])[0] + ':')
        if len(names[-1]) > max_name_length:
            max_name_length = len(names[-1])
        frame_counts.append(len(frames[i]))
        if len(str(frame_counts[-1])) > max_frame_length:
            max_frame_length = len(str(frame_counts[-1]))

    # Логируем информацию о фреймах
    for i in range(9):
        log_message = '%-*s %*d frames' % (max_name_length, names[i], max_frame_length, frame_counts[i])
        logging.info(log_message)
        print(log_message)

    def animate(fi):
        bars = []
        for i in range(9):
            if (len(frames[i]) > fi):
                axs[i].cla()
                axs[i].set_title(titles[i])
                axs[i].set_xticks([])
                axs[i].set_yticks([])
                bars += axs[i].bar(list(range(Data.data_count)),
                                   [d.value for d in frames[i][fi]],
                                   1,
                                   color=[d.color for d in frames[i][fi]]
                                   ).get_children()
        return bars

    max_frame = max(len(f) for f in frames)
    anim = animation.FuncAnimation(fig, animate, frames=max_frame, interval=frame_interval)
    logging.info(f"All animations created with maximum {max_frame} frames")
    return plt, anim


def auto_start():
    """Автоматический запуск с настройками по умолчанию"""
    # Устанавливаем размер 30 элементов
    Data.data_count = 30

    # Создаем случайные данные от 0 до 100
    original_data = [random.randint(0, 100) for _ in range(Data.data_count)]

    logging.info(f"Auto-start: Generated {Data.data_count} random numbers from 0 to 100: {original_data}")
    print(f"Автоматический запуск: сгенерирован список из {Data.data_count} элементов от 0 до 100")
    print(f"Список: {original_data}")

    # Запускаем визуализацию всех алгоритмов
    frame_interval = 100  # интервал по умолчанию
    plt, anim = draw_all_charts(original_data, frame_interval)

    print("Запуск визуализации... Закройте окно для завершения.")
    plt.show()


if __name__ == "__main__":
    # Если нет аргументов командной строки - автоматический запуск
    if len(sys.argv) == 1:
        auto_start()
    else:
        # Оригинальная логика для ручного управления
        Data.data_count = 30  # Устанавливаем 30 по умолчанию

        logging.info(f"Program started with data count: {Data.data_count}")

        stype = -1
        if len(sys.argv) > 2:
            if sys.argv[2] in stype_dic:
                stype = stype_dic[sys.argv[2]]
            else:
                error_msg = 'Error: Wrong argument!'
                logging.error(error_msg)
                print(error_msg)
                exit()
        stype_str = list(stype_dic.keys())[list(stype_dic.values()).index(stype)]

        dtype = 'random'
        if len(sys.argv) > 3:
            dtype = sys.argv[3]
            if dtype not in ('random', 'reversed', 'few-unique', 'almost-sorted'):
                error_msg = 'Error: Wrong argument!'
                logging.error(error_msg)
                print(error_msg)
                exit()

        logging.info(f"Running {stype_str} with data type: {dtype}")
        od = create_original_data(dtype)

        if sys.argv[1] == 'play':
            try:
                fi = int(input('Please set the frame interval(100): '))
            except:
                fi = 100
            logging.info(f"Playing animation with frame interval: {fi}")
            plt, _ = draw_all_charts(od, fi) if stype == -1 else draw_chart(stype, od, fi)
            plt.show()
            logging.info("Animation playback completed")
        elif sys.argv[1] == 'save-mp4':
            default_fn = stype_str + '-' + dtype + '-animation'
            fn = input('Please input a filename(%s): ' % default_fn)
            if fn == '':
                fn = default_fn
            try:
                fps = int(input('Please set the fps(25): '))
            except:
                fps = 25

            logging.info(f"Saving MP4 animation: {fn}.mp4 with fps: {fps}")
            _, anim = draw_all_charts(od, 100) if stype == -1 else draw_chart(stype, od, 100)
            print('Please wait...')
            anim.save(fn + '.mp4', writer=animation.FFMpegWriter(fps=fps, extra_args=['-vcodec', 'libx264']))
            success_msg = f'The file has been successfully saved in {os.path.abspath(fn + ".mp4")}'
            logging.info(success_msg)
            print(success_msg)
        elif sys.argv[1] == 'save-html':
            default_fn = stype_str + '-' + dtype + '-animation'
            fn = input('Please input a filename(%s): ' % default_fn)
            if fn == '':
                fn = default_fn
            try:
                fps = int(input('Please set the fps(25): '))
            except:
                fps = 25

            logging.info(f"Saving HTML animation: {fn}.html with fps: {fps}")
            _, anim = draw_all_charts(od, 100) if stype == -1 else draw_chart(stype, od, 100)
            print('Please wait...')
            anim.save(fn + '.html', writer=animation.HTMLWriter(fps=fps))
            success_msg = f'The file has been successfully saved in {os.path.abspath(fn + ".html")}'
            logging.info(success_msg)
            print(success_msg)

    logging.info("Program finished")