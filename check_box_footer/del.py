import vincent as vi
from random import randint

def visualiter(count, step):
	# vincent.core.initialize_notebook()
	line = vi.Line([randint(0, 10) for i in range(count)])
	line.axis_titles(x='X-axis', y='Y-axis')
	line.to_json('static/example.json', html_out=True)

if __name__ == "__main__":
    visualiter(5, 1)


