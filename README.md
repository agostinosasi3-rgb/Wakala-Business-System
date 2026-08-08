# Wakala-Business-System
Aim to help my customers in my business of mobile phone transaction
Mfumo wa kisasa na wa kitaalamu wa kusimamia biashara ya mawakala wa fedha nchini Tanzania. Mfumo huu unakusaidia kufuatilia float za mitandao yote (M-Pesa, Mix by Yas / Halotel-Tigo, Airtel Money, Tigo Pesa, na Wakala wa Benki), pesa taslimu zilizopo kwenye droo (Cash in Hand), miamala ya kila siku, na kutoa ripoti kamili za faida au hasara za kila wiki na mwezi.

---

## 💡 Jinsi Mfumo Unavyofanya Kazi (System Workflow)

### 1. Usajili na Usimamizi wa Watumiaji (User & Role Management)
* **Owner (Mmiliki):** Ana uwezo wa kuona ripoti za faida/hasara, kukagua matumizi, na kudhibiti akaunti za mawakala.
* **Agent (Wakala):** Anaingia kwenye mfumo na kuanzisha siku ya kazi, kurekodi miamala ya wateja, na kufunga hesabu za siku.

---

### 2. Mzunguko wa Siku (Daily Session Lifecycle)

#### A. Kufungua Siku (Asubuhi)
Wakala akiingia asubuhi, anaingiza:
* **Float ya Asubuhi (Opening Float):** Kwa kila mtandao mmoja mmoja (mfano: M-Pesa = TZS 500,000, Mix by Yas = TZS 300,000, Airtel Money = TZS 200,000, Tigo Pesa = TZS 150,000).
* **Cash in Hand ya Asubuhi (Opening Cash):** Pesa taslimu zote zilizopo kwenye droo la duka (mfano: TZS 1,000,000).

#### B. Ukaguzi wa Mchana (Midday Check)
Wakala anaweza kuingiza hesabu za mchana ili kuhakikisha hakuna upungufu au kosa linaloendelea siku ikiwa katikati.

#### C. Kufunga Siku (Jioni / Closing)
Mwisho wa siku, wakala anahesabu na kuingiza:
* **Float ya Jioni (Closing Float):** Bakaa ya salio kwa kila mtandao.
* **Cash in Hand ya Jioni (Closing Cash):** Pesa taslimu zote zilizopo kwenye droo jioni.

---

### 3. Miamala na Kazi za Kila Siku (Transactions & Operations)
Kila muamala unapofanyika, wakala anarekodi:
* **Mitandao Inayohusika:** Kuchagua kama ni M-Pesa, Mix by Yas, Airtel Money, Tigo Pesa, au Benki Wakala.
* **Aina ya Muamala:** 
  * **Cash-In (Kuweka Pesa):** Ongezeko la Cash, Punguzo la Float ya mtandao husika.
  * **Cash-Out (Kutoa Pesa):** Punguzo la Cash, Ongezeko la Float ya mtandao husika.
  * **Float Rebalance / Till Transfer:** Kuhamisha float kati ya benki na mtandao.
* **Auto-Commission Engine:** Mfumo unatumia jedwali la viwango vya kamisheni (*Tariffs*) kukokotoa kamisheni inayotarajiwa (*Estimated Commission*) kwa kila muamala badala ya kusubiri mwisho wa mwezi.

---

### 4. Injection ya Kiotomatiki ya Reconciliation (Auto Reconciliation Engine)
Mfumo unafanya hesabu za kiotomatiki wakati wa kufunga siku:
* **Expected Float Calculation:**  
  $$\text{Expected Float} = \text{Opening Float} + \text{Total Cash-Outs} - \text{Total Cash-Ins}$$
* **Expected Cash Calculation:**  
  $$\text{Expected Cash} = \text{Opening Cash} + \text{Total Cash-Ins} - \text{Total Cash-Outs} - \text{Expenses}$$
* **Variance Alert:** Mfumo unalinganisha kiasi kilichoingizwa na kinachostahili kuwepo. Kama kuna punguzo au ziada (*Shortage / Excess*), mfumo unatoa alert na kurekodi kwenye **Audit Log**.

---

### 5. Ripoti za Kifedha (Weekly & Monthly Profit/Loss Reports)
* **Kipato cha Kamisheni:** Jumla ya kamisheni zilizopatikana kwenye kila mtandao.
* **Matumizi ya Duka (Expenses):** Kurekodi kodi ya pango, umeme, chakula, au usafiri.
* **Net Profit / Loss:**  
  $$\text{Net Profit} = \text{Total Commissions} - \text{Total Expenses} - \text{Shortages}$$

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python 3.11+), SQLAlchemy ORM, Pydantic, Passlib (Bcrypt), PyJWT
* **Database:** PostgreSQL / SQLite
* **Database Migrations:** Alembic
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)
* **Containerization:** Docker & Docker Compose

---




## ⚙️ Jinsi ya Kuendesha Mradi (Local Setup)

### 1. Kuandaa Backend

```bash
cd backend

# Tengeneza Virtual Environment
python -m venv venv
source venv/bin/activate  # Kwenye Windows: venv\Scripts\activate

# Weka Packages
pip install -r requirements.txt
# Tengeneza faili la .env kutokana na mfano
cp .env.example .env

# Endesha Server
uvicorn app.main:app --reload

###file structure
wakala-business-system/
│
├── backend/
│   ├── app/
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   ├── security.py
│   │   │   └── auth.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── provider.py
│   │   │   ├── daily_session.py
│   │   │   ├── transaction.py
│   │   │   ├── tariff.py
│   │   │   ├── expense.py
│   │   │   └── audit_log.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── user_schema.py
│   │   │   ├── provider_schema.py
│   │   │   ├── daily_session_schema.py
│   │   │   ├── transaction_schema.py
│   │   │   ├── expense_schema.py
│   │   │   └── report_schema.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   │   ├── provider_service.py
│   │   │   ├── session_service.py
│   │   │   ├── transaction_service.py
│   │   │   ├── reconciliation_service.py
│   │   │   └── report_service.py
│   │   │
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── auth_router.py
│   │   │   ├── provider_router.py
│   │   │   ├── session_router.py
│   │   │   ├── transaction_router.py
│   │   │   ├── expense_router.py
│   │   │   └── report_router.py
│   │   │
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── transactions.html
│   ├── reports.html
│   ├── css/
│   └── js/
│
└── README.md

