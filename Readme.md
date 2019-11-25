# CrowdEmotion Flask Server

This is a flask based solution for the CrowdEmotion's 'Frontend Developer Exercise 2 - Implement Dynata Web App'

**Demo:**

**TODO**:[https://crowdemotion-dynata.netlify.com/api](https://crowdemotion-dynata.netlify.com/api)


## Installing for local development

**Pre-requirements:** 

- python 3.4+
- pip 18+
- virtualenv 15+

**Installation steps:**

Clone the git repository to your local machine:

```
$ git clone git@github.com:4d4mm/crowdemotion-be-test.git
```

Change directory to the cloned repository.

```
$ cd crowdemotion-be-test
```

Create a virtual environment using python 3:

```
$ which python3
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
$ virtualenv -p /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 venv
```

*NOTE:* you need pass the path, from output of the first command, to the second command -p argument.

Activate the virtual environment:

```
$ source venv/bin/activate
```

Install the the python packages required for the project.

```
(venv)$ pip install -r requirements.txt
```

See the configuration section for environment variable requirements.

To run the app locally:

```
(venv)$ python app.py
```

The app will run at:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Configuration

| Environment Variable | Description |
|-----|----|
| CROWDEMOTION_DEMAND_API_URL | Dynata api url  |
| CROWDEMOTION_DEMAND_API_CLIENT_ID | Dynata client id  |
| CROWDEMOTION_DEMAND_API_USERNAME | Dynata username |
| CROWDEMOTION_DEMAND_API_PASSWORD | Dynata password |
| CROWDEMOTION_APP_SECRET_KEY | Application secret key |
| CROWDEMOTION_CACHE_DEFAULT_TIMEOUT | Cache timeout (default: 300s, optional)| 

Use export on linux based systems for example :

```
export CROWDEMOTION_DEMAND_API_URL="https://demo-url.api.dynata.com/"
```

On windows based systems:

```
set CROWDEMOTION_DEMAND_API_URL="https://demo-url.api.dynata.com/"
```

The easiest way to set the configuration locally is to add the following lines to the end of the `venv/bin/activate` shellscript:

```
export CROWDEMOTION_DEMAND_API_URL="https://demo-url.api.dynata.com/"
export CROWDEMOTION_DEMAND_API_CLIENT_ID="api"
export CROWDEMOTION_DEMAND_API_PASSWORD="super-secret-passowrd"
export CROWDEMOTION_DEMAND_API_USERNAME="crowd_emotion_demo_sample_api"
export CROWDEMOTION_APP_SECRET_KEY="uber-secret-application-key"
export CROWDEMOTION_API_USER="rest-web-api-user"
export CROWDEMOTION_API_PASSWORD="rest-web-api-password"
```

Obviously the demand api parameters (`CROWDEMOTION_DEMAND_API_URL`, `CROWDEMOTION_DEMAND_API_CLIENT_ID`, `CROWDEMOTION_DEMAND_API_PASSWORD`, `CROWDEMOTION_DEMAND_API_USERNAME`) need to be substituted to a working account's credentials. 

## API

The implemented api and base request can be tested via the included (/spec/Insomnia_2019-11-25.json) InsomniaREST workspace. The Demand Api folder contains the Dynata api requests. The API folder contains the request for the Web Api. Both the Dynata token and Api JWT token needs to be saved to the Insomnia environment for testing.

**Authenticate**:

```
POST /auth HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "username": "joe",
    "password": "pass"
}
```

Response:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E"
}
```


This token can then be used to make requests against protected endpoints:

```
GET /protected HTTP/1.1
Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E
```

**GET countries**:

```
GET /countries HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E
```

Response:

```
{
  "data": [
    {
      "countryName": "United Arab Emirates",
      "id": "AE",
      "isoCode": "AE",
      "supportedLanguages": [
        {
          "id": "en",
          "isoCode": "en",
          "languageName": "English (UAE)"
        }
      ]
    },
    ...
     {
      "countryName": "Vietnam",
      "id": "VN",
      "isoCode": "VN",
      "supportedLanguages": [
        {
          "id": "vi",
          "isoCode": "vi",
          "languageName": "Vietnamese"
        }
      ]
    },
    {
      "countryName": "South Africa",
      "id": "ZA",
      "isoCode": "ZA",
      "supportedLanguages": [
        {
          "id": "en",
          "isoCode": "en",
          "languageName": "English (South Africa)"
        }
      ]
    }
  ],
  "status": {
    "errors": [],
    "message": "success"
  }
}
```

**GET attributes**:

```
GET /attributes HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E
```

Response:

```
{
  "data": [
    {
      "category": {
        "mainCategory": {
          "id": "DEMOGRAPHIC",
          "localizedText": "Demographic",
          "text": "Demographic"
        }
      },
      "id": "11",
      "isAllowedInFilters": true,
      "isAllowedInQuotas": true,
      "localizedText": "What is your gender?",
      "name": "Gender",
      "options": [
        {
          "id": "1",
          "localizedText": "Male",
          "text": "Male"
        },
        {
          "id": "2",
          "localizedText": "Female",
          "text": "Female"
        }
      ],
      "state": "ACTIVE",
      "text": "What is your gender?",
      "tier": "Standard",
      "type": "LIST"
    },
    ...
    {
      "category": {
        "mainCategory": {
          "id": "AUTOMOTIVE",
          "localizedText": "Automotive",
          "text": "Automotive"
        }
      },
      "id": "12371676",
      "isAllowedInFilters": true,
      "isAllowedInQuotas": true,
      "localizedText": "Which, if any, of the following best describes your current most-used car model? (Tesla)",
      "name": "PRIMARY MODEL - Tesla",
      "options": [
        {
          "id": "1",
          "localizedText": "Model 3",
          "text": "Model 3"
        },
        {
          "id": "2",
          "localizedText": "Model S",
          "text": "Model S"
        },
        {
          "id": "3",
          "localizedText": "Model X",
          "text": "Model X"
        },
        {
          "id": "4",
          "localizedText": "Roadster",
          "text": "Roadster"
        },
        {
          "id": "5",
          "localizedText": "Other",
          "text": "Other"
        }
      ],
      "state": "ACTIVE",
      "text": "Which, if any, of the following best describes your current most-used car model? (Tesla)",
      "tier": "Premium - Car",
      "type": "LIST"
    }
  ],
  "status": {
    "errors": [],
    "message": "success"
  }
}
```

**GET surveys**:

```
GET /surveys HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E
```

Response:

```
{
  "data": [
    {
      "author": {
        "name": "crowd_emotion_demo_sample_api",
        "type": "api",
        "username": "crowd_emotion_demo_sample_api"
      },
      "createdAt": "2019/11/07 21:12:02",
      "extProjectId": "project001",
      "jobNumber": "PO-1234",
      "state": "PROVISIONED",
      "stateLastUpdatedAt": "2019/11/07 21:12:01",
      "title": "..",
      "updatedAt": "2019/11/15 12:15:31"
    }
  ],
  "status": {
    "errors": [],
    "message": "success"
  }
}
```

**GET Survey**:

```
GET /surveys/project001 HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6MSwiaWF0IjoxNDQ0OTE3NjQwLCJuYmYiOjE0NDQ5MTc2NDAsImV4cCI6MTQ0NDkxNzk0MH0.KPmI6WSjRjlpzecPvs3q_T3cJQvAgJvaQAPtk1abC_E
```

Response:

```
{
  "data": {
    "author": {
      "name": "crowd_emotion_demo_sample_api",
      "type": "api",
      "username": "crowd_emotion_demo_sample_api"
    },
    "category": {
      "surveyTopic": [
        "AUTOMOTIVE",
        "BUSINESS"
      ]
    },
    "createdAt": "2019/11/07 21:12:02",
    "devices": [
      "mobile",
      "desktop",
      "tablet"
    ],
    "exclusions": {
      "list": [],
      "type": ""
    },
    "extProjectId": "project001",
    "jobNumber": "PO-1234",
    "lineItems": [
      {
        "countryISOCode": "US",
        "createdAt": "2019/11/07 21:12:02",
        "daysInField": 20,
        "deliveryType": "BALANCED",
        "endLinks": {
          "complete": "https://demo-url.api.dynata.com/respondent/exit?rst=1&psid={psid}&med={calculatedSecurityCode}",
          "overquota": "https://demo-url.api.dynata.com/respondent/exit?rst=3&psid={psid}",
          "screenout": "https://demo-url.api.dynata.com/respondent/exit?rst=2&psid={psid}",
          "securityKey1": "93896",
          "securityKey2": "42614",
          "securityLevel": "MEDIUM"
        },
        "extLineItemId": "lineItem001",
        "indicativeIncidence": 20,
        "languageISOCode": "en",
        "launchedAt": "",
        "lengthOfInterview": 10,
        "quotaPlan": {
          "filters": [
            {
              "attributeId": "11",
              "operator": "INCLUDE",
              "options": [
                "2"
              ]
            }
          ]
        },
        "requiredCompletes": 800,
        "sources": [
          {
            "id": 100
          }
        ],
        "state": "PROVISIONED",
        "stateLastUpdatedAt": "2019/11/07 21:12:02",
        "surveyTestURL": "www.mysurvey.com/test/survey?pid=<#testId>&k2=<#Project[Secure Key 2]>&psid=<#IdParameter[Value]>",
        "surveyURL": "www.mysurvey.com/live/survey?pid=<#testId>&k2=<#Project[Secure Key 2]>&psid=<#IdParameter[Value]>",
        "targets": [
          {
            "count": 800,
            "dailyLimit": 0,
            "softLaunch": 0,
            "type": "COMPLETE"
          }
        ],
        "title": "US College",
        "updatedAt": "2019/11/15 12:15:31"
      }
    ],
    "notificationEmails": [
      "api-test@dynata.com"
    ],
    "state": "PROVISIONED",
    "stateLastUpdatedAt": "2019/11/07 21:12:01",
    "title": "..",
    "updatedAt": "2019/11/15 12:15:31"
  },
  "meta": null,
  "status": {
    "errors": [],
    "message": "success"
  }
}
```

# Possible enhancements

- Implement persistent user

# References

[Flask](http://flask.palletsprojects.com/en/1.1.x/)
[Flask-JWT](https://pythonhosted.org/Flask-JWT/)
[Flask-Caching](https://flask-caching.readthedocs.io/en/latest/index.html)
[flask-cors](https://flask-cors.readthedocs.io/en/latest/)
[Insomnia Rest Client](https://insomnia.rest/)