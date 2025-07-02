import sentry_sdk
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Sentry
SENTRY_DSN = os.getenv('SENTRY_DSN')
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        send_default_pii=True,
        traces_sample_rate=1.0,
        environment=os.getenv('ENVIRONMENT', 'development')
    )
    print("Sentry initialized successfully!")
    print("Triggering a divide by zero error...")
    
    # This will trigger a ZeroDivisionError that Sentry should capture
    division_by_zero = 1 / 0
else:
    print("SENTRY_DSN not found in environment variables")