from sqlalchemy.orm import Session

from core.security import hash_password, verify_password
from models.user_model import User
from schema.userSchema import UserCreate


def create_user(db: Session, user: UserCreate) -> User:
	existing_user = db.query(User).filter(User.email == user.email).first()
	if existing_user:
		raise ValueError("Email already registered")

	new_user = User(
		username=user.username,
		email=user.email,
		password=hash_password(user.password),
	)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user


def authenticate_user(db: Session, email: str, password: str) -> User | None:
	db_user = db.query(User).filter(User.email == email).first()
	if not db_user:
		return None
	if not verify_password(password, db_user.password):
		return None
	return db_user
