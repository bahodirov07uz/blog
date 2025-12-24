## Django Portfolio & Blog

A modern, black-and-white, TailwindCSS-powered personal portfolio and blog built with Django.

### Running locally

1. **Create and activate a virtualenv (PowerShell on Windows):**

```powershell
cd C:\Users\User\Desktop\blog
python -m venv .venv
.venv\Scripts\activate
```

2. **Install dependencies:**

```powershell
pip install -r requirements.txt
```

3. **Apply migrations:**

```powershell
python manage.py migrate
```

4. **Create a superuser for the admin:**

```powershell
python manage.py createsuperuser
```

5. **Run the development server:**

```powershell
python manage.py runserver
```

6. **Access the site:**

- Frontend: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

### Managing content

- **Home hero copy**: `SiteHero` in the `pages` app.
- **About sections + images**: `AboutSection` and inline `AboutSectionImage` in `pages`.
- **Projects, tech badges, gallery**: `Project`, `TechTag`, and inline `ProjectImage` in `projects`.
- **Blog posts + gallery images**: `BlogPost` and inline `BlogImage` in `blog`.

Media uploads are stored under the `media/` directory and served in development via `MEDIA_URL`/`MEDIA_ROOT` configured in `config/settings.py`.


