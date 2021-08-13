# admin
Docker Django REST framework

# Clone the project
`mkdir admin` 
`cd admin`
`git init`
`touch README.md`
`git add README.md`
`git commit -m "first commit"`
`git remote add origin git@github.com:lizhen/admin.git`
`git clone git@github.com:lizhen/admin.git` 
`git push -u origin master`


# Start the VS code
`code .`

# Create a virtual environment to isolate our package dependencies locally
`python -m venv venv`
`source venv/bin/activate` 
## On Windows use 
1. 已管理员身份打开PowerShell，输入下列指令以获取有效的执行策略列表：
`PS D:\workspase\admin> Get-ExecutionPolicy -List`
2. 输入以下指令设置执行策略：
`PS D:\workspase\admin> Set-ExecutionPolicy RemoteSigned`
3. 激活虚拟环境：
`PS D:\workspase\admin\venv\Scripts> .\activate`
4. 激活成功:
`(venv) PS D:\workspase\admin\venv\Scripts>`

`.\venv\Script\activate`
# Install Django and Django REST framework into the virtual environment
`pip install django`
`pip install djangorestframework`

# Set up a new project with a single application
`django-admin startproject admin .` # Note the trailin '.' character
`cd admin`
`django-admin startapp admin`
`cd ..`

# Start the application
`python manage.py runserver`

`touch Dockerfile`
`touch docker-compose.yml`

`pip freeze > requirements.txt` # Install `pip install -r requirements.txt`

`docker-compose build`
`docker-compose up`


