from app.models.retrieved_bug import (RetrievedBug)

class RetrievalService:

    def search(self, query: str) -> list[RetrievedBug]:
        return []
retrieval_service = RetrievalService()