# ENGCMP 0610 Examples (Fall 2026)

This repository holds programming examples from Pat Healy's ENGCMP 0610: *Composing Digital Media* course from Fall 2026.

Pat will update this repository as we continue to explore new concepts throughout the semester.

## Terminal Command Cheat-Sheet

Much of our work in this unit will require we engage with the terminal (or Command Prompt on Windows). Below are a bunch of common commands you'll be using a whole lot! I use `<>` to signify parameters in these commands, which you'll have to fill in with whatever's appropriate for what you're trying to do. Note that you should not include the `<>` symbols when you run these commands, they're just there to signify what is or is not a parameter.

```
pwd
```

The `pwd` command stands for "print working directory" --- it prints out what folder your terminal is currently occupying. Reminder that the terminal is always sitting in a particular folder. It's kinda like a text-based file explorer (like Explorer in Windows or Finder in Mac).

```
On Mac/Linux: ls
On Windows: dir
```

This command is different on Mac vs Windows. On mac, `ls` will list the files and folder in the current working directory. It is helpful for orienting yourself, knowing what files are around for you to work on or folders are around to move to. On windows, that same command is `dir` (the output is formatted a little different, but it gives you the same info).

```
cd <directory>
```

The `cd` command stands for "change directory" --- it's how you move from one folder to another. For example, if you used `pwd` and noticed you're in your user's home folder, you could use `cd Documents` to move into the Documents folder. 

If you ever want to move out of a folder, back into its parent folder, you can use the command `cd ..`

```
mkdir <name-of-a-new-folder>
```

The above command creates a new folder (it's named `mkdir` as short for "make directory") inside your current folder.


```
python <name-of-python-program>.py

or

python3 <name-of-python-program>.py
```

Assuming you have python appropriately installed, the above commands will run a python program you specify, which must be in your current working directory. Note that depending on how your python was installed, you may have to use `python` or `python3`. This is due to a historic break between python 2.x and python 3.x (which is no longer important, since python 2 was fully deprecated years ago).


### Creating and activating a virtual environment

A python virtual environment is a safe playground for installing and using custom python packages. We want to use virtual environment any time we are working with externally-developed packages to make sure we don't accidentally break our python install (python now requires this!). 

```
mkdir venv
```

The first thing you'll want to do is make a folder to contain your new virtual environment. The above command makes a new folder wherever you're currently working and names that new folder `venv`. 

```
cd venv
```

Once the folder exists, we should use the above command to move into that folder.


```
python3 -m venv .
```

This above command creates a new virtual environment inside the current working directory. It's an interesting-looking command --- the `python3 -m` part of it is a generic way of running a python module (that being something installed as a part of python itself). So, `python3 -m venv` runs the virtual environment creation program, which takes in one parameter. The `.` is the one parameter, which is the location where you will save the new virtual environment. The `.` location refers to "here" -- as in the current working directory.

Now we need to activate our virtual environment. Within this `venv` folder, on **Mac** and **Linux** you will run this command:

```
source ./bin/activate
```

On **Windows**, you'll instead run this command:

```
.\Scripts\activate
```

Any time you want to work on a script inside this virtual environment later, you don't need to make it again, you only need to activate it with the above command.

### Installing Python packages

Once you are inside a python virtual environment, you can install packages that can be used by python scripts. The following command installs a package:

```
pip install <package-name>
```

For example, if you want to install *flask*, a package we will use a lot for the rest of this semester, you have to run the command `pip install flask`


### Running Flask applications

To run a flask application (assuming you are inside a virtual environment with flask installed), you need to run the following command:

```
flask --app <name-of-flask-script>.py run
```

So, for example, if you happened to have a simple flask web server script in `hello.py`, you would need to run `flask --app hello.py run`. This will start up a web server running on your localhost: http://127.0.0.1:5000

