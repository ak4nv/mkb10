#
# Use `settings.py` file for all override default settings.
#


from app.core import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
