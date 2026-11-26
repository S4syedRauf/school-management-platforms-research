#!/usr/bin/env python3
"""Extract structured competitive evidence from every platform dossier in the repo."""
import glob, json, os, sys
from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI

MODEL = "gpt-6-luna"
OUT = "/home/ubuntu/v2/extract"
os.makedirs(OUT, exist_ok=True)
client = OpenAI()

CAPS = ["admissions_crm", "online_enrollment", "student_records", "guardian_household", "attendance",
        "biometric_rfid_qr_attendance", "timetable_auto_scheduling", "cover_substitution", "gradebook",
        "standards_competency_grading", "exams_management", "report_cards_transcripts", "lms_homework",
        "curriculum_planning", "parent_app", "student_app", "teacher_mobile_app", "messaging_sms_email_push",
        "whatsapp", "multilingual_ui", "fees_billing", "online_payments", "accounting_ledger", "payroll_hr",
        "recruitment", "transport_gps", "hostel", "library", "inventory_assets", "health_medical",
        "behavior_pastoral", "safeguarding", "special_education_iep", "mtss_early_warning",
        "analytics_dashboards", "custom_report_builder", "genai_assistant", "predictive_analytics",
        "government_statutory_reporting", "accreditation_obe", "higher_ed_registration_degree_audit",
        "financial_aid_scholarships", "alumni_advancement_fundraising", "marketing_website_cms", "open_api",
        "standards_oneroster_lti_edfi", "sso", "offline_mode", "nocode_workflow_automation",
        "marketplace_plugins", "multi_campus_group", "data_export_portability", "visitor_management",
        "canteen_cashless", "placements_careers", "research_management"]
LEVELS = ["full", "partial", "none_or_not_documented"]
CLUSTERS = ["cost_pricing", "complexity_usability", "support_implementation", "dated_ui_mobile",
            "reporting_rigidity", "lockin_migration", "security_privacy", "local_compliance_gaps",
            "connectivity_offline_language", "fragmented_tools", "ai_shallow_or_risky",
            "performance_reliability", "product_uncertainty_ownership", "segment_limited", "other"]
ROLES = ["owner_trustee_group_ceo", "principal_head", "academic_coordinator", "front_office_admin",
         "admissions_counsellor", "accountant_bursar", "exam_controller_registrar", "dean_hod",
         "accreditation_iqac", "teacher_faculty", "counsellor_senco_safeguarding", "transport_manager",
         "hostel_warden", "librarian", "hr_manager", "it_data_manager", "parent", "student",
         "alumni", "government_inspector"]

schema = {
    "type": "object", "additionalProperties": False,
    "required": ["platform", "segments", "coverage", "distinctive_features", "weaknesses",
                 "roles_well_served", "roles_poorly_served", "ai_features", "pricing_model_summary",
                 "biggest_strategic_gap"],
    "properties": {
        "platform": {"type": "string"},
        "segments": {"type": "array", "items": {"type": "string", "enum": [
            "preschool", "k12_public", "k12_private_independent", "international_ib", "higher_ed",
            "coaching_vocational", "multi_campus_group", "government"]}},
        "coverage": {"type": "object", "additionalProperties": False, "required": CAPS,
                     "properties": {c: {"type": "string", "enum": LEVELS} for c in CAPS}},
        "distinctive_features": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["feature", "why_it_matters"],
            "properties": {"feature": {"type": "string"}, "why_it_matters": {"type": "string"}}}},
        "weaknesses": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["issue", "cluster", "affected_role"],
            "properties": {"issue": {"type": "string"}, "cluster": {"type": "string", "enum": CLUSTERS},
                           "affected_role": {"type": "string", "enum": ROLES}}}},
        "roles_well_served": {"type": "array", "items": {"type": "string", "enum": ROLES}},
        "roles_poorly_served": {"type": "array", "items": {"type": "string", "enum": ROLES}},
        "ai_features": {"type": "array", "items": {"type": "string"}},
        "pricing_model_summary": {"type": "string"},
        "biggest_strategic_gap": {"type": "string"},
    },
}

SYS = ("You are a precise product analyst. Extract ONLY what the dossier supports. Coverage: 'full' if the dossier "
       "documents a native capability, 'partial' if limited/add-on/third-party/legacy, otherwise 'none_or_not_documented'. "
       "distinctive_features: up to 10 capabilities that are advanced or unusual vs typical school ERPs, each with a one-sentence "
       "why_it_matters for the institution. weaknesses: up to 10 concrete issues from Weaknesses/complaints/pricing/security "
       "sections, each mapped to a cluster and the role most affected. Keep every string under 30 words.")

def run(path):
    pid = os.path.basename(path)[:-3]
    dest = os.path.join(OUT, os.path.basename(os.path.dirname(path)) + "__" + pid + ".json")
    if os.path.exists(dest):
        return dest, "cached"
    text = open(path, encoding="utf-8").read()
    for attempt in range(6):
        try:
            r = client.chat.completions.create(
                model=MODEL, max_completion_tokens=4000,
                extra_body={"reasoning": {"effort": "low"}},
                messages=[{"role": "system", "content": SYS}, {"role": "user", "content": text}],
                response_format={"type": "json_schema",
                                 "json_schema": {"name": "dossier", "strict": True, "schema": schema}})
            data = json.loads(r.choices[0].message.content)
            data["_file"] = path.replace("/home/ubuntu/repo/", "")
            json.dump(data, open(dest, "w"), indent=1, ensure_ascii=False)
            return dest, "ok"
        except TypeError as e:
            err = str(r)[:300]; import time; time.sleep(30)
        except Exception as e:  # retry
            import time; time.sleep(20)
            err = str(e)
    return dest, "FAIL " + err[:200]

files = sorted(glob.glob("/home/ubuntu/repo/02-platform-profiles/*/*.md"))
files = [f for f in files if not f.endswith("README.md")]
with ThreadPoolExecutor(4) as ex:
    for d, s in ex.map(run, files):
        print(s, os.path.basename(d), flush=True)
