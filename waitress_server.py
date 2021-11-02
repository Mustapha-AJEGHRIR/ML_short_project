from waitress import serve
import app


serve(app.app, host='51.178.17.141', port=80)