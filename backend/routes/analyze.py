from fastapi import APIRouter, UploadFile, File
from backend.services.parser import parse_text
from backend.services.detector import detect_patterns
from backend.services.risk_engine import calculate_risk
from backend.services.insights import generate_insights
from backend.services.masker import mask_data
from backend.services.policy_engine import apply_policy
from backend.services.parser import parse_by_type
from backend.services.log_analyzer import analyze_logs


router = APIRouter()

@router.post("/analyze")
def analyze(input_type: str, content: str):

    options = {
        "mask": True,
        "block_high_risk": True,
        "log_analysis": True
    }

    lines = parse_by_type(input_type, content)

    if input_type == "log":
        findings = analyze_logs(content)
    else:
        findings = []
        for i, line in enumerate(lines, start=1):
            findings.extend(detect_patterns(line, i))

    risk_score, risk_level = calculate_risk(findings)

    action = apply_policy(risk_level, options)

    insights = generate_insights(findings)

    masked_content = mask_data(content)

    return {
        "summary": "Analysis completed",
        "content_type": input_type,
        "findings": findings,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "action": action,
        "insights": insights,
        "masked_content": masked_content
    }

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    content = content.decode("utf-8")

    from backend.services.log_analyzer import analyze_logs
    from backend.services.risk_engine import calculate_risk
    from backend.services.insights import generate_insights
    from backend.services.masker import mask_data

    findings = analyze_logs(content)
    score, level = calculate_risk(findings)
    insights = generate_insights(findings)
    masked = mask_data(content)

    return {
        "summary": "File analyzed successfully",
        "content_type": "log",
        "findings": findings,
        "risk_score": score,
        "risk_level": level,
        "insights": insights,
        "masked_content": masked
    }