# The AP Elections API

## Project goal

This project started at Associated Press in order to give their customers a library to request and parse responses from the [AP Elections API](https://developer.ap.org/ap-elections-api/docs/index.html#t=Welcome.htm). It helps manage the history of requests to use appropriate URLs, returns detailed error codes, and defines the valid parameters for a request to reduce magic strings. The response parsing portion of the library is incomplete -- responses can only be accessed as JSON or a CSV.

## Project notes

The API has four types of data: election race information, election reports, advance turnout data, and delegate allocation data.


### Getting started

Create a `.env` file and add your API key as a variable named `API_KEY`.

### Structure

An example query is in `run.ipynb`. As it shows, the top level object to interact with the API is an `APIClient` object that handles all the requests and responses. A few pieces that it simplifies:

- To request updated data for a given query, you're supposed to use a URL from the response of your last request (detailed [here](https://developer.ap.org/ap-elections-api/docs/Receiving_Election_Updates.htm)). The client tracks all those queries and the associated request URLs, using the last returned URL by default.

- The 403 response code means the user should wait 5-10 seconds and retry. The client will automatically retry when receiving that code.

The `APIClient` takes an instance of the `QueryParameters` object to send a request. This class helps define the fields and data types that make a valid request more narrowly. For each of the four data types, we inherit this base class and add functions to validate the parameters and transform them into a valid URL.

The output of a query is a `ResponseParser` object. I haven't implemented it for all four data types, but it flattens JSON responses completely to make a CSV. Depending on the end result we want, it could have methods to export to different formats.

All the fields that go into a request and the options for each field are defined as custom data types.

### Overview of scripts

- `run.ipynb`: A notebook with an example of how to interact with the API.
- `client.py`: The highest level file outlining the `APIClient` class. The `query` method here has the bulk of the request-response logic.
- `exceptions.py`: Custom exceptions for each response status code.
- `_utils.py`: Function to handle response error codes and flatten JSON objects.
- `_fields.py`: Define all the categorical variables as custom data types.
- `param_schema/`: A folder for all the scripts relating to the `QueryParameters` code.
    - `_base_param.py`: Defines the abstract `QueryParameters` class, a dictionary mapping from Python variable names to the API's variable names, and a function to convert parameter fields to dictionary.
    - Each data type has its own file that inherits `QueryParameters` to list the relevant fields and implement specific data validation checks
- `response_schema/`: A folder for all the scripts relating to the `ResponseParser` code.
    - `_base_response.py`: Defines the `ResponseParser` class.
    - Each data type has its own file that inherits `ResponseParser`. Not implemented yet.

---
*Thank you to the data team at AP for shaping this project!*