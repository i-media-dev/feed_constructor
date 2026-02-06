CREATE_RC_TABLE = '''
CREATE TABLE residential_complex (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(500),
    city VARCHAR(255),
    developer VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
UNIQUE KEY unique_rc (name, address)
);
'''

CREATE_YANDEX_TABLE = '''
CREATE TABLE rc_yandex (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rc_id INT NOT NULL,
    yandex_building_id VARCHAR(50) NOT NULL,
    yandex_house_id VARCHAR(50),
UNIQUE KEY uniq_yandex (yandex_building_id, yandex_house_id),
FOREIGN KEY (rc_id) REFERENCES residential_complex(id) ON DELETE CASCADE
);
'''

CREATE_CIAN_TABLE = '''
CREATE TABLE rc_cian (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rc_id INT NOT NULL,
    cian_complex_id VARCHAR(50) NOT NULL,
UNIQUE KEY uniq_cian (cian_complex_id),
FOREIGN KEY (rc_id) REFERENCES residential_complex(id) ON DELETE CASCADE
);
'''

CREATE_AVITO_TABLE = '''
CREATE TABLE rc_avito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rc_id INT NOT NULL,
    avito_complex_id VARCHAR(50) NOT NULL,
UNIQUE KEY uniq_avito (avito_complex_id),
FOREIGN KEY (rc_id) REFERENCES residential_complex(id) ON DELETE CASCADE
);
'''
