# Cloud Data Extractor

Cloud Data Extractor is a modular Python library designed to standardize and simplify the process of retrieving structured data from Google Cloud Firestore and transforming it into analytics-ready formats. The project was developed to address the recurring need for a reusable, reliable, and testable data extraction layer that can serve machine learning pipelines, analytics workflows, and application backends. Instead of tightly coupling applications directly to the Firestore SDK, CDE introduces a clean abstraction layer that handles authentication, connection management, collection retrieval, error handling, and data transformation.

## Features  
* Connection to GCP Firestore.
* Functionality to load user-provided credentials.
* Converting fetched data useful data structures.
* Interface class.

## Technologies used
* Python programming language
* Firebase Admin SDK for Python
* Pandas
* Black
* Unittest

## Tests  
The project includes a comprehensive set of tests to ensure that all functionalities are working correctly.  

## Documentation  
The documentation can be found on the [Software Documentation Website](https://patrickschroeder98.github.io/software_documentation/cloud_data_extractor_docs/index.html).  
Or in the websie [repository](https://github.com/PatrickSchroeder98/software_documentation/tree/main/cloud_data_extractor_docs).  