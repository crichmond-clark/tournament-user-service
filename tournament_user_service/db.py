import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine, select
from sqlalchemy.orm.exc import NoResultFound, IntegrityError

from .models import User, Profile

load_dotenv()

turso_url = os.environ.get("TURSO_URL")

db = create_engine(turso_url, echo=True)


async def get_all_users() -> list[User]:
    try:
        with Session(db) as session:
            statement = select(User)
            users = session.exec(statement)
            return users
    except NoResultFound:
        return None


async def get_user(user_id: int) -> User:
    try:
        with Session(db) as session:
            statement = select(User).where(User.id == user_id)
            user = session.exec(statement).first()
            return user
    except NoResultFound:
        return None


async def create_user(user: User) -> User:
    try:
        user = User(**user)
        profile = Profile(user_id=user.id)
        with Session(db) as session:
            session.add(user)
            session.add(profile)
            session.commit()
            return user
    except IntegrityError:
        return None


async def update_user(user: User) -> User:
    try:
        with Session(db) as session:
            statement = select(User).where(User.id == user.id)
            user = session.exec(statement).one()
            [
                setattr(user, key, value)
                for key, value in user.items()
                if key != "profile"
            ]
            session.commit()
            return user
    except NoResultFound:
        return None


async def delete_user(user_id: int) -> User:
    try:
        with Session(db) as session:
            statement = select(User).where(User.id == user_id)
            user = session.exec(statement).one()
            session.delete(user)
            session.commit()
            return user
    except NoResultFound:
        return None
