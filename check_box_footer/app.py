import os
from random import randint
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/', methods=['GET', 'POST'])
def main():
	# old_count = request.form.get('count', '')
	# print(old_count)
	old_count = 9
	# old_count = request.form.get("old_count","")
	# print(request.args.get('list'))
	elems = request.form.getlist('option')
	print(old_count)
	# count = randint(0, 10)

	count = int(old_count) + 1 if old_count else 0
	return render_template('index.html', count=count, elems=elems)

if __name__ == "__main__":
	app.run(debug=True)

