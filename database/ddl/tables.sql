create table VULNERABILITY_HIST (project,dependency,details,current_version,issue_type,cve,cvss_score,cvss_severity,name,fix_version, scan_date);
create table PRODUCTS (product_name);
create table project_java_stack(project,java_version,spring_version,spring_boot_version);
create table project_aws_stack(project,aws_services);
create table project_tech_stack(project,other_tech);
