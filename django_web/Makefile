.ONESHELL:
migrate:
	cls
	if "$(app)"=="" (
		echo App name is required. Use: make migrate app=your_app_name
		exit /b 1
	) else (
		python manage.py makemigrations $(app) && python manage.py migrate
	)
create:
	cls
	if "$(app)"=="" (
		echo App name is required.
		exit /b 1
	) else (
		python manage.py startapp $(app)
	)
genuser:
	cls
	python manage.py createsuperuser