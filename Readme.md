Blog project created using Django, Django REST framework and react as frontend. Frontend fetches all info from API and then shows it.

Blog contains 3 pages:
1. Homepage. Shows 3 last blogs with their thumb images
2. Blog detail. Shows all information about one blog with it`s full_image. 
3. Tag search details. Shows all blogs that contain specific tag with their thumb images.

How to run server using Docker:
1. Download docker, start it
2. In project directory run command: docker-compose up --build

Tests are running on gitlab: https://gitlab.com/ctanislavkrohmal2/blog_test_task

You can access api by these endpoints:
1. /api/blogs/ POST. Create blog. Example of input JSON:
2. {'title': 'New Blog', 'content': 'New Content', 'tags': [1], 'full_image': 'path_to_image'}
3. /api/tags/ POST. Create tag. Example of input JSON: {"name": "tagname"} 
4. /api/blogs/blog_id/ GET. Get specific blog. Response contains all information about blog
5. /api/blogs-by-tag/sample-tag/ GET. Get all blogs by tag. Response contains all blogs to that tag.
6. /api/blogs/latest_blogs/ GET. Returns 3 latest blogs.

If you want to run server on local machine, you have to:
1. Change in settings.py default value for name, user and password to data from your database.
2. Install dependencies by running command: pip install -r requirements.txt
3. Run commands: python manage.py makemigrations and python manage.py migrate
4. Run server by python manage.py runserver

You can create test data by doing these steps:
1. Run generate_fixtures.py
2. python manage.py loaddata fixtures/tags.json
3. python manage.py loaddata fixtures/blogs.json 