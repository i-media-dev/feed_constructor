CREATE_RC_TABLE = '''
CREATE TABLE IF NOT EXISTS residential_complex (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NULL,
    country VARCHAR(100) NULL,
    region VARCHAR(255) NULL,
    city VARCHAR(255) NULL,
    address_raw TEXT NOT NULL,
    latitude DECIMAL(10, 7) NULL,
    longitude DECIMAL(10, 7) NULL,
    is_virtual BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
UNIQUE KEY uq_rc_address_geo (
    address_raw(255),
    latitude,
    longitude
)
)
'''

CREATE_YANDEX_TABLE = '''
CREATE TABLE IF NOT EXISTS yandex_newbuilding (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    yandex_building_id VARCHAR(64) NOT NULL,
    yandex_house_id VARCHAR(64) NULL,
    name VARCHAR(255) NULL,
    region VARCHAR(255) NULL,
    city VARCHAR(255) NULL,
    address_raw TEXT NULL,
    latitude DECIMAL(10, 7) NULL,
    longitude DECIMAL(10, 7) NULL,
    residential_complex_id BIGINT UNSIGNED NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
UNIQUE KEY uq_yandex_building (yandex_building_id),
KEY idx_yandex_rc (residential_complex_id),
CONSTRAINT fk_yandex_rc
    FOREIGN KEY (residential_complex_id)
    REFERENCES residential_complex(id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)
'''

CREATE_CIAN_TABLE = '''
CREATE TABLE IF NOT EXISTS cian_newbuilding (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    cian_complex_id VARCHAR(64) NOT NULL,
    name VARCHAR(255) NULL,
    region VARCHAR(255) NULL,
    city VARCHAR(255) NULL,
    address_raw TEXT NULL,
    latitude DECIMAL(10, 7) NULL,
    longitude DECIMAL(10, 7) NULL,
    residential_complex_id BIGINT UNSIGNED NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
UNIQUE KEY uq_cian_complex (cian_complex_id),
KEY idx_cian_rc (residential_complex_id),
CONSTRAINT fk_cian_rc
    FOREIGN KEY (residential_complex_id)
    REFERENCES residential_complex(id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
)
'''
