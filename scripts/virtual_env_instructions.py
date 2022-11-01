# ignore this file, it's for development only

print("\n**************************************************************************")
print("A virtual environment is simply a tool that separates the dependencies of different projects by creating a separate isolated environment for each project.\n\
These are simply the directories so that unlimited virtual environments can be created. This is one of the popular tools used by most of the Python developers.\n\n\
Why do we need a virtual environment?\n\
Python has various modules and packages for different applications. During our project, it may require a third-party library, which we install.\n\
Another project also uses the same directory for retrieval and storage but doesn't require any other third-party packages. \n\
So, the virtual environment can come into play and make a separate isolated environment for both projects, and each project can store\n\
and retrieve packages from their specific environment.\n\n\
Also, let us consider another case where we are creating a web application using Django. Suppose you are working on two projects project1 and project2.\n\
If project1 uses Django-2.2 and project2 uses Django-3.2, they would be stored in the same directory with the same name, and the error may occur. \n\
Then, in such cases, virtual environments can be really helpful for you to maintain the dependencies of both the projects.\n")

print("To start virtual environment, open the terminal and type: 'Scripts/Activate.ps1'")
print("To end a virtual environment, open the terminal while the virtual environment is active and type: 'deactivate'")
print("Remember that any modules installed in the virtual environment are local to it, and connot be used in other projects.")
print("**************************************************************************\n")
