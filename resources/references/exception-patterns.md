# 🎨 Common Exception Patterns

> **Quick reference for implementing robust exception handling patterns.**

## 📋 Basic Exception Patterns

### Simple Custom Exception
```python
class CustomError(Exception):
    """Basic custom exception."""
    pass

# Usage
raise CustomError("Something went wrong")
```

### Exception with Context
```python
class EnhancedError(Exception):
    """Exception with debugging context."""

    def __init__(self, message: str, context: dict[str, Any] | None = None):
        super().__init__(message)
        self.context = context or {}

# Usage
raise EnhancedError(
    "Operation failed",
    {"input": user_data, "step": "validation", "attempt": 3}
)
```

### Exception Hierarchy
```python
# Base exception
class ServiceError(Exception):
    """Base exception for service errors."""
    pass

# Specific exceptions
class ValidationError(ServiceError):
    """Input validation failed."""
    pass

class ProcessingError(ServiceError):
    """Processing operation failed."""
    pass

class TimeoutError(ServiceError):
    """Operation timed out."""
    pass
```

## 🛡️ Defensive Exception Patterns

### Input Validation Pattern
```python
def validate_input(value: Any, name: str) -> None:
    """Validate input with clear error messages."""
    if value is None:
        raise ValueError(f"{name} cannot be None")

    if not isinstance(value, (int, float)):
        raise TypeError(
            f"{name} must be numeric, got {type(value).__name__}",
            {"value": value, "expected_types": ["int", "float"]}
        )

    if math.isnan(value):
        raise ValueError(f"{name} cannot be NaN")
```

### Exception Chaining Pattern
```python
def process_data(data: str) -> ProcessedData:
    """Process data with exception chaining."""
    try:
        parsed = json.loads(data)
    except json.JSONDecodeError as e:
        raise ValidationError("Invalid JSON format") from e

    try:
        return ProcessedData(parsed)
    except KeyError as e:
        raise ValidationError(f"Missing required field: {e}") from e
```

### Error Boundary Pattern
```python
def service_operation(request: Request) -> Response:
    """Service operation with error boundary."""
    try:
        # Main business logic
        validated = validate_request(request)
        processed = process_request(validated)
        result = finalize_result(processed)
        return Response(result)

    except ValidationError as e:
        logger.warning(f"Validation failed: {e}")
        return ErrorResponse("Invalid request", status=400)

    except ProcessingError as e:
        logger.error(f"Processing failed: {e}")
        return ErrorResponse("Processing failed", status=500)

    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        return ErrorResponse("Internal error", status=500)
```

## 🔄 Retry Patterns

### Simple Retry
```python
def retry_operation(operation: Callable, max_attempts: int = 3) -> Any:
    """Retry operation with exponential backoff."""
    for attempt in range(max_attempts):
        try:
            return operation()
        except RetryableError as e:
            if attempt == max_attempts - 1:
                raise FinalError(f"Failed after {max_attempts} attempts") from e

            sleep_time = 2 ** attempt  # Exponential backoff
            time.sleep(sleep_time)
            logger.warning(f"Attempt {attempt + 1} failed, retrying in {sleep_time}s")
```

### Circuit Breaker Pattern
```python
class CircuitBreaker:
    """Circuit breaker for failing operations."""

    def __init__(self, failure_threshold: int = 5, reset_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "closed"  # closed, open, half-open

    def call(self, operation: Callable) -> Any:
        if self.state == "open":
            if time.time() - self.last_failure_time > self.reset_timeout:
                self.state = "half-open"
            else:
                raise CircuitOpenError("Circuit breaker is open")

        try:
            result = operation()
            if self.state == "half-open":
                self.state = "closed"
                self.failure_count = 0
            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = "open"

            raise
```

## 📊 Logging Integration Patterns

### Structured Error Logging
```python
def log_error(error: Exception, context: dict[str, Any] | None = None) -> None:
    """Log error with structured information."""
    error_info = {
        "error_type": type(error).__name__,
        "error_message": str(error),
        "context": context or {},
        "traceback": traceback.format_exc()
    }

    if isinstance(error, ValidationError):
        logger.warning("Validation error occurred", extra=error_info)
    elif isinstance(error, ProcessingError):
        logger.error("Processing error occurred", extra=error_info)
    else:
        logger.critical("Unexpected error occurred", extra=error_info)
```

### Error Metrics Pattern
```python
class ErrorTracker:
    """Track error metrics for monitoring."""

    def __init__(self):
        self.error_counts = defaultdict(int)
        self.error_rates = defaultdict(list)

    def record_error(self, error: Exception) -> None:
        """Record error for metrics."""
        error_type = type(error).__name__
        timestamp = time.time()

        self.error_counts[error_type] += 1
        self.error_rates[error_type].append(timestamp)

        # Clean old entries (keep last hour)
        cutoff = timestamp - 3600
        self.error_rates[error_type] = [
            t for t in self.error_rates[error_type] if t > cutoff
        ]

    def get_error_rate(self, error_type: str, window_seconds: int = 300) -> float:
        """Get error rate for the given window."""
        cutoff = time.time() - window_seconds
        recent_errors = [
            t for t in self.error_rates[error_type] if t > cutoff
        ]
        return len(recent_errors) / window_seconds
```

## 🧪 Testing Exception Patterns

### Testing Exception Raising
```python
def test_validation_error():
    """Test that validation raises appropriate error."""
    with pytest.raises(ValidationError) as exc_info:
        validate_input("invalid", "number")

    assert "must be numeric" in str(exc_info.value)
    assert exc_info.value.context["expected_types"] == ["int", "float"]
```

### Testing Exception Context
```python
def test_exception_context():
    """Test exception includes useful context."""
    try:
        risky_operation("bad_input")
        assert False, "Should have raised exception"
    except ProcessingError as e:
        assert "input" in e.context
        assert "step" in e.context
        assert e.context["input"] == "bad_input"
```

### Mock Exception Testing
```python
@patch('module.external_service')
def test_error_handling(mock_service):
    """Test error handling with mocked failures."""
    mock_service.side_effect = ConnectionError("Network failed")

    with pytest.raises(ServiceError) as exc_info:
        call_external_service()

    assert "Network failed" in str(exc_info.value.__cause__)
```

---

## 🔗 See Also

- **[Defensive Programming Checklist](defensive-checklist.md)**
- **[EAFP vs LBYL Guide](eafp-vs-lbyl.md)**
- **[Python Exception Docs](https://docs.python.org/3/library/exceptions.html)**
