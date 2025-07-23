"""
VENV (Virtual ENVironment)

- Safe space to install project's packages, isolated from the rest of your system.
- Avoids version conflicts between different projects.

- Real Life Example:

    Project A uses numpy version 1.20

    Project B uses numpy version 1.25

- Using venv, both versions are kept in different environments.
- Otherwise, one version would overwrite the other and break the project.

- Venv Commands :- [Only to be typed in terminal]

    1). To create a virtual environment:

        python3 -m venv myenv

    2). To activate the virtual environment:

        source myenv/bin/activate (see the change as (myenv) user@machine %)

    3). Now, install packages inside this environment:

        pip install numpy
        pip install emoji etc
    
    4). Deactivate the environment:

        deactivate
    
    5). Delete the virtual environment:

        rm -rf myenv
"""