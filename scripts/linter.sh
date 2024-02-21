
printf "\nRunning flake8...\n"
flake8 ./

printf "\nRunning flake8...\n"
if ! flake8 ./; then
    ISSUES_DETECTED=1
else
    echo "-->> No flake8 issues found."
fi

printf "\nRunning isort...\n"
if ! isort ./ --check-only; then
    ISSUES_DETECTED=1
else
    echo "-->> No isort changes needed."
fi

printf "\nRunning black...\n"
if ! black -l 120 ./ --exclude ".*\/migrations\/.*" --check; then
    ISSUES_DETECTED=1
else
    echo "-->> No black changes needed."
fi

if [ "$ISSUES_DETECTED" -eq "1" ]; then
    echo ""
    echo "-------"
    echo "Issues were detected. Please address the above issues."
    echo "-------"
    exit 1
else
    echo ""
    echo "-------"
    echo "All checks passed successfully."
    echo "-------"
fi
