from flask import Flask

# application factory
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello Pybo~!'

    @app.route('/hello')
    def hello():
        return 'hello page입니다!'

    # blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app