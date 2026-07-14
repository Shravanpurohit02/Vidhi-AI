from app.verification.engine import VerificationEngine


engine = VerificationEngine()

print("=" * 80)
print("VIDHI AI VERIFICATION")
print("=" * 80)

passed = 0

results = engine.run()

for result in results:

    status = "PASS" if result.passed else "FAIL"

    print(f"[{status}] {result.name}")
    print(result.details)
    print(f"Duration: {result.duration:.3f}s")
    print()

    if result.passed:
        passed += 1

print("=" * 80)
print(f"Passed {passed}/{len(results)} checks")
