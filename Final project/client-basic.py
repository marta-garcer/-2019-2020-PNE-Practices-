import http.client

SERVER = "localhost"
PORT= 8080
endpoints = ["/", "/listSpecies", "/listSpecies?limit=10", "/listSpecies?limit=fish" , "/listSpecies?limit=", "/listSpecies?limit=56789","/karyotype", "/karyotype?specie=mouse", "/karyotype?specie=","/karyotype?specie=coronavirus","/karyotype?specie=homo+sapiens","/chromosomeLength?specie=mouse&chromo=18", "/chromosomeLength?specie=homo+sapiens&chromo=1",
             "/chromosomeLength?specie=mouse&chromo=sndd", "/chromosomeLength?specie=fishes&chromo=1"]

counter = 0

for ENDPOINT in endpoints:
    counter += 1
    URL = SERVER + ENDPOINT

    print()
    print('* TEST', counter,':\n')
    print('* INPUT: ')
    print(URL, '\n')
    print('* OUTPUT: ')

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER, PORT)

    # -- Send the request message, using the GET method.
    try:
        conn.request("GET", ENDPOINT)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    data1 = r1.read().decode("utf-8")
    print(data1, '\n')