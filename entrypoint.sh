
# Wait for the database to become available
echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started."

echo "Running migrations..."
python manage.py makemigrations blogapp
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/tags.json
python manage.py loaddata fixtures/blogs.json

echo "Starting Django server..."
exec "$@"
