# Quant Position Tracker (v1.0)

## Project Roadmap

### 1. Project Goal

Build a robust system to manage and track quant-related job positions, improve data entry efficiency with LLM-based parsing, and provide administrative and personal dashboards with role-based access control.

### 2. 




# Detailed Setup

---

## 1. Environment

### 1-1. Development Stack

| Layer         | Tech Stack                         |
|---------------|------------------------------------|
| Backend       | FastAPI, SQLAlchemy, PostgreSQL    |
| Frontend      | Next.js, Tailwind CSS              |
| Auth          | JWT                                |
| Parsing       | OpenAI GPT-4o API                  |
| DevOps        | Railway (API + DB) and Vercel (FE) |
| Testing       | Pytest, HTTPX, Faker               |
| Other         | dotenv, Alembic, Docker (TBD)      |


### 1-2. Local Dev Environment Setup

| Component          | Tool / Setup                                |
|--------------------|---------------------------------------------|
| OS                 | macOS (15.4)                                |
| IDE                | PyCharm                                     |
| Python             | 3.12                                        |
| DB                 | PostgreSQL                                  |
| Package Manager    | `pip` + `virtual env`                       |

---

## 2. Project Tree

```bash
QuantPositions/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── crud/
│   ├── routers/
│   ├── core/
│   └── services/
├── sql/init/
├── tests/
├── .env
├── requirements.txt
├── README.md
├── Dockerfile (optional)
└── .github/workflows/
```

## 3. Database

### 3-1. Schema

DB name: `quantpositions` <br>
Env: Postgres SQL

| Table       | Description                                         |
|-------------|-----------------------------------------------------|
| `users`     | Stores user account data, role, and hashed password |
| `companies` | Stores metadata about hiring companies              |
| `positions` | Represents open job opportunities                   |
| `applied`   | Associative table for tracking user applications    |

---

### 3-2. Table Definitions

#### 1) `users`

Stores user profiles and access credentials.

| Column          | Type           | Description                                                          |
|-----------------|----------------|----------------------------------------------------------------------|
| `usrid`         | `varchar(50)`  | Primary key — user ID                                                |
| `email`         | `varchar(255)` | Unique, not null                                                     |
| `first_name`    | `varchar(100)` | First name                                                           |
| `last_name`     | `varchar(100)` | Last name                                                            |
| `school`        | `varchar(100)` | School Info                                                          |
| `level`         | `varchar(20)`  | Intern, NewGrad, Junior, Senior, VP                                  |
| `password_hash` | `text`         | Securely stored password                                             |
| `auth`          | `varchar(50)`  | User role `read`, `edit`, `admin`                                    |
| `created_at`    | `timestamp`    | Default: now()                                                       |
| `updated_at`    | `timestamp`    | Default: now()                                                       |
| `cover_letter`  | `text`         | Personalized cover letter form to automate filling out cover letters |

---

#### 2) `companies`

| Column        | Type           | Description                                |
|---------------|----------------|--------------------------------------------|
| `cpid`        | `varchar(50)`  | Primary key — company ID                   |
| `cpname`      | `varchar(255)` | Company name                               |
| `industry`    | `varchar(50)`  | Industry classification                    |
| `importance`  | `int`          | Priority level (1=top, 2=mid, 99=optional) |
| `headquarter` | `varchar(100)` | Location of HQ                             |
| `created_at`  | `timestamp`    | Default: now()                             |
| `updated_at`  | `timestamp`    | Default: now()                             |
| `updated_by`  | `varchar(20)`  | Auditor's name (e.g., admin email)         |

**Notes:**
- cpid examples: CTDSEC - Citdadel Securities
- Check: `industry` field must be either {`HedgeFund`, `QuantTrading`, `AssetManagement`, `InvestmentBank`, `CommercialBank`, `FinancialServices`, `Insurance`, `FinancialAdvisor`, `Fintech`, `Technology`, `Exchange`, `Consulting`, `PensionFund`, `Etc`}

---

#### 3) `positions`

Represents individual job postings.

| Column       | Type           | Description                           |
|--------------|----------------|---------------------------------------|
| `cpid`       | `varchar(50)`  | Foreign key to `companies.cpid`       |
| `pztid`      | `varchar(50)`  | Primary key — position ID             |
| `pztname`    | `varchar(255)` | Job title                             |
| `pztlevel`   | `varchar(20)`  | Intern, NewGrad, Junior, Senior, VP   |
| `year`       | `int`          | Target year - starting from May 1     |
| `url`        | `text`         | URL to job posting                    |
| `jd`         | `text`         | Job description (long text)           |
| `note`       | `text`         | Additional Notes                      |
| `active`     | `boolean`      | Whether this posting is still open    |
| `deadline`   | `timestamp`    | Application Deadline                  |
| `updated_by` | `varchar(100)` | Audit trail                           |
| `created_at` | `timestamp`    | Default: now()                        |
| `updated_at` | `timestamp`    | Default: now()                        |

**Notes:**
- cpid examples: CTDL
- ptzid examples: 20250330_intern_1
- created_at: decide who take the OA first using a modula operation
- updated_at: decide the recent OAs (up to 7 days before)
- year: define the year based on the date May 1 ( i.e. [May 1 2024, May 1 2025] = 2024 year )
- Check: `pztlevel` in {Intern, NewGrad, Associate, Senior, VP}
- Referenced by: `applied`

---

#### 4) `applied`

Tracks which users have applied to which positions.

| Column       | Type                | Description                               |
|--------------|---------------------|-------------------------------------------|
| `usrid`      | `varchar(50)`       | Foreign key to `users.usrid`              |
| `cpid`       | `varchar(50)`       | Foreign key to `companies.cpid`           |
| `pztid`      | `varchar(50)`       | Foreign key to `positions.pztid`          |
| `applied`    | `boolean`           | True if the user submitted an application |
| `applied_at` | `timestamp`         | Time of application                       |

---

## Constraints

| Field       | Enum Values                                                                                                                                                                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `users.level`, `positions.pztlevel` | Intern, NewGrad, Associate, Senior, VP                                                                                                                                                |
| `companies.industry` | HedgeFund, QuantTrading, AssetManagement, InvestmentBank, CommercialBank, FinancialServices, Insurance, FinancialAdvisor, Fintech, Technology, Exchange, Consulting, PensionFund, Etc |
| `companies.importance` | 1 (top tier), 2 (secondary), 99 (unranked)                                                                                                                                            |
| `users.autho` | read, edit, admin                                                                                                                                                                     |

---

## Detailed Project Roadmaps

Read Roadmap.md file



## Phase 1 – Initialization & DB Schema Setup (Completed)

### Tasks:
- [x] Initialize project structure in PyCharm.
- [x] Create PostgreSQL schema via SQL script.
- [x] Add sample data and validate using `review_init_db.py`.

### Files:
- `sql/init/quantpositions_schema.sql`
- `sql/init/test/sample1.sql`
- `sql/init/test/review_init_db.py`
- `.env` with `DATABASE_URL`

---

## 🔐 Phase 2 – Authentication & Role-Based Access

### Tasks:
- JWT-based login and signup using FastAPI's OAuth2PasswordBearer.
- Password hashing (`passlib` / `bcrypt`).
- User roles: `admin`, `read_only`.
- Token generation and validation utilities.
- Auth endpoints:
  - `POST /auth/signup`
  - `POST /auth/login`
  - `GET /auth/me`

### Files:
- `app/routers/auth.py`
- `app/core/security.py`
- `app/core/deps.py`
- `app/crud/users.py`
- `app/schemas/users.py`

---

## 🛠️ Phase 3 – Core CRUD APIs

### Tasks:
- Implement all CRUD endpoints:
  - `/users/`, `/companies/`, `/positions/`, `/applied/`
- Filtering:
  - `/positions?industry=QuantTrading&level=Intern`
- Business Logic:
  - `oa_first` flag logic
- Protect endpoints by role (`Depends(get_current_user)`)

### Files:
- `app/crud/` (users.py, positions.py, companies.py, applied.py)
- `app/routers/` (same structure)
- `app/schemas/` (Pydantic I/O models)
- `app/models/` (SQLAlchemy DB models)

---

## 💻 Phase 4 – Frontend with Next.js (Planned)

### Pages to Build:
- Login / Signup
- Dashboard (positions in the last 7 days)
- Full DB view with sorting/filtering
- Applied status view per user
- URL submission + preview via LLM

### Components:
- `PositionTable.tsx`, `JobUpload.tsx`, `JobPreviewModal.tsx`, `AppliedStatus.tsx`

### Notes:
- Use `Zustand` or `React Query` for state/API
- Use JWT in localStorage or secure HTTP-only cookie

---

## 🤖 Phase 5 – LLM Integration for Job Parsing

### Tasks:
- Extract job title, visa, deadline, level, etc. from a job posting URL.
- Use Playwright or BeautifulSoup to fetch HTML (optional pre-parsing).
- Send cleaned text to GPT API.
- Show preview table in frontend → confirm → insert to DB.

### Files:
- `app/services/llm_extraction.py`
- `app/routers/llm.py`
- `app/schemas/llm.py`

### Endpoint:
- `POST /llm/extract_from_url` → returns JSON with extracted fields

---

## 🧪 Phase 6 – Testing with Pytest

### Tasks:
- Write unit + integration tests for:
  - Auth (success/fail)
  - CRUD endpoints
  - LLM API (mocked)
- Use `conftest.py` for:
  - Test DB session
  - Dependency overrides

### Files:
- `tests/conftest.py`
- `tests/test_auth.py`
- `tests/test_users.py`
- `tests/test_positions.py`
- `tests/test_llm.py` (optional)

---

## 🚀 Phase 7 – CI/CD & Deployment

### Backend:
- Deploy FastAPI + PostgreSQL on [Railway](https://railway.app)
- Use `.env` or Railway secrets
- Dockerfile (if using)

### Frontend:
- Vercel auto-deploy from `main` branch

### GitHub Actions:
- Run Pytest on PR
- Deploy if tests pass

### Files:
- `.github/workflows/backend.yml`
- `Dockerfile`
- `vercel.json`

---

## 🧠 Phase 8 – Advanced Features (Optional)

| Feature           | Details                                                   |
|------------------|------------------------------------------------------------|
| Email Alerts     | Notify user 3 days before application deadlines            |
| Resume Matching  | Score JD vs Resume via LLM or similarity model             |
| Admin Analytics  | Dashboard for job stats, company pipelines, user activity  |
| Job Scraper      | Auto-fetch jobs from known job boards via Playwright       |
| Role UI Controls | Frontend visibility toggles based on `autho`               |

---

## 🗓 Suggested Sprint Timeline (6 Weeks)

| Sprint | Scope                                    |
|--------|------------------------------------------|
| Week 1 | Setup, models, DB validation             |
| Week 2 | Auth endpoints, user CRUD                |
| Week 3 | Company/Position CRUD + filtering logic  |
| Week 4 | Frontend login + dashboard               |
| Week 5 | LLM integration + data entry             |
| Week 6 | CI/CD, testing, deployment, polish       |

---

## ✅ Summary

You now have a complete and production-ready roadmap tailored for:
- **macOS + PyCharm**
- Real-world database structure
- LLM integration from day one
- Fully testable and deployable architecture

---

### 📌 Want More?

I can provide:
- 🧪 Prewritten test cases  
- 🧰 Sample CRUD implementations  
- 📐 OpenAPI docs (Swagger schema)  
- 🧱 Dockerfile + docker-compose  
- 📊 ERD visualization in dbdiagram format  

Let me know what you’d like to generate next, and I’ll prepare it instantly.