class JSONMixin:
    """A Mixin to provide JSON serialization."""
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    """A Mixin to provide logging capabilities."""
    def log(self, message):
        print(f"[LOG - {self.__class__.__name__}]: {message}")

# The base class
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Multiple Inheritance: Employee + JSON capabilities + Logging capabilities
class TechLead(Employee, JSONMixin, LogMixin):
    def promote(self):
        self.log(f"Promoting {self.name}")
        # Logic here...

# Usage
lead = TechLead("Alice", "Engineering Manager")
lead.promote()
print(lead.to_json())