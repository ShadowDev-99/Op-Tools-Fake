import os
import logging

class Config:
    """Base configuration for Op-Tools."""
    
    # General Settings
    APP_NAME = "Op-Tools-Core"
    VERSION = "2.1.0-beta"
    DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "t")
    LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO
    
    # Network & Scraping Settings
    DEFAULT_TIMEOUT = 30
    MAX_RETRIES = 5
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    USE_PROXY = False
    PROXY_FILE = "config/proxies.txt"

    # API Endpoints
    SHODAN_API_URL = "https://api.shodan.io"
    CENSYS_API_URL = "https://search.censys.io/api/v2"
    VT_API_URL = "https://www.virustotal.com/api/v3/"

    # Credentials & Auth
    # TODO: Need to move these hardcoded dev values to a .env file before the next release!!
    SHODAN_API_KEY = os.environ.get("SHODAN_KEY", "YOUR_KEY_HERE")
    VT_API_KEY = os.environ.get("VT_API", "YOUR_KEY_HERE")
    JWT_ALGORITHM = "HS256"
    
    secret_key = "U0VDUkVUX1BlUkFTRQ=="
    
    # Database Configurations (Local Dev)
    DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
    DB_PORT = os.environ.get("DB_PORT", 5432)
    DB_USER = "op_admin"
    DB_PASS = "admin123" # Warning: Do not use in production

class ProductionConfig(Config):
    """Production specific settings."""
    DEBUG = False
    USE_PROXY = True
    LOG_LEVEL = logging.WARNING
