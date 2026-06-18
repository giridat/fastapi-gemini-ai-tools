from app.agents.classifier_agent import (
    classifier_agent
)

from app.agents.severity_agent import (
    severity_agent
)

from app.agents.jira_agent import (
    jira_agent
)

from app.agents.planner_agent import (planner_agent)
from typing import Any


class BugWorkflow:

    def run(self, issue: str):

        try:

            plan = planner_agent.run(
                issue
            )

        except Exception as e:

            return {
                "issue": issue,
                "plan": None,
                "classification": None,
                "severity": None,
                "jira_ticket": None,
                "error": str(e)
            }
        if plan["run_classification"]:
            try:
                state["classification"] = (
                    classifier_agent.run(issue)
                )

            except Exception as e:

                state["error"] = str(e)

                return state
        if (plan["run_severity"] and state["classification"]):
            try:
                state["severity"] = (severity_agent.run(
                    issue,
                    state["classification"]["module"],
                    state["classification"]["issue_type"]
                ))
            except Exception as e:

                state["error"] = str(e)

                return state
        if (plan["run_jira"] and state["severity"]):

            try:
                state["jira_ticket"] = (
                    jira_agent.run(
                        issue,
                        state["severity"]["severity"]
                    )
                )

            except Exception as e:

                state["error"] = str(e)

                return state

        return state


bug_workflow = BugWorkflow()
