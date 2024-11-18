# from fastapi import FastAPI, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from datetime import datetime, timedelta

# app = FastAPI()

# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # Password hashing context
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# users_db = {}

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def authenticate_user(username: str, password: str):
#     user = users_db.get(username)
#     if user and verify_password(password, user['password']):
#         return user
#     return None

# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# @app.post("/register")
# async def register(form_data: OAuth2PasswordRequestForm = Depends()):
#     username = form_data.username
#     if username in users_db:
#         raise HTTPException(status_code=400, detail="User already exists")
#     hashed_password = get_password_hash(form_data.password)
#     users_db[username] = {"password": hashed_password}
#     return {"msg": "User registered"}

# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     access_token = create_access_token(data={"sub": form_data.username})
#     return {"access_token": access_token, "token_type": "bearer"}

# @app.get("/users/me")
# async def read_users_me(token: str = Depends(oauth2_scheme)):
#     return {"token": token}
