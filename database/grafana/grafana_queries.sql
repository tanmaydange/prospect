SELECT "dependency",  "cvss_score", "cvss_severity","current_version", "fix_version" FROM VULNERABILITY_HIST WHERE issue_type = 'Security Issue' order by cvss_score DESC,dependency;

select z.product_name, a.project,a.SECURITY_ISSUE,b.QUALITY_ISSUE,c.LICENSE_ISSUE from PRODUCTS z left join
(select project, count(*) as SECURITY_ISSUE from VULNERABILITY_HIST where  issue_type="Security Issue" group by project) a
on z.product_name=a.project 
left join
(select project, count(*) as QUALITY_ISSUE from VULNERABILITY_HIST where  issue_type="outdated dependency" group by project) b
on z.product_name=b.project
left join 
(select project, count(*) as LICENSE_ISSUE from VULNERABILITY_HIST where  issue_type="unlicensed dependency" group by project) c
on z.product_name=c.project 
group by z.product_name;


select a.cvss_severity as SEVERITY, FIXABLE, NO_FIX , (FIXABLE+ NO_FIX) as TOTAL from (
select cvss_severity , count(*) as NO_FIX from VULNERABILITY_HIST WHERE  project="$project_name" and  fix_version="NO_SAFE_VERSION" group by cvss_severity
) a,
(select cvss_severity, count(*) as FIXABLE from VULNERABILITY_HIST WHERE  project="$project_name" and  fix_version!="NO_SAFE_VERSION" group by cvss_severity
) b where a.cvss_severity=b.cvss_severity group by SEVERITY;

