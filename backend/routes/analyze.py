from fastapi import APIRouter, UploadFile, File
from services.parser import parse_input
from services.log_analyzer import analyze_logs
from services.risk_engine import calculate_risk
from services.insights import generate_insights
from services.masker import mask_sensitive_data

router = APIRouter()

# ✅ FILE UPLOAD API (MAIN)
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = (await file.read()).decode("utf-8")

    parsed = parse_input(content)

    findings = analyze_logs(parsed)

    score, level = calculate_risk(findings)

    insights = generate_insights(findings)

    masked_content = mask_sensitive_data(parsed)

    return {
        "summary": "File analyzed successfully",
        "content_type": "log",
        "findings": findings,
        "risk_score": score,
        "risk_level": level,
        "action": "masked",
        "insights": insights,
        "masked_content": masked_content
    }


# ✅ TEXT INPUT API (OPTIONAL)
@router.post("/analyze")
async def analyze_text(content: str):
    parsed = parse_input(content)

    findings = analyze_logs(parsed)

    score, level = calculate_risk(findings)

    insights = generate_insights(findings)

    masked_content = mask_sensitive_data(parsed)

    return {
        "summary": "Analysis completed",
        "content_type": "text",
        "findings": findings,
        "risk_score": score,
        "risk_level": level,
        "action": "masked",
        "insights": insights,
        "masked_content": masked_content
    }