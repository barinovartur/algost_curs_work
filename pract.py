import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Функция для чтения данных из указанного файла
def load_dataset(file_path):
    return pd.read_csv(file_path, sep=", ", header=None, engine='python',
                       names=['method', 'scenario', 'array_size', 'time'])


# Функция для создания графиков времени выполнения поиска
def visualize_search_performance(dataset):
    unique_methods = dataset['method'].unique()

    for method in unique_methods:
        method_data = dataset[dataset['method'] == method]
        generate_plots_for_method(method_data, method)


# Генерация графиков для каждого метода поиска
def generate_plots_for_method(data, method):
    cases = {'Лучший': data[data['scenario'] == 'Лучший'],
             'Средний': data[data['scenario'] == 'Средний'],
             'Худший': data[data['scenario'] == 'Худший']}

    plt.figure(figsize=(10, 6))

    # Построение графиков с учетом регрессии для каждой ситуации
    for case_name, case_data in cases.items():
        if not case_data.empty:
            x_values = case_data['array_size']
            y_values = case_data['time']

            # Настройка степени регрессии
            if method == 'Линейный поиск' and case_name in ['Средний', 'Худший']:
                poly_degree = 1  # Линейная регрессия
            elif method == 'Интерполяционный поиск' and case_name == 'Средний':
                poly_degree = 1  # Линейная регрессия для среднего случая
            else:
                poly_degree = 2  # Квадратичная регрессия

            regression_coeffs = np.polyfit(x_values, y_values, poly_degree)
            regression_poly = np.poly1d(regression_coeffs)

            # Вывод уравнения регрессии в консоль
            print(f'{method} ({case_name}) - Уравнение регрессии:')
            print(f'  {regression_poly}')

            # Построение точек данных
            plt.plot(x_values, y_values, label=case_name)

            # Добавление линии регрессии
            x_fit = np.linspace(x_values.min(), x_values.max(), 100)
            y_fit = regression_poly(x_fit)
            plt.plot(x_fit, y_fit, linestyle='--', label=f'{case_name} - регрессия')

            # Сохранение параметров регрессии в файл
            with open(f'{method}_regression_details.txt', 'a') as file:
                file.write(f'{case_name} регрессия: {regression_poly}\n')

    plt.title(f'График времени выполнения: {method}')
    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время (сек)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{method}_plot.png')
    plt.show()


def main():
    # Задайте путь к вашему входному файлу
    file_path = 'C:/Users/Comp/Desktop/DATA.txt'

    # Загрузка данных
    dataset = load_dataset(file_path)

    # Визуализация времени выполнения поиска
    visualize_search_performance(dataset)


if __name__ == "__main__":
    main()
