"""Day 8: Packages and virtual environments."""


# Questions 1-5: Run these commands in order from a terminal opened in this
# Day 8 folder. The optional requests install is needed for Tasks 2 and 3.
print("Questions 1-5: Virtual environment and packages")
print("1. Create the environment:        python -m venv test_env")
print("2. Activate in Windows PowerShell: .\\test_env\\Scripts\\Activate.ps1")
print("   (In Command Prompt:             test_env\\Scripts\\activate.bat)")
print("3. Show starting packages:         python -m pip list")
print("4. Install colorama:               pip install colorama")
print("   Install for Tasks 2 and 3:       pip install requests")
print("5. Export installed packages:      python -m pip freeze > my_packages.txt")

# Question 6: Deactivate now; deleting the environment is a separate manual step.
print("\nQuestion 6: Deactivate and optional manual cleanup")
print("Deactivate the environment:        deactivate")
print("After deactivating, delete only test_env manually if you want:")
print("PowerShell: Remove-Item -Recurse -Force .\\test_env")
print("Command Prompt: rmdir /s /q test_env")
print("Do not run the delete command while the environment is active.")
