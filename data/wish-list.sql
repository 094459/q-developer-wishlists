-- Users table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Gift lists table to store different lists created by users
CREATE TABLE gift_lists (
    list_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    list_name VARCHAR(255) NOT NULL,
    is_public BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- Gift items table to store items in gift lists
CREATE TABLE gift_items (
    item_id SERIAL PRIMARY KEY,
    list_id INTEGER NOT NULL,
    item_name VARCHAR(255) NOT NULL,
    description TEXT,
    item_url VARCHAR(2048) NOT NULL,
    is_purchased BOOLEAN DEFAULT false,
    purchased_at TIMESTAMP,
    purchased_by_user_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (list_id) REFERENCES gift_lists(list_id) ON DELETE CASCADE,
    FOREIGN KEY (purchased_by_user_id) REFERENCES users(user_id) ON DELETE SET NULL
);
