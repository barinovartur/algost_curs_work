from sympy import symbols, log
from sympy.plotting import plot

# Диапазон для n
start_range = 2
end_range = 50

n = symbols('n')

# Линейный поиск
linear_title = "Линейный поиск"
linear_worst = 2*n
linear_best = 1
linear_avg = n
linear_plot = plot(linear_worst, (n, start_range, end_range), show=False, label="Худший случай", xlabel="n", ylabel="T(n)", title=linear_title)
linear_plot2 = plot(linear_best, (n, start_range, end_range), show=False, label="Лучший случай")
linear_plot3 = plot(linear_avg, (n, start_range, end_range), show=False, label="Средний случай")
linear_plot.extend(linear_plot2)
linear_plot.extend(linear_plot3)
linear_plot.legend = True
linear_plot.show()

# Бинарный поиск
binary_title = "Бинарный поиск"
binary_worst = 20*log(n, 2)
binary_best = 1
binary_avg = 10*log(n, 2)
binary_plot = plot(binary_worst, (n, start_range, end_range), show=False, label="Худший случай", xlabel="n", ylabel="T(n)", title=binary_title)
binary_plot2 = plot(binary_best, (n, start_range, end_range), show=False, label="Лучший случай")
binary_plot3 = plot(binary_avg, (n, start_range, end_range), show=False, label="Средний случай")
binary_plot.extend(binary_plot2)
binary_plot.extend(binary_plot3)
binary_plot.legend = True
binary_plot.show()

# Экспоненциальный поиск
exp_title = "Экспоненциальный поиск"
exp_worst = 20*log(n, 2)
exp_best = 1
exp_avg = 10*log(n, 2)
exp_plot = plot(exp_worst, (n, start_range, end_range), show=False, label="Худший случай", xlabel="n", ylabel="T(n)", title=exp_title)
exp_plot2 = plot(exp_best, (n, start_range, end_range), show=False, label="Лучший случай")
exp_plot3 = plot(exp_avg, (n, start_range, end_range), show=False, label="Средний случай")
exp_plot.extend(exp_plot2)
exp_plot.extend(exp_plot3)
exp_plot.legend = True
exp_plot.show()

# Интерполяционный поиск
interp_title = "Интерполяционный поиск"
interp_worst = n
interp_best = 1
interp_avg = log(log(n, 2), 2)
interp_plot = plot(interp_worst, (n, start_range, end_range), show=False, label="Худший случай", xlabel="n", ylabel="T(n)", title=interp_title)
interp_plot2 = plot(interp_best, (n, start_range, end_range), show=False, label="Лучший случай")
interp_plot3 = plot(interp_avg, (n, start_range, end_range), show=False, label="Средний случай")
interp_plot.extend(interp_plot2)
interp_plot.extend(interp_plot3)
interp_plot.legend = True
interp_plot.show()
