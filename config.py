from urllib.parse import quote_plus

password = quote_plus("ua5/m-,x!z_a3HW")

class Config:
    SECRET_KEY = "mysecretkey"

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://postgres:{password}@"
        "db.jmwkgzopgtpjgvgrcuap.supabase.co:5432/postgres"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False