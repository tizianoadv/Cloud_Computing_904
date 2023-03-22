# Serverless application with GCP

The solution developped is based on a serverless architecture and a Backend-as-a-Service (BAAS) solution. The objective of this work was to design and deploy an application that would provide a list of candidates and collect votes, communicating with a BAAS application coupled with a database.

## Function 1
The first serverless function is responsible for retrieving user requests, retrieving the list of candidates from the BaaS, and sending the response containing the list of candidates. This function was developed using Python technology.

## Function 2
The second serverless function is responsible for retrieving user requests, retrieving the vote collection from the BaaS, and sending the response containing the voting results. This function was also developed using Python technology.

## BaaS
The BaaS application is responsible for retrieving requests from the serverless functions, saving the data in the database, retrieving information from the database, and sending the response containing the data to the serverless functions. This application was developed using Flask technology.

## Stockage
The database used in this application is a MySQL database. It stores the voting data and the list of candidates in the form of a table.