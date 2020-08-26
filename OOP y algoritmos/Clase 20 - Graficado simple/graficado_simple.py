# Clase 20: **Graficado Simple.**

from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores quieres graficar?: '))
    x_vals = list(range(total_vals))
    y_vals = [int(input(f'Valor y para {x} ')) for x in x_vals]
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)  # No funciona en GoogleColab
