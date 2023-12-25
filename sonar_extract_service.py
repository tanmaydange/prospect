import requests
from requests.exceptions import HTTPError
import sqlite3
import datetime
import configparser
from tqdm import tqdm
from sonarqube import SonarQubeClient
import json
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.INFO,  filename="logs/prospect-sonar.log")


current_date = datetime.date.today()

#Constants
PROJECT_NAME_KEY = "Affected Project"
VULENERABILITY_ISSUE_KEY="Vulnerability Issues"
DEPENDENCY_KEY="Dependency"
DETAILS_KEY="Details"
REVISION_KEY="Revision"
ISSUE_TYPE_KEY="Issue Type"
TYPE_KEY="Type"
SECURITY_ISSUE_KEY="Security Issue"
CVE_KEY="CVE"
CVSS_SCORE_KEY="CVSS Score"
CVSS_SEVERITY_KEY="CVSS Severity"
NAME_KEY="Name"
REMEDIATION_ADVICE_KEY="Remediation Advice"
QUALITY_ISSUES_KEY="Quality Issues"
PACKAGE_LICENSE_ISSUES_KEY="Package License Issues"


  

def main():
    
    config_parser = configparser.RawConfigParser()   
    config_file_parser = r'config.prop'
    config_parser.read(config_file_parser)
    
    auth_key = config_parser.get('sonar-config', 'auth_key')
    url=config_parser.get('sonar-config', 'url')
    db=config_parser.get('sonar-config', 'db')
   
    sonar = SonarQubeClient(sonarqube_url=url, token=auth_key)

    con = sqlite3.connect(db)
    cur = con.cursor()


    product_map = {}

    cursor= con.execute("SELECT project,sonar_project_key from project_sonar_key")
    for row in cursor:
        product_map[row[0]] = row[1]
    
    try:
        for project in tqdm(product_map):
            # Initilizing the local variables
            quality_gate_status = "N/A"
            overall_coverage=0
            new_coverage=0
            overall_security_hotspots_reviewed=0
            new_security_hotspots_reviewed=0
            logging.info("Processing for Product :"+project)
            sonar_project_key = product_map[project]
            metric_keys = "quality_gate_details,bugs,new_bugs,vulnerabilities,new_vulnerabilities,security_hotspots_reviewed,new_security_hotspots_reviewed,code_smells,new_code_smells,coverage,new_coverage,duplicated_lines_density,new_duplicated_lines_density"
            component = sonar.measures.get_component_with_specified_measures(component=sonar_project_key,
                                                                 branch="master",
                                                                 fields="metrics,periods",
                                                                 metricKeys=metric_keys)
            

            for measure in component['component']['measures']:
                if measure["metric"] == "quality_gate_details":
                    if json.loads(measure["value"])["level"] is not None:
                        quality_gate_status = json.loads(measure["value"])["level"]
                    else:
                        quality_gate_status = "N/A"
                if measure["metric"] == "new_bugs":
                    new_bugs = measure["period"]["value"]
                if measure["metric"] == "new_vulnerabilities":
                    new_vulnerabilities = measure["period"]["value"]
                if measure["metric"] == "new_security_hotspots_reviewed":
                    new_security_hotspots_reviewed = measure["period"]["value"]
                if measure["metric"] == "security_hotspots_reviewed":
                    overall_security_hotspots_reviewed = measure["value"]
                if measure["metric"] == "coverage":
                    if measure["value"] is not None:
                        overall_coverage = measure["value"]
                    else:
                        overall_coverage = 0           
                if measure["metric"] == "vulnerabilities":
                    overall_vulnerabilities = measure["value"]                       
                if measure["metric"] == "duplicated_lines_density":
                    overall_duplicated_lines_density = measure["value"]                 
                if measure["metric"] == "bugs":
                    overall_bugs = measure["value"]       
                if measure["metric"] == "new_duplicated_lines_density":
                    new_duplicated_lines_density = measure["period"]["value"]                    
                if measure["metric"] == "code_smells":
                    if measure["value"] is not None:
                        overall_code_smells = measure["value"]
                    else:
                        overall_code_smells = 0       
                if measure["metric"] == "new_code_smells":
                    new_code_smells = measure["period"]["value"]       
                if measure["metric"] == "new_coverage":
                    new_coverage = measure["period"]["value"]    
            
                                
            query_str = "delete from sonar_metrics where project ='"+project+"'"
            cur.execute(query_str)
            cur.execute("insert into sonar_metrics(project, quality_gate_status,overall_code_smells,overall_coverage,overall_security_hotspots_reviewed,overall_bugs,overall_vulnerabilities,overall_duplicated_lines_density,new_code_smells,new_coverage,new_security_hotspots_reviewed,new_bugs,new_vulnerabilities,new_duplicated_lines_density) values(?,?,?,?,?,?,?,?,?,?,?,?,?,? )" , (project, quality_gate_status,overall_code_smells,overall_coverage,overall_security_hotspots_reviewed,overall_bugs,overall_vulnerabilities,overall_duplicated_lines_density,new_code_smells,new_coverage,new_security_hotspots_reviewed,new_bugs,new_vulnerabilities,new_duplicated_lines_density))
            last_run_query="update last_update set last_run=datetime(\'now\', \'localtime\') where metric=\'SONAR\'"
            cur.execute(last_run_query)
                

    except HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error(f'Other error occurred: {err}')

    logging.info("Done")   
    con.commit()


if __name__ == "__main__":
    main()
