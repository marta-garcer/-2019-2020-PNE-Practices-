import http.client

SERVER = "localhost"
PORT= 8080
endpoints = ["/geneSeq", "/geneSeq?gene=FRAT1", "/geneSeq?gene=TP53" , "/geneSeq?gene=", "/geneSeq?gene=hello","/geneInfo", "/geneInfo?gene=FRAT1", "/geneInfo?gene=TP53","/geneInfo?gene=","/geneInfo?gene=","/geneInfo?gene=hi", "/geneCalc",
             "/geneCalc?gene=FRAT1", "/geneCalc?gene=IL6","/geneCalc?gene=","/geneCalc?gene=bye","/geneList"
             ,"/geneList?chromo=1&start=0&end=30000","/geneList?chromo=6&start=5&end=3000","/geneList?chromo=&start=&end=",
             "/geneList?chromo=&start=1&end=30000","/geneList?chromo=18&start=&end=","/geneList?chromo=1&start=9&end=987654321"]

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