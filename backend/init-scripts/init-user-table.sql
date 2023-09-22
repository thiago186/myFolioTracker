CREATE TABLE "users" (
    user_id UUID PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(50) UNIQUE NOT NULL,
    hashed_password VARCHAR(250) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT current_timestamp,
    last_login TIMESTAMP,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,
    role VARCHAR(30) NOT NULL
);
