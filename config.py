import os
from urllib.parse import quote_plus

password = quote_plus("OeggxjMExYrwD8kR")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"postgresql://postgres:{password}@db.jmwkgzopgtpjgvgrcuap.supabase.co:5432/postgres"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False