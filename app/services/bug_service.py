from app.database.database import SessionLocal
from app.models.bug_model_sql import Bug


class BugService:

    def get_all_bugs(self):
        session = SessionLocal()

        try:
            return session.query(Bug).all()
        finally:
            session.close()

    def create_bug(self, data):

        session = SessionLocal()
        try:
            bug = Bug(
                bug_id=data.bug_id,
                title=data.title,
                description=data.description,
                root_cause=data.root_cause,
                fix=data.fix,
                severity=data.severity,
                module=data.module,
                issue_type=data.issue_type
            )
            session.add(bug)
            session.commit()
            return bug
        except Exception as e:
             print(f"Something went wrong writing data: {e}")

             session.rollback()
             raise
        finally:
            session.close()

    def get_bug_by_id(self, bug_id: str):
        session = SessionLocal()
        try:

            return (
                session.query(Bug).filter(Bug.bug_id == bug_id).first()
            )

        finally:
            session.close()

    def delete_bug(self, bug_id: str):
        session = SessionLocal()

        try:

            bug = (
                session.query(Bug).filter(Bug.bug_id == bug_id).first()
            )
            if not bug:
                return False
            session.delete(bug)
            session.commit()
            return True
        finally:
            session.close()

    def update_bug(self, bug_id: str, data):
        session = SessionLocal()

        try:
            bug = (session.query(Bug).filter(Bug.bug_id == bug_id).first())
            if not bug:
                return None

            bug.title = data.title
            bug.description = data.description
            bug.root_cause = data.root_cause
            bug.fix = data.fix
            bug.severity = data.severity
            bug.module = data.module
            bug.issue_type = data.issue_type
            session.commit()

            session.refresh(bug)

            return bug
        finally:
            session.close()


bug_service = BugService()
