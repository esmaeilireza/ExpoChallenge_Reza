# Smart Waste Sorting Robot — ExpoChallenge

6-class waste classifier (plastic, paper, glass, metal, organic, other).
FastAPI + YOLOv8 + SQLite + Bootstrap. Trained on Colab, inference local.

## Structure
- `api/`    FastAPI backend
- `model/`  YOLOv8 inference & weights loader
- `data/`   dataset pipeline (TrashNet → 6-class)
- `ui/`     Bootstrap frontend
- `tests/`  pytest suite
- `db/`     SQLite schema & helpers

## Workflow
Trunk-based. Branch `feature/<task>`, PR into `main`. Branches ≤ 1 day.
Run `pytest` before every merge.

## Sprint
9-day sprint — Phase 1: Setup.

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn api.main:app --reload
```

`requirements.txt`
```txt
fastapi==0.115.0
uvicorn[standard]==0.30.6
python-multipart==0.0.9
ultralytics==8.2.0
pytest==8.3.2
```