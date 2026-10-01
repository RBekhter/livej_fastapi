from fastapi import FastAPI
from fastapi_pagination import add_pagination 
from fastapi.middleware.cors import CORSMiddleware
from app.routers import posts_django, groups, comments
from app.routers.auth_users import router as auth_users_router

# 1. Описываем функцию жизненного цикла (lifespan)
async def lifespan(app: FastAPI):
    # Код, который выполнится до старта приложения
    yield
    # Код, который выполнится после завершения

# 2. Создаем ЕДИНСТВЕННЫЙ экземпляр приложения
app = FastAPI(title="livej_fastAPI", lifespan=lifespan)

# 3. НАСТРОЙКА CORS (Обязательно сразу после создания app)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Разрешаем наши адреса
    allow_credentials=True,      # Критично важно для кук
    allow_methods=["*"],         # Разрешаем все методы (GET, POST, OPTIONS и др.)
    allow_headers=["*"],         # Разрешаем любые заголовки
)

# 4. ПОДКЛЮЧАЕМ РОУТЕРЫ
app.include_router(auth_users_router)
app.include_router(posts_django.router)
app.include_router(groups.router)
app.include_router(comments.router)

# 5. ИНИЦИАЛИЗИРУЕМ ПАГИНАЦИЮ
add_pagination(app)
