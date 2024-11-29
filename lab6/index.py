from http.server import BaseHTTPRequestHandler, HTTPServer
import sqlite3
import urllib.parse
from importing import import_to_json, import_to_xml

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/favicon.ico':
            self.send_response(204)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')  # Указание кодировки UTF-8
        self.end_headers()

        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == "/":
            self.show_home_page()
        else:
            self.send_error(404)

    def show_home_page(self):
        conn = sqlite3.connect('med_db.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT PATIENT.name, PATIENT.surname, DOCTOR.name, DOCTOR.surname, APPOINTMENT.date
        FROM APPOINTMENT
        JOIN PATIENT ON PATIENT.id = APPOINTMENT.patient_id
        JOIN DOCTOR ON DOCTOR.id = APPOINTMENT.doctor_id
        """)

        rows = cursor.fetchall()
        conn.close()

        html = """
        <html>
        <head>
            <meta charset="UTF-8">  <!-- Указание кодировки UTF-8 в HTML -->
            <title>Приемы</title>
        </head>
        <body>
        <h2>Список приемов</h2>
        <table border="1">
        <tr><th>Пациент</th><th>Доктор</th><th>Дата</th></tr>
        """

        for row in rows:
            html += f"<tr><td>{row[0]} {row[1]}</td><td>{row[2]} {row[3]}</td><td>{row[4]}</td></tr>"

        html += """
        </table>

        <form action="/import_json" method="post">
            <button type="submit">Импортировать в JSON</button>
        </form>

        <form action="/import_xml" method="post">
            <button type="submit">Импортировать в XML</button>
        </form>

        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        if self.path == "/import_json":
            self.import_json()
        elif self.path == "/import_xml":
            self.import_xml()
        else:
            self.send_error(404)

    def import_json(self):
        try:
            import_to_json()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write("Данные успешно импортированы в формат JSON!")
        except Exception as e:
            self.send_error(500, f"Ошибка при импорте в JSON: {str(e)}")

    def import_xml(self):
        try:
            import_to_xml()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write("Данные успешно импортированы в формат XML!")
        except Exception as e:
            self.send_error(500, f"Ошибка при импорте в XML: {str(e)}")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
