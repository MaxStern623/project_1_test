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

## 📚 **Learning Resources**

### 📖 **Comprehensive Guides**
- **[Exception Design](resources/guides/01-exceptions.md)** - Building robust error handling
- **[Input Validation](resources/guides/02-validation.md)** - Defending against bad data  
- **[Error-Safe Operations](resources/guides/03-operations.md)** - Bulletproof arithmetic
- **[CLI Design](resources/guides/04-cli.md)** - Professional command-line interfaces

### 🔧 **Quick References**
- **[Complete Solutions](COMPLETE_SOLUTIONS.md)** - 🏆 Full working implementations
- **[Defensive Programming Checklist](resources/references/defensive-checklist.md)**
- **[EAFP vs LBYL Decision Guide](resources/references/eafp-vs-lbyl.md)**
- **[Exception Patterns Reference](resources/references/exception-patterns.md)**

## 🎯 Success Metrics

You'll know you're making progress when:

- ✅ **Tests Pass**: `pytest tests/` shows green
- ✅ **Type Checking**: `mypy src/` finds no issues
- ✅ **Quality Gates**: `make qa` passes all checks
- ✅ **CLI Works**: `python3 -m src.main add 2 3` outputs `5`
- ✅ **Error Handling**: `python3 -m src.main divide 1 0` shows clear error message

## 🆘 Getting Help

### When You're Stuck
1. **Check the Solutions**: [`resources/references/complete-solutions.md`](resources/references/complete-solutions.md) - All answers in one place
2. **Read the Guide**: Each guide has troubleshooting sections
3. **Run Tests**: `pytest tests/test_operations.py::TestAddition -v` for specific feedback
3. **Test Your Progress**: `pytest tests/ -v`
4. **Compare with Examples**: [`complete_solutions/`](complete_solutions/)
5. **Iterate and Improve**: Add logging, better error messages, edge cases
5. **Use the Debugger**: VS Code debug configurations are set up

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
