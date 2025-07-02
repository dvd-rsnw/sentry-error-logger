import sentry_sdk
import logging
import random
import time
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Sentry DSN from environment variable
SENTRY_DSN = os.getenv('SENTRY_DSN')

if not SENTRY_DSN:
    print("Error: SENTRY_DSN environment variable is not set.")
    print("Please set it in your .env file or export it as an environment variable.")
    print("Example: export SENTRY_DSN='your-sentry-dsn-here'")
    sys.exit(1)

# Initialize Sentry
sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    traces_sample_rate=1.0,  # Capture 100% of transactions for performance monitoring
    profiles_sample_rate=1.0,  # Capture 100% of transactions for profiling
    environment=os.getenv('ENVIRONMENT', 'development')
)

# Set up local logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ErrorLogger:
    """A simple error logging microapplication demonstrating Sentry integration."""
    
    def __init__(self):
        self.error_count = 0
        self.success_count = 0
    
    def simulate_operation(self):
        """Simulate various operations that might fail."""
        operations = [
            self._divide_by_zero,
            self._access_invalid_key,
            self._type_error,
            self._custom_error,
            self._successful_operation
        ]
        
        operation = random.choice(operations)
        try:
            result = operation()
            self.success_count += 1
            logger.info(f"Operation succeeded: {operation.__name__} - Result: {result}")
            return result
        except Exception as e:
            self.error_count += 1
            logger.error(f"Operation failed: {operation.__name__} - Error: {str(e)}")
            # Sentry will automatically capture unhandled exceptions
            raise
    
    def _divide_by_zero(self):
        """Simulate a division by zero error."""
        return 10 / 0
    
    def _access_invalid_key(self):
        """Simulate a KeyError."""
        data = {"name": "test"}
        return data["invalid_key"]
    
    def _type_error(self):
        """Simulate a TypeError."""
        return "string" + 123
    
    def _custom_error(self):
        """Simulate a custom error."""
        raise ValueError("This is a custom error for testing Sentry")
    
    def _successful_operation(self):
        """A successful operation."""
        return {"status": "success", "timestamp": datetime.now().isoformat()}
    
    def log_custom_event(self, message, level="info", extra_data=None):
        """Log a custom event to Sentry."""
        with sentry_sdk.push_scope() as scope:
            if extra_data:
                for key, value in extra_data.items():
                    scope.set_extra(key, value)
            
            if level == "error":
                sentry_sdk.capture_message(message, level="error")
            elif level == "warning":
                sentry_sdk.capture_message(message, level="warning")
            else:
                sentry_sdk.capture_message(message, level="info")
            
            logger.info(f"Custom event logged to Sentry: {message}")
    
    def get_stats(self):
        """Get current statistics."""
        return {
            "error_count": self.error_count,
            "success_count": self.success_count,
            "total_operations": self.error_count + self.success_count
        }


def main():
    """Main application entry point."""
    print("Sentry Error Logger Microapplication")
    print("====================================")
    print("This app demonstrates Sentry integration for error tracking.")
    print()
    
    error_logger = ErrorLogger()
    
    # Log a startup event
    error_logger.log_custom_event(
        "Application started",
        level="info",
        extra_data={"version": "1.0.0", "environment": "development"}
    )
    
    while True:
        print("\nOptions:")
        print("1. Simulate random operation (may fail)")
        print("2. Log custom message to Sentry")
        print("3. View statistics")
        print("4. Trigger specific error")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            try:
                result = error_logger.simulate_operation()
                print(f"✓ Operation successful: {result}")
            except Exception as e:
                print(f"✗ Operation failed: {type(e).__name__}: {str(e)}")
                print("  (Error has been sent to Sentry)")
        
        elif choice == "2":
            message = input("Enter message to log: ")
            level = input("Enter level (info/warning/error) [info]: ") or "info"
            error_logger.log_custom_event(message, level)
            print("✓ Message logged to Sentry")
        
        elif choice == "3":
            stats = error_logger.get_stats()
            print(f"\nStatistics:")
            print(f"  Total operations: {stats['total_operations']}")
            print(f"  Successful: {stats['success_count']}")
            print(f"  Failed: {stats['error_count']}")
        
        elif choice == "4":
            print("\nSelect error type:")
            print("1. ZeroDivisionError")
            print("2. KeyError")
            print("3. TypeError")
            print("4. Custom ValueError")
            
            error_choice = input("Enter choice (1-4): ")
            try:
                if error_choice == "1":
                    error_logger._divide_by_zero()
                elif error_choice == "2":
                    error_logger._access_invalid_key()
                elif error_choice == "3":
                    error_logger._type_error()
                elif error_choice == "4":
                    error_logger._custom_error()
                else:
                    print("Invalid choice")
            except Exception as e:
                print(f"✗ Error triggered: {type(e).__name__}: {str(e)}")
                print("  (Error has been sent to Sentry)")
        
        elif choice == "5":
            error_logger.log_custom_event("Application shutting down", level="info")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user")
        sentry_sdk.capture_message("Application interrupted by user", level="info")
    except Exception as e:
        print(f"\n\nUnexpected error: {str(e)}")
        # This will be automatically captured by Sentry
        raise