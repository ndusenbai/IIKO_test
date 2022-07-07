# IIKO_test

создать вертуальную среду
  python -m venv env
  
устанаваить бибтеотеки с requirements.txt

и запустить проект в вертуальной среде

Использывал
  PYTHON 3.10
  Django
  SQLite3
  
![image](https://user-images.githubusercontent.com/77536930/177697391-f6663ceb-4bdf-41a4-a676-199f056de6c0.png)
это файл (data.ipynb) для рандомного создания более 50000 сотруников  

superuser
  login:admin
  password:admin
  
![image](https://user-images.githubusercontent.com/77536930/177697753-16c533cf-cef4-4a00-8389-8745291b5d65.png)
это главная страница без авторизации. Вы можите войти с данными superuser или пройти регистрацию 


после удачной ауторизации. Вы длжни видить сотрудников с данными(там лиш данные 100 сотруников). Так как я не мог полностю реализовать pagination, решил просто сделать запрос для 100 сотруников. 
![image](https://user-images.githubusercontent.com/77536930/177698091-c845e233-c14d-4b04-9ddc-c8a1bd562174.png)

в DROPDOWN есть рабочие 2 вкладкий это ADD Employee и API
![image](https://user-images.githubusercontent.com/77536930/177698852-2f40ae64-6fef-433c-818e-91cb74f444b3.png)


API был создан с помошю REST FRAMWORK, и pagination 100 для page 
![image](https://user-images.githubusercontent.com/77536930/177698998-a2bf4704-a08c-45b4-b450-32f3c06a5cbf.png)


Сотрудника можно добавить только авторизованный пользователь 
![image](https://user-images.githubusercontent.com/77536930/177699391-3a4c173c-0622-4763-bc6d-a08afd9abd17.png)

