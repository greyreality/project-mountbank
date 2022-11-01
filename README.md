### Project:
1. To create a simple mock server with these endpoints
- GET /projects 
  - return data from projects.json
- GET /results/:projectId 
  - return data from results.json
- POST /stability 
  - header with key 
  - return success when 
    - Header contains “Authorization”: “Basic authenticationKeyForMockServer“ 
    - Body contains JSON 
2. To create a script to consume data from and feed the data back the mock server 
- Get list of projects from the mock server 
- For each project 
  - Get list of test results of the project 
  - Process data to be in example_request.json format 
    - successRate = Count(PASS results) / Count(results) 
    - totalRuns = Count(results) 
    - totalDuration = Sum(duration) 
  - Sent the result back to the mock server
Example of projects.json
```javascript
[ 
    { 
        "id": 1, 
        "name": "Powerbuy" 
    }, 
    { 
        "id": 2, 
        "name": "TOPS" 
    }, 
    { 
        "id": 3, 
        "name": "SuperSports" 
    }1 
] 
```
Example of results.json
```javascript
[ 
    { 
        "runId": 1001, 
        "status": "Passed", 
        "testsTotal": 12, 
        "testsPassed": 12, 
        "testsFailed": 0, 
        "duration": 600, 
        "timeStarted": "2021-07-09 01:00:00.510398", 
        "timeFinished": "2021-07-09 01:10:00.107914" 
    }, 
    { 
        "runId": 1002, 
        "status": "Passed", 
        "testsTotal": 12, 
        "testsPassed": 12, 
        "testsFailed": 0, 
        "duration": 600, 
        "timeStarted": "2021-07-09 02:00:00.510398", 
        "timeFinished": "2021-07-09 02:10:00.107914" 
    }, 
    { 
        "runId": 1003, 
        "status": "Failed", 
        "testsTotal": 12, 
        "testsPassed": 1, 
        "testsFailed": 11, 
        "duration": 1010, 
        "timeStarted": "2021-07-09 03:00:00.510398", 
        "timeFinished": "2021-07-09 03:16:50.107914" 
    }, 
    { 
        "runId": 1004, 
        "status": "Failed", 
        "testsTotal": 12, 
        "testsPassed": 1, 
        "testsFailed": 11, 
        "duration": 1010, 
        "timeStarted": "2021-07-09 04:00:00.510398", 
        "timeFinished": "2021-07-09 04:16:50.107914" 
    }, 
    { 
        "runId": 1005, 
        "status": "Passed", 
        "testsTotal": 12, 
        "testsPassed": 12, 
        "testsFailed": 0, 
        "duration": 600, 
        "timeStarted": "2021-07-09 05:00:00.510398", 
        "timeFinished": "2021-07-09 05:10:00.107914" 
    }, 
    { 
        "runId": 1006, 
        "status": "Failed", 
        "testsTotal": 12, 
        "testsPassed": 1, 
        "testsFailed": 11, 
        "duration": 1010, 
        "timeStarted": "2021-07-09 06:00:00.510398", 
        "timeFinished": "2021-07-09 06:16:50.107914" 
    }, 
    { 
        "runId": 1007, 
        "status": "Failed", 
        "testsTotal": 12, 
        "testsPassed": 1, 
        "testsFailed": 11, 
        "duration": 1010, 
        "timeStarted": "2021-07-09 07:00:00.510398", 
        "timeFinished": "2021-07-09 07:16:50.107914" 
    }, 
    { 
        "runId": 1008, 
        "status": "Failed", 
        "testsTotal": 12, 
        "testsPassed": 1, 
        "testsFailed": 11, 
        "duration": 1010, 
        "timeStarted": "2021-07-09 08:00:00.510398", 
        "timeFinished": "2021-07-09 08:16:50.107914" 
    }, 
    { 
        "runId": 1009, 
        "status": "Passed", 
        "testsTotal": 12, 
        "testsPassed": 12, 
        "testsFailed": 0, 
        "duration": 600, 
        "timeStarted": "2021-07-09 08:00:00.510398", 
        "timeFinished": "2021-07-09 08:10:00.107914" 
    }, 
    { 
        "runId": 1010, 
        "status": "Failed", 
        "testsTotal": 12, 
        "testsPassed": 1, 
        "testsFailed": 11, 
        "duration": 1010, 
        "timeStarted": "2021-07-10 04:00:00.510398", 
        "timeFinished": "2021-07-10 04:16:50.107914" 
    } 
] 
```
Example of example_request.json 
```javascript
{ 
    "id": 1, 
    "name": "Powerbuy", 
    "platform": "Desktop", 
    "successRate": 90.00, 
    "totalRuns": 10, 
    "totalDuration": 10 
} 
```

### How to use:
Install mock
```
npm install -g mountebank
```
Start mock by script
```
./start_mb_local.sh
```
Import collection to Postman UI to check that mock works
```
chmod +x script.py
``` 
Execute script on python2 to update mock data
```
./script.py
```
### Celebrate
![](https://github.com/greyreality/project-mountbank/blob/main/files/celebration.gif)
### Additional
Question: How to setup a schedule run every day for the script in #2?
Answer: Task Scheduler, Cron in CICD pipeline