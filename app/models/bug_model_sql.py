

from sqlalchemy.orm import (DeclarativeBase, Mapped, mapped_column)


class Base(DeclarativeBase):
    pass


class Bug(Base):

    __tablename__ = "Bugs"

    bug_id: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    root_cause: Mapped[str] = mapped_column()
    fix: Mapped[str] = mapped_column()
    severity:  Mapped[str] = mapped_column()
    module:  Mapped[str] = mapped_column()
    issue_type: Mapped[str] = mapped_column()
