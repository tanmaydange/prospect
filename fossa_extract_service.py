import requests
from requests.exceptions import HTTPError
import sqlite3
import datetime
import configparser
from tqdm import tqdm 
import logging

current_date = datetime.date.today()
logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s', level=logging.INFO,  filename="logs/prospect-fossa.log")

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


def find_security_issues(json_response,cur):
    vulnerability_list=json_response[VULENERABILITY_ISSUE_KEY]

    for vul in vulnerability_list:
        cur.execute("insert into VULNERABILITY_HIST (project,dependency,details,current_version,issue_type,cve,cvss_score,cvss_severity,name,fix_version,scan_date) VALUES(?, ?,?,?, ?,?,?, ?,?,?,?)", (vul[PROJECT_NAME_KEY],vul[DEPENDENCY_KEY],vul[DETAILS_KEY],vul[REVISION_KEY],SECURITY_ISSUE_KEY,vul[CVE_KEY],vul[CVSS_SCORE_KEY],vul[CVSS_SEVERITY_KEY],vul[NAME_KEY],vul[REMEDIATION_ADVICE_KEY],current_date))

    
def find_quality_issues(json_response,cur):    
    quality_list=json_response[QUALITY_ISSUES_KEY]
    
    for vul in quality_list:
        cur.execute("insert into VULNERABILITY_HIST(project,dependency,details,current_version,issue_type,scan_date) VALUES(?, ?,?,?, ?,?)", (vul[PROJECT_NAME_KEY],vul[DEPENDENCY_KEY],vul[DETAILS_KEY],vul[REVISION_KEY],vul[TYPE_KEY], current_date))

def find_license_issues(json_response,cur):    
    
    license_issue_list=json_response[PACKAGE_LICENSE_ISSUES_KEY]
   
    for vul in license_issue_list:
        cur.execute("insert into VULNERABILITY_HIST(project,dependency,details,current_version,issue_type, scan_date) VALUES(?, ?,?,?, ?,?)", (vul[PROJECT_NAME_KEY],vul[DEPENDENCY_KEY],vul[DETAILS_KEY],vul[REVISION_KEY],vul[ISSUE_TYPE_KEY], current_date))                 
    

def main():
    
    config_parser = configparser.RawConfigParser()   
    config_file_parser = r'config.prop'
    config_parser.read(config_file_parser)
    
    auth_key = config_parser.get('fossa-config', 'auth_key')
    url=config_parser.get('fossa-config', 'url')
    db=config_parser.get('fossa-config', 'db')
   
    
    con = sqlite3.connect(db)
    cur = con.cursor()

    auth = { 'Authorization': 'Bearer '+auth_key }

    URL_POST = "/export-issues/json"
    LOCATOR_PREFIX = "custom%2B28167%2Fgithub.com%2Fadvancedcsg%2F"
    
    product_list = []

    cursor= con.execute("SELECT product_name from PRODUCTS")
    for row in cursor:
        product_list.append(row[0])

    try:
        for project in tqdm(product_list):
            URL=url+LOCATOR_PREFIX+project+URL_POST

            logging.info("Processing for Product :"+project)
            response = requests.get(URL, headers=auth)
            response.raise_for_status()
            json_response = response.json()
            #print(jsonResponse)
            
            cur.execute("delete from VULNERABILITY_HIST where project =?  and scan_date=?", (project, current_date))


            find_security_issues(json_response,cur)
            find_license_issues(json_response,cur)
            find_quality_issues(json_response,cur)
            last_run_query="update last_update set last_run=datetime(\'now\', \'localtime\') where metric=\'FOSSA\'"
            cur.execute(last_run_query)
            

    except HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error(f'Other error occurred: {err}')

    logging.info("Done")   
    con.commit()


if __name__ == "__main__":
    main()
