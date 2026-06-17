from fastapi import APIRouter


from app.models.flutter_review_model import FlutterReviewRequest
from app.services.flutter_review_service import flutter_review_service
print("Flutter Review Router Loaded")
router = APIRouter(
    prefix="/flutter-review",
    tags=["Flutter Review"]
)



@router.post("")
def review_flutter_code(
    request: FlutterReviewRequest
):

    review = flutter_review_service.review_code(
      request.code
    )

    return {
        "review":review
    }