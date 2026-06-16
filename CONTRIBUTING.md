# Contributing

Thanks for contributing to this repository.

The goal of this project is to remain a compact and credible reference implementation for a Microsoft Graph to object storage ingestion pattern. Contributions should improve practical reuse, clarity, and extensibility without overstating the maturity of the codebase.

## Contribution Principles

- Keep the repository useful as a reference implementation, not as a tutorial or sandbox.
- Prefer changes that strengthen reuse, maintainability, or architectural clarity.
- Keep documentation aligned with what the code actually delivers today.
- Avoid adding claims, examples, or abstractions that suggest capabilities the repository does not yet implement.

## What Good Contributions Look Like

- Better separation of concerns in the transfer flow
- Improved configuration handling
- Additional tests for existing behavior
- Safer error handling and clearer failure modes
- Documentation updates that improve practical adoption
- Incremental extensions that preserve the repository's small and reusable nature

## Suggested Workflow

1. Fork the repository.
2. Create a focused branch for your change.
3. Implement the change with clear, minimal scope.
4. Add or update tests when behavior changes.
5. Update documentation if the change affects usage or repository scope.
6. Open a pull request with a concise explanation of the problem addressed and the design choice made.

## Coding Expectations

- Follow PEP 8 for Python style.
- Favor readable, explicit code over premature abstraction.
- Add tests for meaningful behavior changes.
- Preserve compatibility with the repository's current structure unless a refactor clearly improves reuse.

## Issues And Enhancements

When opening an issue or proposing an enhancement, please include:

- the problem being solved
- the practical use case
- the expected impact on reuse or extensibility
- any tradeoffs introduced by the change

## Scope Discipline

This repository is intentionally small. Large additions are welcome when they clearly support the reference-implementation purpose, but they should not turn the project into a broad framework or a collection of unrelated experiments.
