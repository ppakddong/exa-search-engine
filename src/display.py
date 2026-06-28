def print_results(results):
    print("=" * 70)

    for i, result in enumerate(results, start=1):
        print(f"[{i}] {result.title}")
        print(f"URL : {result.url}")

        if result.text:
            print(result.text[:250] + "...")

        print("-" * 70)