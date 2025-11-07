# Sprint 1 Retrospective (Days 1-3)

**Date:** [Your Current Date]
**Participants:** Maanya, Krishank, Kshema, Krishal

---

### What went well?

* **Team Collaboration:** We successfully split all tasks for Day 2 (Auth) and Day 3 (Digest Engine) among all four team members.
* **Git Workflow:** We used the "branch-per-feature" workflow correctly. Every new feature was developed on a branch (e.g., `feature/US-003...`, `feature/US-006...`) and merged via a Pull Request.
* **Velocity:** We completed all planned features for Sprint 1, including user registration, login, preferences, and the entire core logic for the digest generator (mock API, template, and generator module).
* **Testing:** We successfully wrote and ran our first unit tests for the `DigestGenerator` and fixed the `pytest` path issues.

### What didn't go well?

* **Blockers:** We were blocked for a while by the `ModuleNotFoundError: No module named 'src'` when running `pytest`. This was an environment/path issue that we had to debug.
* **CI Pipeline:** Our current CI pipeline in `main.yml` is very basic. It only runs `build` and `test` and doesn't enforce any quality gates yet.
* **Test Coverage:** We only have tests for the `DigestGenerator`. The `Auth` (`US-001`, `US-002`) and `Preferences` (`US-003`, `US-004`) modules have no unit tests yet, so our code coverage is very low.

### Action items for Sprint 2 (starting tomorrow)

1.  **CI `pytest` Fix:** Update the `main.yml` test stage to run `python -m pytest` to prevent the `ModuleNotFoundError` from happening on the GitHub runner.
2.  **Add More Tests (High Priority):** Create test files (`test_auth.py`, `test_preferences.py`) and write unit tests for the auth and preferences endpoints to increase our code coverage.
3.  **Harden CI/CD Pipeline:** This is our main goal. We must add the `Coverage` (with a >=75% failure threshold), `Lint` (with a >=7.5 score threshold), and `Security` stages.
4.  **Implement Remaining Features:** Complete the final user stories: `US-008` (Preview Endpoint) and `US-009` (Admin Log Endpoint).