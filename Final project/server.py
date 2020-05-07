import http.server
import http.client
import socketserver
import termcolor
import json
from pathlib import Path
from Seq1 import Seq
seq_get = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",]


# -- Function to obtain the ID of the human specie
def gene_seq(gene):
    connection = http.client.HTTPConnection(HOSTNAME)
    ENDPOINT1 = '/xrefs/symbol/human/'
    PARAMETERS1 = gene + PARAMETERS

    try:
        connection.request("GET", ENDPOINT1 + PARAMETERS1)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = connection.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode()

    # -- Create a variable with the data,
    # -- form the JSON received
    info = json.loads(data1)[0]
    gene_id = info["id"]
    return gene_id


 # -- Function to obtain the sequence of a given specie ID
def get_seq(gene_id):
    connection = http.client.HTTPConnection(HOSTNAME)
    ENDPOINT1 = "/sequence/id/"
    PARAMETERS2 = gene_id + PARAMETERS

    try:
        connection.request("GET", ENDPOINT1 + PARAMETERS2)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

     # -- Read the response message from the server
    r1 = connection.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode()

    # -- Create a variable with the data,
    # -- form the JSON received
    seq = json.loads(data1)["seq"]
    return seq


# Server´s port
PORT = 8080
HOSTNAME = "rest.ensembl.org"
PARAMETERS = '?content-type=application/json'
conn = http.client.HTTPConnection(HOSTNAME)

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # User line
        user_line = self.requestline.split(" ")

        # Take the symbol / out of the path
        path = user_line[1]

        # Read the text
        u_text = path.split('?')

        # Read the first thing of the text
        header = u_text[0]

        # Open the form1.html file
        # Read the index from the file

        if header == "/":
            # Read the index from the file open
            contents = Path('Index.html').read_text()
            error_code = 200


        elif header == "/listSpecies":
            try:
                ENDPOINT = "/info/species/"
                counter = 0
                pairs = self.path.find("=")
                limit = self.path[pairs + 1:]  # --> Conseguir el limite

                try:
                    conn.request("GET", ENDPOINT + PARAMETERS)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the species data from the JSON received
                info = json.loads(data1)["species"]
                count = 0
                for i in info:
                    name = i["display_name"]
                    count += 1

                contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> List of Species </title >
                            </head >
                            <body style="background-color: PALEVIOLETRED;">
                            <font face="calibri" size="5" color="black">The total length is: {count}
                             <br>
                             The limit you have selected is : {limit} 
                             <br>
                             The names of the species are: </font>
                            <font size="4" 
                             
                            </body>
                            </html>
                            """


                if limit == "" or "limit=" not in self.path:
                    for i in info:
                        name = i["display_name"]
                        contents += f"<i><li>{name}</li></i>"
                    contents += f"""<br><br><br><a href="/">Main page</a>"""

                else:
                    while counter < int(limit):
                        counter += 1
                        names = info[counter]["display_name"]
                        contents += f"<i><li>{names}</li>"
                    contents += f"""<br><br><br><a href="/">Main page</a>"""


                error_code = 200
            except ValueError:
                contents = Path('Error.html').read_text()
                error_code = 404

            except IndexError:
                contents = Path('Error.html').read_text()
                error_code = 404

            except KeyError:
                contents = Path("Error.html").read_text()
                error_code = 404

        elif header == "/karyotype":
            try:
                ENDPOINT = "/info/assembly/"
                pair = self.path.find("=")
                specie = self.path[pair + 1:]
                for a in specie:
                    if a == "+":
                        specie = specie.replace("+", "_")
                PARAMS = specie + PARAMETERS
                try:
                    conn.request("GET", ENDPOINT + PARAMS)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the data,
                # -- form the JSON received
                info = json.loads(data1)["karyotype"]
                # Html code
                contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> Karyotype </title >
                        </head >
                        <body style="background-color:lavender ;">
                        <font face="calibri" size="5" color="black">The names of the chromosomes are:
                        </font>
                        
                        
                        </body>
                        </html>
                        """
                for chrom in info:
                    contents += f"<p> {chrom} </p>"
                contents += f"""<br><br><br><a href="/">Main page</a>"""
                error_code = 200
            except KeyError:
                contents = Path('Error.html').read_text()
                error_code = 404

        elif header == "/chromosomeLength":
            try:
                ENDPOINT = '/info/assembly/'
                separate = self.path.split('&')  # Separate the specie from the chromosome
                pairs = separate[0].find('=')
                pairs2 = separate[1].find('=')
                specie = separate[0][pairs+1:]
                chromo = separate[1][pairs2+1:]
                for a in specie:
                    if a == "+":
                        specie = specie.replace("+", "_")
                PARAMETERS2 = specie + "/" + chromo + PARAMETERS



                try:
                    conn.request("GET", ENDPOINT + PARAMETERS2)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the data,
                # -- form the JSON received
                info = json.loads(data1)



                # Html code
                contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> Chromosome Length </title >
                            </head >
                            <body style="background-color:lavender ;">
                            <font face="calibri" size="5" color="black">
                            </font>
                            <font face = "calibri" size="5">

                            
                            </body>
                            </html>
                            """
                for k,v in info.items():
                    if k=="length":
                        length =str(v)
                        contents +=  f"""<i> The length of the chromosome is: {length} </i> <br><br><br><a href="/">Main page</a>"""

                    elif f"{r1.status} {r1.reason}" == "400 Bad Request":
                        contents = Path("Error.html").read_text()

                    elif f"{r1.status} {r1.reason}" == "404 Not Found":
                        contents = Path('Error.html').read_text()
                error_code = 200

            except ValueError:
                contents = Path("Error.html").read_text()
                error_code = 404


        elif header == "/geneSeq":


            try:
                pairs = self.path.find("=")
                genes = self.path[pairs + 1:]
                if "&" in genes:
                    pair = genes.split("&")
                    gene = pair[0]
                else:
                    gene = genes
                gene1 = gene_seq(gene)
                sequence = get_seq(gene1)
                PARAMETERS1 = gene1 + PARAMETERS

                # Html code
                contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> Gene sequence </title >
                            </head >
                            <body style="background-color:lavender ;">
                            <font face="calibri" size="5" color="black">
                            </font>
                            <font face = "calibri" size="5">


                            </body>
                            </html>
                             """
                error_code = 200



                contents += f"""<p> The sequence of {gene} gene is: </p><p>{sequence} </p><br><br><br><a href="/">Main page</a>"""


            except IndexError:
                contents = Path("Error.html").read_text()
                error_code = 404

            except KeyError:
                contents = Path("Error.html").read_text()
                error_code = 404

            except ValueError:
                contents = Path("Error.html").read_text()
                error_code = 404




        elif header == "/geneInfo":
            try:
                ENDPOINT = '/lookup/id/'
                pairs = self.path.find('=')
                genes = self.path[pairs + 1:]

                if '&' in genes:  # (When json=1 appears)
                    argument = genes.split('&')
                    gene = argument[0]  # Take just the name of the gene

                else:
                    gene = genes
                gene1 = gene_seq(gene)
                sequence = get_seq(gene1)
                PARAMETERS2 = gene1 + PARAMETERS

                try:
                    conn.request("GET", ENDPOINT + PARAMETERS2)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the species data from the JSON received
                info = json.loads(data1)
                seq = Seq(sequence)
                contents = f"""
                            <!DOCTYPE html>
                            <html lang = "en">
                            <head>
                            <meta charset = "utf-8" >
                              <title> Gene sequence </title >
                            </head >
                            <body style="background-color:PALEGREEN;">
                            <font face="calibri" size="5" color="black">
                            </font>
                            <font face = "calibri" size="5">


                            </body>
                            </html>
                             """


                if f"{r1.status} {r1.reason}" == "200 OK":
                    contents += f"""<h3>Information about the {gene} gene:</h3>
                                 <p>Starting point: {info['start']}</p>
                                 <p>Ending point: {info['end']}</p>
                                <p>The length of the gene's sequence is: {seq.len()}</p>
                                <p>The ID of the gene is: {info['id']}</p>
                                <p>This gene is located in the chromosome: {info['seq_region_name']}</p>
                                <br><br><br><a href="/">Main page</a>
                                """

                error_code = 200


            except IndexError:
                contents = Path("Error.html").read_text()
                error_code = 404

            except KeyError:
                contents = Path("Error.html").read_text()
                error_code = 404

            except ValueError:
                contents = Path("Error.html").read_text()
                error_code = 404


        elif header == "/geneCalc":
            try:
                pairs = self.path.find('=')
                genes = self.path[pairs + 1:]

                if '&' in genes:  # (When json=1 appears)
                    argument = genes.split('&')
                    gene = argument[0]  # Take just the name of the gene

                else:
                    gene = genes
                gene1 = gene_seq(gene)
                sequence = get_seq(gene1)
                seq = Seq(sequence)
                PARAMETERS2 = gene1 + PARAMETERS
                bases = ['A', 'C', 'T', 'G']


                contents = f"""
                         <!DOCTYPE html>
                         <html lang = "en">
                         <head>
                         <meta charset = "utf-8" >
                         <title> Gene calculations </title >
                         </head >
                         <body style="background-color:ROSYBROWN;">
                         
                         <font face = "calibri" size="5">
                         <h3>Calculations on human gene</h3>
                         <p>The length of the {gene} gene is: {seq.len()}</p>

                          </body>
                          </html>
                           """
                error_code = 200

                for base in bases:
                    perc_base = round(seq.count_base(base) * 100/seq.len(),2)
                    contents += f"""<p>{base}: {seq.count_base(base)} ({perc_base}%) </p>"""
                contents += f"""<br><br><br><a href="/">Main page</a></body></html>"""

            except IndexError:
                contents = Path("Error.html").read_text()
                error_code = 404
            except KeyError:
                contents = Path("Error.html").read_text()
                error_code = 404

            except ValueError:
                contents = Path("Error.html").read_text()
                error_code = 404


        elif header == "/geneList":
            try:
                ENDPOINT = "overlap/region/human/"
                pairs = self.path.split("&")   #Separate chromosome from the rest
                arg = pairs[0].find("=")
                chromo = pairs[0][arg + 1:]   #Name of the chromosome
                arg2 = pairs[1].find("=")
                start = pairs[1][arg2 +1:]    #Starting point
                arg3 = pairs[2].find("=")
                end = pairs[2][arg3+ 1:]      #Ending point
                PARAMETERS1 = "?feature=gene;content-type=application/json"
                PARAMETERS2 = ENDPOINT + chromo + ":" + start + "-" + end + PARAMETERS1

                try:
                    conn.request("GET", PARAMETERS2)

                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()

                # -- Read the response message from the server
                r1 = conn.getresponse()

                # -- Print the status line
                print(f"Response received!: {r1.status} {r1.reason}\n")

                # -- Read the response's body
                data1 = r1.read().decode()

                # -- Create a variable with the species data from the JSON received
                info = json.loads(data1)

                contents = f"""
                         <!DOCTYPE html>
                         <html lang = "en">
                         <head>
                         <meta charset = "utf-8" >
                         <title> Gene List</title >
                         </head >
                        <body style="background-color:HONEYDEW;">

                         <font face = "calibri" size="5">
                         <h3>Genes located in the {chromo} chromosome</h3>
                         <h4>From {start} to {end}</h4>
                     
                         </body>
                         </html>
                         """
                error_code = 200

                for i in info:
                    contents += f"""<li>{i["external_name"]}</li>"""
                contents += f"""<br><br><br><a href="/">Main page</a></body></html>"""

            except IndexError:
                contents = Path("Error.html").read_text()
                error_code = 404
            except KeyError:
                contents = Path("Error.html").read_text()
                error_code = 404

            except ValueError:
                contents = Path("Error.html").read_text()
                error_code = 404
































        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

    # ------------------------
    # - Server MAIN program
    # ------------------------
    # -- Set the new handler


Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()