import http.client

SERVER = "localhost"
PORT= 8080
endpoints = ["/", "/list/Species", "/listSpecies?limit=10", "/listSpecies?limit=fish" , "/listSpecies?limit=", "/listSpecies?limit=56789","/karyotype", "/karyotype?specie=mouse", "/karyotype?specie=","/karyotype?specie=coronavirus",""]