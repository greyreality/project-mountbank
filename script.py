#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import json
from json_generator import generate_json
import shutil

def generate_json_file(json_file_path, project_id, project_name, project_test_run_count,
             total_duration, success_rate):
    with open('template/template.json',
              "r") as file:
        schema_str = file.read().replace('\n', '').replace(' ', '')
        args_dict = {"$.id": project_id,
                     "$.name": project_name,
                     "$.platform": "Desktop",
                     "$.successRate": success_rate,
                     "$.totalRuns": project_test_run_count,
                     "$.totalDuration": total_duration}
    json_body = generate_json(
        json_schema=schema_str, args=args_dict,
        remove_null=False, remove_empty=False)
    with open(json_file_path, "w") as file:
        file.write(json_body)
    return

def update_stub_file(project_index, path_to_stub_file, path_to_project_file):
    input_file = open(path_to_stub_file, "r")
    json_object = json.load(input_file)
    input_file.close()
    
    project_file = open(path_to_project_file, "r")
    project_json_file = json.load(project_file)
    json_object['responses'][0]['is']['body'][project_index] = project_json_file
    # print(json_object)
    file = open(path_to_stub_file, "w")
    json.dump(json_object, file)
    file.close()
    
def main():
    projects_response = requests.get("http://localhost:4545/projects")
    # print(projects_response.json())
    projects = json.loads(projects_response.text)
    #Copy file with original stub configuration
    shutil.copy('stubs/projectsStub.json', 'stubs/projectsStub_for_update.json')
    # For every project from stub response
    for projects in projects:
        project_id = projects['id']
        project_name = projects['name']
        testresults_response = requests.get(
            "http://localhost:4546/results?project=" + str(project_id))
        project_test_run_count = len(testresults_response.json())
        testresults = json.loads(testresults_response.text)
        total_duration = 0
        total_passed = 0
        for testresults in testresults:
            duration = testresults['duration']
            total_duration += duration
            if testresults['status'] == 'Passed':
                total_passed += 1
        success_rate = float(total_passed) / (
                    float(project_test_run_count) / 100.00)
        
        # Generate json file per project
        json_file_path = "json/%s.json" % (projects['id'])
        generate_json_file(json_file_path, project_id, project_name, project_test_run_count, total_duration, success_rate)
        project_index = project_id - 1

        # Add more project values to stub configuration
        update_stub_file(project_index, 'stubs/projectsStub_for_update.json', json_file_path)

    before = requests.get('http://localhost:4545/projects')
    print("Stub value before update: ", json.loads(before.text))
    # Update stub of mountbank with new configuration
    response = requests.put('http://localhost:2525/imposters/4545/stubs/0',
                            data=open('stubs/projectsStub_for_update.json', 'rb'))
    after = requests.get('http://localhost:4545/projects')
    print("Stub value after update: ", json.loads(after.text))

if __name__ == "__main__":
    print("===Generate json per project and update stub 4545")
    main()
