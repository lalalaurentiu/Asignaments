from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from socketserver import ThreadingMixIn

HOST = '0.0.0.0'
PORT = 35780

names_dict = {'john':'smith',
            'david':'jones',
            'michael':'johnson',
            'chris':'lee'}
class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        data = '''<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body>
                        <h1>Chose a method</h1><br>
                        <a href="/do_get_from_client">GET Method</a><br>
                        <a href="/do_post_from_client">POST Method</a><br>
                        <a href="/do_delete_from_client">DELETE Method</a>
                    </body>
                    </html>'''
        self.log_message("Incoming GET request...")
        
        if self.path == '/': 
            self.send_response(200)
            self.end_headers()
            self.wfile.write(data.encode())
            self.wfile.write
        elif self.path[1:] == 'do_get_from_client':
            self.do_get_from_client()
        elif 'do_get_from_client?name' in self.path:
            self.parse_Data_Get()
        elif self.path[1:] == 'do_post_from_client':
            self.do_post_from_client()
        elif 'do_post_from_client?name' in self.path:
            self.do_POST()
        elif self.path[1:] == 'do_delete_from_client':
            self.do_delete_from_client()
        elif 'do_delete_from_client?name' in self.path:
            self.do_DELETE()
        else:
             self.send_response_to_client(404, '<h1>Page not found</h1>')

    def do_get_from_client(self):
        data = '''<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body>
                        <h1>Find name or last name from dictionary</h1>
                        <form action="">
                            <label for="name">First name or Last Name:</label>
                            <input type="text" id="name" name="name"><br><br>
                            <input type="submit" value="Submit">
                        </form>
                    </body>
                    </html>'''
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data.encode())

    def parse_Data_Get(self):
            try:
                name = parse_qs(self.path[20:])['name'][0]
            except:
                self.send_response_to_client(404, '<h1>Incorrect parameters provided</h1>')
                self.log_message("Incorrect parameters provided")
                return

            for key, value in names_dict.items():
                if name in names_dict.keys() or names_dict.values(): 
                    if key == name:
                        self.send_response_to_client(200, f'<h1>Name found, last name is {names_dict[key]}</h1>')
                        self.log_message("Name found")
                        break
                    elif value == name:
                        self.send_response_to_client(200, f'<h1>Last Name fond, name is {key}</h1> ')
                        self.log_message("Last Name")
                        break
            else:
                
                self.send_response_to_client(404, '<h1>Name not found</h1>')
                self.log_message("Name not found")

    def do_POST(self):
            
        self.log_message('Incoming POST request...')
        
        try:
            data = parse_qs(self.path[21:])
            names_dict[data['name'][0]] = data['last_name'][0]
            self.send_response_to_client(200, f'<h1>{names_dict}</h1>')
            
        except KeyError:
            self.send_response_to_client(404, '<h1>Incorrect parameters provided</h1>')
            self.log_message("Incorrect parameters provided")


    def do_post_from_client(self):
        data = '''<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body>
                        <h1>Adding name and last name in dictionary</h1>
                        <form action="">
                            <label for="fname">First name:</label>
                            <input type="text" id="name" name="name"><br><br>
                            <label for="lname">Last name:</label>
                            <input type="text" id="lasl_name" name="last_name"><br><br>
                            <input type="submit" value="Submit">
                        </form>
                    </body>
                    </html>'''
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data.encode())

    def do_DELETE(self):
        self.log_message('Incoming DELETE request...')

        try:
            name = parse_qs(self.path[23:])['name'][0]  
        except KeyError:
            self.send_response_to_client(404, self.path[23:])
            self.log_message("Incorrect parameters provided")
            return
            
        for key, value in names_dict.items():
            if name in names_dict.keys() or names_dict.values(): 
                if key == name:
                    del names_dict[key]
                    self.send_response_to_client(200, f'<h1>Name found and deleted</h1> {names_dict}')
                    self.log_message("Name found and deleted")
                    
                    break
                elif value == name:
                    del names_dict[key]
                    self.send_response_to_client(200, f'<h1>Last Name found and deleted</h1> {names_dict}')
                    self.log_message("Last Name found and deleted")
                    
                    break
                else:
                    self.send_response_to_client(404, f'<h1>Name not found</h1> {names_dict}')
                    self.log_message("Name not found")
                    break

    def do_delete_from_client(self):
        data = '''<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body>
                        <h1>Delete name or last name from dictionary</h1>
                        <form action="">
                            <label for="name">First name or Last Name:</label>
                            <input type="text" id="name" name="name"><br><br>
                            <input type="submit" value="Submit">
                        </form>
                    </body>
                    </html>'''
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data.encode())

 
    def send_response_to_client(self, status_code, data):
    
        # Send OK status
        self.send_response(status_code)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
 
        # Send the response
        self.wfile.write(str(data).encode())
 

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):   
    pass

if __name__=='__main__':
    print('Starting httpd on port {}'.format(PORT))
    server = ThreadedHTTPServer((HOST,PORT), RequestHandler)
    server.serve_forever()