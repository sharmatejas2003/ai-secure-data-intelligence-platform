from fastapi import APIRouter
from services.parser import parse_text
from services.detector import detect_patterns
from services.risk_engine import calculate_risk
from services.insights import generate_insights
from services.masker import mask_data
from services.policy_engine import apply_policy

router = APIRouter()

@router.post("/analyze")
def analyze(input_type: str, content: str):

    options = {
        "mask": True,
        "block_high_risk": True,
        "log_analysis": True
    }

    lines = parse_text(content)

    findings = []
    for i, line in enumerate(lines, start=1):
        findings.extend(detect_patterns(line, i))

    risk_score, risk_level = calculate_risk(findings)

    action = apply_policy(risk_level, options)

    insights = generate_insights(findings)

    masked_content = mask_data(content) if action == "masked" else content

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