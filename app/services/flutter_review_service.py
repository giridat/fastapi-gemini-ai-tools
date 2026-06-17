from app.core.gemini_client import client


class FlutterReviewService:
    def review_code(self, code: str) -> str:
        prompt = f"""
         You are a senior Flutter architect.

        Review the following Flutter code.

        Identify:
        1. Bugs
        2. Performance issues
        3. Architecture improvements
        4. Best practices

        Code:

        {code}"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


flutter_review_service = FlutterReviewService()
