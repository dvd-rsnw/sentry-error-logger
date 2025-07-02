# Sentry Error Logger Microapplication

A simple Python microapplication demonstrating Sentry integration for error tracking and monitoring.

## Features

- Automatic error capture and reporting to Sentry
- Interactive CLI for testing different error scenarios
- Custom event logging
- Error statistics tracking
- Multiple error type demonstrations
- Environment-based configuration

## Installation

### Option 1: Using pip (recommended)

```bash
pip install -e .
```

### Option 2: Manual installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your Sentry DSN:
```
SENTRY_DSN=your-sentry-dsn-here
ENVIRONMENT=development  # optional, defaults to 'development'
```

3. Get your Sentry DSN from:
   - Sign up at [sentry.io](https://sentry.io)
   - Create a new project
   - Go to Settings → Projects → [Your Project] → Client Keys (DSN)

## Running the Application

If installed with pip:
```bash
sentry-logger
```

Or run directly:
```bash
python app.py
```

## Usage

The application provides an interactive menu with the following options:

1. **Simulate random operation** - Randomly triggers either a successful operation or one of several error types
2. **Log custom message** - Send custom messages to Sentry with different severity levels
3. **View statistics** - Display success/error counts
4. **Trigger specific error** - Manually trigger specific error types for testing
5. **Exit** - Shutdown the application

## Error Types Demonstrated

- ZeroDivisionError
- KeyError
- TypeError
- Custom ValueError

All errors are automatically captured and sent to your Sentry dashboard where you can:
- View error details and stack traces
- Track error frequency
- Set up alerts
- Monitor application performance

## Development

To contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.