import urllib.request
import json

def test():
    # 1. Login
    req = urllib.request.Request(
        "http://127.0.0.1:8000/api/auth/login",
        data=json.dumps({"email": "demo@careerpath.ai", "password": "Demo@123"}).encode(),
        headers={"Content-Type": "application/json"}
    )
    res = urllib.request.urlopen(req)
    data = json.loads(res.read().decode())
    token = data["access_token"]
    print("[*] Logged in successfully as:", data["user"]["name"])

    # 2. Test Dashboard
    dash_req = urllib.request.Request(
        "http://127.0.0.1:8000/api/dashboard",
        headers={"Authorization": f"Bearer {token}"}
    )
    dash_res = json.loads(urllib.request.urlopen(dash_req).read().decode())
    print("[*] Dashboard data:", dash_res["student_name"], "| Target:", dash_res["target_role_title"], "| Readiness:", dash_res["job_readiness"], "%")

    # 3. Test Skill Gap
    gap_req = urllib.request.Request(
        "http://127.0.0.1:8000/api/skill-gap/analyze",
        data=json.dumps({}).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    )
    gap_res = json.loads(urllib.request.urlopen(gap_req).read().decode())
    print("[*] Skill gap analysis:", gap_res["job_role_title"], "| Match:", gap_res["overall_match_score"], "% | Gaps count:", gap_res["gap_skills_count"])

    # 4. Test ML Explanation
    exp_req = urllib.request.Request(
        "http://127.0.0.1:8000/api/readiness/explanation",
        headers={"Authorization": f"Bearer {token}"}
    )
    exp_res = json.loads(urllib.request.urlopen(exp_req).read().decode())
    print("[*] Top positive factor:", exp_res["positive_factors"][0]["name"], exp_res["positive_factors"][0]["impact"])

    # 5. Test Model Metrics
    model_req = urllib.request.Request("http://127.0.0.1:8000/api/models/metrics")
    model_res = json.loads(urllib.request.urlopen(model_req).read().decode())
    print("[*] ML Best Model:", model_res["best_model_name"], "| Accuracy:", model_res["best_model_metrics"]["accuracy"])

    print("[SUCCESS] All core backend APIs tested and verified!")

if __name__ == "__main__":
    test()
