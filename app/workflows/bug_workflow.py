from app.agents.classifier_agent import (
    classifer_agent
)

from app.agents.severity_agent import (
    severity_agent
)

from app.agents.jira_agent import (
    jira_agent
)


class BugWorkflow:

    def run(self, issue: str):

        try:

            classification = (
                classifer_agent.run(issue)
            )

        except Exception as e:
            return {
                "error": str(e)
            }

        try:
            severity = severity_agent.run(
                issue,
                classification["module"],
                classification["issue_type"]
            )
        except Exception as e:
            return {
                "error": str(e)
            }
        try:
            jira = (
                jira_agent.run(issue,
                               severity["severity"]
                               )
            )
        except Exception as e:
            return {
                "error": str(e)
            }

        return {
            "classification": classification,
            "severity": severity,
            "jira_ticket": jira
        }


bug_workflow = BugWorkflow()
