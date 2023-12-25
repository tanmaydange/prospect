INSERT INTO PRODUCTS (product_name) VALUES ('pse-e5UIPOC');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-usermanager');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-keycloak-usermanager');
INSERT INTO PRODUCTS (product_name) VALUES ('myworkplace-launchpad');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-payments-framework');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-e5UI');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-e5-Messaging');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-e5-RestServices');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-esupplier');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-e5-portal-services');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-e5-query');
INSERT INTO PRODUCTS (product_name) VALUES ('pse-coh-portal');

--
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('pse-e5UIPOC','Java 11','2.5.12','2.5.12');
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('pse-esupplier','Java 8','5.3.5','1.5.7');
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('pse-keycloak-usermanager','Java 11','2.1.8','2.1.8');
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('pse-payments-framework','Java 8','1.4.2','1.4.2');
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('myworkplace-launchpad','Java 11','2.1.8','2.1.8');
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('pse-bpm','Java 11','5.3.20','2.5.14');
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('pse-e5portals','Java 11','5.3.25','2.7.8');
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('pse-cloud-files','Java 11','5.3.25','2.7.8');
INSERT INTO project_java_stack (project,java_version,spring_version,spring_boot_version) VALUES('pse-e5UI','Java 8','N/A','N/A');

--
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UIPOC','EC2');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UIPOC','ECS');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UIPOC','ECR');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UIPOC','CloudWatch');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UIPOC','Secrets Manager');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UIPOC','Systems Manager');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UIPOC','RDS - Postgres');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UIPOC','Code Artefactory');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-esupplier','N/A (On Prem)');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-keycloak-usermanager','N/A (On Prem)');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-payments-framework','N/A (On Prem)');
INSERT INTO project_aws_stack (project,aws_services) values ('myworkplace-launchpad','N/A (On Prem)');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-bpm','SNS');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-bpm','EC2');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-bpm','Elasticache');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-bpm','Cloudwatch');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5portals','N/A (On Prem)');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-cloud-files','N/A (On Prem)');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UI','EC2');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UI','ECS');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UI','ECR');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UI','CloudWatch');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UI','Secrets Manager');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UI','Systems Manager');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UI','RDS - Postgres');
INSERT INTO project_aws_stack (project,aws_services) values ('pse-e5UI','Code Artefactory');

--

INSERT INTO project_tech_stack (project,other_tech) values ('pse-keycloak-usermanager','Mosaic 3.1.8');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-keycloak-usermanager','SQL Server v2019');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-payments-framework','In memory embedded Redis DB');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-e5UIPOC','Mosaic 3.1.8');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-e5UIPOC','Postgres 11');
INSERT INTO project_tech_stack (project,other_tech) values ('myworkplace-launchpad','Mosaic 3.1.8');
INSERT INTO project_tech_stack (project,other_tech) values ('myworkplace-launchpad','Oracle 19C (12.2.0.3)');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-bpm','NodeJS');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-bpm','VueJS');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-e5portals','NodeJS');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-e5portals','VueJS');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-cloud-files','NodeJS');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-cloud-files','VueJS');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-esupplier','Struts2 v2.5.26');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-e5UI','Html');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-e5UI','CSS');
INSERT INTO project_tech_stack (project,other_tech) values ('pse-e5UI','Javascript');
