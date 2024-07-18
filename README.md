# Explore Election API

Python wrapper to use the [AP Elections API](https://developer.ap.org/ap-elections-api/docs/index.html#t=Welcome.htm).

*Created by Arushi Gupta (<argupta@ap.org>)*

*Reporter: Arushi Gupta (<argupta@ap.org>)*

## Project goal

Provide some Python tools to easily send requests and parse responses from AP's Election API. 

## Project notes

The API has four types of data: election race information, election reports, advance turnout data, and delegate allocation data.

### Staff involved

Arushi Gupta (<argupta@ap.org>, <arushi.gupta@gmail.com>)

## Technical

All the files are in the `analysis/` folder.

### Project setup instructions

After cloning the git repo:

`python .first_install.py` to set up the Python environment.

Create a `.env` file and add your API key as a variable named `API_KEY`.

### Structure

An example query is in `run.ipynb`. As it shows, the top level object to interact with the API is an `APIClient` object that handles all the requests and responses. A few pieces that it simplifies:

- To request updated data for a given query, you're supposed to use a URL from the response of your last request (detailed [here](https://developer.ap.org/ap-elections-api/docs/Receiving_Election_Updates.htm)), so the client tracks all those queries and the associated request URLs.

- The 403 response code means the user should wait 5-10 seconds and retry. The client will automatically retry when receiving that code.

- [not tested] Some responses include an "isTruncated" variable, which means some data wasn't returned and the same request should be sent until the variable becomes false. The client automatically requeries.

The `APIClient` takes an instance of the `QueryParameters` object to send a request. This class helps define the fields and data types that make a valid request more narrowly. For each of the four data types, we inherit this base class and add functions to validate the parameters and transform them into a variable.

The output of a query is a `ResponseParser` object. I haven't implemented it for all four data types, but the hope is that this class structure can parse the JSON or XML that's returned to create a CSV (or some other data type). Right now, the ResponseParser only works for JSON and just flattens everything completely to make a giant CSV. Depending on the end result we want, it could have methods to export to different formats.

### All files

- `run.ipynb`: A notebook with an example of how to interact with the API.
- `client.py`: The highest level file outlining the `APIClient` class. The `query` method here has the bulk of the request-response logic.
- `exceptions.py`: Custom exceptions for each response status code.
- `utils.py`: Function to handle response error codes and flatten JSON objects.
- `_fields.py`: Define all the categorical variables as custom data types.
- `param_schema/`: A folder for all the scripts relating to the `QueryParameters` code.
    - `_base_param.py`: Defines the abstract `QueryParameters` class, a dictionary mapping from Python variable names to the API's variable names, and a function to convert parameter fields to dictionary.
    - Each data type has its own file that inherits `QueryParameters` to list the relevant fields and implement specific data validation checks
- `response_schema/`: A folder for all the scripts relating to the `ResponseParser` code.
    - `_base_response.py`: Defines the `ResponseParser` class.
    - Each data type has its own file that inherits `ResponseParser`. Not implemented yet.

### Ideas of where to go next

- Add more validation checks to the `QueryParameters`
- Implement the `ResponseParser` objects for each data type
- Implement the `APIClient.query()` to support all four data types
- Make the exceptions more detailed
