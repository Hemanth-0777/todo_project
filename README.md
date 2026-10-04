🚀 Django To-Do App Deployment on PythonAnywhere
A complete deployment guide for hosting a Django To-Do application on PythonAnywhere using GitHub, Virtual Environments, SQLite, and Django Static Files.

📋 Project Information
Item	Value
Project Name	todo_project
Framework	Django
Python Version	3.11
Django Version	5.2.x
Hosting Platform	PythonAnywhere
Database	SQLite
Domain	hemanth20051215.pythonanywhere.com
📂 Project Structure
todo_project/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── staticfiles/
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── todos/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/
1️⃣ Create PythonAnywhere Account
Create a free account on PythonAnywhere.
Login to Dashboard.
Open:

Dashboard → Consoles → Bash
2️⃣ Clone GitHub Repository
git clone https://github.com/Hemanth-0777/todo_project.git

cd todo_project
Verify:

ls
Expected:

manage.py
todo_project
todos
3️⃣ Create Virtual Environment
python3.11 -m venv myenv
Activate:

source myenv/bin/activate
Expected:

(myenv)
4️⃣ Install Dependencies
If requirements.txt exists:

pip install -r requirements.txt
Or manually:

pip install django
Verify:

pip list
5️⃣ Run Database Migrations
python manage.py migrate
Expected:

Applying...
OK
6️⃣ Configure settings.py
File:

todo_project/settings.py
✅ Configure ALLOWED_HOSTS
❌ Incorrect
ALLOWED_HOSTS = [*]
Error:

SyntaxError: Invalid star expression
✅ Correct
ALLOWED_HOSTS = [
    'hemanth20051215.pythonanywhere.com',
]
For testing only:

ALLOWED_HOSTS = ['*']
✅ Configure STAT*C_ROOT
❌ Error
Impro*erlyConfigured:
You're using the s*aticfiles app without having set t*e STATIC_ROOT setting
✅ F*x
STATIC_URL = 'static/*

STATIC_ROOT = BASE_DIR / 'static*iles'
✅ Recommended P*oduction Settings
DEBUG*= False

ALLOWED_HOSTS = [
    'he*anth20051215.pythonanywhere.com',
*

STATIC_URL = 'static/'

STATIC_R*OT = BASE_DIR / 'staticfiles'
*---

7️⃣ Collect Static Files
R*n:

python manage.py colle*tstatic
Type:

yes
``*

Expected:

```text
127 static fi*es copied to
'/home/hemanth2005121*/todo_project/staticfiles'
✅ tatic files successfully collected

8️⃣ Create PythonAnywhere*Web App
Open:

PythonAnyw*ere → Web
Click:

Add*a new web app
Select:

Manual Configuration
Python *ersion:

Python 3.11
*--

9️⃣ Configure Source Code Pa*h
Source Code:

/home/hem*nth20051215/todo_project
Work*ng Directory:

/home/heman*h20051215/todo_project
#*🔟 Configure Virtual Environment

*eb Tab → Virtualenv

/home*hemanth20051215/todo_project/myenv*```

Save.

---

# 1️⃣1️⃣ Configur* Static Files

Web Tab → Static Fi*es

Add:

```text
URL: /static/
``*

Directory:

```text
/home/hemant*20051215/todo_project/staticfiles
*``

Save.

---

# 1️⃣2️⃣ Configure*WSGI File

Open:

```text
Web → WS*I Configuration File
Remove PthonAnywhere's default "Hello Worl" code.

Replace with:

*mport os
import sys

path = '/home*hemanth20051215/todo_project'

if *ath not in sys.path:
    sys.path.*ppend(path)

os.environ.setdefault*
    'DJANGO_SETTINGS_MODULE',
   *'todo_project.settings'
)

from dj*ngo.core.wsgi import get_wsgi_appl*cation

application = get_wsgi_app*ication()
Save.

1️⃣3️* Validate Django Configuration
Ru*:

python manage.py check
*``

Expected:

```text
System chec* identified no issues
*️⃣4️⃣ Reload Application
Open:

*text PythonAnywhere → Web


Cl*ck:

```text
Reload
Wait a fe* seconds.

1️⃣5️⃣ Open Webs*te
Visit:

https://hemant*20051215.pythonanywhere.com
-*-

🛠 Common Errors & Solutions
*---

Error 1: STATIC_ROOT Missi*g
Error
ImproperlyCo*figured:
You're using the staticfi*es app without having set the STAT*C_ROOT setting
Fix
STATIC_ROOT = BASE_DIR / 'stat*cfiles'
Error 2: Inva*id Star Expression
Error
SyntaxError:
ALLOWED_HOSTS = [*]
Fix
ALLOWED_*OSTS = ['*']
or

AL*OWED_HOSTS = [
    'hemanth2005121*.pythonanywhere.com'
]
#* Error 3: Bad Request (400)

C*use
Improper ALLOWED_HOSTS config*ration.

Fix
ALLOWE*_HOSTS = [
    'hemanth20051215.pythonanywhere.com',
]
Then:

``*text Web → Reload


---

## Err*r 4: Static Files Not Loading

Run*

```bash
python manage.py collect*tatic
Verify:

/stati*/
/home/hemanth20051215/todo_proje*t/staticfiles
exists in Stati* Files Mapping.

Error 5: *00 Internal Server Error
Open:

*text PythonAnywhere → Web → Error*Log


Check the latest tracebac*.

---

## Error 6: ModuleNotFound*rror

Install missing packages:

`*`bash
pip install -r requirements.*xt
or

pip install pa*kage_name
Reload website.

--*

Error 7: Database Not Found
*un:

python manage.py migr*te
Verify:

db.sqlite*
exists.

🔄 Updating *ebsite After Code Changes
Pull la*est code:

cd ~/todo_proje*t

git pull origin main
Activ*te environment:

source my*nv/bin/activate
Run migration*:

python manage.py migrat*
Collect static files:

python manage.py collectstatic
`*`

Reload website:

```text
Web → *eload
🔧 Useful Comman*s
Activate Environment
source ~/todo_project/myenv/bin/a*tivate
Run Development Ser*er
python manage.py runse*ver
Apply Migrations
python manage.py migrate
#* Create Migrations

python*manage.py makemigrations
C*llect Static Files
python*manage.py collectstatic
Django System Check
python manage.py check
Pull Latest GitHub Changes
git pull origin main
🚦 Deployment Workflow
GitHub Repository
        │
        ▼
 Clone Repository
        │
        ▼
 Create Virtual Environment
        │
        ▼
 Install Requirements
        │
        ▼
 Run Migrations
        │
        ▼
 Configure settings.py
        │
        ▼
 Configure STATIC_ROOT
        │
        ▼
 collectstatic
        │
        ▼
 Create Web App
        │
        ▼
 Configure WSGI
        │
        ▼
 Configure Virtualenv
        │
        ▼
 Configure Static Files
        │
        ▼
 Reload Website
        │
        ▼
 Live Django Application
✅ Final Deployment Checklist
✅ PythonAnywhere account created
✅ Repository cloned from GitHub
✅ Virtual environment created
✅ Django installed
✅ Dependencies installed
✅ Database migrations completed
✅ ALLOWED_HOSTS configured
✅ STATIC_ROOT configured
✅ collectstatic completed
✅ WSGI configured
✅ Virtualenv configured
✅ Static files mapped
✅ Website reloaded
✅ Domain configured
✅ Application live
🎉 Deployment Successful
Your Django To-Do application is now ready to be hosted on PythonAnywhere.

Live URL

https://hemanth20051215.pythonanywhere.com
Whenever you update your GitHub project:

git pull origin main
python manage.py migrate
python manage.py collectstatic
Then click:

Web → Reload
and your changes will be live.
