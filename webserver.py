import sys
import logging
import web
import json
import configparser
import sqlite3

logging.basicConfig(format='%(asctime)s %(levelname)s %(name)s %(message)s',filename='logs/webserver.log',level=logging.INFO)
web.config.debug = False

config_parser = configparser.RawConfigParser()   
config_file_parser = r'config.prop'
config_parser.read(config_file_parser)
db=config_parser.get('webserver-config', 'db')




urls = (
    "/enroll", "Index"
)

render = web.template.frender('static/enroll.html')

class Index(object):
    def GET(self):
        return render()

    def POST(self):
        data = web.data()
        con = sqlite3.connect(db)
        cur = con.cursor()
        web.header('Content-Type', 'application/json')
        try:
            result = json.loads(data)
            project = result["project"]
            product = result["product"]
            sonar_key = result["sonar_key"]
            java_version = result["java_version"]
            spring_version = result["spring_version"]
            sprint_boot_version = result["springboot_version"]
            aws_services = result["aws_services"]
            other_tech = result["other_technologies"]
            logging.info("Registration Request recieved for project " + project)

            
            project_qry_str = "INSERT INTO PRODUCTS (product_name) VALUES ('"+project+"')"
            cur.execute(project_qry_str)
            cur.execute("insert into product_repo_map (product, project) values (?,?)",(product,project))
            cur.execute("insert into project_sonar_key values (?, ?)", (project,sonar_key))
            cur.execute("INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES(?,?,?,?)" , (project, java_version, spring_version, sprint_boot_version))
            
            for service in aws_services:
                cur.execute("INSERT INTO project_aws_stack (project,aws_services) values (?,?)", (project,service))
            for tech in other_tech:
                cur.execute("INSERT INTO project_tech_stack (project,other_tech) values (?,?)" , (project,tech))
                
            
            con.commit()
            return '{"status" : "Registeration Successful" }'
           
        except ValueError as err:
           logging.error(err)
           return '{"status" : "Registeration Failure" }'

if __name__ == "__main__":
    logging.info("[Server] Starting server.")
    app = web.application(urls, globals())
    app.run()