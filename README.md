# Autotests Project

This project contains automated tests for the Trello website.

## Getting Started

1. Create a `.env` file based on the `.env.draft` template for environment variables.

2. Create and activate virtual environment if needed
```commandline
 python3 -m venv venv
```

```commandline
 source venv/bin/activate
```

3. Install dependencies:
```commandline
pip install -r requirements.txt
 ```


Run tests
``` commandline
 pytest
```
you can modify in pytest.ini


Run tests using Dockerfile
```commandline
docker build -t app_image .
docker run -p 8000:8000 app_image

```
This allows viewing the report locally after building.

Open link to see html report
```commandline
http://localhost:8000/html_report/report.html
```


## Black formatter
 Apply python standard formatting.
 [for more information](https://black.readthedocs.io/en/stable/)
<br/>To run, run the following command in the terminal
 ```commandline
 black .
 ```


 ## Flake8
 Your Tool For Style Guide Enforcement
 [for more information](https://flake8.pycqa.org/en/latest/index.html)
 <br/>To run, run the following command in the terminal
```commandline
 flake8
 ```

