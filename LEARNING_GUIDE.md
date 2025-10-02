# 🎯 Defensive Programming Calculator - Learning Guide

Welcome to your journey into **defensive programming**! This guide will walk you through building a robust calculator while learning industry-standard practices.

## 🗺️ Learning Path

### Phase 1: Understanding the Foundation (30 minutes)
1. **Read the Theory** → [`docs/00-mindset-history.md`](docs/00-mindset-history.md)
2. **Understand Project Structure** → [`docs/03-structure.md`](docs/03-structure.md)  
3. **Set Up Your Environment** → [`docs/02-setup.md`](docs/02-setup.md)

### Phase 2: Hands-On Implementation (2-3 hours)
4. **Custom Exceptions** → [`resources/guides/01-exceptions.md`](resources/guides/01-exceptions.md)
5. **Input Validation** → [`resources/guides/02-validation.md`](resources/guides/02-validation.md)
6. **Error-Safe Operations** → [`resources/guides/03-operations.md`](resources/guides/03-operations.md)
7. **CLI with Error Handling** → [`resources/guides/04-cli.md`](resources/guides/04-cli.md)

### Phase 3: Quality & Polish (1 hour)
8. **Testing Your Code** → [`docs/05-testing.md`](docs/05-testing.md)
9. **Code Quality Tools** → [`docs/04-tooling.md`](docs/04-tooling.md)
10. **Type Safety** → [`docs/06-typing.md`](docs/06-typing.md)

## 🚀 Getting Started

### Step 1: Environment Setup
```bash
# Make sure you're in the project directory
cd /path/to/Project_test

# Activate virtual environment
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Verify setup
python3 -m src.main --help  # Should show help (may error - that's expected!)
pytest tests/ -v            # Will show what needs implementing
```

### Step 2: Start with Exceptions
Open [`src/exceptions.py`](src/exceptions.py) and follow the TODOs. This builds the foundation for all error handling.

### Step 3: Follow the Guides
Each guide in [`resources/guides/`](resources/guides/) builds on the previous one. Work through them in order.

## 📚 Learning Resources

### Quick References
- **[Python Exception Best Practices](resources/references/exception-patterns.md)**
- **[Defensive Programming Checklist](resources/references/defensive-checklist.md)**
- **[EAFP vs LBYL Guide](resources/references/eafp-vs-lbyl.md)**

### Code Examples
- **[Complete Implementation](resources/examples/complete_implementation/)** - Reference when stuck
- **[Common Patterns](resources/examples/patterns/)** - Reusable code patterns
- **[Error Scenarios](resources/examples/error-handling/)** - How to handle edge cases

### External Resources
- **[Python Official: Errors & Exceptions](https://docs.python.org/3/tutorial/errors.html)**
- **[Real Python: Exception Handling](https://realpython.com/python-exceptions/)**
- **[PEP 8: Style Guide](https://www.python.org/dev/peps/pep-0008/)**
- **[Clean Code Principles](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29)**

## 🎯 Success Metrics

You'll know you're making progress when:

- ✅ **Tests Pass**: `pytest tests/` shows green
- ✅ **Type Checking**: `mypy src/` finds no issues  
- ✅ **Quality Gates**: `make qa` passes all checks
- ✅ **CLI Works**: `python3 -m src.main add 2 3` outputs `5`
- ✅ **Error Handling**: `python3 -m src.main divide 1 0` shows clear error message

## 🆘 Getting Help

### When You're Stuck
1. **Check the Examples**: [`resources/examples/`](resources/examples/)
2. **Read the Guide**: Each guide has troubleshooting sections
3. **Run Tests**: `pytest tests/test_operations.py::TestAddition -v` for specific feedback
4. **Use the Debugger**: VS Code debug configurations are set up

### Common Issues
- **Import Errors**: Make sure you're running from the project root
- **Test Failures**: Expected! They guide what to implement next
- **Type Errors**: Check [`resources/references/typing-guide.md`](resources/references/typing-guide.md)

## 🏆 Next Steps

After completing this project:

1. **Build Your Own**: Apply these patterns to a larger project
2. **Learn More**: Explore [`docs/careers.md`](docs/careers.md) for career paths
3. **Share**: Create a blog post about what you learned
4. **Practice**: Try the advanced exercises in [`resources/guides/advanced/`](resources/guides/advanced/)

---

**Ready to start?** Open [`resources/guides/01-exceptions.md`](resources/guides/01-exceptions.md) and begin your journey! 🚀