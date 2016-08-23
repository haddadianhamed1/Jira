from jira import JIRA
from getpass import getpass
 
def main():
    options = {
        'server': 'https://staging-jira.engsrv.mobileiron.com/',
	'verify': False
    }
    password = getpass()
    jira = JIRA(options, basic_auth=('hhaddadian', password))
 
    # Get the mutable application properties for this server (requires
    # jira-system-administrators permission)
    # props = jira.application_properties()
 
    # Find all issues reported by the admin
    issues = jira.search_issues('assignee=hhaddadian')
    print issues 
    # Find the top three projects containing issues reported by admin
    from collections import Counter
    top_three = Counter(
        [issue.fields.project.key for issue in issues]).most_common(3)
 
    
    new_issue = jira.create_issue(project='IS', summary='New issue form Jira-python', description='look into this python', issuetype={'name': 'Task'})



if __name__ == "__main__":
    main()
